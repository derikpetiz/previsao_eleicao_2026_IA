import pandas as pd
from model import treinar_e_avaliar_modelo, prever_novo_cenario


def executar_previsao_eleicoes_2026():
    print("==================================================")
    print(" INICIANDO PREDIÇÃO OFICIAL - ELEIÇÕES OUTUBRO 2026")
    print("==================================================")

    # 1. Carrega e treina o modelo com a base histórica sólida
    modelo = treinar_e_avaliar_modelo()

    if not modelo:
        print("Erro ao carregar o modelo.")
        return

    # 2. Dados reais/atuais simulados com base nas últimas rodadas de pesquisas e contexto de 2026
    # (Aqui você pode substituir os valores pelos dados reais dos principais candidatos da sua região ou disputa presidencial)
    candidatos_2026 = pd.DataFrame({
        'candidato': ['Candidato Líder nas Pesquisas', 'Candidato Opositor Principal', 'Terceiro Colocado'],
        'votos_validos_pct': [46.5, 41.0, 12.5],
        'fundo_eleitoral_milhoes': [120.0, 95.0, 40.0],
        # 1 se tiver forte apoio de partidos/lideranças locais
        'apoio_caciques_politicos': [1, 1, 0]
    })

    print("\n[INFO] Cenário de intenção de voto e recursos injetados no modelo:")
    print(candidatos_2026)

    # 3. Executa a predição baseada na Inteligência Artificial
    resultados_finais = prever_novo_cenario(modelo, candidatos_2026)

    print("\n--------------------------------------------------")
    print(" 📊 RESULTADO DA PREDIÇÃO PREDITIVA PARA OUTUBRO DE 2026")
    print("--------------------------------------------------")
    print(resultados_finais[['candidato',
          'votos_validos_pct', 'probabilidade_vitoria_%']])
    print("==================================================")


if __name__ == "__main__":
    executar_previsao_eleicoes_2026()
