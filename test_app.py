from app import app

def test_health():
    client = app.test_client()
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json["status"] == "ok"

def test_orders():
    response = app.test_client().get("/orders")
    assert response.status_code == 200
    assert response.json["orders"][0]["id"] == 101
