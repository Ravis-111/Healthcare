import csv
import random
from datetime import datetime, timedelta

rows = 500

encounter_types = [
    "Inpatient",
    "Outpatient",
    "Telemedicine",
    "Routine Checkup",
    "Emergency"
]

start_date = datetime(2020, 1, 1)
end_date = datetime(2024, 12, 31)

def random_date(start, end):
    delta = end - start
    random_days = random.randint(0, delta.days)
    return start + timedelta(days=random_days)

with open("D:\myhealtproject\gcp-healthcare-project\data\EMR\hospital-b\encounters.csv", "w", newline="") as f:
    writer = csv.writer(f)

    writer.writerow([
        "EncounterID","PatientID","EncounterDate","EncounterType",
        "ProviderID","DepartmentID","ProcedureCode",
        "InsertedDate","ModifiedDate"
    ])

    for i in range(1, rows + 1):

        encounter_id = f"ENC{i:06d}"
        patient_id = f"HOSP1-{random.randint(1,5000):06d}"
        encounter_date = random_date(start_date, end_date)

        inserted_date = random_date(start_date, end_date)
        modified_date = random_date(inserted_date, end_date)

        writer.writerow([
            encounter_id,
            patient_id,
            encounter_date.strftime("%Y-%m-%d"),
            random.choice(encounter_types),
            f"PROV{random.randint(1,500):04d}",
            f"DEPT{random.randint(1,20):03d}",
            random.randint(10000, 99999),
            inserted_date.strftime("%Y-%m-%d"),
            modified_date.strftime("%Y-%m-%d")
        ])

print("encounters.csv with 500 rows generated successfully.")