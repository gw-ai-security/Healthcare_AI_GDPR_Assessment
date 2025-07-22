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
```
---

### 🛑 False Positive / False Negative Strategy

#### ⚠️ False Positives

| Scenario                                 | Description                                                            | Mitigation Strategy                                  |
|------------------------------------------|------------------------------------------------------------------------|------------------------------------------------------|
| Legitimate research partners (non-EU)    | Medical research with separate research consent                       | Cross-check with `research_consent_flag`             |
| Test/dev environments using mock data    | Simulated data triggers export logic                                  | Tag test systems in logs (e.g., `env=dev`)           |
| Cloud/CDN proxy masking IP origin        | GeoIP misidentifies EU-based users due to reverse proxies             | Enrich logs with ASN info (e.g., MaxMind ASN fields) |

#### ❌ False Negatives

| Scenario                                  | Description                                                   | Mitigation Strategy                                |
|-------------------------------------------|---------------------------------------------------------------|----------------------------------------------------|
| VPN or proxy usage disguises true location | GeoIP sees EU but traffic originates outside the EU           | GeoIP confidence score + ASN analysis              |
| Consent flag incorrectly set to `true`     | Application bug or improper log ingestion                     | Cross-check with audit trail of consent changes    |
| Missing data in logs                       | Logs missing IP or consent info (e.g., system crash)          | Add fallback alert for missing mandatory fields    |

#### 🎯 Tuning Recommendations

- Trigger only when `geoip.country NOT IN (EU)` **AND** `consent_flag != true`
- Optional: Trigger only if ≥3 such events per session to reduce noise
- Enrich data with WHOIS/ASN to verify real IP ownership
