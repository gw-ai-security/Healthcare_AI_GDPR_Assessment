# AI-Specific Threat Model (STRIDE Analysis)

This document identifies and describes potential security threats specific to Healthcare AI systems using the STRIDE methodology.

---

## 🎯 Purpose
To analyze AI system components for security threats and design appropriate mitigations, supporting GDPR Art. 32 (Security of Processing) and Privacy by Design (Art. 25).

---

## 📌 STRIDE Threat Categories

### S – Spoofing
**Description:** Impersonating a legitimate user or system component.  
✅ *AI-Specific Example:*  
- Adversarial examples crafted to mislead AI model output.

**Mitigations:**  
- Input validation and adversarial training.  
- User authentication for API access.

---

### T – Tampering
**Description:** Unauthorized modification of data or code.  
✅ *AI-Specific Example:*  
- Data poisoning attacks corrupting training data.  
- Unauthorized changes to model weights.

**Mitigations:**  
- Secure data pipelines.  
- Integrity checks and version control for training datasets.  
- Model signing and verification.

---

### R – Repudiation
**Description:** Denial of actions without traceability.  
✅ *AI-Specific Example:*  
- Lack of audit logs for model predictions.  
- No evidence of data processing consent.

**Mitigations:**  
- Robust logging of API calls and predictions.  
- Consent logging and auditability.

---

### I – Information Disclosure
**Description:** Unauthorized exposure of information.  
✅ *AI-Specific Example:*  
- Model inversion attacks revealing training data.  
- Logging of sensitive health data without encryption.

**Mitigations:**  
- Encrypt sensitive logs.  
- Differential privacy techniques.  
- Pseudonymization of data fields.

---

### D – Denial of Service
**Description:** Making a service unavailable or degrading performance.  
✅ *AI-Specific Example:*  
- Overloading AI inference API with adversarial queries.  
- Resource exhaustion via malformed inputs.

**Mitigations:**  
- Rate limiting.  
- Input validation.  
- Resource isolation for model serving.

---

### E – Elevation of Privilege
**Description:** Unauthorized increase in access rights.  
✅ *AI-Specific Example:*  
- Prompt injection attacks in LLM components.  
- API key leakage enabling unrestricted model access.

**Mitigations:**  
- Strong access controls and key management.  
- Prompt sanitization for LLMs.  
- Role-based access policies.

---

## ✅ Outcome
A documented AI-specific threat model that:
- Supports Privacy by Design principles.
- Identifies and mitigates GDPR Art. 32 security risks.
- Provides clear guidance for security architecture and SIEM rule design.

