# 📌 Healthcare AI SIEM Rulebook – Use Cases

This section documents the **detection use cases** prioritized for SIEM monitoring in Healthcare AI environments.

---

## ✅ UC-01: Non-EU Data Export without Consent

- **Description:** Detects data exports to Non-EU destinations without documented patient consent.
- **Severity:** High
- **Risk Impact:** High
- **Likelihood:** Medium
- **Priority:** High
- **GDPR Mapping:** Article 44 (Transfers to third countries)
- **AI Act Mapping:** High-Risk System Logging Requirement
- **HIPAA Mapping:** Transmission Security
- **Business Impact:** Avoid fines up to €20 million; demonstrate cross-border compliance.

---

## ✅ UC-02: Access to Unencrypted Raw Data

- **Description:** Detects access to storage locations without encryption at rest.
- **Severity:** High
- **Risk Impact:** High
- **Likelihood:** High
- **Priority:** High
- **GDPR Mapping:** Article 32 (Security of processing)
- **AI Act Mapping:** Risk Management Measures
- **HIPAA Mapping:** Encryption/Decryption Controls
- **Business Impact:** Prevent data breach penalties; secure patient trust.

---

## ✅ UC-03: AI Model Manipulation / Data Poisoning

- **Description:** Detects unusual data uploads that could poison AI training.
- **Severity:** Medium
- **Risk Impact:** High
- **Likelihood:** Low
- **Priority:** Medium
- **GDPR Mapping:** Article 5 (Integrity), Article 25 (Privacy by Design)
- **AI Act Mapping:** High-Risk System Security
- **HIPAA Mapping:** Integrity Controls
- **Business Impact:** Avoid compromised diagnoses and reputational loss.

---

## ✅ UC-04: Unauthorized Access to PHI

- **Description:** Detects user accounts accessing Protected Health Information without proper RBAC authorization.
- **Severity:** High
- **Risk Impact:** High
- **Likelihood:** Medium
- **Priority:** High
- **GDPR Mapping:** Article 32 (Access control)
- **AI Act Mapping:** Logging / Oversight
- **HIPAA Mapping:** Access Control Standard
- **Business Impact:** Avoid breach notifications, protect patient privacy.

---

## ✅ UC-05: Excessive Data Fields without Minimization

- **Description:** Detects storage of unnecessary data fields violating data minimization principles.
- **Severity:** High
- **Risk Impact:** Medium
- **Likelihood:** High
- **Priority:** High
- **GDPR Mapping:** Article 5(1)(c) (Data Minimization)
- **AI Act Mapping:** Risk Management
- **HIPAA Mapping:** Minimum Necessary Standard
- **Business Impact:** Avoid overcollection risks and audit failures.

---

## ✅ UC-06: Consent Check Failures

- **Description:** Detects transactions lacking consent verification step.
- **Severity:** High
- **Risk Impact:** High
- **Likelihood:** Medium
- **Priority:** High
- **GDPR Mapping:** Article 6, 9 (Lawfulness of Processing)
- **AI Act Mapping:** Logging of High-Risk Processing
- **HIPAA Mapping:** Authorization Requirements
- **Business Impact:** Ensure legal processing basis, avoid fines.

---

## ✅ UC-07: Cloud Misconfiguration (Open Buckets)

- **Description:** Detects misconfigured cloud storage with public access.
- **Severity:** Medium
- **Risk Impact:** High
- **Likelihood:** Low
- **Priority:** Medium
- **GDPR Mapping:** Article 32
- **AI Act Mapping:** Risk Management, Security by Design
- **HIPAA Mapping:** Transmission Security, Integrity
- **Business Impact:** Prevent data leaks, protect brand.

---

*Version 1.0 – Georg Wiesmüller*

