# AI Incident Response Playbook

_Use this template to plan and document a structured incident response process tailored for AI systems handling sensitive personal data._

---

## 🎯 Purpose
To ensure a clear, consistent, and auditable approach to managing incidents that could impact data protection, privacy, and security, in line with GDPR requirements.

---

## 📌 1️⃣ Scope

- **System / Product:**  
- **Business Owner:**  
- **Data Protection Officer:**  
- **Security Lead:**  
- **Version / Last Updated:**  

✅ *Instructions:*  
Define which AI systems or data flows this playbook applies to.

---

## 📌 2️⃣ Incident Types

List incident categories relevant to AI systems:

- **Data Leak:** Unauthorized disclosure of personal or health data.
- **Data Poisoning Attack:** Manipulated training data to bias model.
- **Adversarial Attack:** Inputs designed to fool AI outputs.
- **Unauthorized Access:** Breach of access controls.
- **Retention Policy Violation:** Data kept longer than allowed.
- **Cross-Border Transfer Issue:** Data sent without safeguards.
- **Bias Discovery:** Algorithmic discrimination identified.

✅ *Instructions:*  
Customize the list to your use case.

---

## 📌 3️⃣ Detection & Triage

- **Detection Sources:**  
  - SIEM alerts
  - Logs
  - User reports
  - Third-party notifications

- **Initial Triage Questions:**  
  - What data is impacted?
  - How many data subjects?
  - Is health data (Article 9) involved?
  - Is the incident ongoing?
  - Potential GDPR reporting obligations?

✅ *Instructions:*  
Include clear steps for the incident handler.

---

## 📌 4️⃣ Response Steps

1️⃣ **Containment:**  
- Isolate affected systems.  
- Disable compromised accounts or APIs.  

2️⃣ **Analysis:**  
- Determine root cause.  
- Assess impacted data fields.  
- Identify if Article 9 special categories are exposed.  

3️⃣ **Eradication:**  
- Remove malware or malicious inputs.  
- Patch vulnerabilities.  

4️⃣ **Recovery:**  
- Restore safe, compliant state.  
- Validate model integrity.  

5️⃣ **Notification:**  
- Data Protection Officer (DPO)  
- Security team  
- Legal/Compliance  
- Supervisory Authority (if required under GDPR Art. 33)  
- Data Subjects (if required under Art. 34)

✅ *Instructions:*  
Adapt to your incident response process.

---

## 📌 5️⃣ Roles and Responsibilities

| Role               | Responsibility                           |
|---------------------|------------------------------------------|
| Incident Handler    | Coordinates response and documentation  |
| Security Lead       | Leads technical investigation           |
| Data Protection Officer | Assesses GDPR reporting requirements |
| AI Product Manager  | Validates impact on AI system           |
| Legal/Compliance    | Manages regulatory notifications        |
| Communications Lead | Coordinates internal/external messaging |

✅ *Instructions:*  
Assign real people in your organization.

---

## 📌 6️⃣ Communication Plan

- **Initial Notification:**  
  - Who must be informed immediately?
  - Method (email, phone, ticketing system)

- **Regular Updates:**  
  - Frequency (e.g. every 2 hours)
  - Stakeholders to receive updates

- **Executive Summary:**  
  - For management/CISO/Board

✅ *Instructions:*  
Define clear channels and escalation paths.

---

## 📌 7️⃣ Post-Incident Review

- Timeline of events  
- Root cause analysis  
- Lessons learned  
- Policy or process improvements  
- Update detection rules / SIEM  
- Staff training needs

✅ *Instructions:*  
Document outcomes to prevent repeat incidents.

---

## 📌 8️⃣ Sign-off

- **Incident Handler:**  
- **DPO:**  
- **Security Lead:**  
- **Date Closed:**  

✅ *Instructions:*  
Ensure formal closure and audit readiness.

---

## ✅ Outcome
A **clear, auditable plan** for managing AI-related privacy and security incidents that:  
- Demonstrates GDPR Art. 32 "Security of Processing" compliance.  
- Supports rapid, coordinated responses.  
- Reduces regulatory and reputational risk.

