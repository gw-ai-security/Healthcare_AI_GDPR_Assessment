# 👥 Stakeholder Views – Security Analytics Dashboard

This document outlines role-specific dashboard components for key stakeholders involved in GDPR compliance and security monitoring within a healthcare AI environment.

Each view provides tailored KPIs, visualizations, and actions to enable effective, compliant, and role-aware decision-making.

---

## 🧑‍💼 CISO View (Chief Information Security Officer)

### 🎯 Purpose
Monitor overall security posture, GDPR-related risk exposure, and ROI from implemented controls.

### 📊 KPIs
- Overall GDPR Risk Score (0–100)
- Number of Critical Incidents (last 30 days)
- Estimated Cost Avoidance (€)
- AI Drift Events Detected

### 📈 Visuals
- 📉 Risk Trend Over Time
- 🔝 Top 5 Risky Actions by Department
- 🧠 AI Drift / Misuse Map
- 🏥 Non-EU Transfers Heatmap

### ⚙️ Controls
- Enable/disable anomaly detection modules
- Drill-down into high-risk alerts
- Export Executive Summary

---

## 👩‍⚖️ DPO View (Data Protection Officer)

### 🎯 Purpose
Ensure lawful processing, consent compliance, and GDPR Article accountability.

### 📊 KPIs
- Active Consent Violations
- Article 9 Data Exposures
- Art. 44 Transfers Without SCC
- Art. 22 Automated Processing Alerts

### 📈 Visuals
- 🗺️ Consent Heatmap (per system/unit)
- 📌 GDPR Article Violation Breakdown
- 🌍 Transfers by Country (EU/Non-EU)

### 📋 Functions
- Art. 30 ROPA Export
- View Subject Access Request (SAR) Logs
- Consent Proofs Linked to Alert Events

---

## 🧑‍💻 SOC Analyst View

### 🎯 Purpose
Detect, respond to, and monitor GDPR-relevant incidents with SIEM integration.

### 📊 KPIs
- Active Alerts (by severity)
- Mean Time to Detect (MTTD)
- Mean Time to Respond (MTTR)
- Triggered SIEM Rule IDs

### 📈 Visuals
- 🕒 Alert Timeline
- 📎 Rule Hit Frequency (per rule)
- 🔁 Repeat Offenders by UserID/IP

### ⚙️ Actions
- Acknowledge / Escalate / Suppress Alert
- View Raw Log Entry
- Assign to Playbook (e.g., Consent Breach)

---

## 🧾 Auditor View

### 🎯 Purpose
Verify compliance, traceability, and documentation quality for GDPR audits.

### 📊 KPIs
- Art. 30 Record Coverage (%)
- Data Access Log Completeness Score
- Number of Manual Overrides

### 📈 Visuals
- 🧾 Access Log Table
- 📄 Policy Violation Summary
- 📤 Export Events with Missing Legal Basis

### 📁 Export Features
- One-click download of:
  - GDPR Checklist
  - DSFA Report
  - Incident Response Logs
  - Rulebook with Mapping (GDPR ↔ RuleID ↔ Risk)

---

## ✅ Summary Table

| Role       | Primary KPI Focus                   | Key Features                  |
|------------|--------------------------------------|-------------------------------|
| CISO       | Risk Score, Incidents, ROI          | Trends, Cost Avoidance, Drilldown |
| DPO        | Consent, Article Violations         | Article Mapping, ROPA Export |
| SOC        | Alert Volume, MTTR, Rule Hits       | Live Alerts, Log Details     |
| Auditor    | Logs, Documentation, Completeness   | Report Exports, Traceability |


