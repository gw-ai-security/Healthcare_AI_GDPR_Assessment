# 🛡️ Security Architecture – Healthcare AI System

This document outlines the technical and organizational security measures implemented in the Healthcare AI GDPR Dashboard. These measures follow principles of Privacy by Design (Art. 25 GDPR), Security of Processing (Art. 32), and industry best practices (ISO 27001, NIST CSF).

---

## 🔐 Authentication & Access Control

| Control           | Description                                                                 |
|-------------------|-----------------------------------------------------------------------------|
| Multi-Factor Authentication (MFA) | All users must pass an MFA step before accessing dashboard views. |
| Role-Based Access Control (RBAC) | Access to CISO, DPO, SOC, Auditor views is limited by user role. |
| Session Timeout   | Inactivity results in automatic logout after X minutes.                      |

---

## 📋 Audit Logging & Monitoring

| Feature             | Description                                                             |
|---------------------|-------------------------------------------------------------------------|
| Audit Trail Logging | All user actions (view access, export, updates) are timestamped and logged. |
| GDPR Art. 30 Mapping | All alerts and exports are traceable to their relevant Article.        |
| Anomaly Monitoring  | Sudden access patterns trigger SOC alerts.                             |

---

## 🔒 Data Protection Measures

| Control             | Description                                                             |
|---------------------|-------------------------------------------------------------------------|
| Pseudonymization    | Patient IDs are pseudonymized using SHA256.                             |
| Field-Level Masking | High-risk fields (e.g., diagnosis code) are masked per role.            |
| Data Minimization   | Only relevant fields for the user's role are visible in the UI.         |
| Secure Storage      | Logs stored with AES-256 encryption (optional backend feature).         |

---

## ⚙️ System Architecture Highlights

| Component        | Security Feature                                      |
|------------------|--------------------------------------------------------|
| Streamlit Frontend | Session state protection, routing enforcement        |
| Backend Storage   | Encrypted CSV / DB storage for alert and log data     |
| Playbook Engine   | AI incident responses (consent breach, model drift)   |
| Export Interface  | PDF/CSV export only available for authenticated users |

---

## ✅ Compliance Alignment

| Regulation        | Security Feature Alignment                          |
|-------------------|------------------------------------------------------|
| **GDPR Art. 5**   | Purpose limitation, data minimization                |
| **GDPR Art. 25**  | Privacy by Design – RBAC, Pseudonymization           |
| **GDPR Art. 30**  | Full audit trail with subject-level traceability     |
| **GDPR Art. 32**  | Access control, logging, encryption                  |
| **ISO/IEC 27001 A.9** | Access management and role controls             |
| **NIST CSF**      | Identify, Protect, Detect, Respond, Recover          |

---

## 🛠️ Future Improvements

- 🔐 Integration with enterprise IAM systems (e.g., Azure AD)
- 📈 Real-time alerting dashboard (Streamlit + Kafka or similar)
- 🧠 AI-powered anomaly detection (auto-tuning thresholds)
- 📊 Visual access matrix per role / GDPR article


