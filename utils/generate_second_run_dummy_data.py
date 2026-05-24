from pathlib import Path
import csv

BASE_DIR = Path(__file__).resolve().parent.parent / "data" / "EMR"
OUTPUT_DIR = BASE_DIR / "dummy_second_run"


def write_csv(path: Path, header, rows):
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(header)
        writer.writerows(rows)


hospital_a = {
    "departments": [
        ["DEPT101", "Cardiology"],
        ["DEPT102", "Neurology"],
        ["DEPT103", "Emergency"],
    ],
    "providers": [
        ["PROV1001", "Amelia", "Hart", "Cardiology", "DEPT101", 1182456712],
        ["PROV1002", "Noah", "Singh", "Neurology", "DEPT102", 2249812057],
        ["PROV1003", "Sofia", "Mendez", "Emergency Medicine", "DEPT103", 5512349876],
    ],
    "patients": [
        ["HOSP1-000101", "Emma", "Davis", "A", "112-33-4455", "555-111-2233", "Female", "1990-03-12", "120 Oak Street, Austin, TX 78701", "2024-10-01"],
        ["HOSP1-000102", "Liam", "Brown", "B", "223-44-5566", "555-222-3344", "Male", "1985-08-18", "88 Pine Avenue, Dallas, TX 75201", "2024-10-02"],
        ["HOSP1-000103", "Olivia", "Wilson", "C", "334-55-6677", "555-333-4455", "Female", "1998-12-25", "17 Cedar Lane, Houston, TX 77002", "2024-10-03"],
    ],
    "encounters": [
        ["ENC100001", "HOSP1-000101", "2024-10-01", "Inpatient", "PROV1001", "DEPT101", 93000, "2024-10-01", "2024-10-01"],
        ["ENC100002", "HOSP1-000102", "2024-10-02", "Outpatient", "PROV1002", "DEPT102", 99213, "2024-10-02", "2024-10-02"],
        ["ENC100003", "HOSP1-000103", "2024-10-03", "Emergency", "PROV1003", "DEPT103", 99283, "2024-10-03", "2024-10-03"],
    ],
    "transactions": [
        ["TRANS100001", "ENC100001", "HOSP1-000101", "PROV1001", "DEPT101", "2024-10-01", "2024-10-01", "2024-10-02", "Follow-up", 450.00, "Insurance", 320.00, "CLAIM100001", "PAYOR1001", 93000, "I10", "Commercial", "MEDA10001", "MCARE10001", "2024-10-01", "2024-10-02"],
        ["TRANS100002", "ENC100002", "HOSP1-000102", "PROV1002", "DEPT102", "2024-10-02", "2024-10-02", "2024-10-02", "Consultation", 180.00, "Self-pay", 180.00, "CLAIM100002", "PAYOR1002", 99213, "G47.33", "Self-Pay", "MEDA10002", "MCARE10002", "2024-10-02", "2024-10-02"],
        ["TRANS100003", "ENC100003", "HOSP1-000103", "PROV1003", "DEPT103", "2024-10-03", "2024-10-03", "2024-10-03", "Emergency", 620.00, "Medicare", 500.00, "CLAIM100003", "PAYOR1003", 99283, "R05", "Medicare", "MEDA10003", "MCARE10003", "2024-10-03", "2024-10-03"],
    ],
}

hospital_b = {
    "departments": [
        ["DEPT201", "Pediatrics"],
        ["DEPT202", "Radiology"],
        ["DEPT203", "Oncology"],
    ],
    "providers": [
        ["PROV2001", "Ava", "Parker", "Pediatrics", "DEPT201", 3377401155],
        ["PROV2002", "Mason", "Rivera", "Radiology", "DEPT202", 4491228901],
        ["PROV2003", "Ella", "Brooks", "Oncology", "DEPT203", 6623954013],
    ],
    "patients": [
        ["HOSP2-000201", "Sophia", "Mills", "A", "445-66-7788", "555-444-5566", "Female", "1994-04-16", "55 Maple Drive, San Antonio, TX 78201", "2024-10-04"],
        ["HOSP2-000202", "James", "Moran", "B", "556-77-8899", "555-555-6677", "Male", "1988-09-09", "102 Birch Road, Fort Worth, TX 76101", "2024-10-05"],
        ["HOSP2-000203", "Aria", "Chen", "C", "667-88-9900", "555-666-7788", "Female", "2001-12-01", "9 Sunset Boulevard, El Paso, TX 79901", "2024-10-06"],
    ],
    "encounters": [
        ["ENC200001", "HOSP2-000201", "2024-10-04", "Outpatient", "PROV2001", "DEPT201", 99391, "2024-10-04", "2024-10-04"],
        ["ENC200002", "HOSP2-000202", "2024-10-05", "Inpatient", "PROV2002", "DEPT202", 71020, "2024-10-05", "2024-10-05"],
        ["ENC200003", "HOSP2-000203", "2024-10-06", "Routine Checkup", "PROV2003", "DEPT203", 11101, "2024-10-06", "2024-10-06"],
    ],
    "transactions": [
        ["TRANS200001", "ENC200001", "HOSP2-000201", "PROV2001", "DEPT201", "2024-10-04", "2024-10-04", "2024-10-05", "Routine", 260.00, "Insurance", 210.00, "CLAIM200001", "PAYOR2001", 99391, "Z00.00", "Commercial", "MEDB20001", "MCARE20001", "2024-10-04", "2024-10-05"],
        ["TRANS200002", "ENC200002", "HOSP2-000202", "PROV2002", "DEPT202", "2024-10-05", "2024-10-05", "2024-10-05", "Follow-up", 420.00, "Medicare", 380.00, "CLAIM200002", "PAYOR2002", 71020, "M17.9", "Medicare", "MEDB20002", "MCARE20002", "2024-10-05", "2024-10-05"],
        ["TRANS200003", "ENC200003", "HOSP2-000203", "PROV2003", "DEPT203", "2024-10-06", "2024-10-06", "2024-10-06", "Consultation", 540.00, "Self-pay", 540.00, "CLAIM200003", "PAYOR2003", 11101, "E11.9", "Self-Pay", "MEDB20003", "MCARE20003", "2024-10-06", "2024-10-06"],
    ],
}

for hospital_name, hospital_data in (("hospital-a", hospital_a), ("hospital-b", hospital_b)):
    write_csv(
        OUTPUT_DIR / hospital_name / "departments.csv",
        ["DeptID", "Name"],
        hospital_data["departments"],
    )
    write_csv(
        OUTPUT_DIR / hospital_name / "providers.csv",
        ["ProviderID", "FirstName", "LastName", "Specialization", "DeptID", "NPI"],
        hospital_data["providers"],
    )
    if hospital_name == "hospital-a":
        write_csv(
            OUTPUT_DIR / hospital_name / "patients.csv",
            ["PatientID", "FirstName", "LastName", "MiddleName", "SSN", "PhoneNumber", "Gender", "DOB", "Address", "ModifiedDate"],
            hospital_data["patients"],
        )
    else:
        write_csv(
            OUTPUT_DIR / hospital_name / "patients.csv",
            ["ID", "F_Name", "L_Name", "M_Name", "SSN", "PhoneNumber", "Gender", "DOB", "Address", "ModifiedDate"],
            hospital_data["patients"],
        )
    write_csv(
        OUTPUT_DIR / hospital_name / "encounters.csv",
        ["EncounterID", "PatientID", "EncounterDate", "EncounterType", "ProviderID", "DepartmentID", "ProcedureCode", "InsertedDate", "ModifiedDate"],
        hospital_data["encounters"],
    )
    write_csv(
        OUTPUT_DIR / hospital_name / "transactions.csv",
        ["TransactionID", "EncounterID", "PatientID", "ProviderID", "DeptID", "VisitDate", "ServiceDate", "PaidDate", "VisitType", "Amount", "AmountType", "PaidAmount", "ClaimID", "PayorID", "ProcedureCode", "ICDCode", "LineOfBusiness", "MedicaidID", "MedicareID", "InsertDate", "ModifiedDate"],
        hospital_data["transactions"],
    )

print(f"Generated CSVs in {OUTPUT_DIR}")
