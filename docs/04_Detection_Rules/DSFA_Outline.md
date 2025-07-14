# DSFA Outline

This document serves as a template for conducting a **Data Protection Impact Assessment (DPIA/DSFA)** for the Healthcare AI GDPR Compliance Assessment project.

---

## 🎯 Purpose
To identify, analyze, and mitigate privacy risks associated with processing sensitive health data via an AI system.

---

## 📌 DPIA Sections

### 1️⃣ Description of Processing
- Purpose of the AI system
- Categories of data processed (e.g. diagnosis codes, timestamps)
- Data flows and storage locations
- Transfers to non-EU countries

✅ *Example:*  
"AI system for radiology analysis processes patient diagnosis codes, user IDs, timestamps, and country data. Logs may be transferred to cloud storage, including non-EU locations."

---

### 2️⃣ Necessity and Proportionality
- Is data processing justified for its purpose?
- Are there less intrusive alternatives?
- Has Data Minimization been applied?

✅ *Checklist:*  
- [ ] Clear purpose documented  
- [ ] Data fields reviewed for necessity  
- [ ] Minimization strategies implemented

---

### 3️⃣ Risk Assessment Table

| Risk Description       | Likelihood | Impact   | GDPR Penalty Potential | Risk Score (1-10) | Mitigation Measures                     |
|-------------------------|------------|----------|------------------------|-------------------|-----------------------------------------|
| Data leak               | High       | Severe   | Up to €20M             | 9/10              | Encryption, access controls             |
| Consent missing         | Medium     | High     | €10M                   | 7/10              | Consent validation systems              |
| Unauthorized access     | Medium     | Medium   | €10M                   | 6/10              | Logging, monitoring, SIEM alerts        |
| Retention policy breach | Medium     | Medium   | €10M                   | 6/10              | Automated deletion, retention policies  |
| Cross-border transfer   | Medium     | High     | €20M                   | 8/10              | SCCs, adequacy checks                   |

---

### 4️⃣ Measures to Mitigate Risks
- Data encryption and pseudonymization
- Strong access controls
- Consent management workflows
- Regular audits and logging
- Employee training

---

### 5️⃣ Consultation with DPO
- Review DSFA with the Data Protection Officer
- Ensure legal approval before deployment

---

## ✅ Notes on Use
- Fill in all sections for your specific use case.
- Review and update regularly.
- Attach supporting documents as needed (Dataflow Diagram, Detection Rules, Policies).

---

## 📌 Outcome
A complete, auditable DSFA document demonstrating GDPR Article 35 compliance and supporting Privacy by Design (Article 25) obligations.

