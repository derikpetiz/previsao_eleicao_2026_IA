import os
import pandas as pd


def gerar_base_historica_exemplo():
    """
    Gera uma base de dados estruturada simulando o histórico eleitoral por estado (UF),
    servindo como base de treino robusta para o modelo de Machine Learning.
    """
    print("Iniciando a preparação da base de dados históricos...")

    # Garantir que as pastas de destino existem
    os.makedirs("data/raw", exist_ok=True)
    os.makedirs("data/processed", exist_ok=True)

    # Dados históricos estruturados (exemplo cobrindo estados e variáveis explicativas)
    dados_historicos = {
        'ano': [2022, 2022, 2022, 2022, 2022, 2022],
        'uf': ['CE', 'CE', 'SP', 'SP', 'RJ', 'RJ'],
        'cargo': ['Governador', 'Governador', 'Governador', 'Governador', 'Governador', 'Governador'],
        'candidato': ['Candidato A', 'Candidato B', 'Candidato C', 'Candidato D', 'Candidato E', 'Candidato F'],
        'votos_validos_pct': [54.2, 45.8, 52.1, 47.9, 56.5, 43.5],
        'fundo_eleitoral_milhoes': [45.0, 30.0, 120.0, 95.0, 60.0, 50.0],
        # 1 para forte apoio regional, 0 caso contrário
        'apoio_caciques_politicos': [1, 0, 1, 0, 1, 0],
        # Variável alvo (Target): 1 = Eleito, 0 = Não eleito
        'eleito': [1, 0, 1, 0, 1, 0]
    }

    df = pd.DataFrame(dados_historicos)

    # Salvando o arquivo bruto e o processado
    caminho_raw = "data/raw/historico_eleitoral_raw.csv"
    caminho_processed = "data/processed/historico_eleitoral_processado.csv"

    df.to_csv(caminho_raw, index=False)
    df.to_csv(caminho_processed, index=False)

    print(f"Base histórica salva com sucesso em: {caminho_processed}")
    return df


if __name__ == "__main__":
    df_historico = gerar_base_historica_exemplo()
    print("\nVisualização das primeiras linhas da base gerada:")
    print(df_historico.head())
