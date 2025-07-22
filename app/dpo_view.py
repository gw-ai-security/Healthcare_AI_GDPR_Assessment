from app.utils.audit_logger import log_action

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

    log_action('demo_user', 'DPO', 'Accessed Dashboard', 'DPO Dashboard')
def show_dpo_dashboard():
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

    fig1, ax1 = plt.subplots()
    articles.set_index('GDPR Article').plot(kind='bar', ax=ax1, color='tomato', legend=False)
    ax1.set_ylabel("Violation Count")
    st.pyplot(fig1)

    st.markdown("## 🌍 Transfers by Country")
    transfers = pd.DataFrame({
        'Country': ['Germany', 'France', 'US', 'India'],
        'Transfers': [14, 11, 7, 5]
    })

    fig2, ax2 = plt.subplots()
    transfers.set_index('Country').plot.pie(y='Transfers', ax=ax2, legend=False, autopct='%1.1f%%')
    ax2.set_ylabel("")
    st.pyplot(fig2)

    st.markdown("## 🧾 Consent Heatmap (Demo)")
    heatmap_data = pd.DataFrame(
        [[0.85, 0.75], [0.90, 0.65], [0.80, 0.95]],
        columns=["Radiology", "Oncology"], index=["Jan", "Feb", "Mar"]
    )
    st.dataframe(heatmap_data.style.background_gradient(cmap='Purples'))