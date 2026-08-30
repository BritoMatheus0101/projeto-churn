from fastapi.testclient import TestClient
from src.app import app

client = TestClient(app)

def test_rotas_iniciais():
    """Verifica se a raiz e o health check estão online e respondendo."""
    response_home = client.get("/")
    assert response_home.status_code == 200
    assert "api" in response_home.json()

    response_health = client.get("/health")
    assert response_health.status_code == 200
    assert response_health.json()["status"] == "saudável"

def test_previsao_sucesso():
    """Envia um cliente válido e espera o cálculo de churn (200 OK)."""
    payload = {
        "gender": 1, "SeniorCitizen": 1, "Partner": 0, "Dependents": 0,
        "tenure": 1, "PhoneService": 1, "PaperlessBilling": 1,
        "MonthlyCharges": 95.50, "TotalCharges": 95.50,
        "MultipleLines_No phone service": 0, "MultipleLines_Yes": 1,
        "InternetService_Fiber optic": 1, "InternetService_No": 0,
        "OnlineSecurity_1.0": 0, "OnlineBackup_No internet service": 0,
        "OnlineBackup_Yes": 0, "DeviceProtection_1.0": 0, "TechSupport_1.0": 0,
        "StreamingTV_1.0": 1, "StreamingMovies_1.0": 1,
        "Contract_One year": 0, "Contract_Two year": 0,
        "PaymentMethod_Credit card (automatic)": 0,
        "PaymentMethod_Electronic check": 1, "PaymentMethod_Mailed check": 0
    }
    response = client.post("/predict", json=payload)
    assert response.status_code == 200
    assert "churn_prediction" in response.json()

def test_previsao_falha_contrato():
    """Envia dados propositalmente errados para testar o bloqueio (422)."""
    payload_invalido = {"tenure": "dois meses"}
    response = client.post("/predict", json=payload_invalido)
    assert response.status_code == 422