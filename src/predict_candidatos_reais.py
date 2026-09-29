import pandas as pd
from model import treinar_e_avaliar_modelo, prever_novo_cenario


def prever_eleicoes_com_candidatos_reais():
    print("==================================================================")
    print(" 🗳️ PREDIÇÃO OFICIAL POR CANDIDATO — ELEIÇÕES OUTUBRO 2026")
    print("==================================================================")

    # 1. Treina o modelo com a base histórica
    modelo = treinar_e_avaliar_modelo()
    if not modelo:
        return

    # 2. Definindo a matriz de candidatos reais por cenário (Ex: Cenário Presidencial e Estadual)
    # Aqui listamos os principais nomes cotados nas pesquisas recentes de 2026
    candidatos_2026 = pd.DataFrame({
        'uf': ['BR', 'BR', 'BR', 'CE', 'CE', 'SP', 'SP'],
        'cargo': ['Presidente', 'Presidente', 'Presidente', 'Governador', 'Governador', 'Governador', 'Governador'],
        'candidato': [
            'Lula (PT)',
            'Tarcísio de Freitas (REPUBLICANOS)',
            'Flávio Bolsonaro (PL)',
            'Elmano de Freitas (PT)',
            'Capitão Wagner (UNIÃO)',
            'Tarcísio de Freitas (REPUBLICANOS)',
            'Fernando Haddad (PT)'
        ],
        'votos_validos_pct': [45.0, 38.0, 17.0, 52.0, 48.0, 51.0, 49.0],
        'fundo_eleitoral_milhoes': [150.0, 130.0, 110.0, 45.0, 40.0, 120.0, 115.0],
        'apoio_caciques_politicos': [1, 1, 0, 1, 0, 1, 1]
    })

    # Executa a predição usando a IA
    resultados = prever_novo_cenario(modelo, candidatos_2026)

    print("\n------------------------------------------------------------------")
    print(" 📊 RANKING PREDITIVO DE PROBABILIDADE DE VITÓRIA (OUTUBRO 2026)")
    print("------------------------------------------------------------------")

    # Exibe os resultados formatados por cargo/UF
    for uf in resultados['uf'].unique():
        print(f"\n📍 Unidade Federativa / Âmbito: {uf}")
        subset = resultados[resultados['uf'] == uf]
        for index, row in subset.iterrows():
            print(
                f"   -> {row['candidato']} | Intenção: {row['votos_validos_pct']}% | 🏆 Probabilidade de Vitória (IA): {row['probabilidade_vitoria_%']}%")

    print("==================================================================")


if __name__ == "__main__":
    prever_eleicoes_com_candidatos_reais()
