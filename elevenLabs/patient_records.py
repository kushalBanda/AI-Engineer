"""
Mock patient database.
In production, replace with a real DB / EHR lookup.
"""

PATIENTS: dict[str, dict] = {
    "john smith": {
        "patient_id": "P001",
        "dob": "1985-04-12",
        "doctor": "Dr. Emily Carter",
        "upcoming_appointments": ["2026-03-15 10:00 AM"],
        "notes": "Allergic to penicillin. Prefers morning slots.",
    },
    "sarah lee": {
        "patient_id": "P002",
        "dob": "1990-07-23",
        "doctor": "Dr. James Patel",
        "upcoming_appointments": [],
        "notes": "New patient. Referral from GP for annual check-up.",
    },
}

# Reverse index for O(1) patient ID lookups
_BY_ID: dict[str, dict] = {r["patient_id"].lower(): r for r in PATIENTS.values()}


def lookup(name: str | None = None, patient_id: str | None = None) -> dict:
    """Return patient record by name or patient_id, or an error dict."""
    if patient_id:
        record = _BY_ID.get(patient_id.lower().strip())
        if record:
            return record

    if name:
        record = PATIENTS.get(name.lower().strip())
        if record:
            return record

    return {"error": "Patient not found. Please verify name or patient ID."}
