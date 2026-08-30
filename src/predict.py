import joblib
import pandas as pd
import os

# Caminhos absolutos para garantir que a API encontre os arquivos
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MODEL_PATH = os.path.join(BASE_DIR, 'models', 'champion_model.pkl')
SCALER_PATH = os.path.join(BASE_DIR, 'models', 'scaler.pkl')

class ChurnPredictor:
    def __init__(self):
        # Carregar o modelo e o scaler para a memória no momento em que a classe é iniciada
        self.model = joblib.load(MODEL_PATH)
        self.scaler = joblib.load(SCALER_PATH)
        
        
        self.expected_columns = [
            'gender', 'SeniorCitizen', 'Partner', 'Dependents', 'tenure',
            'PhoneService', 'PaperlessBilling', 'MonthlyCharges', 'TotalCharges',
            'MultipleLines_No phone service', 'MultipleLines_Yes',
            'InternetService_Fiber optic', 'InternetService_No',
            'OnlineSecurity_1.0', 'OnlineBackup_No internet service',
            'OnlineBackup_Yes', 'DeviceProtection_1.0', 'TechSupport_1.0',
            'StreamingTV_1.0', 'StreamingMovies_1.0', 'Contract_One year',
            'Contract_Two year', 'PaymentMethod_Credit card (automatic)',
            'PaymentMethod_Electronic check', 'PaymentMethod_Mailed check'
        ]

    def predict(self, customer_data: dict) -> dict:
       
        df_input = pd.DataFrame([customer_data])
        
        #Garantir que as colunas estejam na ordem correta e preenche ausências com 0
        df_input = df_input.reindex(columns=self.expected_columns, fill_value=0)
        
        X_scaled = self.scaler.transform(df_input)
        
        prediction = self.model.predict(X_scaled)[0]
        probability = self.model.predict_proba(X_scaled)[0][1]
        
        return {
            "churn_prediction": int(prediction),
            "churn_probability": round(float(probability), 4)
        }