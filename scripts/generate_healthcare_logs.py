
import pandas as pd
import random
from datetime import datetime, timedelta

# Configuration
n = 100  # number of rows
start_date = datetime(2024, 1, 1)

# Sample options
diagnosis_codes = ['C50.9', 'E11.9', 'I10', 'J45.9', 'K21.0']
countries = ['DE', 'FR', 'IT', 'NL', 'SE', 'PL', 'US', 'CA', 'CN', 'IN']
roles = ['admin', 'clinician', 'researcher', 'ai_service', 'external_vendor']

# Generate data
data = []
for i in range(n):
    user_id = f"U{str(i+1).zfill(3)}"
    timestamp = start_date + timedelta(hours=random.randint(0, 1440))
    diagnosis = random.choice(diagnosis_codes)
    country = random.choice(countries)
    consent = random.choice([True, False])
    role = random.choice(roles)

    data.append({
        "UserID": user_id,
        "Timestamp": timestamp.isoformat() + "Z",
        "DiagnosisCode": diagnosis,
        "Country": country,
        "ConsentStatus": consent,
        "Role": role
    })

# Create DataFrame and export
df = pd.DataFrame(data)
df.to_csv("../data/healthcare_logs.csv", index=False)
print("✅ healthcare_logs.csv with 'Role' column successfully generated.")
