# 🇧🇷 Simulador Preditivo Eleitoral 2026

Projeto Aplicado desenvolvido para o **MBA em Data Science & Inteligência Artificial**.

## 🎯 Sobre o Projeto
Este sistema aplica técnicas avançadas de Engenharia de Dados, Modelagem Preditiva de Machine Learning (`Random Forest`) e Desenvolvimento de Aplicações Web (`Streamlit`) para estimar probabilidades e cenários eleitorais para os cargos majoritários e proporcionais nas eleições brasileiras de 2026.

## 🛠️ Arquitetura do Repositório
```text
eleicoes_2026_mba/
│
├── data/
│   ├── raw/                 # Dados brutos históricos e metadados
│   └── processed/           # Bases tratadas e limpas por UF
│
├── src/
│   ├── ingestion.py         # Automação de ingestão e estruturação de dados
│   └── model.py             # Treinamento do modelo de Machine Learning
│
├── app.py                   # Dashboard interativo em Streamlit
└── requirements.txt         # Dependências do projeto