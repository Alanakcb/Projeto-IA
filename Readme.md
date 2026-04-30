# Resolução do Trabalho de Classificação com Perceptron

### 1 e 2. Resultados dos 5 treinamentos (Tabela)

Foram executados 5 treinamentos independentes utilizando a Regra de Hebb (com taxa de aprendizado = 0.01), onde os pesos foram inicializados com valores aleatórios entre `0` e `1` a cada execução.

| Treinamento | Peso Inicial (w0) | Peso Inicial (w1) | Peso Inicial (w2) | Peso Inicial (w3) | Peso Final (w0) | Peso Final (w1) | Peso Final (w2) | Peso Final (w3) | Número de Épocas |
|---|---|---|---|---|---|---|---|---|---|
| **1º (T1)** | 0.3745 | 0.9507 | 0.7320 | 0.5987 | -3.1655 | 1.6028 | 2.5471 | -0.7529 | **441** |
| **2º (T2)** | 0.8231 | 0.0261 | 0.2108 | 0.6184 | -2.8769 | 1.4151 | 2.3711 | -0.6705 | **358** |
| **3º (T3)** | 0.0338 | 0.4891 | 0.8461 | 0.4114 | -3.0862 | 1.5745 | 2.4837 | -0.7374 | **386** |
| **4º (T4)** | 0.1067 | 0.6843 | 0.5350 | 0.3692 | -3.0933 | 1.5669 | 2.4888 | -0.7368 | **404** |
| **5º (T5)** | 0.2752 | 0.6392 | 0.6239 | 0.7780 | -2.9048 | 1.4265 | 2.3974 | -0.6775 | **334** |

---

### 3. Tabela de Classificação das Novas Amostras

Após o treinamento, todos os 5 modelos finais foram testados com as novas amostras (onde `y` é a classe classificada). Como o problema é perfeitamente linearmente separável, todos os 5 modelos convergiram para hiperplanos equivalentes, resultando nas exatas mesmas classificações.

| Amostra | x1 | x2 | x3 | y (T1) | y (T2) | y (T3) | y (T4) | y (T5) |
|---|---|---|---|---|---|---|---|---|
| **1** | -0.3565 | 0.0620 | 5.9891 | -1 | -1 | -1 | -1 | -1 |
| **2** | -0.7842 | 1.1267 | 5.5912 | 1 | 1 | 1 | 1 | 1 |
| **3** | 0.3012 | 0.5611 | 5.8234 | 1 | 1 | 1 | 1 | 1 |
| **4** | 0.7757 | 1.0648 | 8.0677 | 1 | 1 | 1 | 1 | 1 |
| **5** | 0.1570 | 0.8028 | 6.3040 | 1 | 1 | 1 | 1 | 1 |
| **6** | -0.7014 | 1.0316 | 3.6005 | 1 | 1 | 1 | 1 | 1 |
| **7** | 0.3748 | 0.1536 | 6.1537 | -1 | -1 | -1 | -1 | -1 |
| **8** | -0.6920 | 0.9404 | 4.4058 | 1 | 1 | 1 | 1 | 1 |
| **9** | -1.3970 | 0.7141 | 4.9263 | -1 | -1 | -1 | -1 | -1 |
| **10** | -1.8842 | -0.2805 | 1.2548 | -1 | -1 | -1 | -1 | -1 |

---

### 4. Explique por que o número de épocas de treinamento varia a cada vez que executamos o treinamento do perceptron.

O número de épocas varia porque os pesos da rede neural são **inicializados com valores aleatórios** no início de cada execução. 
Matematicamente, as épocas representam a quantidade de iterações ("passos") que o hiperplano de separação precisa dar no espaço vetorial para corrigir seus erros e encontrar a angulação perfeita de divisão entre as classes. 
Se os pesos iniciais começarem "por sorte" em uma coordenada já próxima dessa posição ideal, o algoritmo precisará de poucos ajustes e finalizará o treinamento rapidamente. Por outro lado, se a aleatoriedade inicial colocar o hiperplano numa posição inicial muito distante ou ruim, o algoritmo demorará mais iterações para atravessar o espaço até convergir.

---

### 5. Qual a principal limitação do perceptron quando aplicado em problemas de classificação de padrões.

A principal limitação estrutural do Perceptron clássico (de camada única) é a sua incapacidade de resolver problemas que não sejam **linearmente separáveis**. 
Isso significa que o Perceptron só funciona perfeitamente caso exista a possibilidade de se traçar uma linha reta simples (ou um plano reto) que consiga cortar e separar completamente a Classe 1 da Classe 2 no gráfico. Quando nos deparamos com dados mais complexos em que as classes estão "misturadas" de forma circular, em espiral ou intercaladas (como no conhecido problema da porta lógica XOR), não é possível fazer essa divisão com uma única reta. Nestes cenários de separação não-linear, o modelo do Perceptron Simples entrará num loop sem fim em que os erros nunca se tornam zero, exigindo que sejam adotadas redes multicamadas (MLP - Multi-Layer Perceptrons) para contornar o problema.
