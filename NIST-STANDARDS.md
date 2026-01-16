# NIST Standards Research and Reference Guide

This document provides a comprehensive reference to NIST (National Institute of Standards and Technology) publications relevant to secure software development, system administration, and compliance. All resources are from the official [nist.gov](https://www.nist.gov) domain.

**Purpose:** Create a reusable framework for NIST compliance research that can be applied to any project.

**Last Updated:** 2026-01-16

---

## Table of Contents

1. [Core Frameworks](#core-frameworks)
2. [Security and Privacy Controls](#security-and-privacy-controls)
3. [Secure Software Development](#secure-software-development)
4. [Cryptography and Key Management](#cryptography-and-key-management)
5. [Identity and Authentication](#identity-and-authentication)
6. [Audit and Logging](#audit-and-logging)
7. [System Security](#system-security)
8. [Incident Response and Forensics](#incident-response-and-forensics)
9. [Risk Management](#risk-management)
10. [Post-Quantum Cryptography](#post-quantum-cryptography)
11. [Control Family Quick Reference](#control-family-quick-reference)
12. [Implementation Checklist](#implementation-checklist)

---

## Core Frameworks

### NIST Cybersecurity Framework (CSF) 2.0

The overarching framework for managing cybersecurity risk.

| Resource | URL |
|----------|-----|
| **Main Publication** | https://csrc.nist.gov/pubs/cswp/29/the-nist-cybersecurity-framework-csf-20/final |
| **PDF Document** | https://nvlpubs.nist.gov/nistpubs/CSWP/NIST.CSWP.29.pdf |
| **CSF Website** | https://www.nist.gov/cyberframework |

**CSF 2.0 Core Functions:**
- **Govern (GV)** - Establish and monitor cybersecurity risk management strategy
- **Identify (ID)** - Understand organizational context and risk
- **Protect (PR)** - Implement safeguards for critical services
- **Detect (DE)** - Identify cybersecurity events
- **Respond (RS)** - Take action regarding detected incidents
- **Recover (RC)** - Restore capabilities after incidents

**Key Improvement:** CSF 2.0 added the "Govern" function to emphasize organizational governance of cybersecurity.

---

## Security and Privacy Controls

### SP 800-53 Rev. 5 - Security and Privacy Controls

The comprehensive catalog of security and privacy controls for information systems.

| Resource | URL |
|----------|-----|
| **Main Publication** | https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final |
| **PDF Document** | https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-53r5.pdf |
| **Assessment Guide (800-53A)** | https://csrc.nist.gov/pubs/sp/800/53/a/r5/final |

**Key Features:**
- Consolidated security and privacy controls
- Control baselines moved to SP 800-53B
- OSCAL format available (JSON, XML, YAML)
- Mappings to CSF, Privacy Framework, ISO 27001

**Control Families (20 total):**
| ID | Family | Description |
|----|--------|-------------|
| AC | Access Control | Who can access what |
| AT | Awareness and Training | Security education |
| AU | Audit and Accountability | Logging and monitoring |
| CA | Assessment, Authorization, Monitoring | Security assessments |
| CM | Configuration Management | System configuration |
| CP | Contingency Planning | Disaster recovery |
| IA | Identification and Authentication | Identity verification |
| IR | Incident Response | Handling security incidents |
| MA | Maintenance | System maintenance |
| MP | Media Protection | Protecting storage media |
| PE | Physical and Environmental | Physical security |
| PL | Planning | Security planning |
| PM | Program Management | Organization-wide security |
| PS | Personnel Security | Employee security |
| PT | PII Processing and Transparency | Privacy controls |
| RA | Risk Assessment | Identifying risks |
| SA | System and Services Acquisition | Secure procurement |
| SC | System and Communications Protection | Network security |
| SI | System and Information Integrity | Data integrity |
| SR | Supply Chain Risk Management | Third-party risk |

---

## Secure Software Development

### SP 800-218 - Secure Software Development Framework (SSDF)

Recommendations for mitigating software vulnerabilities.

| Resource | URL |
|----------|-----|
| **Main Publication (v1.1)** | https://csrc.nist.gov/pubs/sp/800/218/final |
| **PDF Document** | https://nvlpubs.nist.gov/nistpubs/specialpublications/nist.sp.800-218.pdf |
| **SSDF Project Page** | https://csrc.nist.gov/projects/ssdf |
| **Draft v1.2** | https://csrc.nist.gov/pubs/sp/800/218/r1/ipd |
| **AI Extension (800-218A)** | https://csrc.nist.gov/pubs/sp/800/218/a/final |

**SSDF Practice Groups:**
1. **Prepare the Organization (PO)** - Organizational preparation
2. **Protect the Software (PS)** - Protect code and configurations
3. **Produce Well-Secured Software (PW)** - Secure development practices
4. **Respond to Vulnerabilities (RV)** - Vulnerability management

**Relevance:** Maps to Executive Order 14028 requirements for secure software development.

---

## Cryptography and Key Management

### SP 800-57 - Key Management Guidelines

Comprehensive guidance on cryptographic key management.

| Resource | URL |
|----------|-----|
| **Part 1 Rev. 5 (General)** | https://csrc.nist.gov/pubs/sp/800/57/pt1/r5/final |
| **Part 1 Rev. 6 (Draft)** | https://csrc.nist.gov/pubs/sp/800/57/pt1/r6/ipd |
| **Part 2 Rev. 1 (Best Practices)** | https://csrc.nist.gov/pubs/sp/800/57/pt2/r1/final |
| **Part 3 Rev. 1 (Application-Specific)** | https://csrc.nist.gov/pubs/sp/800/57/pt3/r1/final |
| **Key Management Project** | https://csrc.nist.gov/projects/key-management/key-management-guidelines |

**Three-Part Structure:**
- **Part 1:** General guidance and best practices
- **Part 2:** Policy and security planning requirements
- **Part 3:** Application-specific guidance

**Key Topics:**
- Algorithm selection and key sizes
- Key lifecycle management
- Key storage and protection
- Key recovery and archival

---

## Identity and Authentication

### SP 800-63-4 - Digital Identity Guidelines

Technical requirements for digital identity services.

| Resource | URL |
|----------|-----|
| **Main Guidelines (800-63-4)** | https://pages.nist.gov/800-63-4/ |
| **Identity Proofing (800-63A-4)** | https://csrc.nist.gov/pubs/sp/800/63/a/4/final |
| **Authentication (800-63B-4)** | https://csrc.nist.gov/pubs/sp/800/63/b/4/final |
| **Federation (800-63C-4)** | https://csrc.nist.gov/pubs/sp/800/63/c/4/final |

**Assurance Levels:**
- **IAL (Identity Assurance Level):** Confidence in identity proofing
- **AAL (Authenticator Assurance Level):** Strength of authentication
- **FAL (Federation Assurance Level):** Strength of federated assertions

**Key Updates in Rev. 4:**
- Syncable authenticators (passkeys) guidance
- Updated phishing-resistant requirements
- Equity and usability considerations

---

## Audit and Logging

### SP 800-92 - Log Management Planning Guide

Guidance on cybersecurity log management.

| Resource | URL |
|----------|-----|
| **Original (2006)** | https://csrc.nist.gov/pubs/sp/800/92/final |
| **PDF Document** | https://nvlpubs.nist.gov/nistpubs/legacy/sp/nistspecialpublication800-92.pdf |
| **Draft Rev. 1** | https://csrc.nist.gov/pubs/sp/800/92/r1/ipd |
| **Log Management Project** | https://csrc.nist.gov/projects/log-management |

**Key Topics:**
- Log management infrastructure
- Log generation, transmission, storage
- Log analysis and retention
- Regulatory compliance

### SP 800-137 - Continuous Monitoring

Information Security Continuous Monitoring (ISCM) guidance.

| Resource | URL |
|----------|-----|
| **Main Publication** | https://csrc.nist.gov/pubs/sp/800/137/final |
| **PDF Document** | https://nvlpubs.nist.gov/nistpubs/legacy/sp/nistspecialpublication800-137.pdf |
| **Assessment Guide (800-137A)** | https://csrc.nist.gov/pubs/sp/800/137/a/final |

**ISCM Components:**
- Security status monitoring
- Threat and vulnerability awareness
- Security control effectiveness

---

## System Security

### SP 800-123 - General Server Security

Guide to securing servers that provide network services.

| Resource | URL |
|----------|-----|
| **Main Publication** | https://csrc.nist.gov/pubs/sp/800/123/final |
| **PDF Document** | https://nvlpubs.nist.gov/nistpubs/legacy/sp/nistspecialpublication800-123.pdf |

**Security Areas:**
- Access Control
- Configuration Management
- Identification and Authentication
- System and Communications Protection
- System and Information Integrity

### SP 800-40 Rev. 4 - Patch Management

Guide to enterprise patch management planning.

| Resource | URL |
|----------|-----|
| **Main Publication** | https://csrc.nist.gov/pubs/sp/800/40/r4/final |
| **PDF Document** | https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-40r4.pdf |

**Key Concepts:**
- Patching as preventive maintenance
- Risk-based prioritization
- Testing vs. rapid deployment tradeoffs

---

## Incident Response and Forensics

### SP 800-86 - Forensic Techniques

Guide to integrating forensics into incident response.

| Resource | URL |
|----------|-----|
| **Main Publication** | https://csrc.nist.gov/pubs/sp/800/86/final |
| **PDF Document** | https://nvlpubs.nist.gov/nistpubs/legacy/sp/nistspecialpublication800-86.pdf |

**Four-Step Forensics Process:**
1. **Collection** - Identify and acquire data
2. **Examination** - Process collected data
3. **Analysis** - Derive useful information
4. **Reporting** - Document findings

### SP 800-61 Rev. 2 - Incident Handling

Computer security incident handling guide.

| Resource | URL |
|----------|-----|
| **Main Publication** | https://csrc.nist.gov/pubs/sp/800/61/r2/final |
| **PDF Document** | https://nvlpubs.nist.gov/nistpubs/specialpublications/nist.sp.800-61r2.pdf |

---

## Risk Management

### SP 800-30 Rev. 1 - Risk Assessment

Guide for conducting risk assessments.

| Resource | URL |
|----------|-----|
| **Main Publication** | https://csrc.nist.gov/pubs/sp/800/30/r1/final |

### SP 800-37 Rev. 2 - Risk Management Framework

Risk Management Framework (RMF) for information systems.

| Resource | URL |
|----------|-----|
| **Main Publication** | https://csrc.nist.gov/pubs/sp/800/37/r2/final |

**RMF Steps:**
1. Categorize
2. Select
3. Implement
4. Assess
5. Authorize
6. Monitor

---

## Post-Quantum Cryptography

Standards for cryptography resistant to quantum computer attacks.

### FIPS 203 - ML-KEM (Key Encapsulation)

| Resource | URL |
|----------|-----|
| **Main Publication** | https://csrc.nist.gov/pubs/fips/203/final |

Based on CRYSTALS-KYBER. Parameter sets: ML-KEM-512, ML-KEM-768, ML-KEM-1024.

### FIPS 204 - ML-DSA (Digital Signatures)

| Resource | URL |
|----------|-----|
| **Main Publication** | https://csrc.nist.gov/pubs/fips/204/final |

Based on CRYSTALS-Dilithium. Primary standard for post-quantum signatures.

### FIPS 205 - SLH-DSA (Hash-Based Signatures)

| Resource | URL |
|----------|-----|
| **Main Publication** | https://csrc.nist.gov/pubs/fips/205/final |

Based on SPHINCS+. Stateless hash-based digital signatures.

### PQC Project Page

| Resource | URL |
|----------|-----|
| **Project Home** | https://csrc.nist.gov/Projects/post-quantum-cryptography |
| **Standardization Process** | https://csrc.nist.gov/projects/post-quantum-cryptography/post-quantum-cryptography-standardization |

**Timeline:** Standards finalized August 2024. Migration should begin immediately.

---

## Control Family Quick Reference

Common SP 800-53 controls with example implementations:

### Access Control (AC)
| Control | Title | Example Implementation |
|---------|-------|------------------------|
| AC-2 | Account Management | User/service account lifecycle management |
| AC-3 | Access Enforcement | Role-based permission enforcement |
| AC-4 | Information Flow Enforcement | Network segmentation, firewall rules |
| AC-7 | Unsuccessful Logon Attempts | Account lockout after failed attempts |
| AC-10 | Concurrent Session Control | Session limits per user |

### Audit and Accountability (AU)
| Control | Title | Example Implementation |
|---------|-------|------------------------|
| AU-2 | Event Logging | Comprehensive security event logging |
| AU-3 | Content of Audit Records | Structured logs with timestamp, user, action |
| AU-4 | Audit Log Storage Capacity | Log rotation, compression, archival |
| AU-6 | Audit Record Review | Log analysis tools, SIEM integration |
| AU-7 | Audit Record Reduction | Log filtering, search capabilities |
| AU-9 | Protection of Audit Information | Append-only logs, separate log server |
| AU-11 | Audit Record Retention | Defined retention periods (e.g., 90 days) |
| AU-12 | Audit Record Generation | Automatic logging in applications |

### Configuration Management (CM)
| Control | Title | Example Implementation |
|---------|-------|------------------------|
| CM-2 | Baseline Configuration | Documented system configurations |
| CM-3 | Configuration Change Control | Change management process, approvals |
| CM-5 | Access Restrictions for Change | Privileged access for system changes |
| CM-6 | Configuration Settings | Hardened configurations, CIS benchmarks |
| CM-7 | Least Functionality | Disable unnecessary services/features |

### Contingency Planning (CP)
| Control | Title | Example Implementation |
|---------|-------|------------------------|
| CP-2 | Contingency Plan | Documented disaster recovery procedures |
| CP-4 | Contingency Plan Testing | Regular restore/failover testing |
| CP-9 | System Backup | Encrypted backups, offsite storage |

### Identification and Authentication (IA)
| Control | Title | Example Implementation |
|---------|-------|------------------------|
| IA-2 | Identification and Authentication | Multi-factor authentication |
| IA-5 | Authenticator Management | Password policies, credential storage |
| IA-5(1) | Password-Based Authentication | Complexity and length requirements |

### System and Communications Protection (SC)
| Control | Title | Example Implementation |
|---------|-------|------------------------|
| SC-4 | Information in Shared Resources | Memory/storage isolation |
| SC-7 | Boundary Protection | Firewalls, network segmentation |
| SC-13 | Cryptographic Protection | TLS 1.3, AES-256, SHA-256+ |
| SC-28 | Protection of Information at Rest | Full disk encryption, database encryption |

### System and Information Integrity (SI)
| Control | Title | Example Implementation |
|---------|-------|------------------------|
| SI-3 | Malicious Code Protection | Antivirus, code scanning |
| SI-7 | Software/Information Integrity | File integrity monitoring, checksums |
| SI-10 | Information Input Validation | Input sanitization, parameterized queries |
| SI-11 | Error Handling | Graceful error handling, no info leakage |

### Media Protection (MP)
| Control | Title | Example Implementation |
|---------|-------|------------------------|
| MP-6 | Media Sanitization | Secure wipe, destruction procedures |

### Security Assessment (CA)
| Control | Title | Example Implementation |
|---------|-------|------------------------|
| CA-2 | Control Assessments | Penetration testing, security audits |
| CA-7 | Continuous Monitoring | Real-time security monitoring |

### System and Services Acquisition (SA)
| Control | Title | Example Implementation |
|---------|-------|------------------------|
| SA-11 | Developer Testing | Automated security testing in CI/CD |

---

## Implementation Checklist

Use this checklist when implementing NIST standards in a new project:

### Phase 1: Foundation
- [ ] Review CSF 2.0 for organizational context
- [ ] Identify applicable SP 800-53 control families
- [ ] Document security requirements
- [ ] Establish risk tolerance levels

### Phase 2: Development
- [ ] Implement SSDF practices (SP 800-218)
- [ ] Apply secure coding standards
- [ ] Implement input validation
- [ ] Add comprehensive logging

### Phase 3: Security Controls
- [ ] Implement access controls (AC family)
- [ ] Configure audit logging (AU family)
- [ ] Apply configuration management (CM family)
- [ ] Implement cryptographic protections (SC family)

### Phase 4: Operations
- [ ] Establish log management (SP 800-92)
- [ ] Implement continuous monitoring (SP 800-137)
- [ ] Create incident response procedures (SP 800-61)
- [ ] Establish patch management (SP 800-40)

### Phase 5: Assessment
- [ ] Conduct security assessments (SP 800-53A)
- [ ] Perform risk assessments (SP 800-30)
- [ ] Document compliance status
- [ ] Plan remediation activities

---

## Additional Resources

### NIST Computer Security Resource Center (CSRC)
- **Homepage:** https://csrc.nist.gov
- **Publications Search:** https://csrc.nist.gov/publications
- **SP 800 Series:** https://csrc.nist.gov/publications/sp800

### NIST Glossary
- **Cybersecurity Glossary:** https://csrc.nist.gov/glossary

### Useful Tools
- **OSCAL (Open Security Controls Assessment Language):** https://pages.nist.gov/OSCAL/
- **National Vulnerability Database (NVD):** https://nvd.nist.gov

---

## Document History

| Date | Change |
|------|--------|
| 2026-01-16 | Initial creation with core NIST publications |

---

## Contributing

To add new NIST resources to this document:
1. Verify the resource is from nist.gov domain
2. Include both CSRC page and PDF links where available
3. Add brief description of relevance
4. Update the Table of Contents if adding new sections
