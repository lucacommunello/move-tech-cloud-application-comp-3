from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_health():
    r = client.get("/health")
    assert r.status_code == 200
    assert r.json() == {"database": "ok", "status": "ok"}

def test_criar_e_listar_pedido():
    r = client.post("/orders", json={"customer": "Teste"})
    assert r.status_code == 201
    pedido = r.json()
    assert pedido["customer"] == "Teste"

    r2 = client.get("/orders")
    assert r2.status_code == 200
    assert any(p["id"] == pedido["id"] for p in r2.json())
