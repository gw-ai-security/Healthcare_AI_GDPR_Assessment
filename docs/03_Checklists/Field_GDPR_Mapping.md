# Field-to-GDPR Article Mapping

This document maps specific data fields in the Healthcare AI system logs to GDPR articles and compliance principles.

---

## Purpose
To demonstrate how each data field is covered by GDPR requirements, making compliance checks auditable and clear.

---

## Mapping Table

| Field Name       | GDPR Article / Principle             | Compliance Requirement                                         | Notes / Observations                   |
|-------------------|-------------------------------------|----------------------------------------------------------------|----------------------------------------|
| UserID            | Art. 5 - Purpose Limitation         | Must only be used for diagnosis and audit purposes             | Consider pseudonymization              |
| Timestamp         | Art. 5 - Data Minimization          | Store only if necessary for auditing and traceability          | Define retention period                |
| DiagnosisCode     | Art. 9 - Special Categories         | Requires explicit consent and special safeguards                | Encrypt or pseudonymize in logs        |
| Country           | Art. 44 - Transfers to Non-EU       | Must ensure adequacy decision or safeguards (e.g. SCCs)         | Document transfer mechanisms           |
| ConsentStatus     | Art. 7 - Consent Management         | Must verify and document consent for processing                 | Ensure auditability                    |
| PseudonymizedID   | Art. 25 - Privacy by Design         | Data should be pseudonymized wherever possible                  | Review implementation                  |
| AccessedBy        | Art. 32 - Security of Processing    | Access controls must be enforced and logged                     | Include in access control policies     |
| DataSource        | Art. 5 - Purpose Limitation         | Must be clearly documented and limited to legitimate purposes   | Keep source tracking for audits        |
| ProcessingPurpose | Art. 5 - Purpose Limitation         | Must match documented, specific purposes                        | Avoid purpose creep                    |

---

## Notes on Use
- This table is designed to be reviewed with the DPO and Security teams.
- Observations should be updated with real system checks.
- Helps create clear audit trails and mitigation plans.

---

## Outcome
A documented, traceable mapping of all logged data fields to GDPR requirements:
- Supports Privacy by Design reviews.
- Helps identify compliance gaps.
- Provides clear guidance for developers and security architects.

