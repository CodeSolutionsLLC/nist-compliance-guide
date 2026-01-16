#!/usr/bin/env python3
"""
Check NIST publication URLs for updates and broken links.

This script:
1. Extracts all nist.gov URLs from NIST-STANDARDS.md
2. Checks if each URL is accessible
3. Checks Last-Modified headers for recent updates
4. Generates a report of any issues found
"""

import json
import os
import re
import sys
from datetime import datetime, timedelta, timezone
from pathlib import Path
from typing import NamedTuple

import requests

# Configuration
STANDARDS_FILE = "NIST-STANDARDS.md"
REPORT_FILE = "update_report.md"
RESULTS_FILE = "check_results.json"
CHECK_WINDOW_HOURS = 24
REQUEST_TIMEOUT = 30
USER_AGENT = "NIST-Compliance-Guide-Bot/1.0 (https://github.com/CodeSolutionsLLC/nist-compliance-guide)"


class URLCheckResult(NamedTuple):
    """Result of checking a single URL."""
    url: str
    status: str  # 'ok', 'updated', 'moved', 'broken', 'error'
    status_code: int | None
    last_modified: str | None
    redirect_url: str | None
    error: str | None


def extract_nist_urls(content: str) -> list[str]:
    """Extract all nist.gov URLs from markdown content."""
    # Match URLs in markdown links and plain URLs
    url_pattern = r'https?://(?:www\.)?(?:csrc\.)?(?:nvlpubs\.)?nist\.gov[^\s\)>\]"\']*'
    urls = re.findall(url_pattern, content)
    # Remove duplicates while preserving order
    seen = set()
    unique_urls = []
    for url in urls:
        # Clean up URL (remove trailing punctuation)
        url = url.rstrip('.,;:')
        if url not in seen:
            seen.add(url)
            unique_urls.append(url)
    return unique_urls


def check_url(url: str) -> URLCheckResult:
    """Check a single URL for accessibility and updates."""
    headers = {"User-Agent": USER_AGENT}

    try:
        # Use HEAD request first to be polite
        response = requests.head(
            url,
            headers=headers,
            timeout=REQUEST_TIMEOUT,
            allow_redirects=True
        )

        # If HEAD fails, try GET
        if response.status_code >= 400:
            response = requests.get(
                url,
                headers=headers,
                timeout=REQUEST_TIMEOUT,
                allow_redirects=True,
                stream=True  # Don't download full content
            )

        status_code = response.status_code
        last_modified = response.headers.get("Last-Modified")
        redirect_url = None

        # Check for redirects to different domain
        if response.url != url and not response.url.startswith(url.split('/')[0] + '//' + url.split('/')[2]):
            redirect_url = response.url

        # Determine status
        if status_code >= 400:
            return URLCheckResult(
                url=url,
                status="broken",
                status_code=status_code,
                last_modified=last_modified,
                redirect_url=redirect_url,
                error=f"HTTP {status_code}"
            )

        if redirect_url:
            return URLCheckResult(
                url=url,
                status="moved",
                status_code=status_code,
                last_modified=last_modified,
                redirect_url=redirect_url,
                error=None
            )

        # Check if recently updated
        if last_modified:
            try:
                # Parse Last-Modified header
                modified_time = datetime.strptime(
                    last_modified,
                    "%a, %d %b %Y %H:%M:%S %Z"
                ).replace(tzinfo=timezone.utc)

                now = datetime.now(timezone.utc)
                if now - modified_time < timedelta(hours=CHECK_WINDOW_HOURS):
                    return URLCheckResult(
                        url=url,
                        status="updated",
                        status_code=status_code,
                        last_modified=last_modified,
                        redirect_url=None,
                        error=None
                    )
            except ValueError:
                pass  # Couldn't parse date, continue

        return URLCheckResult(
            url=url,
            status="ok",
            status_code=status_code,
            last_modified=last_modified,
            redirect_url=None,
            error=None
        )

    except requests.exceptions.Timeout:
        return URLCheckResult(
            url=url,
            status="error",
            status_code=None,
            last_modified=None,
            redirect_url=None,
            error="Request timeout"
        )
    except requests.exceptions.ConnectionError as e:
        return URLCheckResult(
            url=url,
            status="error",
            status_code=None,
            last_modified=None,
            redirect_url=None,
            error=f"Connection error: {str(e)[:100]}"
        )
    except Exception as e:
        return URLCheckResult(
            url=url,
            status="error",
            status_code=None,
            last_modified=None,
            redirect_url=None,
            error=f"Unexpected error: {str(e)[:100]}"
        )


def generate_report(results: list[URLCheckResult]) -> str:
    """Generate a markdown report from check results."""
    lines = [
        "# NIST Publication Update Check Report",
        "",
        f"**Check Time:** {datetime.now(timezone.utc).isoformat()}",
        f"**URLs Checked:** {len(results)}",
        "",
    ]

    # Categorize results
    updated = [r for r in results if r.status == "updated"]
    moved = [r for r in results if r.status == "moved"]
    broken = [r for r in results if r.status == "broken"]
    errors = [r for r in results if r.status == "error"]
    ok = [r for r in results if r.status == "ok"]

    # Summary
    lines.extend([
        "## Summary",
        "",
        f"- **OK:** {len(ok)}",
        f"- **Recently Updated:** {len(updated)}",
        f"- **Moved/Redirected:** {len(moved)}",
        f"- **Broken Links:** {len(broken)}",
        f"- **Errors:** {len(errors)}",
        "",
    ])

    # Recently Updated
    if updated:
        lines.extend([
            "## Recently Updated (within 24 hours)",
            "",
            "These publications may have new content:",
            "",
        ])
        for r in updated:
            lines.append(f"- {r.url}")
            if r.last_modified:
                lines.append(f"  - Last-Modified: {r.last_modified}")
        lines.append("")

    # Moved URLs
    if moved:
        lines.extend([
            "## Moved/Redirected URLs",
            "",
            "These URLs redirect to a different location and should be updated:",
            "",
        ])
        for r in moved:
            lines.append(f"- **From:** {r.url}")
            lines.append(f"  - **To:** {r.redirect_url}")
        lines.append("")

    # Broken Links
    if broken:
        lines.extend([
            "## Broken Links",
            "",
            "These URLs returned error status codes:",
            "",
        ])
        for r in broken:
            lines.append(f"- {r.url}")
            lines.append(f"  - Error: {r.error}")
        lines.append("")

    # Errors
    if errors:
        lines.extend([
            "## Check Errors",
            "",
            "These URLs could not be checked:",
            "",
        ])
        for r in errors:
            lines.append(f"- {r.url}")
            lines.append(f"  - Error: {r.error}")
        lines.append("")

    # Action items
    if updated or moved or broken:
        lines.extend([
            "## Recommended Actions",
            "",
        ])
        if updated:
            lines.append("- [ ] Review recently updated publications for content changes")
        if moved:
            lines.append("- [ ] Update moved URLs in NIST-STANDARDS.md")
        if broken:
            lines.append("- [ ] Find replacement URLs for broken links")
        lines.append("")

    return "\n".join(lines)


def main():
    """Main entry point."""
    print(f"NIST Publication Update Checker")
    print(f"================================")
    print(f"Check window: {CHECK_WINDOW_HOURS} hours")
    print()

    # Read the standards file
    standards_path = Path(STANDARDS_FILE)
    if not standards_path.exists():
        print(f"ERROR: {STANDARDS_FILE} not found")
        sys.exit(1)

    content = standards_path.read_text()

    # Extract URLs
    urls = extract_nist_urls(content)
    print(f"Found {len(urls)} unique NIST URLs to check")
    print()

    # Check each URL
    results = []
    for i, url in enumerate(urls, 1):
        print(f"[{i}/{len(urls)}] Checking: {url[:80]}...")
        result = check_url(url)
        results.append(result)
        print(f"         Status: {result.status}")
        if result.error:
            print(f"         Error: {result.error}")

    print()

    # Generate report
    report = generate_report(results)

    # Save report
    Path(REPORT_FILE).write_text(report)
    print(f"Report saved to {REPORT_FILE}")

    # Save JSON results
    json_results = [
        {
            "url": r.url,
            "status": r.status,
            "status_code": r.status_code,
            "last_modified": r.last_modified,
            "redirect_url": r.redirect_url,
            "error": r.error,
        }
        for r in results
    ]
    Path(RESULTS_FILE).write_text(json.dumps(json_results, indent=2))
    print(f"Results saved to {RESULTS_FILE}")

    # Set output for GitHub Actions
    updates_found = any(r.status in ("updated", "moved", "broken") for r in results)

    github_output = os.environ.get("GITHUB_OUTPUT")
    if github_output:
        with open(github_output, "a") as f:
            f.write(f"updates_found={'true' if updates_found else 'false'}\n")
        print(f"\nGitHub Output: updates_found={updates_found}")

    # Print summary
    print()
    print("Summary:")
    print(f"  OK: {sum(1 for r in results if r.status == 'ok')}")
    print(f"  Updated: {sum(1 for r in results if r.status == 'updated')}")
    print(f"  Moved: {sum(1 for r in results if r.status == 'moved')}")
    print(f"  Broken: {sum(1 for r in results if r.status == 'broken')}")
    print(f"  Errors: {sum(1 for r in results if r.status == 'error')}")

    # Exit with error if broken links found
    if any(r.status == "broken" for r in results):
        sys.exit(1)

    return 0


if __name__ == "__main__":
    sys.exit(main())
