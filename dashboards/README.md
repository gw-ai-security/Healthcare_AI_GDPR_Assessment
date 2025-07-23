# Healthcare AI GDPR Dashboard – Stakeholder & Compliance Views

This module provides a structured foundation for a GDPR-compliant, stakeholder-aware dashboard designed to monitor AI-driven healthcare systems. It extends the use cases and detection logic from Project 1.2 and connects them with real-time, role-specific risk visibility and compliance mapping.

---

## Objective

To visualize and operationalize:
- GDPR violations and SIEM alerts
- Role-based KPIs (CISO, DPO, SOC, Auditor)
- Business risk and regulatory impact
- AI threats like model drift or adversarial misuse

---

## Contents

| File                            | Purpose                                                              |
|----------------------------------|----------------------------------------------------------------------|
| `stakeholder_views.md`         | Definition of role-specific dashboard components and KPIs            |
| `security_architecture.md`     | Technical and organizational controls: RBAC, MFA, pseudonymization   |
| `compliance_mapping.md`        | Table linking GDPR articles ↔ SIEM rules ↔ dashboard ↔ business risk |

---

## Roles & Views

Each dashboard view is mapped to the needs of:

- **CISO:** Risk trends, incident KPIs, ROI
- **DPO:** Consent violations, GDPR Article breakdown
- **SOC Analyst:** Real-time alerts, rule hits, MTTR
- **Auditor:** Art. 30 exports, documentation completeness

See [`stakeholder_views.md`](./stakeholder_views.md) for full role breakdown.

---

## Security Architecture Overview

Key features include:

- Role-Based Access Control (RBAC)
- Multi-Factor Authentication (MFA)
- Audit logging for all access/export actions
- Data minimization and pseudonymization
- Article 30 traceability

See [`security_architecture.md`](./security_architecture.md) for technical details.

---

##  Compliance Traceability

This dashboard directly supports:

| Regulation         | Covered By                            |
|--------------------|----------------------------------------|
| GDPR Art. 25       | Privacy by Design / UI Role Filtering  |
| GDPR Art. 30       | Audit Logging & Export Traceability    |
| GDPR Art. 32       | Security of Processing & Access Control|
| EU AI Act (Annex III) | High-risk classification reporting |
| ISO/IEC 27001      | Annex A.9, A.12 – Logging, Access      |

➡ See [`compliance_mapping.md`](./compliance_mapping.md) for full traceability chain.

---

##  Next Development Steps

-  `main.py` + Streamlit dashboard routing
-  Individual role views (`ciso_view.py`, `dpo_view.py`, etc.)
-  Data integration (log parsing, KPIs, charting)
-  Export features (PDF, CSV) per stakeholder

---

## How to Use

Once deployed (e.g., via Streamlit Cloud or container), the dashboard provides:
- Secure login
- Role-based view routing
- Real-time and historical alert visibility
- GDPR impact metrics and documentation export

---

## Tip

This folder complements the rule logic from `/docs/Detection_Rules.md`  
and the audit reporting in `/docs/Audit_Report.md`.

---


