import numpy as np

def carregar_dados(caminho_arquivo):
    dados = np.loadtxt(caminho_arquivo, delimiter=',', skiprows=1)
    X = dados[:, 1:5]
    d = dados[:, 5]
    return X, d

def treinar_adaline(X, d, taxa_aprendizado, precisao, max_epocas):
    num_amostras, num_features = X.shape
    x0 = -np.ones((num_amostras, 1))
    X_com_bias = np.hstack((x0, X))
    
    w = np.random.uniform(0, 1, size=num_features + 1)
    
    eqm_anterior = float('inf')
    historico_eqm = []
    
    epocas_concluidas = 0
    for epoca in range(max_epocas):
        v_total = np.dot(X_com_bias, w)
        eqm_atual = np.mean((d - v_total)**2)
        historico_eqm.append(eqm_atual)
        
        if abs(eqm_atual - eqm_anterior) <= precisao:
            break
            
        eqm_anterior = eqm_atual
        
        # O Adaline pode ser treinado estocástico ou batch.
        # Aqui mantemos a lógica original estocástica que a interface esperava
        for i in range(num_amostras):
            v = np.dot(w, X_com_bias[i])
            erro = d[i] - v
            w = w + taxa_aprendizado * erro * X_com_bias[i]
            
        epocas_concluidas += 1
            
    return w, epocas_concluidas, historico_eqm
