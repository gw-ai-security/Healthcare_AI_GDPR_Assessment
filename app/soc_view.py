from app.utils.audit_logger import log_action
import streamlit as st
import pandas as pd
import matplotlib
matplotlib.use('Agg')  # Für Streamlit
import matplotlib.pyplot as plt

def show_soc_dashboard():
    log_action('demo_user', 'SOC', 'Accessed Dashboard', 'SOC Dashboard')
    
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

    fig1, ax1 = plt.subplots(figsize=(10, 6))
    rule_hits.set_index('Rule ID')['Hits'].plot(
        kind='barh', ax=ax1, color='skyblue', alpha=0.8
    )
    ax1.set_title('Rule Hit Frequency')
    ax1.set_xlabel('Number of Hits')
    st.pyplot(fig1)

    st.markdown("## ⚡ Real-Time Alert Stream")
    alerts = pd.DataFrame({
        'Timestamp': ['15:42:33', '15:41:12', '15:39:45', '15:38:01', '15:36:22'],
        'Alert Type': ['Data Export Anomaly', 'Failed Authentication', 'Unusual Access Pattern', 'Consent Override', 'Data Retention Violation'],
        'Severity': ['High', 'Medium', 'Medium', 'High', 'Low'],
        'Source': ['DB_SERVER_01', 'WEB_APP', 'API_GATEWAY', 'CONSENT_SVC', 'ARCHIVE_SVC']
    })
    st.dataframe(alerts, use_container_width=True)

    st.markdown("## 📈 Alert Volume Trend (24h)")
    hours = list(range(0, 24))
    alert_counts = [2, 1, 0, 1, 3, 2, 4, 6, 8, 12, 15, 18, 22, 25, 20, 18, 16, 14, 12, 10, 8, 6, 4, 3]
    
    fig2, ax2 = plt.subplots(figsize=(12, 6))
    ax2.plot(hours, alert_counts, marker='o', linewidth=2, color='red', alpha=0.7)
    ax2.set_title('24-Hour Alert Volume')
    ax2.set_xlabel('Hour of Day')
    ax2.set_ylabel('Number of Alerts')
    ax2.grid(True, alpha=0.3)
    st.pyplot(fig2)
