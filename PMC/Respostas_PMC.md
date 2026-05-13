# Respostas do Trabalho de PMC (Perceptron Multicamadas)

Abaixo estão as respostas teóricas solicitadas nas atividades. Para preencher as tabelas e gerar os gráficos requisitados nas atividades 1, 2 e 3, basta executar os scripts Python (`pmc1.py`, `pmc2.py`, e `pmc3.py`) desenvolvidos dentro das respectivas pastas (`pmc1`, `pmc2` e `pmc3`) na raiz do diretório `PMC`. Como esses scripts necessitam das bibliotecas `numpy` e `matplotlib` para realizar o treinamento eficiente e a plotagem, eles devem ser rodados em um ambiente virtual ou máquina que os possuam.

---

## PMC 1 - Aproximador Universal de Funções (Sistema de Ressonância Magnética)

### 4. Por que o erro quadrático médio e o número de épocas variam de treinamento para treinamento?

A variação no Erro Quadrático Médio (EQM) e no número de épocas ocorre porque cada treinamento da Rede Neural Perceptron inicializa os pesos sinápticos e os limiares (bias) (matrizes W1, b1, W2 e b2) com valores aleatórios entre 0 e 1.
Isso significa que, a cada novo treinamento, a rede neural inicia sua busca pelo mínimo da superfície da função de erro em um ponto de partida diferente no espaço de pesos. O algoritmo de backpropagation utiliza a descida do gradiente, que traça diferentes trajetórias e atualizações de pesos dependendo dessa condição inicial. Como resultado:
1. **Número de Épocas:** A distância percorrida até o ponto ótimo, assim como o caminho tomado, será diferente, necessitando de uma quantidade maior ou menor de passos (épocas) para satisfazer o critério de parada (precisão de $10^{-6}$).
2. **Erro Quadrático Médio (EQM):** Dependendo do ponto de partida, o treinamento pode convergir para mínimos locais distintos na superfície de erro não convexa gerada por uma rede multicamadas, ou atingir o fundo do vale com pequenos desvios limitados pelo passo do gradiente, o que justifica o valor distinto no erro residual final.

### 6. Qual das configurações finais de treinamento seria a mais adequada para o sistema de ressonância magnética?

A configuração (T1, T2, T3, T4 ou T5) que está oferecendo a **melhor generalização**, e portanto a mais adequada para o sistema, é aquela que apresentar simultaneamente o **menor Erro Relativo Médio (%)** e uma **baixa Variância (%)** no conjunto de teste (Amostras de validação), não necessariamente no conjunto de treinamento. Isso significa que tal treinamento foi o que conseguiu mapear as regras universais da função (variável `y` que mede a energia absorvida com base em `x1, x2, x3`) e se adaptar a novos dados, superando o risco de sobreajuste (overfitting). Os resultados precisos das 5 baterias de testes encontram-se nos arquivos de saídas produzidos pelo script `pmc1.py`.

---

## PMC 2 - Classificadora de Padrões (Conservantes de Bebidas)

A execução do `pmc2.py` irá evidenciar, via gráfico e contagem de tempo, a diferença fundamental da adição da constante de *Momentum* ao treinamento Backpropagation Padrão. Tipicamente, observa-se que o termo Momentum ($=0.9$) auxilia fortemente o algoritmo a ultrapassar platôs e mínimos locais, convergindo e chegando ao critério de parada na precisão em um **número consideravelmente menor de épocas**, acelerando o tempo de processamento. A função de arredondamento simétrico aplicada em Python traduz as saídas preditas reais para o critério binário (ex: se `0.85` e limiar é `0.5`, ajusta-se para `1`) determinando assim, efetivamente, o conservante `A, B` ou `C` que será aplicado.

---

## PMC 3 - Sistemas Variantes no Tempo (Previsão do Mercado Financeiro via TDNN)

### 6. Qual topologia candidata e configuração final seria a mais adequada?

Para um mapeamento fiel de "Time Delay" com melhor predição de preços de ações, avalia-se o comportamento nas amostras de `t=101` a `120`. A melhor Rede (Topologia 1, 2 ou 3) juntamente do seu melhor treinamento (T1, T2 ou T3) será aquela em que a curva gerada pela predição das amostras de Teste se aproxime ou sobreponha perfeitamente sobre a curva Desejada (`f(t)` real) no gráfico gerado. Quantitativamente, deve ser escolhida a Rede que acusar o **menor Erro Relativo Médio (MRE)** durante os ensaios sobre as novas amostras (t = 101...120).

### 7. Principais características e vantagens de variantes do Backpropagation:

#### a. Algoritmo de treinamento Resilient-Propagation (RProp)
O RProp é um método heurístico que modifica a atualização dos pesos da rede considerando estritamente o **sinal do gradiente (positivo ou negativo)** da função de erro em relação aos pesos, mas ignorando a sua magnitude.
*   **Vantagem principal:** Resolve com sucesso o problema do desaparecimento de gradiente (vanishing gradient) — muito comum ao utilizar funções sigmoides — pois o tamanho da atualização dos pesos varia adaptativamente, não ficando excessivamente pequeno nas caudas assintóticas da função de ativação. Com isso, provê uma excelente taxa de convergência e dispensa a necessidade do projetista sintonizar a taxa de aprendizado e o termo momentum, já que ele atualiza as taxas individualmente por cada conexão.

#### b. Algoritmo de treinamento Levenberg-Marquardt (LM)
O Levenberg-Marquardt (LM) é uma mistura sofisticada do método iterativo Gauss-Newton com o método do gradiente descendente. Ele foi concebido para se aproximar à velocidade ótima das soluções de aproximação de segunda ordem sem a obrigação custosa de calcular efetivamente a matriz Hessiana. Ele faz isso computando a matriz Jacobiana (primeira derivada da rede com relação aos parâmetros), o que acarreta em passos computacionais menores.
*   **Vantagem principal:** É frequentemente considerado o **algoritmo mais veloz** para o treinamento prático de Redes Neurais de pequeno a médio porte em diversas aplicações. Sua principal vantagem é possuir uma robustez considerável à divergência (como no Gradiente Descendente) somada à rápida convergência das abordagens de segunda ordem (como no método Gauss-Newton). Seu trade-off ocorre no maior uso de memória, necessário para armazenar a matriz Jacobiana a cada época de treinamento.
