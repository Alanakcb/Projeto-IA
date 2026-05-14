# Respostas do Trabalho de PMC 3 - Sistemas Variantes no Tempo (Previsão do Mercado Financeiro via TDNN)

### 1. Resultados da Rede 1 (p=5, N1=10)

Foram realizados 3 treinamentos (T1, T2 e T3) variando a inicialização aleatória dos pesos.
* **T1:** 4849 épocas | EQM: 0.012586 | Erro Rel Médio: 77.94% | Variância: 42721.72%
* **T2:** 86 épocas | EQM: 0.050479 | Erro Rel Médio: 329.32% | Variância: 1271897.44%
* **T3:** 15031 épocas | EQM: 0.005768 | Erro Rel Médio: 41.03% | Variância: 6726.06%

### 2. Resultados da Rede 2 (p=10, N1=15)

* **T1:** 4788 épocas | EQM: 0.003253 | Erro Rel Médio: 47.58% | Variância: 21286.89%
* **T2:** 161 épocas | EQM: 0.051558 | Erro Rel Médio: 325.83% | Variância: 1243314.13%
* **T3:** 5019 épocas | EQM: 0.003529 | Erro Rel Médio: 48.47% | Variância: 20902.85%

### 3. Resultados da Rede 3 (p=15, N1=25)

* **T1:** 1 época | EQM: 0.494465 | Erro Rel Médio: 1112.51% | Variância: 11837206.39%
* **T2:** 1 época | EQM: 0.494515 | Erro Rel Médio: 1112.55% | Variância: 11838093.05%
* **T3:** 1 época | EQM: 0.494515 | Erro Rel Médio: 1112.55% | Variância: 11838093.38%
*(Nota: A Rede 3 divergiu rapidamente, parando na primeira época de forma prematura devido às limitações do Backpropagation Padrão nessa configuração mais densa).*

### 4. Gráficos de Erro Quadrático Médio (EQM)

Os gráficos com a curva de aprendizado (EQM) para a melhor execução de cada Rede foram gerados e salvos com o nome `graficos_eqm_pmc3.png`.

### 5. Gráficos de Predição (Desejado vs Estimado)

Os gráficos sobrepondo as curvas dos valores originais com a predição feita pelas redes na etapa de Teste (t = 101 a 120) foram salvos em `graficos_predicao_pmc3.png`.

### 6. Qual topologia candidata e configuração final seria a mais adequada?

Para um mapeamento fiel de "Time Delay" com melhor predição de preços de ações, avalia-se o comportamento nas amostras de `t=101` a `120`. A melhor Rede (Topologia 1, 2 ou 3) juntamente do seu melhor treinamento (T1, T2 ou T3) será aquela em que a curva gerada pela predição das amostras de Teste se aproxime ou sobreponha perfeitamente sobre a curva Desejada (`f(t)` real) no gráfico gerado. Quantitativamente, deve ser escolhida a Rede que acusar o **menor Erro Relativo Médio (MRE)** durante os ensaios sobre as novas amostras (t = 101...120).

### 7. Principais características e vantagens de variantes do Backpropagation:

#### a. Algoritmo de treinamento Resilient-Propagation (RProp)
O RProp é um método heurístico que modifica a atualização dos pesos da rede considerando estritamente o **sinal do gradiente (positivo ou negativo)** da função de erro em relação aos pesos, mas ignorando a sua magnitude.
*   **Vantagem principal:** Resolve com sucesso o problema do desaparecimento de gradiente (vanishing gradient) — muito comum ao utilizar funções sigmoides — pois o tamanho da atualização dos pesos varia adaptativamente, não ficando excessivamente pequeno nas caudas assintóticas da função de ativação. Com isso, provê uma excelente taxa de convergência e dispensa a necessidade do projetista sintonizar a taxa de aprendizado e o termo momentum, já que ele atualiza as taxas individualmente por cada conexão.

#### b. Algoritmo de treinamento Levenberg-Marquardt (LM)
O Levenberg-Marquardt (LM) é uma mistura sofisticada do método iterativo Gauss-Newton com o método do gradiente descendente. Ele foi concebido para se aproximar à velocidade ótima das soluções de aproximação de segunda ordem sem a obrigação custosa de calcular efetivamente a matriz Hessiana. Ele faz isso computando a matriz Jacobiana (primeira derivada da rede com relação aos parâmetros), o que acarreta em passos computacionais menores.
*   **Vantagem principal:** É frequentemente considerado o **algoritmo mais veloz** para o treinamento prático de Redes Neurais de pequeno a médio porte em diversas aplicações. Sua principal vantagem é possuir uma robustez considerável à divergência (como no Gradiente Descendente) somada à rápida convergência das abordagens de segunda ordem (como no método Gauss-Newton). Seu trade-off ocorre no maior uso de memória, necessário para armazenar a matriz Jacobiana a cada época de treinamento.
