import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score


def treinar_e_avaliar_modelo():
    """
    Carrega os dados processados, treina um modelo de Machine Learning 
    e avalia sua acurácia preditiva.
    """
    print("Carregando base de dados processada...")
    caminho_dados = "data/processed/historico_eleitoral_processado.csv"

    if not pd.io.common.file_exists(caminho_dados):
        print(
            f"Erro: Arquivo não encontrado em {caminho_dados}. Execute o ingestion.py primeiro.")
        return None

    df = pd.read_csv(caminho_dados)

    # Definindo as variáveis preditoras (Features) e a variável alvo (Target)
    features = ['votos_validos_pct',
                'fundo_eleitoral_milhoes', 'apoio_caciques_politicos']
    target = 'eleito'

    X = df[features]
    y = df[target]

    # Dividindo os dados em treino e teste (75% treino, 25% teste)
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.25, random_state=42)

    print("Treinando o modelo de Inteligência Artificial (Random Forest)...")
    modelo = RandomForestClassifier(n_estimators=100, random_state=42)
    modelo.fit(X_train, y_train)

    # Avaliando a performance no conjunto de teste
    y_pred = modelo.predict(X_test)
    print("Modelo treinado com sucesso!")

    return modelo


def prever_novo_cenario(modelo, novo_cenario_df):
    """
    Realiza predições de vitória com base em novos dados informados (ex: cenário 2026).
    """
    features = ['votos_validos_pct',
                'fundo_eleitoral_milhoes', 'apoio_caciques_politicos']
    probabilidades = modelo.predict_proba(novo_cenario_df[features])

    # Adiciona a probabilidade de vitória ao DataFrame de cenários
    novo_cenario_df['probabilidade_vitoria_%'] = (
        probabilidades[:, 1] * 100).round(2)
    return novo_cenario_df


if __name__ == "__main__":
    # 1. Treinar o modelo
    modelo_treinado = treinar_e_avaliar_modelo()

    if modelo_treinado:
        # 2. Simulando novos dados para a eleição atual (ex: cenário simulado para 2026)
        print("\nSimulando predição para um novo cenário...")
        cenario_2026 = pd.DataFrame({
            'candidato': ['Candidato X', 'Candidato Y'],
            'votos_validos_pct': [51.0, 49.0],
            'fundo_eleitoral_milhoes': [110.0, 85.0],
            'apoio_caciques_politicos': [1, 0]
        })

        resultado_predicao = prever_novo_cenario(modelo_treinado, cenario_2026)
        print(resultado_predicao[[
              'candidato', 'votos_validos_pct', 'probabilidade_vitoria_%']])
