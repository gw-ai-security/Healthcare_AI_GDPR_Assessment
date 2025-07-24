# Repository Structure and Purpose

This repository combines three strategic modules:

- **Project 1.1** – GDPR Compliance & Privacy-by-Design Audit
- **Project 1.2** – SIEM Detection Rulebook with Risk Prioritization
- **Project 1.3** – Security Analytics Dashboard (Role-Based)

All folders and files are interconnected to provide end-to-end **AI security analysis, regulatory mapping, threat detection, and audit reporting** for a healthcare AI use case.

---

## Root Directory

| File | Purpose |
|------|---------|
| `README.md` | Project overview, objectives, architecture, usage instructions |
| `FILES.md` | Describes every folder and file in this repo (you are reading it) |
| `LICENSE` | Repository usage rights (MIT License) |
| `requirements.txt` | Python dependencies (Streamlit, pandas, etc.) |

---

## `app/` – Security Analytics Dashboard

Streamlit-based application with role-specific KPI dashboards and RBAC.

| File | Purpose |
|------|---------|
| `main.py` | Entry point to load the correct dashboard view |
| `audit_logger.py` | Logs all user activity for GDPR Art. 30 traceability |
| `ciso_view.py` | KPI view for Chief Information Security Officers |
| `dpo_view.py` | View for Data Protection Officers: consent violations, article mapping |
| `soc_view.py` | SOC-centric view: alert timeline, rule coverage |
| `auditor_view.py` | Auditor-focused view: exportable logs, DSFA linkage |
| `.streamlit/` | Configuration (theme, secrets, RBAC) |
| `utils/` | Internal helper functions, init files |

---

## `dashboards/` – Role Mapping & Metrics Logic

| File | Purpose |
|------|---------|
| `compliance_mapping.md` | Table: GDPR Article ↔ Rule ↔ Dashboard KPI |
| `stakeholder_views.md` | Describes dashboard requirements by persona (CISO, SOC, DPO) |
| `security_architecture.md` | Describes RBAC, MFA, pseudonymization, audit trail strategy |

---

## `data/` – AI System Logs (Simulated)

| File | Purpose |
|------|---------|
| `healthcare_logs.csv` | Raw log data from the AI system (e.g., patient ID, consent, diagnosis) |
| `alerts_simulated.csv` | Post-processed alerts used for dashboard simulation |
| `alerts_simulated.xlsx` | Excel version (for workshops/presentations) |
| `alerts_siem_ready.csv` | Final alert set formatted for detection rule testing |

---

## `docs/` – Complete Compliance & Threat Analysis

### `00_Use_Case/`

| File | Purpose |
|------|---------|
| `Business_Use_Case.md` | Explains the clinical AI scenario, risks, stakeholder roles |
| `GDPR_Requirements.md` | Mapping of system behavior to GDPR Articles |
| `Stakeholder_Analysis.md` | Summary of affected roles and compliance goals |

### `01_Regulatory_Context/`

| File | Purpose |
|------|---------|
| `healthcare-ai-challenges.md` | Industry-specific risks in medical AI systems |
| `regulatory-context.md` | Overview of GDPR, HIPAA, EU AI Act relevance |
| `technical-organizational-measures.md` | Summary of implemented TOMs for Art. 32 compliance |

### `02_Dataflow/`

| File | Purpose |
|------|---------|
| `data-flow.md` | Data movement diagram and textual explanation |

### `03_Checklists/`

| File | Purpose |
|------|---------|
| `GDPR_Checklist.md` | Article 25 audit checklist |
| `Field_GDPR_Mapping.md` | Mapping of CSV log fields to GDPR relevance |
| `Ethical_Considerations.md` | Bias, transparency, fairness measures |
| `Threat_Model.md` | STRIDE model: Prompt Injection, Model Poisoning, etc. |

### `04_Detection_Rules/`

| File | Purpose |
|------|---------|
| `Detection_Rules.md` | All detection rules with queries, mappings, severity |
| `use-cases.md` | Rule use case definitions, source violations |
| `mapping-overview.md` | Rule ↔ Alert ↔ Business Impact |
| `risk-prioritization.md` | Risk × Likelihood matrix for rule triage |
| `DSFA_Outline.md` | High-level Data Protection Impact Assessment |

### `99_Audit_Report/`

| File | Purpose |
|------|---------|
| `Audit_Report.md` | Final executive report: findings, violations, risk exposure |

---

## `framework/` – Reusable Templates

| File | Purpose |
|------|---------|
| `GDPR_Assessment_Template.md` | Privacy-by-design checklist |
| `Detection_Rule_Template.md` | Rule logic, mapping, impact, mitigation |
| `Incident_Response_Playbook.md` | Incident response for AI/LLM-specific attacks |
| `DSFA_Template.md` | Template for DPIA based on ENISA & EDPB |
| `Stakeholder_Analysis_Template.md` | Template for role mapping and risk linkage |

---

## `logs/` – Audit Logging

| File | Purpose |
|------|---------|
| `audit_log.csv` | Export of actions taken by dashboard users |
| `README.md` | Explains log structure and compliance context (Art. 30 GDPR) |

---

## `notebooks/` – Data Analysis & Simulation

| File | Purpose |
|------|---------|
| `01_Data_Preparation.ipynb` | Initial log parsing, formatting, tagging |
| `02_Feature_engineering.ipynb` | Risk scoring, consent tagging, anonymization |
| `03_Visualization.ipynb` | Risk heatmaps, article violation trends |
| `04_Detection_Simulation.ipynb` | Simulates detection triggers based on rules |
| `05_Risk_Distribution.ipynb` | Graphs risk by actor / department / location |
| `06_Rule_Mapping.ipynb` | Maps alerts → rules → business metrics |
| `07_DSFA_Risk_Matrix.ipynb` | Risk assessment matrix used in DSFA |

---

## `policies/` – Operational and Legal Policies

| File | Purpose |
|------|---------|
| `ai-usage-policy.md` | Defines internal rules for responsible AI |
| `consent-form-template.md` | GDPR-aligned sample form for clinical use |
| `data-protection-policy.md` | Technical and organizational measures (TOMs) overview |

---

## `scenarios/` – Simulated Risk Scenarios

| File | Purpose |
|------|---------|
| `incident_scenarios.md` | 5 clinical incidents (e.g., model manipulation, data leak, insider threat) |

---

## `scripts/` – Utility Scripts (TBC)

| Purpose | Notes |
|---------|-------|
| Currently used for automated alert generation, format validation or future extensions |
