# Respostas do Trabalho de PMC 1 - Aproximador Universal de Funções (Sistema de Ressonância Magnética)

### 1. Tabela com os resultados de todos os treinamentos

Foram executados 5 treinamentos (T1 a T5) inicializando os pesos sinápticos e os limiares aleatoriamente.

| Treinamento | Erro Quadrático Médio (EQM) | Número de Épocas |
|---|---|---|
| **T1** | 0.003986 | 13128 |
| **T2** | 0.004201 | 10562 |
| **T3** | 0.004512 | 14948 |
| **T4** | 0.004389 | 11149 |
| **T5** | 0.003953 | 13295 |

### 2. Tabela de Saídas da Rede nas Amostras de Teste

| Amostra | $y_{desejado}$ | $y_{rede(T1)}$ | $y_{rede(T2)}$ | $y_{rede(T3)}$ | $y_{rede(T4)}$ | $y_{rede(T5)}$ |
|---|---|---|---|---|---|---|
| 1 | 0.4831 | 0.5296 | 0.5396 | 0.5271 | 0.5282 | 0.5189 |
| 2 | 0.5965 | 0.6017 | 0.6006 | 0.6102 | 0.5990 | 0.6049 |
| 3 | 0.5318 | 0.5586 | 0.5670 | 0.5635 | 0.5520 | 0.5459 |
| 4 | 0.6843 | 0.6805 | 0.6765 | 0.6811 | 0.6850 | 0.6923 |
| 5 | 0.2872 | 0.3686 | 0.3690 | 0.3751 | 0.3733 | 0.3637 |
| 6 | 0.7663 | 0.7164 | 0.7168 | 0.7103 | 0.7189 | 0.7189 |
| 7 | 0.5666 | 0.5867 | 0.5872 | 0.5817 | 0.5956 | 0.5935 |
| 8 | 0.6601 | 0.6663 | 0.6726 | 0.6617 | 0.6640 | 0.6571 |
| 9 | 0.5427 | 0.5594 | 0.5541 | 0.5633 | 0.5652 | 0.5713 |
| 10 | 0.5836 | 0.6121 | 0.6184 | 0.6055 | 0.6163 | 0.6105 |
| 11 | 0.6950 | 0.6740 | 0.6786 | 0.6712 | 0.6701 | 0.6643 |
| 12 | 0.6790 | 0.6583 | 0.6548 | 0.6596 | 0.6623 | 0.6687 |
| 13 | 0.2956 | 0.3760 | 0.3804 | 0.3843 | 0.3777 | 0.3676 |
| 14 | 0.7742 | 0.7375 | 0.7348 | 0.7359 | 0.7325 | 0.7377 |
| 15 | 0.4662 | 0.5143 | 0.5229 | 0.5111 | 0.5148 | 0.5059 |
| 16 | 0.8093 | 0.7646 | 0.7617 | 0.7578 | 0.7658 | 0.7704 |
| 17 | 0.7581 | 0.7379 | 0.7378 | 0.7331 | 0.7309 | 0.7262 |
| 18 | 0.5826 | 0.6027 | 0.6065 | 0.6095 | 0.5964 | 0.5950 |
| 19 | 0.7938 | 0.7478 | 0.7441 | 0.7448 | 0.7478 | 0.7558 |
| 20 | 0.5012 | 0.5368 | 0.5441 | 0.5328 | 0.5388 | 0.5314 |

### 3. Avaliação no Conjunto de Teste

| Treinamento | Erro Relativo Médio (%) | Variância (%) |
|---|---|---|
| **T1** | 6.81% | 55.21% |
| **T2** | 7.40% | 59.15% |
| **T3** | 7.19% | 65.19% |
| **T4** | 6.98% | 60.29% |
| **T5** | 6.30% | 45.27% |

### 4. Por que o erro quadrático médio e o número de épocas variam de treinamento para treinamento?

A variação no Erro Quadrático Médio (EQM) e no número de épocas ocorre porque cada treinamento da Rede Neural Perceptron inicializa os pesos sinápticos e os limiares (bias) (matrizes W1, b1, W2 e b2) com valores aleatórios entre 0 e 1.
Isso significa que, a cada novo treinamento, a rede neural inicia sua busca pelo mínimo da superfície da função de erro em um ponto de partida diferente no espaço de pesos. O algoritmo de backpropagation utiliza a descida do gradiente, que traça diferentes trajetórias e atualizações de pesos dependendo dessa condição inicial. Como resultado:
1. **Número de Épocas:** A distância percorrida até o ponto ótimo, assim como o caminho tomado, será diferente, necessitando de uma quantidade maior ou menor de passos (épocas) para satisfazer o critério de parada (precisão de $10^{-6}$).
2. **Erro Quadrático Médio (EQM):** Dependendo do ponto de partida, o treinamento pode convergir para mínimos locais distintos na superfície de erro não convexa gerada por uma rede multicamadas, ou atingir o fundo do vale com pequenos desvios limitados pelo passo do gradiente, o que justifica o valor distinto no erro residual final.

### 5. Gráficos do Erro Quadrático Médio

O gráfico demonstrando as duas maiores curvas de aprendizado (Treinamentos 3 e 5, com maior número de épocas) foi gerado e salvo como `grafico_eqm_pmc1.png`.

### 6. Qual das configurações finais de treinamento seria a mais adequada para o sistema de ressonância magnética?

A configuração (T1, T2, T3, T4 ou T5) que está oferecendo a **melhor generalização**, e portanto a mais adequada para o sistema, é aquela que apresentar simultaneamente o **menor Erro Relativo Médio (%)** e uma **baixa Variância (%)** no conjunto de teste (Amostras de validação), não necessariamente no conjunto de treinamento. Isso significa que tal treinamento foi o que conseguiu mapear as regras universais da função (variável `y` que mede a energia absorvida com base em `x1, x2, x3`) e se adaptar a novos dados, superando o risco de sobreajuste (overfitting). Os resultados precisos das 5 baterias de testes encontram-se nos arquivos de saídas produzidos pelo script `pmc1.py`.
