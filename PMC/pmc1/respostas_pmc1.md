# Respostas do Trabalho de PMC 1 - Aproximador Universal de Funções (Sistema de Ressonância Magnética)

### 4. Por que o erro quadrático médio e o número de épocas variam de treinamento para treinamento?

A variação no Erro Quadrático Médio (EQM) e no número de épocas ocorre porque cada treinamento da Rede Neural Perceptron inicializa os pesos sinápticos e os limiares (bias) (matrizes W1, b1, W2 e b2) com valores aleatórios entre 0 e 1.
Isso significa que, a cada novo treinamento, a rede neural inicia sua busca pelo mínimo da superfície da função de erro em um ponto de partida diferente no espaço de pesos. O algoritmo de backpropagation utiliza a descida do gradiente, que traça diferentes trajetórias e atualizações de pesos dependendo dessa condição inicial. Como resultado:
1. **Número de Épocas:** A distância percorrida até o ponto ótimo, assim como o caminho tomado, será diferente, necessitando de uma quantidade maior ou menor de passos (épocas) para satisfazer o critério de parada (precisão de $10^{-6}$).
2. **Erro Quadrático Médio (EQM):** Dependendo do ponto de partida, o treinamento pode convergir para mínimos locais distintos na superfície de erro não convexa gerada por uma rede multicamadas, ou atingir o fundo do vale com pequenos desvios limitados pelo passo do gradiente, o que justifica o valor distinto no erro residual final.

### 6. Qual das configurações finais de treinamento seria a mais adequada para o sistema de ressonância magnética?

A configuração (T1, T2, T3, T4 ou T5) que está oferecendo a **melhor generalização**, e portanto a mais adequada para o sistema, é aquela que apresentar simultaneamente o **menor Erro Relativo Médio (%)** e uma **baixa Variância (%)** no conjunto de teste (Amostras de validação), não necessariamente no conjunto de treinamento. Isso significa que tal treinamento foi o que conseguiu mapear as regras universais da função (variável `y` que mede a energia absorvida com base em `x1, x2, x3`) e se adaptar a novos dados, superando o risco de sobreajuste (overfitting). Os resultados precisos das 5 baterias de testes encontram-se nos arquivos de saídas produzidos pelo script `pmc1.py`.
