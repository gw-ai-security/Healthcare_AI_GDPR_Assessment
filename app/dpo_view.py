from app.utils.audit_logger import log_action
import streamlit as st
import pandas as pd
import matplotlib
matplotlib.use('Agg')  # Für Streamlit
import matplotlib.pyplot as plt

def show_dpo_dashboard():
    log_action('demo_user', 'DPO', 'Accessed Dashboard', 'DPO Dashboard')
    
    st.title("👩‍⚖️ DPO Dashboard – GDPR Article Compliance")

    st.markdown("""
    This view is designed for the Data Protection Officer (DPO) to monitor consent violations, 
    GDPR Article triggers, and compliance anomalies within the healthcare AI system.
    """)

    # KPIs
    col1, col2, col3 = st.columns(3)
    col1.metric("Consent Violations", "18", "▲ 3")
    col2.metric("Art. 9 Data Exposures", "5", "+1")
    col3.metric("Cross-border Transfers", "7", "▼ 2")

    st.markdown("## 📌 GDPR Article Violations Breakdown")
    articles = pd.DataFrame({
        'GDPR Article': ['Art. 5', 'Art. 7', 'Art. 9', 'Art. 22', 'Art. 44'],
        'Violations': [6, 2, 5, 3, 7]
    })

    fig1, ax1 = plt.subplots(figsize=(10, 6))
    articles.set_index('GDPR Article')['Violations'].plot(
        kind='bar', ax=ax1, color='darkred', alpha=0.8
    )
    ax1.set_title('GDPR Article Violations')
    ax1.set_ylabel('Number of Violations')
    plt.xticks(rotation=45)
    st.pyplot(fig1)

    st.markdown("## 🍪 Consent Withdrawal Heatmap")
    consent_data = pd.DataFrame({
        'Department': ['Radiology', 'Oncology', 'Cardiology', 'Neurology', 'Emergency'],
        'Withdrawals': [3, 7, 2, 4, 2]
    })
    
    fig2, ax2 = plt.subplots(figsize=(10, 6))
    consent_data.set_index('Department')['Withdrawals'].plot(
        kind='barh', ax=ax2, color='purple', alpha=0.7
    )
    ax2.set_title('Consent Withdrawals by Department')
    ax2.set_xlabel('Number of Withdrawals')
    st.pyplot(fig2)

    st.markdown("## 🌍 Cross-Border Transfer Log")
    transfers = pd.DataFrame({
        'Date': pd.date_range("2024-06-15", periods=5, freq='D'),
        'Destination': ['US', 'Canada', 'Switzerland', 'UK', 'Japan'],
        'Data Type': ['Imaging Data', 'Patient Records', 'Research Data', 'Diagnostic Reports', 'Clinical Trial Data'],
        'Legal Basis': ['Adequate Decision', 'SCCs', 'Adequate Decision', 'Adequate Decision', 'SCCs']
    })
    st.dataframe(transfers, use_container_width=True)
