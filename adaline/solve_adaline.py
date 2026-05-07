import numpy as np
import matplotlib.pyplot as plt
import os

# Dados de Treinamento
caminho_csv = os.path.join(os.path.dirname(__file__), 'treinamento.csv')
dados = np.loadtxt(caminho_csv, delimiter=',', skiprows=1)
X_train = dados[:, 1:5] # x1, x2, x3, x4
d_train = dados[:, 5]   # d

# Novas Amostras de Teste
novas_amostras = np.array([
    [0.9694, 0.6909, 0.4334, 3.4965],
    [0.5427, 1.3832, 0.6390, 4.0352],
    [0.6081, -0.9196, 0.5925, 0.1016],
    [-0.1618, 0.4694, 0.2030, 3.0117],
    [0.1870, -0.2578, 0.6124, 1.7749],
    [0.4891, -0.5276, 0.4378, 0.6439],
    [0.3777, 2.0149, 0.7423, 3.3932],
    [1.1498, -0.4067, 0.2469, 1.5866],
    [0.9325, 1.0950, 1.0359, 3.3591],
    [0.5060, 1.3317, 0.9222, 3.7174],
    [0.0497, -2.0656, 0.6124, -0.6585],
    [0.4004, 3.5369, 0.9766, 5.3532],
    [-0.1874, 1.3343, 0.5374, 3.2189],
    [0.5060, 1.3317, 0.9222, 3.7174],
    [1.6375, -0.7911, 0.7537, 0.5515]
])

taxa_aprendizado = 0.0025
precisao = 1e-6
max_epocas = 10000

print("### 1 e 2. Tabela de Treinamentos (ADALINE)")
print("| Treinamento | Inicial (w0) | Inicial (w1) | Inicial (w2) | Inicial (w3) | Inicial (w4) | Final (w0) | Final (w1) | Final (w2) | Final (w3) | Final (w4) | Número de Épocas |")
print("|---|---|---|---|---|---|---|---|---|---|---|---|")

pesos_finais_lista = []
historico_eqm = []

num_amostras, num_features = X_train.shape
x0 = -np.ones((num_amostras, 1))
X_com_bias = np.hstack((x0, X_train))

for t in range(5):
    np.random.seed(42 + t*17) # Seed diferente para cada treinamento
    
    # Pesos iniciais entre 0 e 1
    w_inicial = np.random.uniform(0, 1, size=num_features + 1)
    w = np.copy(w_inicial)
    
    eqm_anterior = float('inf')
    eqm_epoca = []
    epocas_concluidas = 0
    
    for epoca in range(max_epocas):
        # Em ADALINE, o eqm da epoca eh calculado e depois ou antes os pesos sao atualizados.
        # Geralmente aplicamos a regra delta padrao em lote ou estocastica.
        # Faremos estocastico padrao (atualiza padrao a padrao):
        
        # eqm antes da atualizacao na epoca
        v_total = np.dot(X_com_bias, w)
        eqm_atual = np.mean((d_train - v_total)**2)
        eqm_epoca.append(eqm_atual)
        
        if abs(eqm_atual - eqm_anterior) <= precisao:
            break
            
        eqm_anterior = eqm_atual
        
        # Atualizacao de pesos padrao a padrao
        for i in range(num_amostras):
            v = np.dot(w, X_com_bias[i])
            erro = d_train[i] - v # Na Adaline usa-se o erro linear
            w = w + taxa_aprendizado * erro * X_com_bias[i]
            
        epocas_concluidas += 1
            
    pesos_finais_lista.append(w)
    if t < 2:
        historico_eqm.append(eqm_epoca)
    
    print(f"| T{t+1} | {w_inicial[0]:.4f} | {w_inicial[1]:.4f} | {w_inicial[2]:.4f} | {w_inicial[3]:.4f} | {w_inicial[4]:.4f} | {w[0]:.4f} | {w[1]:.4f} | {w[2]:.4f} | {w[3]:.4f} | {w[4]:.4f} | {epocas_concluidas} |")


# 3. Gerar Grafico EQM
plt.figure(figsize=(10, 6))
plt.plot(range(len(historico_eqm[0])), historico_eqm[0], label='Treinamento T1', color='blue')
plt.plot(range(len(historico_eqm[1])), historico_eqm[1], label='Treinamento T2', color='red', linestyle='--')
plt.title('ADALINE - Erro Quadrático Médio (EQM) vs Épocas')
plt.xlabel('Época')
plt.ylabel('EQM')
plt.legend()
plt.grid(True)
caminho_grafico = os.path.join(os.path.dirname(__file__), 'grafico_eqm.png')
plt.savefig(caminho_grafico)

print("\n### 4. Tabela de Classificação das Novas Amostras")
print("| Amostra | x1 | x2 | x3 | x4 | y (T1) | y (T2) | y (T3) | y (T4) | y (T5) |")
print("|---|---|---|---|---|---|---|---|---|---|")

for i, amostra in enumerate(novas_amostras):
    row = f"| {i+1} | {amostra[0]:.4f} | {amostra[1]:.4f} | {amostra[2]:.4f} | {amostra[3]:.4f} "
    for w in pesos_finais_lista:
        x_teste = np.concatenate(([-1], amostra))
        v = np.dot(w, x_teste)
        # Na fase de teste do Adaline/Perceptron aplica-se a funcao sinal (1 ou -1)
        y = 1 if v >= 0 else -1
        row += f"| {y} "
    row += "|"
    print(row)
    
print("\n### 5. Por que os pesos continuam praticamente inalterados?")
print("Embora os pesos sejam inicializados em pontos diferentes e o número de épocas varie para chegar à convergência (atingir a precisão de $10^{-6}$), a rede ADALINE sempre busca o mínimo global da superfície de erro quadrático (que tem o formato de um paraboloide). Como não há mínimos locais, o algoritmo da Regra Delta fatalmente convergirá para o mesmo ponto ótimo de separação (ou um ponto extremamente próximo a ele). Portanto, independente de onde os pesos começam (o que dita o tamanho e o tempo do caminho), o destino final (os pesos finais ótimos) será sempre praticamente o mesmo.")
