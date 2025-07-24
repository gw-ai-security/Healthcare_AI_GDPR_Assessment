# Healthcare-AI Challenges

This section describes the **specific security and compliance challenges** for SIEM monitoring in Healthcare AI environments.

---

## Data Variety and Complexity

- Electronic Medical Records (EMR)
- IoT Devices (Wearables, Remote Monitoring)
- Imaging and Diagnostic Data
- Third-Party Cloud Services

**SIEM Implications:**
- Multiple log formats and data sources
- Need for unified log collection and parsing
- Ensuring data provenance

---

## Sensitive Data Handling

- Health data = GDPR "special category data" (Article 9)
- Need for explicit, documented consent
- Pseudonymization and encryption at rest and in transit

**SIEM Implications:**
- Monitor for unencrypted storage
- Alert on transfers to non-EU locations without consent
- Track access control violations

---

## AI-Specific Attack Vectors

- Adversarial Examples
- Data Poisoning
- Model Inversion or Extraction
- Prompt Injection (for LLM-based systems)

**SIEM Implications:**
- Log and detect unusual training data uploads
- Monitor for repeated failed inference calls
- Track model access logs

---

## Operational Challenges

- Managed SOC providers may lack healthcare context
- Shortage of specialized AI security skills
- Integration with legacy systems

**SIEM Implications:**
- Need for clear detection use cases
- False positive tuning strategies
- Business-focused reporting

---

## Compliance Requirements

- GDPR / EU AI Act High-Risk Classification
- HIPAA for US providers
- EHDS for EU cross-border data sharing

**SIEM Implications:**
- Must provide audit logs
- Demonstrate Privacy by Design
- Enable cross-border compliance evidence



