
# 🗂️ Audit & Operational Logs

This folder contains operational logs related to the GDPR compliance dashboard.  
All log files are machine-generated and provide traceability for security audits, stakeholder access, and GDPR Article 30 documentation.

---

## 📄 Included Files

| File              | Description                                        |
|-------------------|----------------------------------------------------|
| `audit_log.csv`   | Role-based access log for dashboard interactions. |

---

## 🔐 Compliance Purpose

- Enables GDPR **Art. 30** traceability (record of processing activities)
- Supports internal and external **auditors** by tracking who accessed what, when, and under which role
- Can be integrated with downstream SIEM systems or reviewed manually

---

## 🧠 Logging Format

```
timestamp,user,role,view,action
2025-07-22T14:53:00Z,dpo_user,DPO,DPO Dashboard,Exported Consent Report
```

---

## ⚠️ Best Practice

- Do **not commit** real logs to public repositories  
- Add `logs/*.csv` to `.gitignore` in production environments  
- Rotate logs periodically to limit size and exposure risk

---

## ✅ How It's Used

The log entries are written via the function:

```python
from app.utils.audit_logger import log_action

log_action(user, role, action, view)
```

This function is embedded in all role-specific dashboard views.

---

