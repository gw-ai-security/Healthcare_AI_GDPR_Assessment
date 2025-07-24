# GDPR Privacy by Design Checklist

This document provides an actionable checklist for ensuring GDPR compliance (particularly Article 25 - Privacy by Design) when assessing Healthcare AI systems.

---

## Purpose
To translate GDPR principles into practical, auditable questions for AI system assessments.

---

## GDPR Article Mapping – Detailed Audit Checklist

This checklist translates key GDPR Articles into **practical audit questions** for Healthcare AI systems.

| GDPR Article | Purpose                                | Audit Questions                                                            |
|---------------|----------------------------------------|----------------------------------------------------------------------------|
| **Art. 5**    | Principles of Processing               | - Is data minimization enforced in data models?<br>- Is purpose limitation documented?<br>- Is transparency ensured in AI explanations? |
| **Art. 6**    | Lawfulness of Processing               | - Is a valid lawful basis documented for each processing activity?<br>- Are consent records linked to processing logs? |
| **Art. 9**    | Special Categories of Data             | - Is explicit consent obtained for health data?<br>- Is consent verifiable in logs?<br>- Are special categories flagged in SIEM events? |
| **Art. 25**   | Privacy by Design and by Default       | - Are encryption and pseudonymization implemented?<br>- Is access control enforced via RBAC?<br>- Is data minimization enforced at design stage? |
| **Art. 32**   | Security of Processing                 | - Is data encrypted at rest and in transit?<br>- Are access logs monitored?<br>- Is SIEM alerting in place for unauthorized access? |
| **Art. 44+**  | Transfers to Third Countries           | - Is consent required and logged for non-EU transfers?<br>- Is adequacy decision verified?<br>- Is data transfer logging enabled? |

---

**Consulting Notes:**
- This table can be used during client workshops to document compliance gaps.
- Supports Privacy Impact Assessments (DPIA) and Data Protection Impact Analyses.
- Maps directly to SIEM Use Cases and Detection Rules.

---

## Checklist Table

| Principle              | Audit Question                                                       | Status | Notes/Actions                           |
|-------------------------|---------------------------------------------------------------------|--------|-----------------------------------------|
| Data Minimization       | Are only strictly necessary data fields collected and processed?    | [ ]    |                                         |
| Purpose Limitation      | Is data used exclusively for its documented purpose?                | [ ]    |                                         |
| Storage Limitation      | Is there a retention policy with defined deletion timelines?        | [ ]    |                                         |
| Accuracy                | Are data correction procedures in place?                            | [ ]    |                                         |
| Integrity & Confidentiality | Is encryption or pseudonymization applied where needed?         | [ ]    |                                         |
| Access Control          | Are access rights restricted to authorized personnel only?          | [ ]    |                                         |
| Consent Management      | Is explicit consent documented and verifiable?                      | [ ]    |                                         |
| Logging & Monitoring    | Are access and processing logs maintained and auditable?            | [ ]    |                                         |
| Transfers to Non-EU     | Are safeguards (e.g. SCCs) in place for non-EU data transfers?      | [ ]    |                                         |
| Privacy by Default      | Are the least privacy-invasive settings used by default?            | [ ]    |                                         |

---

## Notes on Use
- Each question should be reviewed during the assessment.
- Status can be marked as [✔] compliant or [✖] non-compliant.
- Notes/Actions column is for remediation planning.

---

## Outcome
A completed, auditable checklist that:
- Documents GDPR compliance status.
- Identifies gaps and necessary mitigation actions.
- Supports DPO and Security teams in audits.

