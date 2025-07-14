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

## ✅ EU AI Act

The **EU AI Act** (2023 draft) classifies certain AI systems as **High-Risk**, including those used in healthcare diagnostics.

**Key points:**
- High-Risk AI systems require risk management systems, logging, human oversight
- SIEM Rules must detect anomalies in AI data flows
- Compliance requires explainability and traceability of decisions

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

