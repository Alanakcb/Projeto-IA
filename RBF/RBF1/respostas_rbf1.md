# Respostas RBF 1

### 1. Treinamento da Camada Escondida (K-means)
| Cluster | Centro | Variância |
|---|---|---|
| 1 | [0.1648, 0.6121] | 0.029806 |
| 2 | [0.3990, 0.1571] | 0.038460 |

### 2. Pesos da Camada de Saída
| Peso | Valor |
|---|---|
| W21,0 (bias) | 1.002653 |
| W21,1 | 2.378042 |
| W21,2 | 2.697707 |

### 3 e 4. Classificação e Taxa de Acerto
| Amostra | x1 | x2 | d | y | ypós |
|---|---|---|---|---|---|
| 1 | 0.8705 | 0.9329 | -1 | -1.0025 | -1 |
| 2 | 0.0388 | 0.2703 | 1 | -0.3231 | -1 |
| 3 | 0.8236 | 0.4458 | -1 | -0.9140 | -1 |
| 4 | 0.7075 | 0.1502 | 1 | -0.2201 | -1 |
| 5 | 0.9587 | 0.8663 | -1 | -1.0026 | -1 |
| 6 | 0.6115 | 0.9365 | -1 | -0.9878 | -1 |
| 7 | 0.3534 | 0.3646 | 1 | 0.9665 | 1 |
| 8 | 0.3268 | 0.2766 | 1 | 1.3232 | 1 |
| 9 | 0.6129 | 0.4518 | -1 | -0.4682 | -1 |
| 10 | 0.9948 | 0.4962 | -1 | -0.9966 | -1 |

**Taxa de Acerto (%):** 80.00%

### 5. Estratégias para aumentar a taxa de acerto
Para aumentar a taxa de acerto desta RBF, poderíamos adotar as seguintes estratégias:

1. **Clusterização de todos os padrões:** Em vez de restringir o algoritmo K-means apenas aos padrões com radiação ($d=1$), poderíamos clusterizar o espaço inteiro dos dados de treinamento. Isso faria com que a camada intermediária gerasse representações de ambas as classes, facilitando a criação do hiperplano de separação na camada de saída.
2. **Aumentar o número de centros (K):** Uma rede RBF com apenas 2 neurônios ocultos pode sofrer de *underfitting* em espaços de decisão não-lineares mais sinuosos. Aumentar o número de clusters permitiria mapear a região com maior granularidade.
3. **Treinamento supervisionado das larguras (Variâncias):** Ao invés de calcular a variância fixamente pelas distâncias médias de um cluster k-means, poderíamos calibrar este parâmetro dinamicamente através do gradiente descendente (ajuste fino retropropado) para otimizar os raios de influência de cada neurônio RBF.
