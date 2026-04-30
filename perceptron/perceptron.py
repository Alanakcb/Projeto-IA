import numpy as np
import matplotlib.pyplot as plt
import os

def carregar_dados(caminho_arquivo):
    # Carrega os dados ignorando a primeira linha (cabeçalho)
    # Colunas: 0=Padrão, 1=x1, 2=x2, 3=x3, 4=d
    dados = np.loadtxt(caminho_arquivo, delimiter=',', skiprows=1)
    
    # Separa os inputs X (colunas 1, 2 e 3) e o target d (coluna 4)
    X = dados[:, 1:4]
    d = dados[:, 4]
    return X, d

def treinar_perceptron(X, d, taxa_aprendizado=0.01, max_epocas=1000):
    num_amostras, num_features = X.shape
    
    # Insere o bias (x0 = -1) como a primeira coluna de X
    x0 = -np.ones((num_amostras, 1))
    X_com_bias = np.hstack((x0, X))
    
    # Inicializa os pesos aleatoriamente
    # Tamanho do vetor w: num_features + 1 (por causa do bias)
    np.random.seed(42) # Usando seed para reprodutibilidade
    w = np.random.uniform(-0.5, 0.5, size=num_features + 1)
    
    historico_erros = []
    epocas_concluidas = 0
    
    print("Iniciando treinamento...")
    print(f"Pesos iniciais: {w}\n")
    
    for epoca in range(max_epocas):
        erros_na_epoca = 0
        
        for i in range(num_amostras):
            # Calcula o campo induzido v
            v = np.dot(w, X_com_bias[i])
            
            # Função de ativação (sinal)
            y = 1 if v >= 0 else -1
            
            # Cálculo do erro
            erro = d[i] - y
            
            # Atualiza os pesos caso haja erro
            if erro != 0:
                w = w + taxa_aprendizado * erro * X_com_bias[i]
                erros_na_epoca += 1
                
        historico_erros.append(erros_na_epoca)
        epocas_concluidas = epoca + 1
        
        # Critério de parada: erro 0 na época
        if erros_na_epoca == 0:
            print(f"Convergência atingida na época {epocas_concluidas}!")
            break
            
    if epocas_concluidas == max_epocas and historico_erros[-1] != 0:
        print(f"Treinamento parado pelo limite máximo de épocas ({max_epocas}). O modelo pode não ter convergido totalmente.")
        
    print(f"\nPesos Finais (após treinamento): {w}")
    return w, historico_erros, epocas_concluidas

def plotar_erros(historico_erros):
    plt.figure(figsize=(8, 5))
    plt.plot(range(1, len(historico_erros) + 1), historico_erros, marker='o', linestyle='-', color='b')
    plt.title('Evolução do Erro de Treinamento por Época (Perceptron)')
    plt.xlabel('Época')
    plt.ylabel('Quantidade de Erros')
    plt.grid(True)
    plt.xticks(range(1, len(historico_erros) + 1, max(1, len(historico_erros)//10)))
    plt.savefig(os.path.join(diretorio_atual, 'evolucao_erros.png'))

if __name__ == "__main__":
    # Caminho do arquivo relativo a execucao
    diretorio_atual = os.path.dirname(os.path.abspath(__file__))
    caminho_csv = os.path.join(diretorio_atual, 'treinamento.csv')
    
    if not os.path.exists(caminho_csv):
        print(f"Erro: O arquivo de dados '{caminho_csv}' não foi encontrado.")
    else:
        # 1. Carregar dados
        X, d = carregar_dados(caminho_csv)
        
        # 2. Treinar perceptron
        pesos_finais, erros_epocas, epocas = treinar_perceptron(X, d, taxa_aprendizado=0.01, max_epocas=1000)
        
        # 3. Mostrar os gráficos
        plotar_erros(erros_epocas)
