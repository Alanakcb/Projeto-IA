# Trabalho ADALINE: Resolução e Análise

### 1 e 2. Tabela de Treinamentos (ADALINE)

Foram executados 5 treinamentos (T1 a T5) inicializando os pesos com valores aleatórios entre 0 e 1, taxa de aprendizado de `0.0025` e precisão de parada de `10⁻⁶`.

| Treinamento | Inicial (w0) | Inicial (w1) | Inicial (w2) | Inicial (w3) | Inicial (w4) | Final (w0) | Final (w1) | Final (w2) | Final (w3) | Final (w4) | Número de Épocas |
|---|---|---|---|---|---|---|---|---|---|---|---|
| **1º (T1)** | 0.3745 | 0.9507 | 0.7320 | 0.5987 | 0.1560 | -1.8130 | 1.3129 | 1.6423 | -0.4275 | -1.1778 | **888** |
| **2º (T2)** | 0.9240 | 0.1579 | 0.8669 | 0.0842 | 0.5736 | -1.8131 | 1.3129 | 1.6423 | -0.4277 | -1.1778 | **909** |
| **3º (T3)** | 0.3108 | 0.8190 | 0.3348 | 0.1937 | 0.1103 | -1.8130 | 1.3128 | 1.6422 | -0.4277 | -1.1777 | **880** |
| **4º (T4)** | 0.6064 | 0.6575 | 0.3072 | 0.9620 | 0.5359 | -1.8130 | 1.3129 | 1.6424 | -0.4275 | -1.1778 | **932** |
| **5º (T5)** | 0.1161 | 0.6585 | 0.3756 | 0.6128 | 0.6795 | -1.8130 | 1.3129 | 1.6423 | -0.4276 | -1.1778 | **897** |

---

### 3. Gráficos de Erro Quadrático Médio (EQM)

A imagem do gráfico foi gerada e salva com o nome `grafico_eqm.png` na mesma pasta (`projeto_IA/adaline/`).

---

### 4. Tabela de Classificação das Novas Amostras

As novas 15 amostras ruidosas foram expostas à rede após os treinamentos para indicar o acionamento da válvula A (-1) ou válvula B (1). Note que os 5 modelos convergem para as mesmas decisões.

| Amostra | x1 | x2 | x3 | x4 | y (T1) | y (T2) | y (T3) | y (T4) | y (T5) |
|---|---|---|---|---|---|---|---|---|---|
| **1** | 0.9694 | 0.6909 | 0.4334 | 3.4965 | -1 | -1 | -1 | -1 | -1 |
| **2** | 0.5427 | 1.3832 | 0.6390 | 4.0352 | -1 | -1 | -1 | -1 | -1 |
| **3** | 0.6081 | -0.9196 | 0.5925 | 0.1016 | 1 | 1 | 1 | 1 | 1 |
| **4** | -0.1618 | 0.4694 | 0.2030 | 3.0117 | -1 | -1 | -1 | -1 | -1 |
| **5** | 0.1870 | -0.2578 | 0.6124 | 1.7749 | -1 | -1 | -1 | -1 | -1 |
| **6** | 0.4891 | -0.5276 | 0.4378 | 0.6439 | 1 | 1 | 1 | 1 | 1 |
| **7** | 0.3777 | 2.0149 | 0.7423 | 3.3932 | 1 | 1 | 1 | 1 | 1 |
| **8** | 1.1498 | -0.4067 | 0.2469 | 1.5866 | 1 | 1 | 1 | 1 | 1 |
| **9** | 0.9325 | 1.0950 | 1.0359 | 3.3591 | 1 | 1 | 1 | 1 | 1 |
| **10** | 0.5060 | 1.3317 | 0.9222 | 3.7174 | -1 | -1 | -1 | -1 | -1 |
| **11** | 0.0497 | -2.0656 | 0.6124 | -0.6585 | -1 | -1 | -1 | -1 | -1 |
| **12** | 0.4004 | 3.5369 | 0.9766 | 5.3532 | 1 | 1 | 1 | 1 | 1 |
| **13** | -0.1874 | 1.3343 | 0.5374 | 3.2189 | -1 | -1 | -1 | -1 | -1 |
| **14** | 0.5060 | 1.3317 | 0.9222 | 3.7174 | -1 | -1 | -1 | -1 | -1 |
| **15** | 1.6375 | -0.7911 | 0.7537 | 0.5515 | 1 | 1 | 1 | 1 | 1 |

---

### 5. Embora o número de épocas de cada treinamento realizado no item 2 seja diferente, explique por que então os valores dos pesos continuam praticamente inalterados.

Embora os pesos sejam inicializados em coordenadas aleatórias e o número de épocas varie (já que cada execução precisa percorrer uma distância diferente até a solução ótima para alcançar a precisão requerida de $10^{-6}$), a rede ADALINE ajusta os seus pesos utilizando a Regra Delta. 

A matemática da Regra Delta sempre busca minimizar a função do Erro Quadrático Médio, que possui o formato geométrico de um paraboloide, ou seja, tem apenas **um único ponto de mínimo global** (fundo da bacia). Como não existem mínimos locais nessa superfície para este tipo de problema, o algoritmo fatalmente descerá a curva de erro e convergirá estritamente para a mesma solução ótima de hiperplano. Portanto, independentemente do "caminho" e da "distância" (número de épocas) gerados pela aleatoriedade inicial, o "destino" onde a função de erro atinge o seu valor mínimo será sempre o mesmo, resultando em pesos finais praticamente idênticos.
