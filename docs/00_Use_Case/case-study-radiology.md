# 📌 Case Study: Radiology AI – DICOM Data Processing

This case study illustrates GDPR and EU AI Act compliance challenges for AI systems used in **radiological diagnostics**.

---

## ✅ Business Context

Hospitals and clinics increasingly use AI systems to assist radiologists in diagnosing conditions from DICOM images (e.g., X-rays, CT scans, MRIs).  

AI models analyze **special category health data** to detect anomalies, prioritize urgent cases, and suggest differential diagnoses.  

---

## ✅ Data Characteristics

- Large DICOM imaging files
- Embedded PHI (Patient Identifiers, Date of Birth)
- Metadata (Modality, Acquisition Parameters)

---

## ✅ GDPR Challenges

- **Article 9:** Processing special category data requires explicit consent.
- **Article 25:** Privacy by Design for storage and transmission.
- **Article 32:** Security of processing, encryption of imaging archives.
- **Article 44:** Cross-border data sharing (e.g., cloud AI analysis).

---

## ✅ EU AI Act (2024) High-Risk Classification

- Annex III → Medical Diagnostic Systems = High-Risk AI
- Requires:
  - Risk Management System
  - Logging and Traceability
  - Human Oversight
  - CE Marking under MDR (Medical Device Regulation)

---

## ✅ SIEM Use Cases

- Detect unencrypted storage of imaging archives.
- Alert on exports of DICOM files to non-EU locations.
- Monitor consent verification before AI analysis.
- Log user access to imaging data.
- Detect unusual API calls (e.g., bulk export attempts).

---

## ✅ Recommended Technical & Organizational Measures

- AES-256 encryption at rest; TLS 1.3 in transit.
- Consent management integrated with PACS/RIS systems.
- Immutable logging of access and processing events.
- Role-Based Access Controls (RBAC) for radiology staff.
- Pseudonymization of DICOM metadata before AI processing.

---

## ✅ SIEM Rulebook Example

- Detection Rule: Non-EU Export of DICOM Files without Consent
- Severity: High
- GDPR Mapping: Article 44
- AI Act Mapping: High-Risk Logging Requirement
- HIPAA Mapping: Transmission Security
- Business Impact: Avoid €20M fines; ensure cross-border compliance.
