import numpy as np

# Dados de Treinamento
caminho_csv = 'treinamento.csv'
dados = np.loadtxt(caminho_csv, delimiter=',', skiprows=1)
X_train = dados[:, 1:4]
d_train = dados[:, 4]

# Novas Amostras de Teste
# x1, x2, x3
novas_amostras = np.array([
    [-0.3565, 0.0620, 5.9891],
    [-0.7842, 1.1267, 5.5912],
    [0.3012, 0.5611, 5.8234],
    [0.7757, 1.0648, 8.0677],
    [0.1570, 0.8028, 6.3040],
    [-0.7014, 1.0316, 3.6005],
    [0.3748, 0.1536, 6.1537],
    [-0.6920, 0.9404, 4.4058],
    [-1.3970, 0.7141, 4.9263],
    [-1.8842, -0.2805, 1.2548]
])

taxa_aprendizado = 0.01
max_epocas = 5000

print("### 1 e 2. Tabela de Treinamentos")
print("| Treinamento | Peso Inicial (w0) | Peso Inicial (w1) | Peso Inicial (w2) | Peso Inicial (w3) | Peso Final (w0) | Peso Final (w1) | Peso Final (w2) | Peso Final (w3) | Número de Épocas |")
print("|---|---|---|---|---|---|---|---|---|---|")

pesos_finais_lista = []

for t in range(5):
    np.random.seed(42 + t*10) # Seed diferente para cada treinamento
    num_amostras, num_features = X_train.shape
    x0 = -np.ones((num_amostras, 1))
    X_com_bias = np.hstack((x0, X_train))
    
    # Pesos iniciais entre 0 e 1, como exigido na questao
    w_inicial = np.random.uniform(0, 1, size=num_features + 1)
    w = np.copy(w_inicial)
    
    epocas_concluidas = 0
    for epoca in range(max_epocas):
        erros_na_epoca = 0
        for i in range(num_amostras):
            v = np.dot(w, X_com_bias[i])
            y = 1 if v >= 0 else -1
            erro = d_train[i] - y
            if erro != 0:
                w = w + taxa_aprendizado * erro * X_com_bias[i]
                erros_na_epoca += 1
                
        epocas_concluidas = epoca + 1
        if erros_na_epoca == 0:
            break
            
    pesos_finais_lista.append(w)
    
    print(f"| T{t+1} | {w_inicial[0]:.4f} | {w_inicial[1]:.4f} | {w_inicial[2]:.4f} | {w_inicial[3]:.4f} | {w[0]:.4f} | {w[1]:.4f} | {w[2]:.4f} | {w[3]:.4f} | {epocas_concluidas} |")

print("\n### 3. Tabela de Classificação das Novas Amostras")
print("| Amostra | x1 | x2 | x3 | y (T1) | y (T2) | y (T3) | y (T4) | y (T5) |")
print("|---|---|---|---|---|---|---|---|---|")

for i, amostra in enumerate(novas_amostras):
    row = f"| {i+1} | {amostra[0]:.4f} | {amostra[1]:.4f} | {amostra[2]:.4f} "
    for w in pesos_finais_lista:
        # bias x0 = -1
        x_teste = np.concatenate(([-1], amostra))
        v = np.dot(w, x_teste)
        y = 1 if v >= 0 else -1
        row += f"| {y} "
    row += "|"
    print(row)
