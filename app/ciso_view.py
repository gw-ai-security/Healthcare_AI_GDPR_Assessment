from app.utils.audit_logger import log_action
import streamlit as st
import pandas as pd
import matplotlib
matplotlib.use('Agg')  # Für Streamlit
import matplotlib.pyplot as plt

def show_ciso_dashboard():
    log_action('demo_user', 'CISO', 'Accessed Dashboard', 'CISO Dashboard')
    
    st.title("🧑‍💼 CISO Dashboard – GDPR Security Risk Overview")

    st.markdown("""
    This view provides a real-time overview of key GDPR-related risks, 
    active alerts, and business impact relevant for the Chief Information Security Officer (CISO).
    """)

    # KPI-Zeile
    col1, col2, col3 = st.columns(3)
    col1.metric("Overall GDPR Risk Score", "72", "▲ 5%")
    col2.metric("Critical Incidents (30d)", "3", "-1")
    col3.metric("Estimated Cost Avoided", "€1.2M", "+ €200K")

    st.markdown("## 🔥 Top Risky Actions by Department")
    risky_actions = pd.DataFrame({
        'Department': ['Radiology', 'Oncology', 'IT', 'Research'],
        'High-Risk Events': [15, 9, 6, 12]
    })

    fig, ax = plt.subplots(figsize=(10, 6))
    risky_actions.set_index('Department')['High-Risk Events'].plot(
        kind='bar', ax=ax, color='red', alpha=0.7
    )
    ax.set_title('High-Risk Events by Department')
    ax.set_ylabel('Number of Events')
    plt.xticks(rotation=45)
    st.pyplot(fig)

    st.markdown("## 🚨 Recent Critical Alerts")
    alerts = pd.DataFrame({
        'Time': ['14:23', '13:45', '12:01'],
        'Alert': ['Unauthorized data export attempt', 'Multiple failed login attempts', 'Consent withdrawal not processed'],
        'Severity': ['High', 'Medium', 'High']
    })
    st.dataframe(alerts, use_container_width=True)

    st.markdown("## 📊 Monthly Risk Trend")
    months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun']
    risk_scores = [65, 68, 72, 70, 75, 72]
    
    fig2, ax2 = plt.subplots(figsize=(10, 6))
    ax2.plot(months, risk_scores, marker='o', linewidth=2, markersize=8, color='orange')
    ax2.set_title('GDPR Risk Score Trend')
    ax2.set_ylabel('Risk Score')
    ax2.grid(True, alpha=0.3)
    st.pyplot(fig2)
