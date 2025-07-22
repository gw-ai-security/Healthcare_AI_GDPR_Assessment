
import datetime
import os

AUDIT_LOG_PATH = "logs/audit_log.csv"

def log_action(user, role, action, view=None):
    """
    Logs user activity for GDPR Art. 30 audit trail purposes.

    Parameters:
        user (str): Username
        role (str): User role (e.g., CISO, DPO)
        action (str): Description of the action (e.g., "Viewed Consent Heatmap")
        view (str): Optional dashboard view (e.g., "DPO Dashboard")
    """
    timestamp = datetime.datetime.utcnow().isoformat()
    entry = f"{timestamp},{user},{role},{view or ''},{action}\n"

    log_dir = os.path.dirname(AUDIT_LOG_PATH)
    if not os.path.exists(log_dir):
        os.makedirs(log_dir)

    if not os.path.exists(AUDIT_LOG_PATH):
        with open(AUDIT_LOG_PATH, "w") as f:
            f.write("timestamp,user,role,view,action\n")

    with open(AUDIT_LOG_PATH, "a") as f:
        f.write(entry)
