# 📌 Risk and Likelihood Matrix for Healthcare AI SIEM Use Cases

This matrix prioritizes detection use cases based on their **Risk Impact** and **Likelihood**, supporting risk-based SIEM design.

| Use Case                                  | Risk Impact | Likelihood | Priority  |
|-------------------------------------------|-------------|------------|-----------|
| Non-EU Export without Consent             | High        | Medium     | High      |
| Access to Unencrypted Raw Data            | High        | High       | High      |
| AI Model Manipulation / Poisoning         | High        | Low        | Medium    |
| Unauthorized Access to PHI                | High        | Medium     | High      |
| Excessive Data Fields without Minimization| Medium      | High       | High      |
| Consent Check Failures                    | High        | Medium     | High      |
| Cloud Misconfiguration (Open Buckets)     | High        | Low        | Medium    |

---

## ✅ Legend
- **Risk Impact:** Business / Legal consequences if undetected.
- **Likelihood:** Probability of occurrence.
- **Priority:** Combined rating for SIEM rule design focus.

---

*Version 1.0 – Georg Wiesmüller*

