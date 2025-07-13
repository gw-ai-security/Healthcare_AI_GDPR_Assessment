# Detection Rule Template

_Use this template to design, document, and review security detection rules that monitor for GDPR-relevant events._

---

## 🎯 Purpose
To define clear, auditable detection rules for SIEM or log analysis that help identify potential GDPR compliance violations.

---

## 📌 Detection Rule Summary

- **Rule Name:**  
- **Author:**  
- **Date Created / Updated:**  
- **Use Case / Business Objective:**  
  - What GDPR risk does this rule address?
  - Example: Detect transfers to non-EU countries without consent.

✅ *Instructions:*  
- Clearly describe the purpose of the rule.
- Connect it to specific GDPR articles (e.g. Art. 5, 25, 32).

---

## 📌 Rule Logic / Conditions

- **Data Source:** (e.g. access logs, API calls)
- **Fields Used:** (e.g. Country, ConsentStatus)
- **Logic:**  
  - Example: Country = Non-EU AND ConsentStatus = false
- **Query Example:**  
  - Elastic DSL / SIEM Rule snippet

✅ *Instructions:*  
- Document technical logic in detail.
- Include SIEM-ready queries if possible.

---

## 📌 False Positive / Negative Analysis

| Risk Scenario                    | Likelihood | Impact | Notes / Mitigation             |
|-----------------------------------|------------|--------|-------------------------------|
| Legitimate test environments      | Medium     | Low    | Tag and exclude test logs     |
| Delayed consent sync              | Medium     | Medium | Add time-based grace periods  |
| IP geolocation inaccuracies       | High       | Medium | Regularly update IP mapping   |

✅ *Instructions:*  
- Think critically about how the rule could misfire.
- Include mitigation plans.

---

## 📌 Response / Alerting Plan

- **Severity Level:** (High/Medium/Low)
- **Alert Destination:** (SIEM dashboard, email, ticketing system)
- **Escalation Path:** (e.g. Security team, DPO)
- **Recommended Actions:**  
  - Review logs
  - Validate consent records
  - Notify responsible owners

✅ *Instructions:*  
- Make sure teams know what to do when the rule triggers.

---

## 📌 Testing & Validation

- **Test Date:**  
- **Tester:**  
- **Test Scenario:**  
  - How was the rule validated?
- **Result:**  
  - Passed / Issues found

✅ *Instructions:*  
- Ensure rules are tested before production deployment.

---

## 📌 Version History

| Version | Date       | Changes Made                   | Author            |
|---------|------------|-------------------------------|-------------------|
| 1.0     | YYYY-MM-DD | Initial creation               |                   |
|         |            |                               |                   |

✅ *Instructions:*  
- Maintain an audit trail of rule changes.

---

## ✅ Outcome
A **complete, auditable detection rule** that:
- Supports GDPR compliance monitoring.
- Integrates with SIEM or log analysis.
- Enables clear operational response.

