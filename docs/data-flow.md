# 📌 Healthcare AI Data Flow Diagram

This diagram illustrates the **data flow** in a typical Healthcare AI system.

---

```mermaid
flowchart TD
    User -->|Submit Data| AI_Frontend
    AI_Frontend --> Consent_Check
    Consent_Check --> AI_Model
    AI_Model --> Encrypted_Storage
    Encrypted_Storage --> SIEM_Logging
    SIEM_Logging --> External_Transfer
    External_Transfer --> External_APIs


## ✅ Node Legend

| Node              | Description                             |
|--------------------|-----------------------------------------|
| User               | Patient / Healthcare Provider          |
| AI_Frontend        | Web/App Interface                      |
| Consent_Check      | Verification of documented consent     |
| AI_Model           | Diagnostic / Inference Engine          |
| Encrypted_Storage  | Secure Storage of Sensitive Data       |
| SIEM_Logging       | Security Monitoring and Evidence       |
| External_Transfer  | Cross-Border / Non-EU Data Sharing     |
| External_APIs      | Third-Party Integrations / Cloud APIs  |
