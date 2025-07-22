# 🚨 Healthcare AI – Incident Scenarios

This document describes simulated incidents for testing the Security Analytics Dashboard, designed around GDPR-relevant threats in healthcare-AI systems.

---

## 🩺 Scenario 01 – Medical Device Compromise
- **Description:** External attacker exploits vulnerability in a connected radiology device (e.g., DICOM server), triggering unauthorized data exfiltration.
- **GDPR Impact:** Article 32 (Integrity & Confidentiality)
- **Patient Impact:** Exposure of diagnostic images without consent
- **SIEM Rule ID:** RULE_001_DEVICE_BREACH
- **Dashboard View:** SOC → Real-time alert; CISO → Risk Score spike

---

## 🕵️ Scenario 02 – Insider Access to EHR Logs
- **Description:** Clinician accesses patient records outside treatment relationship.
- **GDPR Impact:** Article 5(1)(c) (Data Minimization), Art. 9 (Special Category)
- **Patient Impact:** Unjustified privacy violation
- **SIEM Rule ID:** RULE_002_UNAUTHORIZED_ACCESS
- **Dashboard View:** DPO → Consent Violation Report; Auditor → Export Flag

---

## 🎭 Scenario 03 – AI Model Drift and Misclassification
- **Description:** A deployed AI model starts misclassifying consent statuses due to data drift.
- **GDPR Impact:** Article 25 (Privacy by Design), Art. 22 (Automated Decision-Making)
- **Patient Impact:** Data used without valid consent
- **SIEM Rule ID:** RULE_003_MODEL_DRIFT
- **Dashboard View:** DPO → Risk Heatmap; CISO → Data Quality Alert

---

## 🌐 Scenario 04 – Non-EU Transfer without Safeguards
- **Description:** Data exported to a US-based research partner without SCC or valid consent.
- **GDPR Impact:** Article 44 (Transfers to Third Countries)
- **Patient Impact:** Potential unlawful cross-border processing
- **SIEM Rule ID:** RULE_004_EXPORT_NO_CONSENT
- **Dashboard View:** CISO → Transfer Risk; Auditor → Alert History

---

## 💉 Scenario 05 – Adversarial Attack on AI Input
- **Description:** Manipulated input leads AI system to misdiagnose and trigger faulty alerts.
- **GDPR Impact:** Article 5(1)(d) (Accuracy), Art. 25 (Security by Design)
- **Patient Impact:** Wrong medical decision, potential liability
- **SIEM Rule ID:** RULE_005_ADVERSARIAL_INPUT
- **Dashboard View:** SOC → Anomaly Detection Trigger; CISO → AI Integrity Score

