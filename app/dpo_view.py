from utils.audit_logger import log_action
import streamlit as st
import pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

def show_dpo_dashboard():
    log_action('demo_user', 'DPO', 'Accessed Dashboard', 'DPO Dashboard')
    
    st.title("DPO Dashboard - GDPR Article Compliance")

    st.markdown("""
    This view is designed for the Data Protection Officer (DPO) to monitor consent violations, 
    GDPR Article triggers, and compliance anomalies within the healthcare AI system.
    """)

    # KPIs
    col1, col2, col3 = st.columns(3)
    col1.metric("Consent Violations", "18", "3")
    col2.metric("Art. 9 Data Exposures", "5", "+1")
    col3.metric("Cross-border Transfers", "7", "-2")

    st.markdown("## GDPR Article Violations Breakdown")
    articles = pd.DataFrame({
        'GDPR Article': ['Art. 5', 'Art. 7', 'Art. 9', 'Art. 22', 'Art. 44'],
        'Violations': [6, 2, 5, 3, 7]
    })

    # Kompaktere Größe
    fig1, ax1 = plt.subplots(figsize=(7, 4))
    articles.set_index('GDPR Article')['Violations'].plot(
        kind='bar', ax=ax1, color='darkred', alpha=0.8
    )
    ax1.set_title('GDPR Article Violations', fontsize=12)
    ax1.set_ylabel('Number of Violations', fontsize=10)
    plt.xticks(rotation=45, fontsize=9)
    plt.yticks(fontsize=9)
    plt.tight_layout()
    st.pyplot(fig1)

    st.markdown("## Consent Withdrawal Heatmap")
    consent_data = pd.DataFrame({
        'Department': ['Radiology', 'Oncology', 'Cardiology', 'Neurology', 'Emergency'],
        'Withdrawals': [3, 7, 2, 4, 2]
    })
    
    # Horizontaler Chart kleiner
    fig2, ax2 = plt.subplots(figsize=(7, 3.5))
    consent_data.set_index('Department')['Withdrawals'].plot(
        kind='barh', ax=ax2, color='purple', alpha=0.7
    )
    ax2.set_title('Consent Withdrawals by Department', fontsize=12)
    ax2.set_xlabel('Number of Withdrawals', fontsize=10)
    plt.xticks(fontsize=9)
    plt.yticks(fontsize=9)
    plt.tight_layout()
    st.pyplot(fig2)

    # Rest bleibt gleich...
    st.markdown("## Cross-Border Transfer Log")
    transfers = pd.DataFrame({
        'Date': pd.date_range("2024-06-15", periods=5, freq='D'),
        'Destination': ['US', 'Canada', 'Switzerland', 'UK', 'Japan'],
        'Data Type': ['Imaging Data', 'Patient Records', 'Research Data', 'Diagnostic Reports', 'Clinical Trial Data'],
        'Legal Basis': ['Adequate Decision', 'SCCs', 'Adequate Decision', 'Adequate Decision', 'SCCs']
    })
    st.dataframe(transfers, use_container_width=True)

    st.markdown("## Data Subject Rights Requests")
    dsr_data = pd.DataFrame({
        'Request Type': ['Access', 'Rectification', 'Erasure', 'Portability', 'Restriction'],
        'This Month': [12, 3, 8, 2, 1],
        'Last Month': [15, 2, 6, 3, 2],
        'Average Response Time (days)': [18, 12, 25, 15, 10]
    })
    st.dataframe(dsr_data, use_container_width=True)

    st.markdown("## Privacy Impact Assessment Status")
    pia_data = pd.DataFrame({
        'Processing Activity': ['AI Diagnosis System', 'Patient Portal', 'Research Database', 'Billing System'],
        'PIA Status': ['Completed', 'In Progress', 'Required', 'Completed'],
        'Risk Level': ['Medium', 'Low', 'High', 'Low'],
        'Next Review Date': ['2024-12-01', '2024-08-15', '2024-07-30', '2025-01-15']
    })
    st.dataframe(pia_data, use_container_width=True)
