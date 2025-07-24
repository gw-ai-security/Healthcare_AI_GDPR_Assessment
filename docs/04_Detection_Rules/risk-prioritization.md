# Risk and Likelihood Matrix for Healthcare AI SIEM Use Cases

This matrix prioritizes detection use cases based on their **Risk Impact** and **Likelihood**, supporting risk-based SIEM design.



| Use Case                            | Beschreibung                                           | Risiko (Impact) | Eintrittswahrscheinlichkeit | Priorität |
|------------------------------------|--------------------------------------------------------|------------------|------------------------------|-----------|
| UC-01: Non-EU Export ohne Consent  | Datenexport in Drittstaaten ohne dokumentierte Einwilligung | Hoch             | Mittel                       | Hoch      |
| UC-02: Zugriff auf Rohdaten        | Zugriff auf unmaskierte Diagnosecodes ohne Audit-Trail | Hoch             | Hoch                         | Hoch      |
| UC-03: Suspicious Consent Toggle   | Wiederholtes Deaktivieren von Consent kurz vor Export  | Mittel           | Mittel                       | Mittel    |
| UC-04: AI-Modellmanipulation       | Modellantworten werden manipuliert (Prompt Injection)  | Hoch             | Niedrig                      | Mittel    |
| UC-05: Admin Access Outside Hours  | Admin-Login außerhalb Dienstzeiten                     | Mittel           | Hoch                         | Hoch      |


---

## Legend
- **Risk Impact:** Business / Legal consequences if undetected.
- **Likelihood:** Probability of occurrence.
- **Priority:** Combined rating for SIEM rule design focus.

---



