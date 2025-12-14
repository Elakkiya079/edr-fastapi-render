from fastapi.testclient import TestClient
from app.main import app
import json

client = TestClient(app)

def test_create_get_update_delete_doctor():
    # Create
    rv = client.post("/Doctor/", json={"name":"Dr. Test","age":45,"gender":"Male","speciality":"Dermatology"})
    assert rv.status_code == 201
    data = rv.json()
    doc_id = data["id"]

    # Get
    rv2 = client.get(f"/Doctor/{doc_id}")
    assert rv2.status_code == 200
    assert rv2.json()["name"] == "Dr. Test"

    # Update
    rv3 = client.put(f"/Doctors/{doc_id}", json={"name":"Dr. Test Updated","age":46})
    assert rv3.status_code == 200
    assert rv3.json()["name"] == "Dr. Test Updated"

    # Delete (soft)
    rv4 = client.delete(f"/Doctors/{doc_id}")
    assert rv4.status_code == 200

    # Verify not found
    rv5 = client.get(f"/Doctor/{doc_id}")
    assert rv5.status_code == 404
