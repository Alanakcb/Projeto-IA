# Projeto Redes Neurais: Perceptron, Adaline e PMC

## Introdução
Este repositório contém a implementação em Python de três modelos clássicos de Redes Neurais Artificiais (Perceptron, Adaline e Multi-Layer Perceptron - PMC), resolvendo diferentes problemas de aproximação de funções, classificação de padrões e previsão de séries temporais (TDNN).

A estrutura do projeto separa a lógica de Core (regras de atualização, algoritmos estocásticos e batch em NumPy) da View (interfaces com CustomTkinter/Tkinter e relatórios Markdown), seguindo boas práticas de acoplamento, tipagem e vetorização de operações tensoriais com a biblioteca `numpy`.

## Análise de Convergência (Gráficos de EQM)
A convergência do aprendizado em nossos modelos (Adaline e PMC) pode ser verificada claramente nos gráficos de Erro Quadrático Médio (EQM). 
Ao longo das épocas (eixos horizontais), nota-se o decaimento exponencial do EQM (eixo vertical) em direção a valores muito próximos de zero, estacionando quando atingem o limiar da precisão definida (ex: $10^{-6}$). Em topologias densas com hiperparâmetros ajustados, variações como o fator *Momentum* (no PMC) demonstram uma aceleração dramática dessa convergência, diminuindo a oscilação na descida do gradiente.

## Estabilidade dos Pesos (Adaline)
Para o Adaline, nota-se uma estabilidade notável: mesmo com diferentes sementes de inicialização aleatória para os pesos no tempo $t=0$, os modelos finais (após $n$ épocas de aprendizado guiadas pela Regra Delta) convergem para praticamente as mesmas matrizes de pesos. 
Isso se deve à superfície de Erro Quadrático da regra linear, que assume a forma de um paraboloide com um único mínimo global. Diferente de superfícies não-lineares repletas de mínimos locais, a Regra Delta fatalmente descerá até o ponto global ótimo, tornando o vetor de pesos finais um ponto de estabilidade independentemente do caminho (número de épocas).

## Algoritmos Alternativos de Otimização: A Importância do RProp
Embora o Gradiente Descendente Padrão (com ou sem Momentum) tenha sido suficiente para a maioria das tarefas propostas, problemas variantes no tempo (como a predição TDNN do PMC3) frequentemente revelam limitações (como convergências prematuras ou passos muito pequenos nas caudas das funções sigmoides).

O **RProp (Resilient Propagation)** surge como um avanço direto ao Backpropagation clássico. Em vez de depender do *valor* numérico absoluto (magnitude) do gradiente para determinar o tamanho do passo na atualização dos pesos — o que causa lentidão quando os gradientes somem (Vanishing Gradient) —, o RProp considera apenas o **sinal da derivada** (positivo ou negativo). 
A taxa de aprendizado torna-se dinâmica e independente para cada conexão de peso (diminuindo o passo se o sinal oscilar bruscamente, e aumentando o passo se o sinal se mantiver), eliminando a necessidade empírica e custosa de sintonizarmos manualmente os hiperparâmetros de $\eta$ (taxa de aprendizado global) e $\alpha$ (Momentum) para garantir a estabilidade.
