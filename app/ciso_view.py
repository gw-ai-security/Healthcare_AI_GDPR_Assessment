
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

def show_ciso_dashboard():
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

    fig, ax = plt.subplots()
    risky_actions.set_index('Department').plot(kind='bar', ax=ax, legend=False)
    ax.set_ylabel("Number of Events")
    st.pyplot(fig)

    st.markdown("## 🌍 Data Export Risk Heatmap")
    heatmap_data = pd.DataFrame(
        [[0.1, 0.5, 0.7], [0.3, 0.9, 0.2], [0.6, 0.2, 0.8]],
        columns=["EU", "US", "Other"], index=["Q1", "Q2", "Q3"]
    )
    st.dataframe(heatmap_data.style.background_gradient(cmap='Oranges'))

    st.markdown("## 📉 GDPR Risk Trend Over Time")
    trend = pd.DataFrame({
        'Date': pd.date_range("2024-06-01", periods=6, freq="W"),
        'Risk Score': [60, 63, 67, 69, 72, 72]
    })
    st.line_chart(trend.set_index("Date"))
