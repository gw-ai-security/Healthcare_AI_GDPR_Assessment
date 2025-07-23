from utils.audit_logger import log_action
import streamlit as st
import pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

def show_auditor_dashboard():
    log_action('demo_user', 'AUDITOR', 'Accessed Dashboard', 'Auditor Dashboard')
    
    st.title("Auditor Dashboard - Documentation & GDPR Traceability")

    st.markdown("""
    This dashboard provides audit-relevant documentation insights for GDPR Art. 30 reporting,
    data access traceability, and policy compliance summaries.
    """)

    # KPIs
    col1, col2, col3 = st.columns(3)
    col1.metric("Art. 30 Coverage", "92%", "+3%")
    col2.metric("Access Log Completeness", "98%", "+1%")
    col3.metric("Manual Overrides", "2", "0")

    st.markdown("## Export Events Without Legal Basis")
    exports = pd.DataFrame({
        'Date': pd.date_range("2024-06-10", periods=5, freq='D'),
        'User': ['U023', 'U015', 'U007', 'U033', 'U018'],
        'Country': ['US', 'IN', 'DE', 'US', 'BR'],
        'Legal Basis Missing': [True, False, True, False, True],
        'Data Volume (MB)': [45.2, 23.1, 67.8, 12.5, 89.3]
    })
    st.dataframe(exports, use_container_width=True)

    st.markdown("## Article 30 Record Completeness")
    art30_data = pd.DataFrame({
        'Processing Activity': ['Patient Registration', 'Diagnostic Imaging', 'Treatment Planning', 'Research Analytics', 'Billing'],
        'Completeness %': [95, 88, 92, 85, 98]
    })
    
    fig1, ax1 = plt.subplots(figsize=(10, 6))
    art30_data.set_index('Processing Activity')['Completeness %'].plot(
        kind='bar', ax=ax1, color='green', alpha=0.7
    )
    ax1.set_title('Article 30 Record Completeness by Processing Activity')
    ax1.set_ylabel('Completeness Percentage')
    ax1.axhline(y=90, color='red', linestyle='--', alpha=0.7, label='Target (90%)')
    ax1.legend()
    plt.xticks(rotation=45)
    st.pyplot(fig1)

    st.markdown("## Data Subject Access Requests (DSAR)")
    dsar_data = pd.DataFrame({
        'Month': ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun'],
        'Requests': [12, 15, 9, 18, 22, 16],
        'Completed on Time': [11, 14, 9, 16, 20, 15]
    })
    
    fig2, ax2 = plt.subplots(figsize=(10, 6))
    x = range(len(dsar_data))
    ax2.bar([i - 0.2 for i in x], dsar_data['Requests'], width=0.4, label='Total Requests', color='lightblue')
    ax2.bar([i + 0.2 for i in x], dsar_data['Completed on Time'], width=0.4, label='Completed on Time', color='darkblue')
    ax2.set_title('Data Subject Access Requests - Monthly Overview')
    ax2.set_xlabel('Month')
    ax2.set_ylabel('Number of Requests')
    ax2.set_xticks(x)
    ax2.set_xticklabels(dsar_data['Month'])
    ax2.legend()
    st.pyplot(fig2)

    st.markdown("## Compliance Score Breakdown")
    compliance_scores = pd.DataFrame({
        'GDPR Article': ['Art. 5 (Principles)', 'Art. 6 (Lawfulness)', 'Art. 7 (Consent)', 'Art. 9 (Special Categories)', 'Art. 30 (Records)'],
        'Score': [85, 92, 78, 88, 95]
    })
    
    fig3, ax3 = plt.subplots(figsize=(10, 6))
    compliance_scores.set_index('GDPR Article')['Score'].plot(
        kind='barh', ax=ax3, color='orange', alpha=0.8
    )
    ax3.set_title('GDPR Compliance Scores by Article')
    ax3.set_xlabel('Compliance Score (%)')
    ax3.axvline(x=80, color='red', linestyle='--', alpha=0.7, label='Minimum Threshold (80%)')
    ax3.legend()
    st.pyplot(fig3)

    st.markdown("## Audit Trail Summary")
    audit_trail = pd.DataFrame({
        'Activity': ['Data Access', 'Data Modification', 'Data Export', 'User Login', 'System Changes'],
        'Total Events (30d)': [1245, 356, 89, 2156, 23],
        'Logged Events': [1245, 356, 89, 2156, 23],
        'Coverage %': [100, 100, 100, 100, 100]
    })
    st.dataframe(audit_trail, use_container_width=True)

    st.markdown("## Data Processing Agreements Status")
    dpa_status = pd.DataFrame({
        'Third Party': ['Cloud Provider A', 'Analytics Service B', 'Backup Service C', 'Research Partner D'],
        'DPA Status': ['Active', 'Active', 'Expired', 'Under Review'],
        'Expiry Date': ['2025-03-15', '2024-12-31', '2024-06-30', '2024-08-15'],
        'Risk Level': ['Low', 'Low', 'High', 'Medium']
    })
    st.dataframe(dpa_status, use_container_width=True)

    st.markdown("## Documentation Completeness")
    doc_completeness = pd.DataFrame({
        'Document Type': ['Privacy Notices', 'Consent Forms', 'Processing Records', 'Impact Assessments', 'Breach Procedures'],
        'Required': [15, 8, 12, 6, 3],
        'Available': [14, 8, 11, 5, 3],
        'Up to Date': [13, 7, 10, 4, 3],
        'Completeness %': [87, 88, 83, 67, 100]
    })
    st.dataframe(doc_completeness, use_container_width=True)
