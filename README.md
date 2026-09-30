# 🗳️ Eleições 2026 — Plataforma Preditiva e Multimetodologia Eleitoral

## 📋 Descrição do Projeto
Sistema analítico avançado e interactivo desenvolvido em **Python** e **Streamlit** para simulação, previsão e contraste de cenários eleitorais brasileiros para o pleito de 2026. A plataforma cobre **100% das Unidades da Federação (UFs)** e os principais cargos executivos e legislativos, integrando três abordagens metodológicas simultâneas para garantir neutralidade e robustez estatística.

---

## 🚀 Acesse a Aplicação Online
* [🔗 Clique aqui para testar a Plataforma ao Vivo (Streamlit Cloud)](https://previsaoeleicao2026ia-mezbbja6cmagvms6otzebg.streamlit.app/)

---

## 🛠️ Tecnologias e Bibliotecas Utilizadas
* **Python**: Linguagem principal para a lógica de simulação e motor analítico.
* **Streamlit**: Construção da interface web executiva e interativa.
* **Plotly Express**: Visualização de dados moderna, limpa e com gráficos de alta interatividade.
* **Pandas & NumPy**: Manipulação de matrizes de dados, cálculos estocásticos e vetorização de métricas.

---

## 📊 Arquitetura e Metodologias
A plataforma opera com um motor multimodelo simultâneo:
1. **Pesquisa Pura (Dados Brutos):** Exposição direta das coletas de intenção de voto apuradas em campo, sem ponderações estocásticas.
2. **Modelo Estatístico Paramétrico:** Aplicação de regressão linear ponderada e calibração histórico-temporal para absorção de tendências contínuas.
3. **Modelo Preditivo com IA (Monte Carlo + Log-Odds):** Simulações estocásticas avançadas ponderadas pelo teto de rejeição institucional, mapeando incertezas e probabilidades reais de êxito eleitoral.

---

## 📈 Visualizações e Telas da Aplicação
*(Dica: Você pode capturar a tela da sua aplicação rodando localmente ou no Streamlit Cloud e inserir os links das imagens aqui)*

* **Painel de Controle e Contraste Multimodelo:**
  > ![Contraste Multimodelo](caminho/para/print_contraste.png)
* **Gráfico Dinâmico em Plotly e Matriz Analítica Detalhada:**
  > ![Distribuição Visual](caminho/para/print_grafico.png)

---

## 💡 Insights e Conclusões Analíticas

A partir da execução das simulações estocásticas e da análise comparativa entre as metodologias, os seguintes insights foram consolidados:

* **Sensibilidade à Rejeição (Efeito Log-Odds):** Observou-se que candidatos com intenções de voto brutas elevadas, mas com taxas de rejeição institucionais superiores a 40%, sofrem quedas expressivas na probabilidade final de sucesso nas simulações de Monte Carlo. Isso comprova que o teto de rejeição atua como um limitador crítico de crescimento no segundo turno.
* **Divergência entre Dados Brutos e Modelos Preditivos:** O contraste multimodelo revelou que praças com eleitorados altamente voláteis apresentam maior dispersão entre a "Pesquisa Pura" e o "Modelo Preditivo com IA", evidenciando a importância de ponderar a migração de eleitores indecisos.
* **Comportamento Proporcional (Quociente Eleitoral):** A projeção de cadeiras para o Legislativo demonstrou que legendas com distribuição homogênea de votos maximizam o quociente partidário com mais eficiência do que aquelas dependentes de candidaturas únicas de puxadores de voto extremos.
* **Impacto da Margem de Erro Demográfica:** A calibração dinâmica da margem de erro baseada no tamanho do colégio eleitoral demonstrou que estados menores (como AC e RR) exigem cautela redobrada na leitura de empates técnicos aparentes, devido à maior amplitude do intervalo de confiança.

---

## ⚙️ Como Executar o Projeto Localmente

1. Clone o repositório:
   ```bash
   git clone [https://github.com/derikpetiz/previsao_eleicao_2026_IA.git](https://github.com/derikpetiz/previsao_eleicao_2026_IA.git)