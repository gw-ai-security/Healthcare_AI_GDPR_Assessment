from utils.audit_logger import log_action, AUDIT_LOG_PATH
import streamlit as st
import pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import os
from datetime import datetime, timedelta

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

    # =========================================================================
    # NEW: LIVE AUDIT LOG SECTION - GDPR Art. 30 Compliance
    # =========================================================================
    st.markdown("---")
    st.markdown("## 📋 Live Audit Log (GDPR Art. 30 Compliance)")
    
    if os.path.exists(AUDIT_LOG_PATH):
        try:
            # Load audit log
            audit_df = pd.read_csv(AUDIT_LOG_PATH)
            
            # Convert timestamp to datetime for better handling
            audit_df['timestamp'] = pd.to_datetime(audit_df['timestamp'])
            audit_df['date'] = audit_df['timestamp'].dt.date
            audit_df['time'] = audit_df['timestamp'].dt.strftime('%H:%M:%S')
            
            # Summary Metrics Row
            st.markdown("### 📊 Audit Log Summary")
            col1, col2, col3, col4 = st.columns(4)
            
            with col1:
                st.metric("Total Log Entries", len(audit_df))
            with col2:
                st.metric("Unique Users", audit_df['user'].nunique())
            with col3:
                st.metric("Unique Roles", audit_df['role'].nunique())
            with col4:
                today_entries = len(audit_df[audit_df['date'] == datetime.now().date()])
                st.metric("Today's Activities", today_entries)
            
            # =====================================================================
            # Recent Audit Entries Table
            # =====================================================================
            st.markdown("### 🕒 Recent Audit Entries (Last 50)")
            
            # Sort by timestamp descending and get recent entries
            recent_entries = audit_df.sort_values('timestamp', ascending=False).head(50)
            
            # Display table with formatted columns
            display_df = recent_entries[['date', 'time', 'user', 'role', 'view', 'action']].copy()
            display_df.columns = ['Date', 'Time', 'User', 'Role', 'Dashboard View', 'Action']
            
            st.dataframe(
                display_df, 
                use_container_width=True,
                hide_index=True
            )
            
            # =====================================================================
            # Activity Breakdown Charts
            # =====================================================================
            col1, col2 = st.columns(2)
            
            with col1:
                st.markdown("### 👥 Activity by Role")
                role_activity = audit_df['role'].value_counts()
                
                fig_roles, ax_roles = plt.subplots(figsize=(6, 4))
                role_activity.plot(kind='bar', ax=ax_roles, color='steelblue', alpha=0.8)
                ax_roles.set_title('Audit Activities by Role', fontsize=12)
                ax_roles.set_ylabel('Number of Activities', fontsize=10)
                ax_roles.set_xlabel('Role', fontsize=10)
                plt.xticks(rotation=45, fontsize=9)
                plt.yticks(fontsize=9)
                plt.tight_layout()
                st.pyplot(fig_roles)
            
            with col2:
                st.markdown("### 🎯 Activity by Action Type")
                action_activity = audit_df['action'].value_counts().head(8)  # Top 8 actions
                
                fig_actions, ax_actions = plt.subplots(figsize=(6, 4))
                action_activity.plot(kind='barh', ax=ax_actions, color='orange', alpha=0.8)
                ax_actions.set_title('Top Actions Logged', fontsize=12)
                ax_actions.set_xlabel('Count', fontsize=10)
                plt.xticks(fontsize=9)
                plt.yticks(fontsize=8)
                plt.tight_layout()
                st.pyplot(fig_actions)
            
            # =====================================================================
            # Activity Timeline (Last 7 Days)
            # =====================================================================
            st.markdown("### 📈 Activity Timeline (Last 7 Days)")
            
            # Filter last 7 days
            seven_days_ago = datetime.now() - timedelta(days=7)
            recent_df = audit_df[audit_df['timestamp'] >= seven_days_ago].copy()
            
            if len(recent_df) > 0:
                # Group by date and count activities
                daily_activity = recent_df.groupby('date').size().reset_index(name='count')
                daily_activity['date'] = pd.to_datetime(daily_activity['date'])
                
                fig_timeline, ax_timeline = plt.subplots(figsize=(10, 3.5))
                ax_timeline.plot(daily_activity['date'], daily_activity['count'], 
                               marker='o', linewidth=2, markersize=6, color='green', alpha=0.8)
                ax_timeline.set_title('Daily Activity Volume (Last 7 Days)', fontsize=12)
                ax_timeline.set_xlabel('Date', fontsize=10)
                ax_timeline.set_ylabel('Activities', fontsize=10)
                ax_timeline.grid(True, alpha=0.3)
                plt.xticks(rotation=45, fontsize=9)
                plt.yticks(fontsize=9)
                plt.tight_layout()
                st.pyplot(fig_timeline)
            else:
                st.info("No activities recorded in the last 7 days.")
            
            # =====================================================================
            # Download/Export Section
            # =====================================================================
            st.markdown("### 💾 Export Audit Log")
            st.markdown("**GDPR Art. 30 Compliance:** Download complete audit trails for regulatory reporting")
            
            col1, col2, col3 = st.columns(3)
            
            with col1:
                # Complete audit log export
                csv_data = audit_df.to_csv(index=False)
                st.download_button(
                    label="📄 Download Complete Log (CSV)",
                    data=csv_data,
                    file_name=f"complete_audit_log_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv",
                    mime="text/csv",
                    help="Export all audit log entries for compliance reporting"
                )
            
            with col2:
                # Last 30 days export
                thirty_days_ago = datetime.now() - timedelta(days=30)
                last_30_days = audit_df[audit_df['timestamp'] >= thirty_days_ago]
                
                csv_30_days = last_30_days.to_csv(index=False)
                st.download_button(
                    label="📅 Download Last 30 Days (CSV)",
                    data=csv_30_days,
                    file_name=f"audit_log_30days_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv",
                    mime="text/csv",
                    help="Export recent audit activities for monthly reporting"
                )
            
            with col3:
                # Filtered by role export
                selected_role = st.selectbox("Filter by Role:", 
                                           ["All"] + list(audit_df['role'].unique()),
                                           key="role_filter")
                
                if selected_role != "All":
                    filtered_df = audit_df[audit_df['role'] == selected_role]
                    csv_filtered = filtered_df.to_csv(index=False)
                    st.download_button(
                        label=f"👤 Download {selected_role} Activities",
                        data=csv_filtered,
                        file_name=f"audit_log_{selected_role.lower()}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv",
                        mime="text/csv",
                        help=f"Export activities for {selected_role} role only"
                    )
            
            # Log the download action when buttons are clicked
            if st.session_state.get('audit_download_clicked'):
                log_action('demo_user', 'AUDITOR', 'Downloaded Audit Log', 'Auditor Dashboard')
                st.session_state['audit_download_clicked'] = False
                        
        except Exception as e:
            st.error(f"❌ Error loading audit log: {str(e)}")
            st.info("💡 The audit log will be created automatically as users interact with the system.")
    else:
        st.info("📝 No audit log file found yet. The log will be created automatically as users interact with the system.")
        st.code(f"Expected location: {AUDIT_LOG_PATH}")
        
        # Create a sample log entry to demonstrate
        if st.button("🔧 Initialize Audit Log (Demo)"):
            log_action('system', 'AUDITOR', 'Initialized audit logging system', 'Auditor Dashboard')
            st.success("✅ Audit log initialized! Refresh the page to see entries.")
            st.rerun()

    # =========================================================================
    # EXISTING CONTENT - Keep all original dashboard content
    # =========================================================================
    st.markdown("---")
    st.markdown("## 🚨 Export Events Without Legal Basis")
    exports = pd.DataFrame({
        'Date': pd.date_range("2024-06-10", periods=5, freq='D'),
        'User': ['U023', 'U015', 'U007', 'U033', 'U018'],
        'Country': ['US', 'IN', 'DE', 'US', 'BR'],
        'Legal Basis Missing': [True, False, True, False, True],
        'Data Volume (MB)': [45.2, 23.1, 67.8, 12.5, 89.3]
    })
    st.dataframe(exports, use_container_width=True)

    st.markdown("## 📊 Article 30 Record Completeness")
    art30_data = pd.DataFrame({
        'Processing Activity': ['Patient Registration', 'Diagnostic Imaging', 'Treatment Planning', 'Research Analytics', 'Billing'],
        'Completeness %': [95, 88, 92, 85, 98]
    })
    
    fig1, ax1 = plt.subplots(figsize=(8, 4))
    art30_data.set_index('Processing Activity')['Completeness %'].plot(
        kind='bar', ax=ax1, color='green', alpha=0.7
    )
    ax1.set_title('Article 30 Record Completeness by Processing Activity', fontsize=12)
    ax1.set_ylabel('Completeness Percentage', fontsize=10)
    ax1.axhline(y=90, color='red', linestyle='--', alpha=0.7, label='Target (90%)')
    ax1.legend()
    plt.xticks(rotation=45, fontsize=9)
    plt.yticks(fontsize=9)
    plt.tight_layout()
    st.pyplot(fig1)

    st.markdown("## 🔍 Data Subject Access Requests (DSAR)")
    dsar_data = pd.DataFrame({
        'Month': ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun'],
        'Requests': [12, 15, 9, 18, 22, 16],
        'Completed on Time': [11, 14, 9, 16, 20, 15]
    })
    
    fig2, ax2 = plt.subplots(figsize=(8, 4))
    x = range(len(dsar_data))
    ax2.bar([i - 0.2 for i in x], dsar_data['Requests'], width=0.4, label='Total Requests', color='lightblue')
    ax2.bar([i + 0.2 for i in x], dsar_data['Completed on Time'], width=0.4, label='Completed on Time', color='darkblue')
    ax2.set_title('Data Subject Access Requests - Monthly Overview', fontsize=12)
    ax2.set_xlabel('Month', fontsize=10)
    ax2.set_ylabel('Number of Requests', fontsize=10)
    ax2.set_xticks(x)
    ax2.set_xticklabels(dsar_data['Month'])
    ax2.legend()
    plt.xticks(fontsize=9)
    plt.yticks(fontsize=9)
    plt.tight_layout()
    st.pyplot(fig2)

    st.markdown("## 📈 Compliance Score Breakdown")
    compliance_scores = pd.DataFrame({
        'GDPR Article': ['Art. 5 (Principles)', 'Art. 6 (Lawfulness)', 'Art. 7 (Consent)', 'Art. 9 (Special Categories)', 'Art. 30 (Records)'],
        'Score': [85, 92, 78, 88, 95]
    })
    
    fig3, ax3 = plt.subplots(figsize=(8, 4))
    compliance_scores.set_index('GDPR Article')['Score'].plot(
        kind='barh', ax=ax3, color='orange', alpha=0.8
    )
    ax3.set_title('GDPR Compliance Scores by Article', fontsize=12)
    ax3.set_xlabel('Compliance Score (%)', fontsize=10)
    ax3.axvline(x=80, color='red', linestyle='--', alpha=0.7,<span class="cursor">█</span>
