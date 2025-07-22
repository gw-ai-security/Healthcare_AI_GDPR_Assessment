from app.utils.audit_logger import log_action

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

    log_action('demo_user', 'SOC', 'Accessed Dashboard', 'SOC Dashboard')
def show_soc_dashboard():
    st.title("🧑‍💻 SOC Analyst Dashboard – Active Alerts & Rule Effectiveness")

    st.markdown("""
    This view is intended for SOC analysts to monitor real-time alerts, 
    rule hits, and operational response metrics.
    """)

    # KPIs
    col1, col2, col3 = st.columns(3)
    col1.metric("Active Alerts", "12", "▲ 4")
    col2.metric("Mean Time to Detect (MTTD)", "3h 15m", "-12%")
    col3.metric("Mean Time to Respond (MTTR)", "5h 40m", "-8%")

    st.markdown("## 🔁 Rule Hit Frequency")
    rule_hits = pd.DataFrame({
        'Rule ID': ['RULE_001', 'RULE_002', 'RULE_003', 'RULE_004', 'RULE_005'],
        'Hits': [8, 15, 4, 12, 5]
    })

    fig1, ax1 = plt.subplots()
    rule_hits.set_index('Rule ID').plot(kind='barh', ax=ax1, color='skyblue', legend=False)
    ax1.set_xlabel("Number of Hits")
    st.pyplot(fig1)

    st.markdown("## 🕒 Alert Timeline")
    alerts = pd.DataFrame({
        'Timestamp': pd.date_range("2024-06-01", periods=10, freq='D'),
        'Alerts': [1, 2, 1, 3, 0, 2, 4, 1, 3, 2]
    })

    st.line_chart(alerts.set_index("Timestamp"))

    st.markdown("## 🚨 Repeat Offenders")
    offenders = pd.DataFrame({
        'User ID': ['U001', 'U007', 'U015', 'U032'],
        'Offense Count': [5, 3, 4, 2]
    })

    st.dataframe(offenders.style.highlight_max(axis=0, color='red'))