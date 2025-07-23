import streamlit as st
from ciso_view import show_ciso_dashboard
from dpo_view import show_dpo_dashboard
from soc_view import show_soc_dashboard
from auditor_view import show_auditor_dashboard
from utils.audit_logger import log_action

# Custom CSS und Theme
def load_custom_css():
    st.markdown("""
    <style>
    /* Healthcare AI GDPR Dashboard Custom Styles */
    
    .main .block-container {
        padding-top: 2rem;
        padding-bottom: 2rem;
    }
    
    .css-1d391kg {
        background-color: #f8f9fa;
        border-right: 2px solid #2E8B57;
    }
    
    [data-testid="metric-container"] {
        background-color: #f8f9fa;
        border: 1px solid #dee2e6;
        padding: 1rem;
        border-radius: 0.5rem;
        box-shadow: 0 0.125rem 0.25rem rgba(0, 0, 0, 0.075);
    }
    
    .dataframe {
        border: 1px solid #dee2e6;
        border-radius: 0.375rem;
    }
    
    .stSuccess {
        background-color: #d1e7dd;
        border-color: #badbcc;
        color: #0f5132;
    }
    
    .stError {
        background-color: #f8d7da;
        border-color: #f5c2c7;
        color: #842029;
    }
    
    .stTextInput > div > div > input {
        border-radius: 0.375rem;
        border: 1px solid #ced4da;
    }
    
    .stButton > button {
        background-color: #2E8B57;
        color: white;
        border-radius: 0.375rem;
        border: none;
        font-weight: 500;
    }
    
    .stButton > button:hover {
        background-color: #236744;
        color: white;
    }
    
    .stDownloadButton > button {
        background-color: #0d6efd;
        color: white;
        border-radius: 0.375rem;
    }
    
    /* Title Styling */
    h1 {
        color: #2E8B57;
        font-weight: 600;
    }
    
    h2 {
        color: #1C1C1C;
        border-bottom: 2px solid #2E8B57;
        padding-bottom: 0.5rem;
    }
    </style>
    """, unsafe_allow_html=True)

# Page Config
st.set_page_config(
    page_title="Healthcare AI GDPR Dashboard",
    page_icon="🛡️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Load custom CSS
load_custom_css()

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
