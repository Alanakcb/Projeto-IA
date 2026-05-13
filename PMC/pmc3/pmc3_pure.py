import math
import random
import time

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

f_t = [0] * 100
for line in data_raw.strip().split('\n'):
    parts = line.strip().split()
    f_t[int(parts[0])-1] = float(parts[1])
    f_t[int(parts[2])-1] = float(parts[3])
    f_t[int(parts[4])-1] = float(parts[5])
    f_t[int(parts[6])-1] = float(parts[7])

f_test = [0] * 20
for line in test_raw.strip().split('\n'):
    parts = line.strip().split()
    f_test[int(parts[0])-101] = float(parts[1])

def sigmoid(x):
    return 1.0 / (1.0 + math.exp(-max(min(x, 500), -500)))

def sigmoid_deriv(x):
    s = sigmoid(x)
    return s * (1.0 - s)

def train_net(input_size, hidden_size, seed_val):
    random.seed(seed_val)
    output_size = 1
    learning_rate = 0.1
    momentum = 0.8
    precision = 0.5e-6
    max_epochs = 20000
    
    # Prep data
    X_train = []
    y_train = []
    for i in range(100 - input_size):
        X_train.append(f_t[i:i+input_size])
        y_train.append(f_t[i+input_size])
        
    X_test = []
    y_test = f_test
    # Need past inputs. t=101 needs t=101-p to 100.
    all_f = f_t + f_test
    for i in range(20):
        start_idx = 100 + i - input_size
        X_test.append(all_f[start_idx:start_idx+input_size])
        
    W1 = [[random.uniform(0, 1) for _ in range(hidden_size)] for _ in range(input_size)]
    b1 = [random.uniform(0, 1) for _ in range(hidden_size)]
    W2 = [[random.uniform(0, 1) for _ in range(output_size)] for _ in range(hidden_size)]
    b2 = [random.uniform(0, 1) for _ in range(output_size)]
    
    vW1 = [[0]*hidden_size for _ in range(input_size)]
    vb1 = [0]*hidden_size
    vW2 = [[0]*output_size for _ in range(hidden_size)]
    vb2 = [0]*output_size
    
    epoch = 0
    prev_mse = float('inf')
    
    while epoch < max_epochs:
        mse = 0
        dW1 = [[0]*hidden_size for _ in range(input_size)]
        db1 = [0]*hidden_size
        dW2 = [[0]*output_size for _ in range(hidden_size)]
        db2 = [0]*output_size
        
        for i in range(len(X_train)):
            Z1 = [0]*hidden_size
            A1 = [0]*hidden_size
            for j in range(hidden_size):
                Z1[j] = b1[j] + sum(X_train[i][k] * W1[k][j] for k in range(input_size))
                A1[j] = sigmoid(Z1[j])
                
            Z2 = b2[0] + sum(A1[k] * W2[k][0] for k in range(hidden_size))
            A2 = sigmoid(Z2)
            
            error = y_train[i] - A2
            mse += error*error
            
            dZ2 = error * sigmoid_deriv(Z2)
            for j in range(hidden_size):
                dW2[j][0] += A1[j] * dZ2
            db2[0] += dZ2
            
            dZ1 = [0]*hidden_size
            for j in range(hidden_size):
                dZ1[j] = dZ2 * W2[j][0] * sigmoid_deriv(Z1[j])
                for k in range(input_size):
                    dW1[k][j] += X_train[i][k] * dZ1[j]
                db1[j] += dZ1[j]
                
        mse /= len(X_train)
        if abs(prev_mse - mse) < precision:
            break
        prev_mse = mse
        epoch += 1
        
        for j in range(hidden_size):
            vW2[j][0] = momentum * vW2[j][0] + learning_rate * dW2[j][0] / len(X_train)
            W2[j][0] += vW2[j][0]
        vb2[0] = momentum * vb2[0] + learning_rate * db2[0] / len(X_train)
        b2[0] += vb2[0]
        
        for j in range(input_size):
            for k in range(hidden_size):
                vW1[j][k] = momentum * vW1[j][k] + learning_rate * dW1[j][k] / len(X_train)
                W1[j][k] += vW1[j][k]
        for j in range(hidden_size):
            vb1[j] = momentum * vb1[j] + learning_rate * db1[j] / len(X_train)
            b1[j] += vb1[j]
            
    # Evaluation
    y_pred = []
    rel_errors = []
    for i in range(len(X_test)):
        Z1 = [b1[j] + sum(X_test[i][k] * W1[k][j] for k in range(input_size)) for j in range(hidden_size)]
        A1 = [sigmoid(z) for z in Z1]
        Z2 = b2[0] + sum(A1[k] * W2[k][0] for k in range(hidden_size))
        A2 = sigmoid(Z2)
        y_pred.append(A2)
        rel_errors.append(abs(y_test[i] - A2) / abs(y_test[i]) * 100)
    
    mean_rel_error = sum(rel_errors)/len(rel_errors)
    var_rel_error = sum((r - mean_rel_error)**2 for r in rel_errors)/len(rel_errors)
    
    return epoch, mse, y_pred, mean_rel_error, var_rel_error

# Topologies
topos = [(5, 10), (10, 15), (15, 25)]
results = []
for idx, (p, N1) in enumerate(topos):
    for t in range(3):
        ep, mse, y_pred, mre, vre = train_net(p, N1, t*42)
        print(f"Rede {idx+1} T{t+1}: Epocas={ep}, EQM={mse:.6f}, RelErr={mre:.2f}%")
        results.append({
            'rede': idx+1, 't': t+1, 'epoch': ep, 'mse': mse,
            'y_pred': y_pred, 'mre': mre, 'vre': vre
        })

with open('resultados_pmc3.txt', 'w') as f:
    for res in results:
        f.write(f"Rede {res['rede']} T{res['t']}: {res['epoch']} epocas, {res['mse']:.6f} EQM, {res['mre']:.2f}% ErrRel, {res['vre']:.2f}% Var\n")
        
    f.write("\nTest Predicts:\n")
    for i in range(20):
        f.write(f"t={101+i}\t")
        for res in results:
            f.write(f"{res['y_pred'][i]:.4f}\t")
        f.write("\n")
