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
