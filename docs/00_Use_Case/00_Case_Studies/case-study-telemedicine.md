# 📌 Case Study: Telemedicine Platform – Cross-Border Data Processing

This case study analyzes GDPR and security compliance challenges for **telemedicine platforms** providing remote patient consultations.

---

## ✅ Business Context

Telemedicine platforms connect doctors and patients via video, chat, and file sharing.  
Features include:
- Remote diagnosis
- Prescription services
- Integration with local EHR systems

These platforms often use **cloud-based APIs** that may involve **cross-border data transfers** (EU / Non-EU).

---

## ✅ Data Characteristics

- Personal identifiers (Name, Address, Insurance)
- Special category health data (Diagnosis, Treatment Notes)
- Video / Audio consultation records
- Prescription data

---

## ✅ GDPR Challenges

- **Article 6:** Lawfulness of processing with clear purpose.
- **Article 9:** Special category data requiring explicit consent.
- **Article 25:** Privacy by Design in cloud infrastructure.
- **Article 32:** Secure transmission and storage.
- **Article 44+:** Transfers to third countries requiring adequate safeguards.

---

## ✅ EU AI Act (2024) High-Risk Classification

- High-Risk AI if recommending treatments or triaging patients.
- Requirements:
  - Risk Management System
  - Logging and Traceability
  - Human Oversight
  - CE Marking for medical device modules

---

## ✅ SIEM Use Cases

- Detect unencrypted video session storage.
- Alert on data exports to Non-EU regions without consent.
- Monitor consent status before consultations.
- Log access to sensitive consultation records.
- Detect anomalous API calls to third-party services.

---

## ✅ Recommended Technical & Organizational Measures

- AES-256 encryption for stored recordings.
- TLS 1.3 for video streaming sessions.
- Consent Management integrated in booking workflow.
- Immutable logging of consultations and consent.
- RBAC for medical staff and admin users.
- Geo-fencing of data storage locations.

---

## ✅ SIEM Rulebook Example

- Detection Rule: Non-EU Data Transfer without Consent Verification
- Severity: High
- GDPR Mapping: Article 44
- AI Act Mapping: High-Risk Logging Requirement
- HIPAA Mapping: Transmission Security
- Business Impact: Avoid €20M fines; maintain cross-border compliance.
