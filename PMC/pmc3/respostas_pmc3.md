# Respostas do Trabalho de PMC 3 - Sistemas Variantes no Tempo (Previsão do Mercado Financeiro via TDNN)

### 6. Qual topologia candidata e configuração final seria a mais adequada?

Para um mapeamento fiel de "Time Delay" com melhor predição de preços de ações, avalia-se o comportamento nas amostras de `t=101` a `120`. A melhor Rede (Topologia 1, 2 ou 3) juntamente do seu melhor treinamento (T1, T2 ou T3) será aquela em que a curva gerada pela predição das amostras de Teste se aproxime ou sobreponha perfeitamente sobre a curva Desejada (`f(t)` real) no gráfico gerado. Quantitativamente, deve ser escolhida a Rede que acusar o **menor Erro Relativo Médio (MRE)** durante os ensaios sobre as novas amostras (t = 101...120).

### 7. Principais características e vantagens de variantes do Backpropagation:

#### a. Algoritmo de treinamento Resilient-Propagation (RProp)
O RProp é um método heurístico que modifica a atualização dos pesos da rede considerando estritamente o **sinal do gradiente (positivo ou negativo)** da função de erro em relação aos pesos, mas ignorando a sua magnitude.
*   **Vantagem principal:** Resolve com sucesso o problema do desaparecimento de gradiente (vanishing gradient) — muito comum ao utilizar funções sigmoides — pois o tamanho da atualização dos pesos varia adaptativamente, não ficando excessivamente pequeno nas caudas assintóticas da função de ativação. Com isso, provê uma excelente taxa de convergência e dispensa a necessidade do projetista sintonizar a taxa de aprendizado e o termo momentum, já que ele atualiza as taxas individualmente por cada conexão.

#### b. Algoritmo de treinamento Levenberg-Marquardt (LM)
O Levenberg-Marquardt (LM) é uma mistura sofisticada do método iterativo Gauss-Newton com o método do gradiente descendente. Ele foi concebido para se aproximar à velocidade ótima das soluções de aproximação de segunda ordem sem a obrigação custosa de calcular efetivamente a matriz Hessiana. Ele faz isso computando a matriz Jacobiana (primeira derivada da rede com relação aos parâmetros), o que acarreta em passos computacionais menores.
*   **Vantagem principal:** É frequentemente considerado o **algoritmo mais veloz** para o treinamento prático de Redes Neurais de pequeno a médio porte em diversas aplicações. Sua principal vantagem é possuir uma robustez considerável à divergência (como no Gradiente Descendente) somada à rápida convergência das abordagens de segunda ordem (como no método Gauss-Newton). Seu trade-off ocorre no maior uso de memória, necessário para armazenar a matriz Jacobiana a cada época de treinamento.
