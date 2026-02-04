import requests
import pytest

BASE_URL = "http://127.0.0.1:5000"

@pytest.fixture
def patient():
    return {
        "id": 1,
        "name": "Ravi",
        "age": 30,
        "gender": "Male",
        "contact": "9999999999",
        "disease": "Fever",
        "doctor": "Dr. Smith"
    }

def test_get_patients():
    r = requests.get(f"{BASE_URL}/api/patients")
    assert r.status_code == 200

def test_add_patient(patient):
    r = requests.post(f"{BASE_URL}/api/patients", json=patient)
    assert r.status_code == 201

@pytest.mark.parametrize("pid", [1])
def test_get_patient(pid):
    r = requests.get(f"{BASE_URL}/api/patients/{pid}")
    assert r.status_code == 200

@pytest.mark.xfail(reason="Known bug")
def test_negative_case():
    r = requests.get(f"{BASE_URL}/api/patients/999")
    assert r.status_code == 200
