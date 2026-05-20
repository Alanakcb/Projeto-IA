import numpy as np
import matplotlib.pyplot as plt
import io

data_raw = """
1	0.1701	26	0.2398	51	0.3087	76	0.3701
2	0.1023	27	0.0508	52	0.0159	77	0.0006
3	0.4405	28	0.4497	53	0.4330	78	0.3943
4	0.3609	29	0.2178	54	0.0733	79	0.0646
5	0.7192	30	0.7762	55	0.7995	80	0.7878
6	0.2258	31	0.1078	56	0.0262	81	0.1694
7	0.3175	32	0.3773	57	0.4223	82	0.4468
8	0.0127	33	0.0001	58	0.0085	83	0.0372
9	0.4290	34	0.3877	59	0.3303	84	0.2632
10	0.0544	35	0.0821	60	0.2037	85	0.3048
11	0.8000	36	0.7836	61	0.7332	86	0.6516
12	0.0450	37	0.1887	62	0.3328	87	0.4690
13	0.4268	38	0.4483	63	0.4445	88	0.4132
14	0.0112	39	0.0424	64	0.0909	89	0.1523
15	0.3218	40	0.2539	65	0.1838	90	0.1182
16	0.2185	41	0.3164	66	0.3888	91	0.4334
17	0.7240	42	0.6386	67	0.5277	92	0.3978
18	0.3516	43	0.4862	68	0.6042	93	0.6987
19	0.4420	44	0.4068	69	0.3435	94	0.2538
20	0.0984	45	0.1611	70	0.2304	95	0.2998
21	0.1747	46	0.1101	71	0.0568	96	0.0195
22	0.3964	47	0.4372	72	0.4500	97	0.4366
23	0.5114	48	0.3795	73	0.2371	98	0.0924
24	0.6183	49	0.7092	74	0.7705	99	0.7984
25	0.3330	50	0.2400	75	0.1246	100	0.0077
"""

test_raw = """
101	0.4173
102	0.0062
103	0.3387
104	0.1886
105	0.7418
106	0.3138
107	0.4466
108	0.0835
109	0.1930
110	0.3807
111	0.5438
112	0.5897
113	0.3536
114	0.2210
115	0.0631
116	0.4499
117	0.2564
118	0.7642
119	0.1411
120	0.3626
"""

f_t = np.zeros(100)
for line in data_raw.strip().split('\n'):
    parts = line.strip().split()
    f_t[int(parts[0])-1] = float(parts[1])
    f_t[int(parts[2])-1] = float(parts[3])
    f_t[int(parts[4])-1] = float(parts[5])
    f_t[int(parts[6])-1] = float(parts[7])

f_test = np.zeros(20)
for line in test_raw.strip().split('\n'):
    parts = line.strip().split()
    f_test[int(parts[0])-101] = float(parts[1])

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def sigmoid_derivative(x):
    return sigmoid(x) * (1 - sigmoid(x))

def train_tdnn(p, N1, seed):
    output_size = 1
    learning_rate = 0.1
    momentum = 0.8
    precision = 1e-6
    
    # Preparar dados de treino
    X_train = []
    y_train = []
    for i in range(100 - p):
        X_train.append(f_t[i:i+p])
        y_train.append(f_t[i+p])
    X_train = np.array(X_train)
    y_train = np.array(y_train).reshape(-1, 1)
    
    # Preparar dados de teste (t=101 a 120)
    X_test = []
    all_f = np.concatenate([f_t, f_test])
    for i in range(20):
        start_idx = 100 + i - p
        X_test.append(all_f[start_idx:start_idx+p])
    X_test = np.array(X_test)
    y_test = f_test.reshape(-1, 1)
    
    np.random.seed(seed)
    W1 = np.random.rand(p, N1)
    b1 = np.random.rand(1, N1)
    W2 = np.random.rand(N1, output_size)
    b2 = np.random.rand(1, output_size)
    
    vW1 = np.zeros_like(W1)
    vb1 = np.zeros_like(b1)
    vW2 = np.zeros_like(W2)
    vb2 = np.zeros_like(b2)
    
    mse_history = []
    epoch = 0
    prev_mse = float('inf')
    
    while epoch < 100000:
        Z1 = np.dot(X_train, W1) + b1
        A1 = sigmoid(Z1)
        Z2 = np.dot(A1, W2) + b2
        A2 = sigmoid(Z2)
        
        error = y_train - A2
        mse = np.mean(error ** 2)
        mse_history.append(mse)
        
        if abs(prev_mse - mse) < precision:
            break
        prev_mse = mse
        epoch += 1
        
        dZ2 = error * sigmoid_derivative(Z2)
        dW2 = np.dot(A1.T, dZ2)
        db2 = np.sum(dZ2, axis=0, keepdims=True)
        
        dZ1 = np.dot(dZ2, W2.T) * sigmoid_derivative(Z1)
        dW1 = np.dot(X_train.T, dZ1)
        db1 = np.sum(dZ1, axis=0, keepdims=True)
        
        vW2 = momentum * vW2 + learning_rate * dW2 / len(X_train)
        vb2 = momentum * vb2 + learning_rate * db2 / len(X_train)
        W2 += vW2
        b2 += vb2
        
        vW1 = momentum * vW1 + learning_rate * dW1 / len(X_train)
        vb1 = momentum * vb1 + learning_rate * db1 / len(X_train)
        W1 += vW1
        b1 += vb1
        
    Z1 = np.dot(X_test, W1) + b1
    A1 = sigmoid(Z1)
    Z2 = np.dot(A1, W2) + b2
    A2 = sigmoid(Z2)
    y_pred = A2
    
    rel_errors = np.abs(y_test - y_pred) / np.abs(y_test) * 100
    mean_rel_error = np.mean(rel_errors)
    var_rel_error = np.var(rel_errors)
    
    return epoch, mse, mse_history, y_pred, mean_rel_error, var_rel_error

topologias = [(5, 10, 'Rede 1'), (10, 15, 'Rede 2'), (15, 25, 'Rede 3')]
all_results = {}

with open('resultados_pmc3.txt', 'w', encoding='utf-8') as f:
    for p, N1, name in topologias:
        f.write(f"--- {name} ---\n")
        all_results[name] = []
        for t in range(3):
            seed = t * 42
            ep, mse, hist, y_pred, mre, vre = train_tdnn(p, N1, seed)
            all_results[name].append((ep, mse, hist, y_pred, mre, vre))
            f.write(f"T{t+1}: {ep} épocas | EQM: {mse:.6f} | Erro Rel Médio: {mre:.2f}% | Variância: {vre:.2f}%\n")
            print(f"{name} T{t+1}: {ep} épocas, EQM={mse:.6f}")

# Gráficos
fig_eqm, axs_eqm = plt.subplots(3, 1, figsize=(10, 15))
fig_pred, axs_pred = plt.subplots(3, 1, figsize=(10, 15))

for idx, (p, N1, name) in enumerate(topologias):
    # Escolhe o melhor treinamento (menor MSE)
    best_t = min(range(3), key=lambda i: all_results[name][i][1])
    ep, mse, hist, y_pred, mre, vre = all_results[name][best_t]
    
    axs_eqm[idx].plot(hist, label=f'{name} (Melhor T{best_t+1})')
    axs_eqm[idx].set_xlabel('Épocas')
    axs_eqm[idx].set_ylabel('EQM')
    axs_eqm[idx].set_title(f'Curva de Aprendizagem - {name}')
    axs_eqm[idx].legend()
    axs_eqm[idx].grid(True)
    
    t_test = np.arange(101, 121)
    axs_pred[idx].plot(t_test, f_test, marker='o', label='Desejado')
    axs_pred[idx].plot(t_test, y_pred, marker='x', label='Estimado')
    axs_pred[idx].set_xlabel('Amostra (t)')
    axs_pred[idx].set_ylabel('Valor')
    axs_pred[idx].set_title(f'Predição - {name} (Melhor T{best_t+1})')
    axs_pred[idx].legend()
    axs_pred[idx].grid(True)

fig_eqm.tight_layout()
fig_eqm.savefig('graficos_eqm_pmc3.png')

fig_pred.tight_layout()
fig_pred.savefig('graficos_predicao_pmc3.png')

print("Finalizado e gráficos salvos!")
