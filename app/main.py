import streamlit as st
from ciso_view import show_ciso_dashboard
from dpo_view import show_dpo_dashboard
from soc_view import show_soc_dashboard
from auditor_view import show_auditor_dashboard
from utils.audit_logger import log_action

# Simple in-memory user database (for demo purposes only)
USER_DB = {
    "ciso_user": {"password": "ciso123", "role": "CISO"},
    "dpo_user": {"password": "dpo123", "role": "DPO"},
    "soc_user": {"password": "soc123", "role": "SOC"},
    "auditor_user": {"password": "audit123", "role": "AUDITOR"}
}

def login():
    st.title("Healthcare AI GDPR Dashboard")
    st.subheader("Login")

    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        if username in USER_DB and USER_DB[username]["password"] == password:
            st.session_state["username"] = username
            st.session_state["role"] = USER_DB[username]["role"]
            st.success(f"Welcome, {username}!")
            log_action(username, USER_DB[username]["role"], "Logged in")
            st.rerun()
        else:
            st.error("Invalid username or password")

def main():
    if "username" not in st.session_state:
        login()
    else:
        role = st.session_state["role"]
        
        if st.sidebar.button("Logout"):
            log_action(st.session_state["username"], role, "Logged out")
            del st.session_state["username"]
            del st.session_state["role"]
            st.rerun()
        
        st.sidebar.write(f"Logged in as: {st.session_state['username']} ({role})")
        
        if role == "CISO":
            show_ciso_dashboard()
        elif role == "DPO":
            show_dpo_dashboard()
        elif role == "SOC":
            show_soc_dashboard()
        elif role == "AUDITOR":
            show_auditor_dashboard()

if __name__ == "__main__":
    main()
