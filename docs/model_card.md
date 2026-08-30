# Model Card: Classificador de Risco de Churn

## 1. Visão Geral do Modelo
* **Desenvolvedor:** Matheus Brito
* **Tipo de Modelo:** Regressão logistica (Elegido entre Regressão Logística, Árvore de Decisão/Random Forest e Rede Neural MLP).
* **Finalidade:** Prever a probabilidade de um cliente cancelar os serviços de telecomunicações, permitindo que a equipe de retenção acione estratégias preventivas.

## 2. Dados e Engenharia de Atributos (Features)
O modelo foi treinado utilizando uma base histórica tratada de clientes de telecom, contendo variáveis demográficas, contratuais e financeiras.
* **Variável Alvo (Target):** `Churn` (1 = O cliente cancelou o serviço, 0 = O cliente permaneceu ativo).
* **Tratamento de Dados:** Normalização de escalas numéricas através de `StandardScaler` e expansão de variáveis categóricas para garantir compatibilidade matemática com o algoritmo.

---

## 3. Performance e Métricas de Avaliação
Como bases de dados de Churn costumam ser naturalmente desbalanceadas (a maioria dos clientes permanece ativa), a acurácia global sozinha não é um bom termômetro. O modelo campeão foi selecionado priorizando o equilíbrio entre o **F1-Score** e a **AUC-ROC**.

* **Matriz de Decisão (Métricas Estimadas no Conjunto de Teste):**
  * **Acurácia Geral:** ~80% a 85% (dependendo do ajuste final do campeão).
  * **F1-Score (Classe Alvo - Churn):** Priorizado para evitar que o modelo erre falsos negativos em excesso (deixando de identificar quem vai cancelar).
  * **AUC-ROC:** Alta capacidade de separação entre o perfil de risco e o perfil de retenção.
* **Validação Cruzada:** Aplicada durante a Etapa 2 para mitigar o risco de *overfitting* e garantir estabilidade de desempenho em diferentes partições da base.

---


## 4. Limitações Técnicas do Modelo
* **Estática Temporal:** O modelo foi treinado com um recorte estático do passado. Mudanças macroeconômicas repentinas, alteração de tarifas de concorrentes ou quedas severas de infraestrutura de rede da operadora alterarão o comportamento de churn sem que o modelo capture de imediato.
* **Correlação vs. Causalidade:** O algoritmo aponta que um cliente com contrato mensal e fibra ótica tem alta probabilidade estatística de evasão, mas o modelo **não explica o motivo raiz** (se é o preço, o atendimento ou a qualidade técnica). O diagnóstico final depende de análise humana da equipe de atendimento.

---

## 5. Governança e Operacionalização
* **Persistência:** O modelo campeão e seu respectivo scaler encontram-se salvos na pasta `models/` nos formatos `champion_model.pkl` e `scaler.pkl`.
* **Consumo via API:** O modelo é carregado de forma otimizada na memória através da classe utilitária `src/predict.py` e exposto via API REST com FastAPI (`src/app.py`), blindado por um contrato de dados rígido via Pydantic para evitar falhas de tipagem em produção.