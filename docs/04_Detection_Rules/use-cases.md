# Healthcare AI SIEM Rulebook – Use Cases

This section documents the **detection use cases** prioritized for SIEM monitoring in Healthcare AI environments.

---

## UC-01: Non-EU Data Export without Consent

- **Description:** Detects data exports to Non-EU destinations without documented patient consent.
- **Severity:** High
- **Risk Impact:** High
- **Likelihood:** Medium
- **Priority:** High
- **GDPR Mapping:** Article 44 (Transfers to third countries)
- **AI Act Mapping:** High-Risk System Logging Requirement
- **HIPAA Mapping:** Transmission Security
- **Business Impact:** Avoid GDPR fines up to €20 million (Art. 44). Estimated cost savings ~€500,000 in legal fees, audit readiness, and cross-border compliance mitigation.


---

## UC-02: Access to Unencrypted Raw Data

- **Description:** Detects access to storage locations without encryption at rest.
- **Severity:** High
- **Risk Impact:** High
- **Likelihood:** High
- **Priority:** High
- **GDPR Mapping:** Article 32 (Security of processing)
- **AI Act Mapping:** Risk Management Measures
- **HIPAA Mapping:** Encryption/Decryption Controls
- **Business Impact:** Prevent data breach penalties (Art. 32), up to €10 million fines. Estimated cost savings ~€300,000 through proactive encryption monitoring and breach response reduction.

---

## UC-03: AI Model Manipulation / Data Poisoning

- **Description:** Detects unusual data uploads that could poison AI training.
- **Severity:** Medium
- **Risk Impact:** High
- **Likelihood:** Low
- **Priority:** Medium
- **GDPR Mapping:** Article 5 (Integrity), Article 25 (Privacy by Design)
- **AI Act Mapping:** High-Risk System Security
- **HIPAA Mapping:** Integrity Controls
- **Business Impact:** Avoid compromised diagnoses and reputational loss. Estimated mitigation value ~€200,000 in incident response and regulatory investigations.

---

## UC-04: Unauthorized Access to PHI

- **Description:** Detects user accounts accessing Protected Health Information without proper RBAC authorization.
- **Severity:** High
- **Risk Impact:** High
- **Likelihood:** Medium
- **Priority:** High
- **GDPR Mapping:** Article 32 (Access control)
- **AI Act Mapping:** Logging / Oversight
- **HIPAA Mapping:** Access Control Standard
- **Business Impact:** Avoid breach notifications and fines up to €20 million (Art. 32). Estimated cost savings ~€400,000 in legal penalties and patient trust protection.

---

## UC-05: Excessive Data Fields without Minimization

- **Description:** Detects storage of unnecessary data fields violating data minimization principles.
- **Severity:** High
- **Risk Impact:** Medium
- **Likelihood:** High
- **Priority:** High
- **GDPR Mapping:** Article 5(1)(c) (Data Minimization)
- **AI Act Mapping:** Risk Management
- **HIPAA Mapping:** Minimum Necessary Standard
- **Business Impact:** Ensure compliance with GDPR Art. 5(1)(c). Estimated savings ~€150,000 in audit remediation costs and overcollection penalties.

---

## UC-06: Consent Check Failures

- **Description:** Detects transactions lacking consent verification step.
- **Severity:** High
- **Risk Impact:** High
- **Likelihood:** Medium
- **Priority:** High
- **GDPR Mapping:** Article 6, 9 (Lawfulness of Processing)
- **AI Act Mapping:** Logging of High-Risk Processing
- **HIPAA Mapping:** Authorization Requirements
- **Business Impact:** Avoid processing without legal basis (Art. 6, 9). Estimated cost savings ~€250,000 in fines, legal reviews, and reputational damage.

---

## UC-07: Cloud Misconfiguration (Open Buckets)

- **Description:** Detects misconfigured cloud storage with public access.
- **Severity:** Medium
- **Risk Impact:** High
- **Likelihood:** Low
- **Priority:** Medium
- **GDPR Mapping:** Article 32
- **AI Act Mapping:** Risk Management, Security by Design
- **HIPAA Mapping:** Transmission Security, Integrity
- **Business Impact:** Prevent data leaks and fines (Art. 32). Estimated cost savings ~€200,000 in breach response, brand protection, and regulator fines.

---



