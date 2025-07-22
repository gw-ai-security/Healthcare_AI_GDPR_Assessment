
# /app/main.py

import streamlit as st
from ciso_view import show_ciso_dashboard
from dpo_view import show_dpo_dashboard
from soc_view import show_soc_dashboard
from auditor_view import show_auditor_dashboard
from audit_logger import log_action

# Simple in-memory user database (for demo purposes only)
USER_DB = {
    "ciso_user": {"password": "ciso123", "role": "CISO"},
    "dpo_user": {"password": "dpo123", "role": "DPO"},
    "soc_user": {"password": "soc123", "role": "SOC"},
    "auditor_user": {"password": "audit123", "role": "AUDITOR"}
}

def login():
    st.title("🛡️ Healthcare AI GDPR Dashboard")
    st.subheader("Login")

    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        if username in USER_DB and USER_DB[username]["password"] == password:
            st.session_state["username"] = username
            st.session_state["role"] = USER_DB[username]["role"]
            st.success(f"Welcome, {username} ({st.session_state['role']})")
            st.experimental_rerun()
        else:
            st.error("Invalid credentials.")

def show_dashboard():
    role = st.session_state.get("role", "UNKNOWN")

    if role == "CISO":
        show_ciso_dashboard()
    elif role == "DPO":
        show_dpo_dashboard()
    elif role == "SOC":
        show_soc_dashboard()
    elif role == "AUDITOR":
        show_auditor_dashboard()
    else:
        st.warning("Unknown role.")

if __name__ == "__main__":
    if "username" not in st.session_state:
        login()
    else:
        show_dashboard()
