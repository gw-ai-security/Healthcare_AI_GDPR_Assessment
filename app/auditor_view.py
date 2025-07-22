from app.utils.audit_logger import log_action

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

    log_action('demo_user', 'AUDITOR', 'Accessed Dashboard', 'Auditor Dashboard')
def show_auditor_dashboard():
    st.title("🧾 Auditor Dashboard – Documentation & GDPR Traceability")

    st.markdown("""
    This dashboard provides audit-relevant documentation insights for GDPR Art. 30 reporting,
    data access traceability, and policy compliance summaries.
    """)

    # KPIs
    col1, col2, col3 = st.columns(3)
    col1.metric("Art. 30 Coverage", "92%", "+3%")
    col2.metric("Access Log Completeness", "98%", "+1%")
    col3.metric("Manual Overrides", "2", "±0")

    st.markdown("## 📥 Export Events Without Legal Basis")
    exports = pd.DataFrame({
        'Date': pd.date_range("2024-06-10", periods=5, freq='D'),
        'User': ['U023', 'U015', 'U007', 'U033', 'U018'],
        'Country': ['US', 'IN', 'DE', 'US', 'BR'],
        'Legal Basis Missing': [True, False, False, True, True]
    })

    st.dataframe(exports.style.applymap(
        lambda val: 'background-color: orange' if val is True else ''
    , subset=['Legal Basis Missing']))

    st.markdown("## 📄 Policy Violation Summary")
    policies = pd.DataFrame({
        'Policy': ['Data Retention', 'Access Control', 'Consent Logging', 'Encryption'],
        'Violations': [2, 1, 0, 3]
    })

    fig1, ax1 = plt.subplots()
    policies.set_index('Policy').plot(kind='bar', ax=ax1, color='darkred', legend=False)
    ax1.set_ylabel("Violation Count")
    st.pyplot(fig1)

    st.markdown("## 📤 Downloadable Artifacts")
    st.markdown("""
    - ✅ [Download GDPR Checklist](#)
    - ✅ [Download DSFA Report](#)
    - ✅ [Download Detection Rulebook](#)
    - ✅ [Download Incident Logs](#)
    """)