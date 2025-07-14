# 📌 Healthcare AI Data Flow Diagram

This diagram illustrates the **data flow** in a typical Healthcare AI system, highlighting consent checks, storage, logging, and external transfers.

---

```mermaid
flowchart TD
    User -->|Submit Data| AI_Frontend
    AI_Frontend --> ConsentCheck
    ConsentCheck --> AI_Model
    AI_Model --> EncryptedStorage
    EncryptedStorage --> SIEM
    SIEM --> ExternalTransfer
    ExternalTransfer --> ExternalAPIs

    %% Labels
    AI_Frontend[AI Frontend]
    ConsentCheck[Consent Verification]
    AI_Model[AI Model / Inference]
    EncryptedStorage[Encrypted Storage]
    SIEM[SIEM Logging]
    ExternalTransfer[External Transfer (EU/Non-EU)]
    ExternalAPIs[Third-Party / Cloud APIs]
