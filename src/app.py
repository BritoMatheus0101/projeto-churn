from fastapi import FastAPI
from pydantic import BaseModel, Field
from src.predict import ChurnPredictor


app = FastAPI(title="API para previsão de churn", version="1.0")
predictor = ChurnPredictor()

class CustomerInput(BaseModel):
    gender: int
    SeniorCitizen: int
    Partner: int
    Dependents: int
    tenure: int
    PhoneService: int
    PaperlessBilling: int
    MonthlyCharges: float
    TotalCharges: float
    
    # Usamos 'alias' para mapear o nome da variável no Python para o nome exato da coluna do modelo
    MultipleLines_No_phone_service: int = Field(alias="MultipleLines_No phone service")
    MultipleLines_Yes: int
    InternetService_Fiber_optic: int = Field(alias="InternetService_Fiber optic")
    InternetService_No: int
    OnlineSecurity_1_0: int = Field(alias="OnlineSecurity_1.0")
    OnlineBackup_No_internet_service: int = Field(alias="OnlineBackup_No internet service")
    OnlineBackup_Yes: int
    DeviceProtection_1_0: int = Field(alias="DeviceProtection_1.0")
    TechSupport_1_0: int = Field(alias="TechSupport_1.0")
    StreamingTV_1_0: int = Field(alias="StreamingTV_1.0")
    StreamingMovies_1_0: int = Field(alias="StreamingMovies_1.0")
    Contract_One_year: int = Field(alias="Contract_One year")
    Contract_Two_year: int = Field(alias="Contract_Two year")
    PaymentMethod_Credit_card_automatic: int = Field(alias="PaymentMethod_Credit card (automatic)")
    PaymentMethod_Electronic_check: int = Field(alias="PaymentMethod_Electronic check")
    PaymentMethod_Mailed_check: int = Field(alias="PaymentMethod_Mailed check")

@app.get("/")
def home():
    """Rota principal com manual de uso da API"""
    return {
        "api": "Api para previsão de churn",
        "versao": "1.0",
        "descricao": "API desenvolvida para prever a probabilidade de cancelamento de clientes.",
        "endpoints": {
            "GET /": "Informações e manual da API",
            "GET /health": "Verifica a saúde do servidor e dos modelos matemáticos",
            "POST /predict": "Recebe os dados do cliente e retorna a previsão de Churn"
        },
    }

@app.get("/health")
def health_check():
    """Verifica se os arquivos .pkl foram carregados corretamente na memória"""
    modelo_ok = predictor.model is not None
    scaler_ok = predictor.scaler is not None
    
    if modelo_ok and scaler_ok:
        return {"status": "saudável", "arquivos_carregados": True}
    else:
        from fastapi import HTTPException
        raise HTTPException(status_code=503, detail="Erro interno: Arquivos do modelo não encontrados.")

@app.post("/predict")
def realizar_previsao(customer_data: CustomerInput):
    dados_validados = customer_data.model_dump(by_alias=True)
    resultado = predictor.predict(dados_validados)
    return resultado