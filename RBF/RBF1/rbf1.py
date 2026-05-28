import numpy as np
from sklearn.cluster import KMeans

rbf1_train_data = """1	0.2563	0.9503	-1
2	0.2405	0.9018	-1
3	0.1157	0.3676	1
4	0.5147	0.0167	1
5	0.4127	0.3275	1
6	0.2809	0.583	1
7	0.8263	0.9301	-1
8	0.9359	0.8724	-1
9	0.1096	0.9165	-1
10	0.5158	0.8545	-1
11	0.1334	0.1362	1
12	0.6371	0.1439	1
13	0.7052	0.6277	-1
14	0.8703	0.8666	-1
15	0.2612	0.6109	1
16	0.0244	0.5279	1
17	0.9588	0.3672	-1
18	0.9332	0.5499	-1
19	0.9623	0.2961	-1
20	0.7297	0.5776	-1
21	0.456	0.1871	1
22	0.1715	0.7713	1
23	0.5571	0.5485	-1
24	0.3344	0.0259	1
25	0.4803	0.7635	-1
26	0.9721	0.485	-1
27	0.8318	0.7844	-1
28	0.1373	0.0292	1
29	0.366	0.8581	-1
30	0.3626	0.7302	-1
31	0.6474	0.3324	1
32	0.3461	0.2398	1
33	0.1353	0.812	1
34	0.3463	0.1017	1
35	0.9086	0.1947	-1
36	0.5227	0.2321	1
37	0.5153	0.2041	1
38	0.1832	0.0661	1
39	0.5015	0.9812	-1
40	0.5024	0.5274	-1"""

rbf1_test_data = """1	0.8705	0.9329	-1
2	0.0388	0.2703	1
3	0.8236	0.4458	-1
4	0.7075	0.1502	1
5	0.9587	0.8663	-1
6	0.6115	0.9365	-1
7	0.3534	0.3646	1
8	0.3268	0.2766	1
9	0.6129	0.4518	-1
10	0.9948	0.4962	-1"""

def parse_data(raw):
    data = []
    for line in raw.strip().split('\n'):
        parts = line.split()
        data.append([float(x) for x in parts[1:]])
    return np.array(data)

train_data = parse_data(rbf1_train_data)
test_data = parse_data(rbf1_test_data)

X_train = train_data[:, 0:2]
d_train = train_data[:, 2]

X_test = test_data[:, 0:2]
d_test = test_data[:, 2]

# 1. K-means em todo o conjunto de treinamento
kmeans = KMeans(n_clusters=2, random_state=42, n_init=10).fit(X_train)
centers = kmeans.cluster_centers_
labels = kmeans.labels_

var = []
for i in range(2):
    cluster_points = X_train[labels == i]
    variance = np.mean(np.sum((cluster_points - centers[i])**2, axis=1))
    var.append(variance)

# Função RBF Gaussiana
def phi(x, c, v):
    return np.exp(-np.sum((x - c)**2) / (2 * v))

# Saída da camada escondida
N = len(X_train)
H = np.zeros((N, 3))
for i in range(N):
    H[i, 0] = -1
    H[i, 1] = phi(X_train[i], centers[0], var[0])
    H[i, 2] = phi(X_train[i], centers[1], var[1])

# 2. Regra Delta
W = np.random.uniform(0, 1, 3)
learning_rate = 0.01
precision = 1e-7

prev_mse = float('inf')
epoch = 0
while True:
    V = np.dot(H, W)
    mse = np.mean((d_train - V)**2)
    if abs(prev_mse - mse) < precision:
        break
    prev_mse = mse
    
    for i in range(N):
        v_i = np.dot(H[i], W)
        erro = d_train[i] - v_i
        W += learning_rate * erro * H[i]
        
    epoch += 1
    if epoch > 50000:
        break

# 3. Validação
H_test = np.zeros((len(X_test), 3))
for i in range(len(X_test)):
    H_test[i, 0] = -1
    H_test[i, 1] = phi(X_test[i], centers[0], var[0])
    H_test[i, 2] = phi(X_test[i], centers[1], var[1])

V_test = np.dot(H_test, W)
y_pos = np.where(V_test >= 0, 1, -1)

acertos = np.sum(y_pos == d_test)
taxa_acerto = acertos / len(d_test) * 100

with open("respostas_rbf1.md", "w", encoding="utf-8") as f:
    f.write("# Respostas RBF 1\n\n")
    f.write("### 1. Treinamento da Camada Escondida (K-means)\n")
    f.write("| Cluster | Centro | Variância |\n")
    f.write("|---|---|---|\n")
    f.write(f"| 1 | [{centers[0][0]:.4f}, {centers[0][1]:.4f}] | {var[0]:.6f} |\n")
    f.write(f"| 2 | [{centers[1][0]:.4f}, {centers[1][1]:.4f}] | {var[1]:.6f} |\n\n")
    
    f.write("### 2. Pesos da Camada de Saída\n")
    f.write("| Peso | Valor |\n")
    f.write("|---|---|\n")
    f.write(f"| W21,0 (bias) | {W[0]:.6f} |\n")
    f.write(f"| W21,1 | {W[1]:.6f} |\n")
    f.write(f"| W21,2 | {W[2]:.6f} |\n\n")
    
    f.write("### 3 e 4. Classificação e Taxa de Acerto\n")
    f.write("| Amostra | x1 | x2 | d | y | ypós |\n")
    f.write("|---|---|---|---|---|---|\n")
    for i in range(len(X_test)):
        f.write(f"| {i+1} | {X_test[i][0]:.4f} | {X_test[i][1]:.4f} | {int(d_test[i])} | {V_test[i]:.4f} | {int(y_pos[i])} |\n")
    f.write(f"\n**Taxa de Acerto (%):** {taxa_acerto:.2f}%\n\n")
    
    f.write("### 5. Estratégias para aumentar a taxa de acerto\n")
    f.write("Para aumentar a taxa de acerto desta RBF, poderíamos adotar as seguintes estratégias:\n\n")
    f.write("1. **Clusterização de todos os padrões:** Em vez de restringir o algoritmo K-means apenas aos padrões com radiação ($d=1$), poderíamos clusterizar o espaço inteiro dos dados de treinamento. Isso faria com que a camada intermediária gerasse representações de ambas as classes, facilitando a criação do hiperplano de separação na camada de saída.\n")
    f.write("2. **Aumentar o número de centros (K):** Uma rede RBF com apenas 2 neurônios ocultos pode sofrer de *underfitting* em espaços de decisão não-lineares mais sinuosos. Aumentar o número de clusters permitiria mapear a região com maior granularidade.\n")
    f.write("3. **Treinamento supervisionado das larguras (Variâncias):** Ao invés de calcular a variância fixamente pelas distâncias médias de um cluster k-means, poderíamos calibrar este parâmetro dinamicamente através do gradiente descendente (ajuste fino retropropado) para otimizar os raios de influência de cada neurônio RBF.\n")

print("RBF1 DONE")
