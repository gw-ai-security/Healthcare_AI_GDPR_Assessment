# Detection Rules for GDPR Compliance Monitoring

This document defines example detection rules for monitoring and alerting on GDPR-relevant risks in Healthcare AI system logs.

---

## 🎯 Purpose
To help Security Architects, DPOs, and Compliance teams detect data processing events that may violate GDPR requirements, enabling timely investigation and mitigation.

---

## 📌 Example Detection Rules

### 1️⃣ Non-EU Transfer Without Consent
**Description:** Detects log events where data is transferred to a non-EU country without recorded consent.

**Logic:**
- Country = Non-EU
- ConsentStatus = false

**Pseudo-Query (Elastic DSL Example):**
```json
{
  "query": {
    "bool": {
      "must": [
        { "match": { "Country": "Non-EU" } },
        { "match": { "ConsentStatus": "false" } }
      ]
    }
  }
}

