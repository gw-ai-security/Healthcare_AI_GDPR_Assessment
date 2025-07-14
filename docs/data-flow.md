# 📌 Healthcare AI Data Flow Diagram

This diagram illustrates the **data flow** in a typical Healthcare AI system, highlighting consent checks, storage, logging, and external transfers.

---

```mermaid
flowchart TD
    User[User / Patient] -->|Submit Data| AI_Frontend
    AI_Frontend --> ConsentCheck[Consent Verification]
    ConsentCheck --> AI_Model[AI Model / Inference]
    AI_Model --> EncryptedStorage[Encrypted Storage]
    EncryptedStorage --> SIEM[SIEM Logging]
    SIEM --> ExternalTransfer[External Transfer (EU/Non-EU)]
    
    ExternalTransfer --> ExternalAPIs[Third-Party / Cloud APIs]

