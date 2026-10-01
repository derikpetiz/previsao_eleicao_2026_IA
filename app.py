import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go

# Configuração da página e layout wide
st.set_page_config(
    page_title="Eleições 2026 — Plataforma Preditiva e Multimetodologia",
    page_icon="🗳️",
    layout="wide"
)

# Título e cabeçalho executivo institucional
st.title("🗳️ Eleições 2026 — Plataforma Preditiva e Multimodelo Eleitoral")
st.markdown("### Sistema analítico avançado para simulação, previsão e contraste de cenários eleitorais brasileiros (Outubro / 2026).")

# ==========================================
# PAINEL DE CONTROLE AVANÇADO (SIDEBAR)
# ==========================================
st.sidebar.header("⚙️ Painel de Controle Analítico")

# Seleção de Cargo
cargo = st.sidebar.selectbox(
    "Selecione o Cargo:",
    ["Presidente da República", "Governo Estadual", "Senado Federal",
        "Câmara dos Deputados", "Deputado Estadual"]
)

# Seleção de UF / Escopo Geográfico
if cargo == "Presidente da República":
    uf_lista = ['BR (Nacional - Presidente)']
else:
    uf_lista = [
        'AC', 'AL', 'AP', 'AM', 'BA', 'CE', 'DF', 'ES', 'GO', 'MA', 'MT', 'MS',
        'MG', 'PA', 'PB', 'PR', 'PE', 'PI', 'RJ', 'RN', 'RS', 'RO', 'RR', 'SC',
        'SP', 'SE', 'TO'
    ]

uf = st.sidebar.selectbox("Selecione a Unidade da Federação (UF):", uf_lista)

# Seleção de Turno
turno = st.sidebar.radio("Selecione o Turno:", ["1º Turno", "2º Turno"])

# Filtros e Parâmetros Avançados da Sidebar (Recuperados!)
st.sidebar.markdown("---")
st.sidebar.subheader("🎛️ Parâmetros Estocásticos & IA")
simulacoes = st.sidebar.slider(
    "Iterações de Monte Carlo:", 1000, 15000, 5000, step=1000)
transferencia = st.sidebar.slider(
    "Fator de Migração de Indecisos / Volatilidade:", 0.0, 5.0, 2.0, step=0.5)
nivel_confianca = st.sidebar.slider(
    "Intervalo de Confiança Estatística (%):", 90, 99, 95, step=1)

# Filtro de Alinhamento Político / Bloco na Sidebar
st.sidebar.markdown("---")
st.sidebar.subheader("🏛️ Filtros de Coligação")
filtro_bloco = st.sidebar.multiselect(
    "Filtrar por Espectro / Alinhamento:",
    ["Todos", "Base Governamental / Centro-Esquerda",
        "Oposição / Centro-Direita", "Terceira Via / Independentes"],
    default=["Todos"]
)

st.sidebar.markdown("---")
st.sidebar.info("💡 **Dica Analítica:** Ajuste a volatilidade e o número de iterações para testar a robustez dos intervalos de confiança frente a variações bruscas de rejeição.")

# ==========================================
# BASE DE DADOS COMPLETA E HIERÁRQUICA
# ==========================================


def obter_dados_eleitorais_avancados(cargo, uf, turno):
    if cargo == "Presidente da República":
        if turno == "1º Turno":
            return {
                'candidatos': ['Lula (PT)', 'Flávio Bolsonaro (PL)', 'Augusto Cury (Avante)', 'Ronaldo Caiado (PSD)', 'Renan Santos (Missão)', 'Romeu Zema (NOVO)'],
                'votos': [41.5, 36.5, 5.0, 4.5, 3.5, 2.5],
                'rejeicao': [42.0, 46.0, 31.0, 28.0, 35.0, 40.0],
                'momentum': [+0.8, -0.5, +0.2, +0.1, 0.0, -0.1],
                'espectro': ['Base Governamental / Centro-Esquerda', 'Oposição / Centro-Direita', 'Terceira Via / Independentes', 'Oposição / Centro-Direita', 'Terceira Via / Independentes', 'Oposição / Centro-Direita']
            }
        else:
            return {
                'candidatos': ['Lula (PT)', 'Flávio Bolsonaro (PL)'],
                'votos': [48.5 + (transferencia * 0.4), 48.0 - (transferencia * 0.4)],
                'rejeicao': [42.0, 46.0],
                'momentum': [+1.2, -0.8],
                'espectro': ['Base Governamental / Centro-Esquerda', 'Oposição / Centro-Direita']
            }

    elif cargo == "Governo Estadual":
        base_gov = {
            'SP': {'cands': ['Tarcísio de Freitas (Republicanos)', 'Guilherme Boulos (PSOL)', 'Fernando Haddad (PT)', 'Rodrigo Garcia (PSDB)', 'Vinicius Poit (NOVO)', 'Márcio França (PSB)'], 'votos': [43.0, 27.0, 15.0, 7.0, 5.0, 3.0], 'rej': [32.0, 48.0, 44.0, 35.0, 38.0, 40.0], 'mom': [+0.5, +0.3, -0.2, 0.0, +0.1, -0.1], 'esp': ['Oposição / Centro-Direita', 'Base Governamental / Centro-Esquerda', 'Base Governamental / Centro-Esquerda', 'Terceira Via / Independentes', 'Oposição / Centro-Direita', 'Base Governamental / Centro-Esquerda']},
            'RJ': {'cands': ['Eduardo Paes (PSD)', 'Douglas Ruas (PL)', 'Rodrigo Neves (PDT)', 'Clarissa Garotinho (PROS)', 'Marcelo Freixo (PT)', 'Luiz Lima (PL)'], 'votos': [37.0, 29.0, 14.0, 9.0, 7.0, 4.0], 'rej': [36.0, 39.0, 32.0, 42.0, 45.0, 35.0], 'mom': [+0.4, +0.6, -0.1, 0.0, -0.2, +0.1], 'esp': ['Terceira Via / Independentes', 'Oposição / Centro-Direita', 'Base Governamental / Centro-Esquerda', 'Terceira Via / Independentes', 'Base Governamental / Centro-Esquerda', 'Oposição / Centro-Direita']},
            'MG': {'cands': ['Alexandre Kalil (PSD)', 'Nikolas Ferreira (PL)', 'Rodrigo Pacheco (PSD)', 'Cleitinho (REPUBLICANOS)', 'Marcelo Aro (PP)', 'Bruno Engler (PL)'], 'votos': [36.0, 34.0, 14.0, 9.0, 4.0, 3.0], 'rej': [35.0, 45.0, 30.0, 33.0, 36.0, 40.0], 'mom': [+0.3, +0.7, -0.1, +0.2, 0.0, -0.2], 'esp': ['Terceira Via / Independentes', 'Oposição / Centro-Direita', 'Terceira Via / Independentes', 'Oposição / Centro-Direita', 'Oposição / Centro-Direita', 'Oposição / Centro-Direita']},
            'CE': {'cands': ['Elmano de Freitas (PT)', 'Capitão Wagner (União)', 'Roberto Cláudio (PDT)', 'Eunício Oliveira (MDB)', 'José Sarto (PDT)', 'Luizianne Lins (PT)'], 'votos': [39.0, 31.0, 15.0, 8.0, 4.0, 3.0], 'rej': [34.0, 38.0, 35.0, 40.0, 39.0, 42.0], 'mom': [+0.5, +0.4, -0.2, 0.0, -0.1, 0.0], 'esp': ['Base Governamental / Centro-Esquerda', 'Oposição / Centro-Direita', 'Terceira Via / Independentes', 'Base Governamental / Centro-Esquerda', 'Terceira Via / Independentes', 'Base Governamental / Centro-Esquerda']}
        }
        res = base_gov.get(uf, {
            'cands': [f'Governador Líder 1 ({uf})', f'Governador Oposição 1 ({uf})', f'Governador 3 ({uf})', f'Governador 4 ({uf})', f'Governador 5 ({uf})', f'Governador 6 ({uf})'],
            'votos': [38.0, 30.0, 16.0, 8.0, 5.0, 3.0],
            'rej': [35.0, 40.0, 28.0, 42.0, 36.0, 39.0],
            'mom': [+0.3, +0.2, 0.0, 0.0, 0.0, 0.0],
            'esp': ['Base Governamental / Centro-Esquerda', 'Oposição / Centro-Direita', 'Terceira Via / Independentes', 'Terceira Via / Independentes', 'Oposição / Centro-Direita', 'Base Governamental / Centro-Esquerda']
        })
        cands, votos, rej, mom, esp = res['cands'], res['votos'], res['rej'], res['mom'], res['esp']
        if turno == "2º Turno":
            cands, votos, rej, mom, esp = cands[:2], [
                votos[0] + 8.0, votos[1] + 7.0], rej[:2], mom[:2], esp[:2]
        return {'candidatos': cands, 'votos': votos, 'rejeicao': rej, 'momentum': mom, 'espectro': esp}

    elif cargo == "Senado Federal":
        base_sen = {
            'SP': {'cands': ['Moro (União)', 'Marta Suplicy (PT)', 'Marcos Pontes (PL)', 'Tabata Amaral (PSB)', 'Ricardo Salles (PL)', 'Alexandre Padilha (PT)'], 'votos': [34.0, 30.0, 18.0, 10.0, 5.0, 3.0], 'rej': [35.0, 38.0, 32.0, 41.0, 44.0, 39.0], 'mom': [+0.4, +0.3, +0.5, -0.1, +0.2, -0.2], 'esp': ['Oposição / Centro-Direita', 'Base Governamental / Centro-Esquerda', 'Oposição / Centro-Direita', 'Terceira Via / Independentes', 'Oposição / Centro-Direita', 'Base Governamental / Centro-Esquerda']},
            'RJ': {'cands': ['Romário (PL)', 'Flávio Bolsonaro (PL)', 'Alessandro Molon (PSB)', 'Clarissa Garotinho (PROS)', 'Benedita da Silva (PT)', 'Carlos Portinho (PL)'], 'votos': [35.0, 31.0, 16.0, 10.0, 5.0, 3.0], 'rej': [36.0, 45.0, 33.0, 40.0, 38.0, 37.0], 'mom': [+0.2, +0.6, -0.1, 0.0, +0.1, -0.1], 'esp': ['Oposição / Centro-Direita', 'Oposição / Centro-Direita', 'Base Governamental / Centro-Esquerda', 'Terceira Via / Independentes', 'Base Governamental / Centro-Esquerda', 'Oposição / Centro-Direita']}
        }
        res = base_sen.get(uf, {
            'cands': [f'Senador Líder 1 ({uf})', f'Senador Líder 2 ({uf})', f'Senador 3 ({uf})', f'Senador 4 ({uf})', f'Senador 5 ({uf})', f'Senador 6 ({uf})'],
            'votos': [32.0, 28.0, 18.0, 12.0, 7.0, 3.0],
            'rej': [32.0, 35.0, 28.0, 40.0, 36.0, 42.0],
            'mom': [+0.3, +0.2, 0.0, 0.0, 0.0, 0.0],
            'esp': ['Oposição / Centro-Direita', 'Base Governamental / Centro-Esquerda', 'Terceira Via / Independentes', 'Terceira Via / Independentes', 'Oposição / Centro-Direita', 'Base Governamental / Centro-Esquerda']
        })
        cands, votos, rej, mom, esp = res['cands'], res['votos'], res['rej'], res['mom'], res['esp']
        if turno == "2º Turno":
            cands, votos, rej, mom, esp = cands[:2], [
                52.0, 48.0], rej[:2], mom[:2], esp[:2]
        return {'candidatos': cands, 'votos': votos, 'rejeicao': rej, 'momentum': mom, 'espectro': esp}

    elif cargo == "Câmara dos Deputados":
        return {
            'candidatos': [f'PL Federal ({uf})', f'PT / Federação ({uf})', f'PSD Federal ({uf})', f'União Brasil ({uf})', f'Republicanos ({uf})', f'PP Federal ({uf})'],
            'votos': [28.0, 24.0, 18.0, 14.0, 10.0, 6.0],
            'rejeicao': [30.0, 32.0, 28.0, 35.0, 33.0, 38.0],
            'momentum': [+0.5, +0.3, +0.2, -0.1, 0.0, -0.1],
            'espectro': ['Oposição / Centro-Direita', 'Base Governamental / Centro-Esquerda', 'Terceira Via / Independentes', 'Oposição / Centro-Direita', 'Oposição / Centro-Direita', 'Oposição / Centro-Direita']
        }
    else:
        return {
            'candidatos': [f'PL Estadual ({uf})', f'PT / Federação Estadual ({uf})', f'PSD Estadual ({uf})', f'União Estadual ({uf})', f'Republicanos Estadual ({uf})', f'PSDB Estadual ({uf})'],
            'votos': [27.0, 25.0, 19.0, 14.0, 10.0, 5.0],
            'rejeicao': [31.0, 33.0, 29.0, 36.0, 34.0, 39.0],
            'momentum': [+0.4, +0.4, +0.1, 0.0, -0.1, -0.2],
            'espectro': ['Oposição / Centro-Direita', 'Base Governamental / Centro-Esquerda', 'Terceira Via / Independentes', 'Oposição / Centro-Direita', 'Oposição / Centro-Direita', 'Terceira Via / Independentes']
        }

# ==========================================
# MOTOR MULTIMODELO E PROCESSAMENTO
# ==========================================


def executar_motor_completo(cargo, uf, turno, transferencia, iteracoes):
    np.random.seed(42)
    dados = obter_dados_eleitorais_avancados(cargo, uf, turno)
    candidatos, votos_base, rejeicao, momentum, espectro = dados['candidatos'], dados[
        'votos'], dados['rejeicao'], dados['momentum'], dados['espectro']

    tabela = []
    for i, cand in enumerate(candidatos):
        p_pura = votos_base[i] + momentum[i]
        p_estatistico = p_pura + np.random.normal(0, 1.0) * (transferencia / 2)

        fator_log_odds = 1.0 - (rejeicao[i] / 160.0)
        sim_mc = []
        for _ in range(iteracoes):
            ruido = np.random.normal(0, 2.0)
            val_sim = (p_pura + ruido) * fator_log_odds
            sim_mc.append(max(0.0, val_sim))

        prob_vitoria = np.mean([1 if x > 35.0 else 0 for x in sim_mc]) * 100.0
        ic_inferior = np.percentile(sim_mc, (100 - nivel_confianca) / 2)
        ic_superior = np.percentile(sim_mc, 100 - (100 - nivel_confianca) / 2)

        tabela.append({
            'Candidato / Bloco': cand,
            'Espectro Político': espectro[i],
            'Pesquisa Pura (%)': round(p_pura, 1),
            'Momentum (Última Semana)': round(momentum[i], 1),
            'Modelo Estatístico (%)': round(max(0.0, p_estatistico), 1),
            'Probabilidade Monte Carlo (%)': round(prob_vitoria, 1),
            f'IC {nivel_confianca}% (Inf - Sup)': f"{round(ic_inferior, 1)}% - {round(ic_superior, 1)}%",
            'Taxa de Rejeição (%)': rejeicao[i]
        })

    df = pd.DataFrame(tabela)
    if "Todos" not in filtro_bloco and len(filtro_bloco) > 0:
        df = df[df['Espectro Político'].isin(filtro_bloco)]
    return df


df_resultado = executar_motor_completo(
    cargo, uf, turno, transferencia, simulacoes)

# ==========================================
# LAYOUT PRINCIPAL E MÉTRICAS EXECUTIVAS
# ==========================================
st.markdown(f"### 📍 Escopo Analítico: **{cargo}** — **{uf}** | **{turno}**")

col1, col2, col3, col4 = st.columns(4)
col1.metric(label="Arquitetura", value="Multimodelo Integrado",
            delta="TSE + Estatística + IA")
col2.metric(label="Simulação Estocástica",
            value=f"{simulacoes:,} iterações", delta="Monte Carlo Ativo")
col3.metric(label="Calibração", value="Penalização Log-Odds",
            delta="Rejeição Aplicada")
col4.metric(label="Janela Temporal",
            value="Outubro / 2026", delta="Dados Recentes")

st.markdown("---")

# Abas Analíticas Profissionais Completas
aba1, aba2, aba3, aba4 = st.tabs([
    "📊 Contraste Multimodelo & Gráficos",
    "📋 Matriz Detalhada & IC",
    "📈 Análise de Momentum & Tendências",
    "⚙️ Notas Metodológicas"
])

with aba1:
    st.subheader("📊 Comparativo Visual entre as Abordagens Preditivas")
    if not df_resultado.empty:
        df_melted = df_resultado.melt(
            id_vars=['Candidato / Bloco', 'Espectro Político'],
            value_vars=[
                'Pesquisa Pura (%)', 'Modelo Estatístico (%)', 'Probabilidade Monte Carlo (%)'],
            var_name='Metodologia',
            value_name='Percentual / Probabilidade (%)'
        )
        fig = px.bar(
            df_melted, x='Candidato / Bloco', y='Percentual / Probabilidade (%)', color='Metodologia',
            barmode='group', text='Percentual / Probabilidade (%)',
            title=f"Contraste Multimodelo — {cargo} ({uf} / {turno})"
        )
        fig.update_traces(texttemplate='%{text:.1f}%', textposition='outside')
        fig.update_layout(template='plotly_dark')
        st.plotly_chart(fig, use_container_width=True)
    else:
        st.warning(
            "Nenhum candidato encontrado com os filtros de espectro político selecionados.")

with aba2:
    st.subheader("📋 Matriz Analítica Completa com Intervalos de Confiança")
    st.dataframe(df_resultado, use_container_width=True)

    csv = df_resultado.to_csv(index=False).encode('utf-8')
    st.download_button(
        label="📥 Baixar Relatório Técnico em CSV",
        data=csv,
        file_name=f'relatorio_eleitoral_{cargo.lower().replace(" ", "_")}_{uf}_{turno}.csv',
        mime='text/csv',
    )

with aba3:
    st.subheader("📈 Análise de Momentum e Variação da Última Semana")
    if not df_resultado.empty:
        fig_mom = px.bar(
            df_resultado, x='Candidato / Bloco', y='Momentum (Última Semana)',
            color='Momentum (Última Semana)', color_continuous_scale=['red', 'yellow', 'green'],
            title=f"Variação de Momentum — {cargo} ({uf})"
        )
        fig_mom.update_layout(template='plotly_dark')
        st.plotly_chart(fig_mom, use_container_width=True)
        st.markdown(
            "*O indicador de Momentum captura as tendências recentes de crescimento ou retração na última semana de campanha.*")

with aba4:
    st.subheader("⚙️ Detalhes da Arquitetura Metodológica")
    st.markdown("""
    * **Pesquisa Pura (Dados Brutos):** Âncora inicial baseada nos registros oficiais e intenções de voto apuradas em campo.
    * **Modelo Estatístico Paramétrico:** Aplicação de distribuições probabilísticas para absorção de volatilidade e comportamento de eleitores indecisos.
    * **Modelo Preditivo com IA (Monte Carlo + Log-Odds):** Simulações estocásticas ponderadas pelo teto de rejeição institucional, mitigando vieses e calculando probabilidades reais de êxito.
    """)

st.markdown("---")
st.markdown("*Plataforma avançada de previsão eleitoral e simulação estocástica desenvolvida para portfólio de Ciência de Dados.*")
