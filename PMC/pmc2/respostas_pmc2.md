# Respostas do Trabalho de PMC 2 - Classificadora de Padrões (Conservantes de Bebidas)

### 1. Resultados dos Treinamentos (Padrão vs Momentum)

Após executar os treinamentos da rede neural com Backpropagation Padrão e com a adição da constante de *Momentum* (0.9), obtivemos os seguintes resultados:

| Algoritmo | Número de Épocas | Tempo de Execução (s) | Acerto (Acurácia) na Classificação |
|---|---|---|---|
| **Backpropagation Padrão** | 27832 | 9.87s | 100.0% |
| **Backpropagation com Momentum (0.9)** | 5616 | 1.93s | 100.0% |

### 2. Gráfico Comparativo do Erro Quadrático Médio (EQM)

O gráfico comparando a convergência do erro (EQM) entre os dois algoritmos ao longo das épocas foi gerado e salvo como `grafico_eqm_pmc2.png`.

### 3. Discussão sobre a influência do termo *Momentum*

A execução do treinamento evidencia, via gráfico e contagem de tempo, a diferença fundamental da adição da constante de *Momentum* ao algoritmo Backpropagation. Observa-se que o termo *Momentum* ($\alpha = 0.9$) auxilia fortemente o algoritmo a ultrapassar platôs e escapar de mínimos locais, mantendo a inércia da direção de descida na superfície de erro. 

Como resultado direto, a rede com Momentum chega ao critério de parada estabelecido em um **número consideravelmente menor de épocas** (redução de aproximadamente 80%), acelerando de forma significativa o tempo de processamento. Ao final, as funções de ativação e limiares determinam com 100% de acurácia, para ambas as técnicas, as saídas desejadas do problema e o respectivo conservante (`A, B` ou `C`).
