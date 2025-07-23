# Documentation – Healthcare AI GDPR Compliance Project

This `/docs` folder contains the structured documentation and consulting deliverables for the Healthcare AI Security & GDPR Compliance Assessment.

The documents are organized into thematic modules aligned with GDPR principles, SIEM detection logic, threat modeling, and audit readiness.

---

## Folder Structure

| Folder               | Description                                                           |
|----------------------|-----------------------------------------------------------------------|
| `00_Use_Case/`       | Business use case, GDPR requirements, stakeholder analysis            |
| `01_Regulatory_Context/` | Legal and ethical landscape incl. AI-specific risks and obligations |
| `02_Dataflow/`       | Visualizations and documentation of data processing and movement      |
| `03_Checklists/`     | Compliance checklists, field mappings, threat model                  |
| `04_Detection_Rules/`| Detection logic, use case mapping, DSFA, risk scoring                 |
| `99_Audit_Report/`   | Final audit report and executive summary                              |

---

## `00_Use_Case/` – Use Case Definition & Stakeholder Roles

- `Business_Use_Case.md`: Real-world AI healthcare scenario (radiology diagnostics)  
- `GDPR_Requirements.md`: Relevant GDPR Articles (Art. 5, 7, 9, 25, 32, 44)  
- `Stakeholder_Analysis.md`: Roles incl. CISO, DPO, AI Product Owner  

Subfolder: `00_Case_Studies/` → for future use

---

##  `01_Regulatory_Context/` – Legal Landscape & AI Threats

- `regulatory-context.md`: Summary of applicable legal frameworks (GDPR, AI Act, HIPAA)  
- `technical-organizational-measures.md`: Access controls, encryption, pseudonymization  
- `healthcare-ai-challenges.md`: Sector-specific risks (IoMT, data poisoning, drift)

---

##  `02_Dataflow/` – Transparency & Traceability

- `data-flow.md`: Data processing path and system boundaries (Mermaid/draw.io)

---

##  `03_Checklists/` – GDPR Compliance Verification

- `GDPR_Checklist.md`: Operationalized checklist of GDPR controls (Art. 5, 25, 32...)  
- `Field_GDPR_Mapping.md`: Mapping data fields ↔ GDPR legal basis  
- `Ethical_Considerations.md`: Bias, fairness, human oversight (Art. 22)  
- `Threat_Model.md`: STRIDE + AI-specific attack surface

---

##  `04_Detection_Rules/` – SIEM Logic, DSFA & Use Cases

- `Detection_Rules.md`: 5–7 GDPR-relevant SIEM detection rules  
- `use-cases.md`: Use case descriptions incl. severity and response  
- `risk-prioritization.md`: Likelihood x Impact matrix  
- `mapping-overview.md`: GDPR ↔ Rule ↔ Business Impact  
- `DSFA_Outline.md`: Privacy risk assessment incl. fine potential  

---

##  `99_Audit_Report/` – Executive-Ready Output

- `Audit_Report.md`: Structured summary incl.  
  - GDPR violations detected  
  - Risk heatmap overview  
  - Recommendations & next steps  
  - Cost/Benefit estimations  
  - Appendix links to rules, mapping, DSFA

---

##  How to Use

- For **auditors**: start at `Audit_Report.md`  
- For **security architects**: go to `Detection_Rules.md` + `Threat_Model.md`  
- For **data protection officers (DPO)**: use `GDPR_Checklist.md`, `Stakeholder_Analysis.md`, `DSFA_Outline.md`

---

##  Recommended Entry Points

- [Use Case & Stakeholders](./00_Use_Case/Business_Use_Case.md)  
- [Detection Logic](./04_Detection_Rules/Detection_Rules.md)  
- [Threat Model](./03_Checklists/Threat_Model.md)  
- [Audit Report](./99_Audit_Report/Audit_Report.md)

---



