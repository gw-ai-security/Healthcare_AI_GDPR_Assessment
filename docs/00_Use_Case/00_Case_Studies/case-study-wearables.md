# 📌 Case Study: Wearable Health Devices – IoT Data Processing

This case study illustrates GDPR and security compliance challenges for **wearable health devices** that collect continuous patient data.

---

## ✅ Business Context

Hospitals and providers increasingly rely on **wearables** to monitor patient vitals (heart rate, sleep, activity, glucose levels). Data streams feed into AI systems for early warning, personalized recommendations, and chronic disease management.

---

## ✅ Data Characteristics

- Continuous streaming data
- Highly sensitive health metrics
- User identifiers and location data
- Integration with mobile apps and cloud APIs

---

## ✅ GDPR Challenges

- **Article 9:** Processing special category health data with explicit consent.
- **Article 6:** Lawfulness of processing, especially with minors or vulnerable patients.
- **Article 25:** Privacy by Design in device firmware and apps.
- **Article 32:** Secure data transmission (e.g., BLE encryption), backend storage.

---

## ✅ EU AI Act (2024) High-Risk Classification

- High-Risk AI when influencing health decisions or monitoring conditions.
- Requires:
  - Risk Management System
  - Human Oversight
  - Logging and Traceability
  - CE Marking under MDR (Medical Device Regulation)

---

## ✅ SIEM Use Cases

- Detect unencrypted BLE communication.
- Alert on unauthorized API calls to cloud storage.
- Monitor for consent verification failures in app backend.
- Log anomalous data exports from cloud services.
- Detect excessive data collection beyond consented scope.

---

## ✅ Recommended Technical & Organizational Measures

- Enforce TLS 1.3 for app-server communication.
- Encrypt BLE pairing and data sessions.
- Tokenization of patient identifiers in transit.
- Role-Based Access Control (RBAC) for platform admins.
- Consent Management integrated in mobile app UX.
- Immutable logs of consent and data processing events.

---

## ✅ SIEM Rulebook Example

- Detection Rule: Unauthorized API Call Exceeding Consent Scope
- Severity: High
- GDPR Mapping: Article 6, 9
- AI Act Mapping: High-Risk Processing Logging
- HIPAA Mapping: Transmission Security
- Business Impact: Avoid €20M fines; maintain patient trust.
