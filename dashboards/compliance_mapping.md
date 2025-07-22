# ✅ Compliance Mapping – GDPR ↔ SIEM Rule ↔ Dashboard ↔ Business Impact

This matrix maps GDPR articles to specific detection rules, affected dashboard views, and the estimated business impact in case of non-compliance.

---

## 📊 Compliance Mapping Table

| GDPR Article | SIEM Rule ID                  | Dashboard View      | Description                                       | Business Impact (€)        |
|--------------|-------------------------------|---------------------|---------------------------------------------------|-----------------------------|
| Art. 32      | RULE_001_DEVICE_BREACH        | CISO, SOC           | Unauthorized access via medical device breach     | €1.5M fine + brand damage   |
| Art. 5, 9    | RULE_002_UNAUTHORIZED_ACCESS  | DPO, Auditor        | Clinician accesses data without treatment reason  | €2M fine + breach report    |
| Art. 22, 25  | RULE_003_MODEL_DRIFT          | DPO, CISO           | AI model misclassifies consent                    | €500K + regulatory scrutiny |
| Art. 44      | RULE_004_EXPORT_NO_CONSENT    | CISO, Auditor       | Data exported to non-EU without SCC/consent       | €20M max fine               |
| Art. 5(1)(d) | RULE_005_ADVERSARIAL_INPUT     | SOC, CISO           | AI fooled by adversarial inputs                   | €1M + operational disruption |

---

## 🧠 Use Case to Regulation Summary

| Use Case                          | Rule ID       | Primary GDPR Article(s)   | Dashboard View |
|----------------------------------|---------------|----------------------------|----------------|
| Non-EU Transfer Without Consent  | RULE_004      | Art. 44                    | CISO, Auditor  |
| Insider EHR Access               | RULE_002      | Art. 5, Art. 9             | DPO, Auditor   |
| AI Model Drift on Consent Status | RULE_003      | Art. 22, Art. 25           | DPO, CISO      |
| Adversarial AI Input Attack      | RULE_005      | Art. 5(1)(d), Art. 25      | SOC, CISO      |
| Device Exploitation (DICOM etc.)| RULE_001      | Art. 32                    | SOC, CISO      |

---

## 💡 Notes

- **High Risk**: RULE_004 (Art. 44) has the highest fine potential under GDPR.
- **Cross-Mapping**: Several dashboard views (e.g., CISO & DPO) overlap in rule visibility but differ in access granularity.
- **Audit Use**: This table supports quick traceability and Art. 30 audit documentation.

---

## ✅ Recommendation for Storage

📂 Speichere die Datei hier:

```plaintext
/docs/compliance_mapping.md

