# 📌 Regulatory Context

This section explains the **regulatory frameworks** that define the requirements for this SIEM Rulebook for healthcare AI systems.

---

## ✅ GDPR (General Data Protection Regulation)

The **GDPR** (EU Regulation 2016/679) applies to any processing of personal data in the EU, especially **special category data** such as health information (Article 9).

**Key GDPR articles relevant for SIEM monitoring:**
- **Article 5:** Principles of data processing (lawfulness, fairness, transparency, purpose limitation, data minimization)
- **Article 25:** Privacy by Design and by Default
- **Article 32:** Security of processing
- **Article 44+:** Restrictions on international data transfers

**SIEM Rules must support:**
- Detection of unauthorized data exports
- Ensuring consent is recorded before transfers
- Monitoring of encryption and access controls

---

## ✅ EU AI Act (2024) – High-Risk Classification

The **EU Artificial Intelligence Act (2024 Final)** explicitly classifies many Healthcare AI systems as **High-Risk** under Annex III. This includes:

- AI systems for medical diagnosis and treatment recommendations
- Clinical decision support systems
- Radiology / Imaging analysis
- Patient triage and risk scoring
- Digital health assistants

**Key Requirements:**
- Comprehensive Risk Management System (Article 9)
- Logging and Traceability for model decisions (Article 12)
- Human Oversight and Interventions (Article 14)
- High-Quality Datasets to reduce bias (Article 10)
- CE Marking and Conformity Assessments (Chapter IV)

**SIEM Rulebook Implications:**
- Detect missing or incomplete logs
- Monitor for consent verification failures
- Alert on unauthorized model access or data exports
- Provide audit-ready evidence for oversight

---

## ✅ National Legislation – Germany Example

In addition to the EU GDPR and AI Act, healthcare providers in Germany must comply with **national health data regulations**, such as:

- **KHZG (Krankenhauszukunftsgesetz):**
  - German Hospital Future Act mandating digitization of healthcare facilities.
  - Requires secure IT infrastructure, audit logging, access control, and interoperability standards.
  - Funding eligibility tied to meeting security-by-design requirements.

- **GDSG (Gesundheitsdatenschutzgesetz, planned):**
  - Proposed German Health Data Protection Act harmonizing GDPR with sector-specific rules.
  - Expected to define stricter consent requirements for research, stronger pseudonymization obligations, and clearer logging mandates.

**SIEM Rulebook Implications:**
- Monitor access logs to meet KHZG security funding criteria.
- Provide consent verification evidence aligned with German rules.
- Enable reporting capabilities for cross-border data transfers and research use.

---

## ✅ HIPAA (Health Insurance Portability and Accountability Act)

**HIPAA** applies to US-based healthcare providers processing Protected Health Information (PHI).

**Key points for Security Monitoring:**
- Audit Controls (45 CFR §164.312(b)): Record and examine activity in systems with PHI
- Integrity Controls
- Person or Entity Authentication
- Transmission Security (encryption)

**Relevance for SIEM:**
- Cross-border compliance (US-EU data flows)
- Unified monitoring strategy for global healthcare providers

---

## ✅ EHDS (European Health Data Space)

The **EHDS** proposal (2022–2023) establishes a framework for health data sharing within the EU.

**Key considerations:**
- Data sharing requires patient consent and strong security
- Interoperability and standardized logging
- Transparency obligations

---

## ✅ How This Rulebook Supports Compliance

This Rulebook maps detection use cases to these regulatory requirements, ensuring:

- Documentation of legal basis for monitoring
- Privacy-by-Design approach with technical and organizational measures
- Detection Rules aligned with regulatory articles
- Audit-ready evidence for regulators and clients

---

*Version 1.0 – Georg Wiesmüller*

