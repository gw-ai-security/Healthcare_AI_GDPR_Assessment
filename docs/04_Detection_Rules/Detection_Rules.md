
# 🛡Detection Rules for GDPR Compliance Monitoring

This document defines example detection rules for monitoring and alerting on GDPR-relevant risks in Healthcare AI system logs.

---

## Purpose

To help Security Architects, DPOs, and Compliance teams detect data processing events that may violate GDPR requirements, enabling timely investigation and mitigation.

---

## Detection Rules Overview

| ID     | Use Case                                  | Severity | GDPR Article | AI Act Mapping          |
|--------|--------------------------------------------|----------|---------------|--------------------------|
| UC-01 | Non-EU Transfer Without Consent            | High     | Art. 44       | High-Risk System         |
| UC-02 | Access to Raw Diagnostic Data              | High     | Art. 5, 32    | -                        |
| UC-03 | Consent Flag Manipulation Pattern          | Medium   | Art. 7        | -                        |
| UC-04 | AI Model Behavior Drift / Manipulation     | Medium   | Art. 22       | High-Risk (Monitoring)   |
| UC-05 | Suspicious Admin Access After Hours        | High     | Art. 32       | -                        |

---

## UC-01: Non-EU Transfer Without Consent

**Description:** Detects log events where data is transferred to a non-EU country without recorded consent.

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

### False Positive / False Negative Strategy

#### False Positives

| Scenario                                 | Description                                                            | Mitigation Strategy                                  |
|------------------------------------------|------------------------------------------------------------------------|------------------------------------------------------|
| Legitimate research partners (non-EU)    | Medical research with separate research consent                       | Cross-check with `research_consent_flag`             |
| Test/dev environments using mock data    | Simulated data triggers export logic                                  | Tag test systems in logs (e.g., `env=dev`)           |
| Cloud/CDN proxy masking IP origin        | GeoIP misidentifies EU-based users due to reverse proxies             | Enrich logs with ASN info (e.g., MaxMind ASN fields) |

#### False Negatives

| Scenario                                  | Description                                                   | Mitigation Strategy                                |
|-------------------------------------------|---------------------------------------------------------------|----------------------------------------------------|
| VPN or proxy usage disguises true location | GeoIP sees EU but traffic originates outside the EU           | GeoIP confidence score + ASN analysis              |
| Consent flag incorrectly set to `true`     | Application bug or improper log ingestion                     | Cross-check with audit trail of consent changes    |
| Missing data in logs                       | Logs missing IP or consent info (e.g., system crash)          | Add fallback alert for missing mandatory fields    |

---

## UC-02: Access to Raw Diagnostic Data

**Description:** Detects unauthorized access to unmasked diagnostic data or unfiltered DICOM logs.

**Pseudo-Query:**
```json
{
  "query": {
    "bool": {
      "must": [
        { "match": { "DataType": "diagnosis_raw" } },
        { "match": { "MaskingStatus": "false" } },
        { "match": { "AccessRole": "non-medical" } }
      ]
    }
  }
}
```

### False Positive / False Negative Strategy

#### False Positives

| Scenario            | Description                                            | Mitigation Strategy                          |
|---------------------|--------------------------------------------------------|----------------------------------------------|
| Data masking tool not yet applied | Timing mismatch causes unmasked logs         | Delay alert trigger by 5 mins post ingestion |
| Legitimate read access by radiologist | Role misclassification                      | Role verification against HR IAM data        |

#### False Negatives

| Scenario           | Description                          | Mitigation Strategy                      |
|--------------------|--------------------------------------|------------------------------------------|
| Manual export via local tools | Not logged in SIEM                  | Endpoint DLP + audit tool integration    |
| Masking errors not logged     | Logging misconfiguration            | Rule to detect absence of expected logs  |

---

## UC-03: Consent Flag Manipulation Pattern

**Description:** Detects patterns where users toggle consent status repeatedly before initiating exports.

**Pseudo-Query (pseudo logic):**
```
IF user toggles `ConsentStatus` from true → false → true ≥ 3 times within 1 hour AND export request follows
THEN alert
```

### False Positive / False Negative Strategy

#### False Positives

| Scenario      | Description                           | Mitigation Strategy                   |
|---------------|---------------------------------------|---------------------------------------|
| Mobile UI bug | Users unintentionally toggle rapidly  | UI logs validation                    |
| Accessibility tech | Automated toggles                  | Tag accessibility client agents       |

#### False Negatives

| Scenario      | Description                            | Mitigation Strategy                   |
|---------------|----------------------------------------|---------------------------------------|
| Low-frequency toggles | Only 1-2 toggles before export      | Lower threshold + score-based model   |
| Out-of-band requests | Data accessed through backend tools | Include backend trace + API monitoring|

---

## UC-04: AI Model Behavior Drift / Manipulation

**Description:** Detects unexpected drift in AI model output characteristics that may signal tampering or adversarial influence.

**Example Metrics Monitored:**
- Sudden shift in output class distribution
- Increased entropy in predictions
- Unusual correlation between features and predictions

**Detection Logic:** Requires ML baseline drift detection pipeline (e.g. EvidentlyAI or custom scripts)

### False Positive / False Negative Strategy

| Type | Scenario | Mitigation |
|------|----------|------------|
| FP   | Model retraining causes shift | Alert suppression window after scheduled training |
| FN   | Gradual poisoning | Implement drift slope monitors over time |

---

## UC-05: Suspicious Admin Access After Hours

**Description:** Detects admin access activity outside of business hours.

**Pseudo-Query:**
```json
{
  "query": {
    "bool": {
      "must": [
        { "match": { "Role": "admin" } },
        { "range": { "timestamp": { "gte": "00:00", "lt": "06:00" } } }
      ]
    }
  }
}
```

### False Positive / False Negative Strategy

#### False Positives

| Scenario              | Description                             | Mitigation Strategy               |
|-----------------------|-----------------------------------------|-----------------------------------|
| On-call incident team | Legitimate emergency intervention       | Cross-check with incident ticket  |
| Remote timezone access| Admin in other region (e.g. Asia team)  | Add timezone-normalized filter    |

#### False Negatives

| Scenario               | Description                      | Mitigation Strategy               |
|------------------------|----------------------------------|-----------------------------------|
| Shared admin accounts  | Attribution not reliable         | Enforce SSO + user audit logging  |
| Time-stamp in UTC only | Alerts misaligned with local time| Normalize log timestamps via ETL  |

---

## Summary

This rulebook outlines GDPR-relevant detection logic, including false positive/negative analysis and contextual mitigation strategies. Each rule connects legal compliance to operational alerting and can be adapted to enterprise SIEM environments like Elastic, Splunk, or Sentinel.
