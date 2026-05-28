# Rede de Hopfield - Sistema de Recuperação de Padrões com Ruído

## Descrição

Este projeto implementa uma rede de Hopfield com 45 neurônios para armazenar e recuperar 4 padrões diferentes de imagens (9×5 pixels) que foram corrompidas durante transmissão por ruído aleatório.

### Especificações

- **Tipo de rede:** Hopfield (memória associativa)
- **Número de neurônios:** 45 (correspondendo a imagens 9×5)
- **Padrões armazenados:** 4 (letras: L, T, O, X)
- **Função de ativação:** Tangente hiperbólica com β = 100 (aproxima função degrau)
- **Regra de treinamento:** Produto externo (Hebbian)
- **Nível de ruído testado:** 20% de pixels corrompidos

## Estrutura do Projeto

```
hopfield/
├── hopfield.py                    # Implementação principal da rede de Hopfield
├── respostas_hopfield.md         # Documentação completa e análise dos resultados
├── README.md                      # Este arquivo
└── resultados/                    # Pasta com as visualizações (criada ao executar)
    ├── hopfield_recuperacao_completa.png
    ├── hopfield_padrao_L.png
    ├── hopfield_padrao_T.png
    ├── hopfield_padrao_O.png
    ├── hopfield_padrao_X.png
    └── analise_ruido.png
```

## Requisitos

```
numpy>=1.20.0
matplotlib>=3.4.0
```

## Como Executar

### 1. Instalar Dependências

```bash
pip install numpy matplotlib
```

### 2. Executar o Script Principal

```bash
python hopfield.py
```

### O que o Script Faz

1. **Treina a rede de Hopfield** com 4 padrões usando a regra do produto externo
2. **Executa 12 simulações** (3 para cada padrão):
   - Simula transmissão com 20% de ruído (corrompimento aleatório de pixels)
   - Apresenta o padrão distorcido à rede
   - A rede recupera o padrão original através de iterações
   - Mostra estatísticas de recuperação
3. **Testa diferentes níveis de ruído** (0% a 50%) para analisar capacidade da rede
4. **Gera visualizações** em alta resolução (150 DPI)

## Saída do Programa

### Saída no Console

```
================================================================================
REDE DE HOPFIELD PARA RECUPERAÇÃO DE PADRÕES
================================================================================

Treinamento concluído com 4 padrões de 45 neurônios

Simulando 12 transmissões (3 para cada padrão)...

================================================================================
PADRÃO 1: 'L'
================================================================================

Simulação 1/12 - Padrão 'L' (teste 1)
--------------------------------------------------------------------------------
Pixels corrompidos: 9/45 (20.0%)
Pixels com erro após recuperação: 0/45 (0.0%)
✓ Padrão recuperado com SUCESSO!

...

================================================================================
ANÁLISE: EFEITO DO NÍVEL DE RUÍDO NA RECUPERAÇÃO
================================================================================

Ruído     Sucesso        Taxa de Acerto
--------------------------------------------------------------------------------
  0%      10/10          100.0%          ✓
  5%      10/10          100.0%          ✓
 10%      10/10          100.0%          ✓
 15%      10/10          100.0%          ✓
 20%      10/10          100.0%          ✓
 25%       9/10           90.0%          ~
 30%       7/10           70.0%          ~
 35%       3/10           30.0%          ✗
 40%       1/10           10.0%          ✗
 50%       0/10            0.0%          ✗

✓ Gráfico salvo: resultados/analise_ruido.png

================================================================================
SIMULAÇÕES CONCLUÍDAS COM SUCESSO!
================================================================================

Arquivos gerados:
  - resultados/hopfield_recuperacao_completa.png
  - resultados/hopfield_padrao_L.png
  - resultados/hopfield_padrao_T.png
  - resultados/hopfield_padrao_O.png
  - resultados/hopfield_padrao_X.png
  - resultados/analise_ruido.png
```

## Visualizações Geradas

### 1. `hopfield_recuperacao_completa.png`
Figura com todas as 12 simulações em uma única imagem (formato 12×3):
- Coluna 1: Padrão original
- Coluna 2: Padrão com ruído (20%)
- Coluna 3: Padrão recuperado

### 2. `hopfield_padrao_X.png` (X = L, T, O, X)
Para cada padrão, uma figura com as 3 simulações:
- Linha 1-3: Cada simulação
- Coluna 1: Original
- Coluna 2: Com ruído
- Coluna 3: Recuperado

### 3. `analise_ruido.png`
Gráfico mostrando a taxa de sucesso em função do nível de ruído:
- X: Nível de ruído (%)
- Y: Taxa de sucesso (%)
- Linha vermelha: Ponto crítico (50%)

## Detalhes da Implementação

### Classe `HopfieldNetwork`

#### Método `train(patterns)`
Treina a rede armazenando os padrões usando a regra do produto externo.

```python
W = (1/p) * Σ(x ⊗ x) para cada padrão x
```

Onde ⊗ representa produto externo e p é o número de padrões.

#### Método `activate(input_pattern, iterations, beta)`
Recupera o padrão através de iterações da dinâmica:

```python
h = W @ x (entrada ponderada)
x_novo = sign(tanh(β * h))
```

Itera até convergência ou número máximo de iterações.

#### Método `add_noise(pattern, noise_percentage)`
Corrompe aleatoriamente um percentual dos pixels do padrão (inverte -1↔+1).

### Padrões Armazenados

Definem 4 padrões diferentes em formato 9×5 (45 bits):
- **Padrão 1 (L):** Letra L
- **Padrão 2 (T):** Letra T
- **Padrão 3 (O):** Letra O (círculo)
- **Padrão 4 (X):** Letra X

Codificação:
- Pixel branco (background): -1
- Pixel escuro (foreground): +1

## Resultados Esperados

### Com 20% de Ruído

- **Taxa de Recuperação:** 100% (12/12 simulações com sucesso)
- **Velocidade de Convergência:** 20-50 iterações em média
- **Padrões Recuperados:** Todos os 4 padrões sem erro

### Com Diferentes Níveis de Ruído

| Ruído | Taxa de Sucesso | Comportamento |
|-------|-----------------|--|
| 0-20% | 90-100% | ✓ Recuperação perfeita |
| 20-35% | 30-90% | ~ Recuperação parcial |
| 35-50% | 0-30% | ✗ Recuperação muito precária |
| >50% | 0% | ✗ Falha total |

## Análise: Por que Falha com Ruído Excessivo?

A rede de Hopfield tem capacidade limitada de recuperação que depende de:

1. **Tamanho da bacia de atração:** Cada padrão tem uma região no espaço de estados da qual pode ser recuperado.

2. **Limite de capacidade:** Aproximadamente 0.138 × N padrões podem ser armazenados sem erro (para N = 45 ≈ 6 padrões máximo).

3. **Crosstalk:** Com muito ruído, os padrões se "misturam" e a rede não consegue desambiguar qual é o padrão original.

4. **Padrões espúrios:** Com ruído > 40%, a rede pode convergir para estados não treinados (atratores espúrios).

Para ruído > 50%, a recuperação se torna impossível pois a informação original é completamente perdida.

## Possíveis Melhorias

1. **Aumentar β:** Aproximar mais a tangente hiperbólica de uma função degrau
2. **Dinâmica assíncrona:** Atualizar neurônios um por um em vez de simultaneamente
3. **Técnicas de correção de erro:** Adicionar bits de paridade ou códigos de Hamming
4. **Redes mais avançadas:** Boltzmann Machines, redes convolucionais, etc.
5. **Pré-processamento:** Aplicar filtros de denoising antes de apresentar à rede

## Referências

- Hopfield, J. J. (1982). "Neural networks and physical systems with emergent collective computational abilities". Proceedings of the National Academy of Sciences.
- Hertz, J., Krogh, A., Palmer, R. G. (1991). "Introduction to the Theory of Neural Computation". Addison-Wesley.

## Autor

Implementação para a disciplina de Laboratório de Inteligência Artificial
Centro Federal de Educação Tecnológica de Minas Gerais
Campus VIII – Varginha

## Licença

Este projeto é fornecido como material educacional.
