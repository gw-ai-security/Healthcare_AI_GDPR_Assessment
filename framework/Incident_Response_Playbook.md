# AI Incident Response Playbook

_Use this template to manage privacy/security incidents involving AI systems handling personal or health data._

---

### Purpose

Ensure a structured, auditable, GDPR-aligned process for responding to AI-specific incidents (e.g. data poisoning, consent violations, unauthorized access).

---

### 1. Scope

| Field                 | Entry                          |
|----------------------|---------------------------------|
| **System / Product** |                                 |
| **Business Owner**   |                                 |
| **Data Protection Officer (DPO)** |                     |
| **Security Lead**    |                                 |
| **Version / Updated**|                                 |

*Specify which AI systems and data flows are in scope.*

---

### 2. Incident Types

| Category                 | Description                                       |
|--------------------------|---------------------------------------------------|
| **Data Leak**            | Unauthorized disclosure of personal/health data  |
| **Data Poisoning**       | Compromised training data biases model behavior  |
| **Adversarial Attack**   | Inputs crafted to mislead AI outputs             |
| **Unauthorized Access**  | Breach of user or system access controls         |
| **Retention Violation**  | Data stored longer than allowed                  |
| **Cross-Border Issue**   | Non-EU transfers without safeguards              |
| **Bias Discovery**       | Algorithmic discrimination uncovered             |

*Adapt based on your specific use cases.*

---

### 3. Detection & Triage

**Detection Sources:**
- SIEM alerts  
- Logs & anomaly detection  
- End-user reports  
- Vendors / Third parties  

**Triage Questions:**
- What data is affected?  
- Volume of subjects?  
- Article 9 data involved (health, biometrics)?  
- Is the incident ongoing?  
- GDPR Art. 33/34 reporting triggered?

---

### 4. Response Steps

| Phase         | Actions |
|---------------|---------|
| **1. Containment** | Isolate systems, revoke access, disable APIs |
| **2. Analysis**    | Root cause, impacted fields, GDPR categorization |
| **3. Eradication** | Remove malicious input/code, close vulnerabilities |
| **4. Recovery**    | Restore safe systems, validate AI output integrity |
| **5. Notification**| DPO, Security, Legal, Regulator (Art. 33), Data Subjects (Art. 34) |

---

### 5. Roles & Responsibilities

| Role                | Responsibility                            |
|---------------------|--------------------------------------------|
| **Incident Handler**| Coordinates process & documents decisions |
| **Security Lead**   | Technical forensics & threat containment  |
| **DPO**             | GDPR compliance, regulator notification    |
| **AI Product Owner**| Assess ML/AI impact                        |
| **Legal/Compliance**| Manage risk exposure & reporting           |
| **Comms Lead**      | Stakeholder and public comms               |

---

### 6. Communication Plan

| Stage                | Details                                     |
|----------------------|---------------------------------------------|
| **Initial Alert**     | Notify Security, DPO, Execs immediately    |
| **Updates**           | Every 2–4 hours (email / ticket updates)   |
| **Escalation**        | Critical: CISO / Board within 24h          |
| **Executive Summary** | Sent post-mitigation with findings         |

---

### 7. Post-Incident Review

- Timeline of events  
- Root cause  
- Detection gaps  
- Mitigation effectiveness  
- Lessons learned  
- SIEM rules to update  
- Policies to revise  
- Staff training actions  

---

### 8. Sign-off

| Role               | Name             | Date       |
|--------------------|------------------|------------|
| Incident Handler   |                  |            |
| DPO                |                  |            |
| Security Lead      |                  |            |
| Final Sign-Off     |                  |            |

---

### Outcome

- Demonstrates compliance with **GDPR Art. 32: Security of Processing**
- Enables repeatable, auditable incident management  
- Reduces legal, reputational and operational risks
