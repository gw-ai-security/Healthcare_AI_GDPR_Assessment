from utils.audit_logger import log_action
import streamlit as st
import pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

def show_ciso_dashboard():
    log_action('demo_user', 'CISO', 'Accessed Dashboard', 'CISO Dashboard')
    
    st.title("CISO Dashboard - GDPR Security Risk Overview")

    st.markdown("""
    This view provides a real-time overview of key GDPR-related risks, 
    active alerts, and business impact relevant for the Chief Information Security Officer (CISO).
    """)

    # KPI Section
    col1, col2, col3 = st.columns(3)
    col1.metric("Overall GDPR Risk Score", "72", "5%")
    col2.metric("Critical Incidents (30d)", "3", "-1")
    col3.metric("Estimated Cost Avoided", "€1.2M", "+ €200K")

    st.markdown("## Top Risky Actions by Department")
    risky_actions = pd.DataFrame({
        'Department': ['Radiology', 'Oncology', 'IT', 'Research'],
        'High-Risk Events': [15, 9, 6, 12]
    })

    # Kleinere Chart-Größe
    fig, ax = plt.subplots(figsize=(8, 4))
    risky_actions.set_index('Department')['High-Risk Events'].plot(
        kind='bar', ax=ax, color='red', alpha=0.7
    )
    ax.set_title('High-Risk Events by Department', fontsize=12)
    ax.set_ylabel('Number of Events', fontsize=10)
    plt.xticks(rotation=45, fontsize=9)
    plt.yticks(fontsize=9)
    plt.tight_layout()
    st.pyplot(fig)

    st.markdown("## Recent Critical Alerts")
    alerts = pd.DataFrame({
        'Time': ['14:23', '13:45', '12:01'],
        'Alert': ['Unauthorized data export attempt', 'Multiple failed login attempts', 'Consent withdrawal not processed'],
        'Severity': ['High', 'Medium', 'High']
    })
    st.dataframe(alerts, use_container_width=True)

    st.markdown("## Monthly Risk Trend")
    months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun']
    risk_scores = [65, 68, 72, 70, 75, 72]
    
    # Kompaktere Chart
    fig2, ax2 = plt.subplots(figsize=(8, 3.5))
    ax2.plot(months, risk_scores, marker='o', linewidth=2, markersize=6, color='orange')
    ax2.set_title('GDPR Risk Score Trend', fontsize=12)
    ax2.set_ylabel('Risk Score', fontsize=10)
    ax2.grid(True, alpha=0.3)
    plt.xticks(fontsize=9)
    plt.yticks(fontsize=9)
    plt.tight_layout()
    st.pyplot(fig2)

    st.markdown("## Risk Assessment Summary")
    risk_categories = pd.DataFrame({
        'Risk Category': ['Data Breach', 'Consent Violations', 'Cross-border Transfers', 'Access Control', 'Data Retention'],
        'Current Level': ['Medium', 'High', 'Low', 'Medium', 'Low'],
        'Impact Score': [7, 9, 3, 6, 4]
    })
    st.dataframe(risk_categories, use_container_width=True)

    st.markdown("## System Performance Metrics")
    performance_metrics = pd.DataFrame({
        'Metric': ['System Uptime', 'Data Processing Speed', 'Alert Response Time', 'Compliance Check Rate'],
        'Current Value': ['99.8%', '2.3s avg', '45min avg', '98.5%'],
        'Target': ['99.9%', '2.0s', '30min', '99.0%'],
        'Status': ['Good', 'Warning', 'Critical', 'Good']
    })
    st.dataframe(performance_metrics, use_container_width=True)
