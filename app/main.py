# /app/main.py

import streamlit as st
from app.ciso_view import show_ciso_dashboard
from app.dpo_view import show_dpo_dashboard
from app.soc_view import show_soc_dashboard
from app.auditor_view import show_auditor_dashboard
from app.audit_logger import log_action

# Dummy login database (to be replaced with secure version)
USER_DB = {
    "ciso_user": {"password": "ciso123", "role": "CISO"},
    "dpo_user": {"password": "dpo123", "role": "DPO"},
    "soc_user": {"password": "soc123", "role": "SOC"},
    "auditor_user": {"password": "audit123", "role": "AUDITOR"},
}

def login():
    st.title("🔐 GDPR Security Dashboard – Login")

    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        user = USER_DB.get(username)
        if user and user["password"] == password:
            st.session_state["logged_in"] = True
            st.session_state["role"] = user["role"]
            st.success(f"Welcome {user['role']}!")
            st.experimental_rerun()
        else:
            st.error("Invalid credentials")

def route_to_dashboard(role):
    if role == "CISO":
        show_ciso_dashboard()
    elif role == "DPO":
        show_dpo_dashboard()
    elif role == "SOC":
        show_soc_dashboard()
    elif role == "AUDITOR":
        show_auditor_dashboard()
    else:
        st.error("Unauthorized access.")

def main():
    if "logged_in" not in st.session_state:
        st.session_state["logged_in"] = False

    if not st.session_state["logged_in"]:
        login()
    else:
        route_to_dashboard(st.session_state["role"])

if __name__ == "__main__":
    main()

