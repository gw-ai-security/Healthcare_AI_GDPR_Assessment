
# 🛡️ Healthcare AI GDPR Compliance Assessment

_A consulting-ready, audit-grade framework to ensure GDPR and AI Act compliance for machine learning systems in healthcare._

---

## 🎯 Project Goal

Deliver a **complete, realistic, portfolio-ready framework** simulating a full consulting engagement for healthcare AI systems, including:

- Data flow and processing risk analysis
- GDPR & EU AI Act requirement mapping
- SIEM rulebook with detection logic and FP/FN strategies
- Threat modeling (STRIDE) and DSFA
- Ethical AI and bias considerations
- Executive-level audit documentation

---

## 📌 Why It Matters

Healthcare AI systems process **special category data** (GDPR Art. 9) and are classified as **High-Risk AI Systems** under the **EU AI Act (2024)**. They require:

- Explicit, traceable consent
- Purpose limitation and minimization
- Technical and Organizational Measures (TOMs)
- Human oversight and explainability (Art. 22)
- Robust detection and audit mechanisms

**Non-compliance = Up to €20 million or 4% of turnover.**

---

## ✅ What This Framework Provides

- ✔️ Real-world use cases from radiology, wearables, and telemedicine
- ✔️ Threat modeling and detection use case mapping
- ✔️ False positive/negative tuning strategies
- ✔️ DSFA structure and risk matrix
- ✔️ Reusable consulting templates and checklists
- ✔️ Ethical AI documentation and GDPR field mapping
- ✔️ Executive-ready audit report for stakeholders

---

## 📂 Repository Structure

| Folder        | Purpose                                                      |
|----------------|-------------------------------------------------------------|
| `/docs`       | Full documentation, use cases, detection rules, audit report |
| `/framework`  | Reusable consulting templates (GDPR, DSFA, rules)           |
| `/policies`   | Sample policies (data protection, AI usage, consent forms)  |
| `/data`       | Synthetic healthcare logs with GDPR violations              |
| `/diagrams`   | System architecture and dataflow diagrams                   |
| `/notebooks`  | Jupyter notebooks for parsing, cleaning, risk scoring       |
| `/scripts`    | Pseudonymization and compliance utilities                   |
| `/templates`  | Markdown templates for assessments and playbooks            |

---

## 🗂️ Highlights

### ✅ /docs

- 📄 `Business_Use_Case.md`: AI usage in healthcare (radiology, IoT, telemedicine)
- 👥 `Stakeholder_Analysis.md`: CISO, DPO, SOC, PM
- ⚖️ `GDPR_Requirements.md`: Art. 5, 7, 9, 25, 32, 44
- 🧾 `Detection_Rules.md`: 5 use cases, queries, FP/FN, AI Act mapping
- 📊 `risk-prioritization.md` + `DSFA_Outline.md`
- 🔒 `technical-organizational-measures.md`: Encryption, RBAC, pseudonymization
- 🔎 `Threat_Model.md`: STRIDE for AI pipelines
- 🧠 `Ethical_Considerations.md`: Bias, explainability, human oversight
- 📑 `Audit_Report.md`: Full summary, risk matrix, recommendations

---

### ✅ /framework

Templates for:

- Stakeholder analysis
- GDPR field assessments
- Detection rule design
- DSFA reports
- Incident response playbooks

---

### ✅ /policies

Example policies:

- Data Protection Policy
- AI Usage Policy
- Consent Form Template (Art. 7)

---

## 🛠️ Tech Stack

- **Languages:** Markdown, Python (Jupyter)
- **Libraries:** pandas, matplotlib, seaborn
- **SIEM Logic:** Elastic DSL, YAML (Sigma-compatible)
- **Model Analysis:** Optional ML drift logic via `Evidently`
- **Diagrams:** draw.io, Mermaid

_All free, open-source, and consulting-compatible._

---

## 📌 How To Use

1️⃣ **Understand the Use Case**
   → `/docs/00_Use_Case/Business_Use_Case.md`

2️⃣ **Analyze Synthetic Logs**
   → `/data/healthcare_logs.csv`  
   → Notebooks: cleaning, enrichment, risk scoring

3️⃣ **Apply Legal Mapping**
   → `/docs/GDPR_Checklist.md`  
   → `/docs/Field_GDPR_Mapping.md`

4️⃣ **Design and Validate Detection Rules**
   → `/docs/Detection_Rules.md` (FP/FN strategies included)

5️⃣ **Conduct Risk Assessment**
   → `/docs/DSFA_Outline.md`  
   → `/docs/risk-prioritization.md`

6️⃣ **Model Threats (STRIDE)**
   → `/docs/Threat_Model.md`

7️⃣ **Review Ethical AI Risks**
   → `/docs/Ethical_Considerations.md`

8️⃣ **Generate Final Audit Report**
   → `/docs/Audit_Report.md`

---

## ✅ Final Outcome

✔️ **Audit-ready documentation & detection rulebook**  
✔️ Aligns with **GDPR Articles 5, 9, 25, 32, 44**  
✔️ Supports **EU AI Act Conformity Readiness**  
✔️ Includes **Risk Matrix, DSFA, STRIDE, Ethical Analysis**  
✔️ Fully reusable for client engagements or interviews

---

## 💼 Target Users

- Security Architects
- DPOs and Data Privacy Officers
- AI Product and Risk Managers
- Compliance Officers
- Privacy & GRC Consultants

---

## 📜 License

MIT License – see LICENSE for details.

---

## ✉️ Author

**Georg Wiesmüller**  
Open an [Issue](https://github.com/gw-ai-security/Healthcare_AI_GDPR_Assessment/issues) or PR to contribute, improve, or collaborate.
