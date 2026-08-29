Machine Learning Canvas - Previsão de Churn

1. Stakeholders

Principais: Diretoria da operadora, focada na receita recorrente.

Usuários Finais: Equipes de Marketing e Atendimento ao Cliente, que usaram para prever churns no dia a dia.

Equipe de Dados: Engenheiros e cientistas responsaveis pela manutenção de desenvolvimento  do modelo em produção.

2. Métricas de Negócio 

Redução do Churn Rate: Diminuição percentual na taxa mensal de cancelamentos da operadora.

Retorno sobre Investimento (ROI) de Retenção: O valor da receita salva pelo modelo comparado ao custo dos descontos oferecidos para manter esses clientes.

Taxa de Sucesso na Retenção: Porcentagem de clientes alertados pelo modelo que aceitaram a oferta da equipe de atendimento e decidiram não cancelar.

3. Proposta de Valor

Transformar uma postura reativa (tentar reverter um cancelamento que já está acontecendo) em uma postura proativa (identificar a insatisfação matematicamente e agir antes que o cliente tome a decisão de sair).

4. Decisões e Ações

O sistema não irá tomar decisões sozinho; ele atuara como um suporte prevendo churn.

O modelo enviará alertas ou listas diárias priorizadas para o sistema de CRM da equipe de atendimento.

O analista humano fará o contato ativo com ofertas direcionadas (ex: upgrade de internet ou desconto na fatura) exclusivas para clientes de alto risco.

5. Tarefa de Machine Learning

Classificação Binária Supervisionada (Prever 0 para quem permanece e 1 para quem cancela).

6. Dados e Variáveis

Perfil: Status de parceiro, dependentes e senioridade.

Serviços Contratados: Suporte técnico, segurança online, tipo de internet e linhas múltiplas.

Financeiro: Tempo de contrato (tenure), modalidade do contrato (mensal/anual), método de pagamento e valor da fatura.

7. Avaliação Offline (Métricas Técnicas)

Recall (Classe 1): Métrica prioritária para evitar falsos negativos (não deixar um cancelamento real passar despercebido).

ROC-AUC: Medida geral de capacidade do modelo em separar as duas classes.