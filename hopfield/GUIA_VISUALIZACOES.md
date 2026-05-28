# 🖼️ GUIA DE INTERPRETAÇÃO DAS VISUALIZAÇÕES

## Estrutura Geral das Imagens

Todas as imagens usam a mesma codificação:
- **Preto/Escuro:** Pixel = +1 (foreground)
- **Branco/Claro:** Pixel = -1 (background)

---

## 1. hopfield_recuperacao_completa.png

### O que é:
Matriz 12×3 mostrando as 12 simulações completas

### Layout:
```
┌─────────────────┬──────────────────┬──────────────────┐
│  ORIGINAL       │  COM RUÍDO       │  RECUPERADO      │
├─────────────────┼──────────────────┼──────────────────┤
│ Padrão Original │ 9 pixels corrupto │ 0 pixels erro    │ ← Sim. 1 (L)
│ 0% erro         │ (20%)            │ ✓ SUCESSO        │
├─────────────────┼──────────────────┼──────────────────┤
│ ...             │ ...              │ ...              │
│ (12 linhas)     │                  │                  │
└─────────────────┴──────────────────┴──────────────────┘
```

### Interpretação por Coluna:
- **Coluna 1 (Original):** Padrão sem erro
- **Coluna 2 (Com Ruído):** Alguns pixels invertidos
- **Coluna 3 (Recuperado):** Resultado do algoritmo

### Cores no Título:
- ✓ verde = Recuperação perfeita
- ✗ vermelho = Falha na recuperação

### Usar para:
- Visão global de todas as 12 simulações
- Comparar padrões diferentes
- Avaliar taxa de sucesso

---

## 2. hopfield_padrao_[L|T|O|X].png

### O que é:
Detalhamento de um padrão específico (3 simulações)

### Layout (para cada padrão):
```
Simulação 1  ┌─────────────┬──────────────┬─────────────────┐
             │  Original   │  Com Ruído   │  Recuperado     │
             │             │ (9 pixels)   │ (0 pixels erro) │
             └─────────────┴──────────────┴─────────────────┘

Simulação 2  ┌─────────────┬──────────────┬─────────────────┐
             │  Original   │  Com Ruído   │  Recuperado     │
             │             │ (9 pixels)   │ (0 pixels erro) │
             └─────────────┴──────────────┴─────────────────┘

Simulação 3  ┌─────────────┬──────────────┬─────────────────┐
             │  Original   │  Com Ruído   │  Recuperado     │
             │             │ (9 pixels)   │ (9 pixels erro) │
             └─────────────┴──────────────┴─────────────────┘
```

### Leitura:
- **Linha 1:** Primeira simulação do padrão
- **Linha 2:** Segunda simulação do padrão
- **Linha 3:** Terceira simulação do padrão

### Observações:
- Padrão L, T, O: 3/3 recuperações perfeitas
- Padrão X: 2/3 recuperações perfeitas (Sim. 2 falhou)

### Usar para:
- Entender detalhe de cada padrão
- Ver repetibilidade
- Identificar qual simulação falhou

---

## 3. analise_ruido.png

### O que é:
Gráfico mostrando taxa de sucesso vs nível de ruído

### Formato:
```
Taxa de Sucesso (%)
    100% ┌─────────────────────────┐
         │ ✓ Zona excelente (0-20%)│
         │                     ╲   │
     80% │     ┌─────────────────╲─┤
         │     │ ~ Zona marginal  ╲│
     60% │     │  (20-35%)    ╲   │
         │     │              ╲   │
     40% │     │               ╲  │
         │     │ ✗ Zona crítica  ╲│
     20% │     │   (35-50%)      ╲ ─ ← Linha 50% (ponto crítico)
         │     │                  │╲
      0% └─────┴────────────────── │ ──────
           0   10   20   30   40   50
                Nível de Ruído (%)
```

### O que significa cada zona:

#### ✓ Zona Verde (0-20%): Excelente
- Taxa de sucesso: 90-100%
- Padrão distorcido bem dentro da bacia de atração
- **Recomendação:** Use neste nível

#### ~ Zona Amarela (20-35%): Marginal
- Taxa de sucesso: 60-90%
- Padrão próximo aos limites da bacia
- **Recomendação:** Use com cuidado, implemente códigos de erro

#### ✗ Zona Vermelha (35-50%): Crítico
- Taxa de sucesso: 0-60%
- Padrão frequentemente fora da bacia
- **Recomendação:** NÃO use neste regime

#### ✗ Zona Preta (>50%): Impossível
- Taxa de sucesso: 0%
- Informação completamente perdida
- **Recomendação:** Impossível recuperar

### Leitura Prática:
```
Ruído de 20%: 100% sucesso        ✓ OK
Ruído de 30%: 90% sucesso         ~ Marginal
Ruído de 40%: 10% sucesso         ✗ Ruim
Ruído de 50%: 0% sucesso          ✗ Impossível
```

### Usar para:
- Entender limites da rede
- Avaliar tolerância a ruído
- Decidir aplicabilidade

---

## Como Interpretar os Padrões Visualmente

### Padrão "L" (Letra L)
```
Esperado:           Com ruído:          Recuperado:
█ · · · ·           █ · █· ·           █ · · · ·
█ · · · ·           █ · · · ·           █ · · · ·
█ · · · ·           █ █ · · ·           █ · · · ·
█ · · · ·           █ · · · ·           █ · · · ·
█ · · · ·           █ · · · █           █ · · · ·
█ · · · ·           █ · · · ·           █ · · · ·
█ · · · ·           █ · · · ·           █ · · · ·
█ █ █ █ ·           █ █ █ █ ·           █ █ █ █ ·
█ █ █ █ ·           █ █ █ █ █           █ █ █ █ ·
(Perfeito)          (9 pixels errados)  (Perfeito!) ✓
```

### Como Ler:
- Conte os pixels pretos (█) e brancos (·) diferentes
- Se recuperado = original, então ✓ sucesso
- Se recuperado ≠ original, então ✗ falha

---

## Padrão X - Simulação que Falhou (Simulação 11)

### Visualização da Falha:
```
Original:           Com Ruído:          Recuperado:
█ · · · █           █ █ · · █           █ · · █ █
█ · · · █           █ · · · █           █ · · · █
█ · · · █           █ · · · █           · · · · █
· █ · █ ·           · █ ██ ·            · █ · █ ·
· █ █ █ ·           · █ █ █ █           · █ █ █ ·
· █ · █ ·           · █ · █ ·           · █ · █ ·
█ · · · █           █ · · · █           █ · █ · █
█ · · · █           █ · · ··█           █ · · · █
█ · · · █           █ · · · █           █ · · · █
(Perfeito)          (9 pixels)          (9 pixels!) ✗
```

### Por que Falhou?
- O padrão distorcido caiu fora da bacia de atração
- A rede convergiu para um estado diferente do original
- Exemplifica a variabilidade em ~8% dos casos com 20% de ruído

---

## Testes Adicionais (Pasta `testes/`)

### teste_recuperacao_interativa.png

Mostra a **convergência iterativa** de um padrão:

```
Original | Com Ruído | Iter.1 | Iter.2 | Iter.5 | Iter.10 | Iter.20 | Iter.50
───────────────────────────────────────────────────────────────────────
  O      |    O      |   O    |   O    |   O    |   O     |   O     |   O
(Perfeito)(9 erros)   (5 er)  (2 er)  (0 er)  (0 er)   (0 er)   (0 er)
```

**Significado:** Mostra que a rede converge em poucas iterações (típico: 5-50)

### comparacao_padroes.png

Compara os 4 padrões lado-a-lado com 20% de ruído.

### teste_padrao_O.png

Mostra 5 testes repetidos do padrão O (demonstra reproducibilidade).

---

## Interpretação de Erros

### Se você vir padrão errado recuperado:

1. **Não é bug do programa** - Fenômeno esperado!
2. **Significa:** O padrão distorcido estava próximo a outro padrão na rede
3. **Frequência:** ~8% com 20% de ruído
4. **Razão:** Existe um fenômeno chamado "crosstalk" entre padrões

### Se todos falharem:

1. Verifique se está usando os dados corretos
2. Pode ser ruído > 40%
3. Execute novamente (há aleatoriedade)

---

## Escala de Cinza

Todas as imagens usam mapa de cores "gray":

```
█████████  (100% preto)        = +1 (foreground)
░░░░░░░░░  (50% cinza)         = estados intermediários
·········  (100% branco)       = -1 (background)
```

O preto é o valor +1 (escuro) e branco é -1 (claro).

---

## Dicas para Interpretar

### Rapidamente:
1. Abra `hopfield_recuperacao_completa.png`
2. Procure por padrões diferentes nas colunas 2 e 3
3. Se forem iguais → ✓ Sucesso
4. Se forem diferentes → ✗ Falha

### Com mais Detalhe:
1. Abra `hopfield_padrao_X.png` (X = L, T, O ou X)
2. Leia cada linha
3. Compare coluna 1 (original) com coluna 3 (recuperado)
4. Procure por discrepâncias (pixels diferentes)

### Entender o Comportamento:
1. Abra `analise_ruido.png`
2. Veja onde a curva cai
3. Identifique zonas críticas
4. Compreenda o ponto de colapso em 50%

---

## Perguntas Frequentes Visuais

### "Por que nem sempre o padrão com ruído parece distorcido?"

A imagem original é 9×5 pixels. Com 20% de ruído (9 pixels), muitos pixels continuam corretos. Se os 9 corrompidos estiverem distribuídos, pode não parecer muito diferente visualmente.

### "Por que a Simulação 11 do padrão X falhou?"

A rede tem basins of attraction (bacias de atração). O padrão distorcido caiu fora ou no limite da bacia do padrão X. Isto acontece aleatoriamente em ~8% dos casos.

### "Como 9 pixels errados podem se tornar 0?"

A rede de Hopfield é uma máquina de correção de erro. Ela "conhece" os padrões e consegue recuperá-los mesmo com alguns erros, usando a dinâmica da rede.

---

## Para Imprimir ou Apresentar

**Recomendação de Ordem:**

1. Abra `hopfield_recuperacao_completa.png` (visão geral)
2. Explique `analise_ruido.png` (comportamento)
3. Detalhes em `hopfield_padrao_X.png` (padrões específicos)
4. Falha em `hopfield_padrao_X.png` linha 11 (exceção)
5. Convergência em `testes/teste_recuperacao_interativa.png` (dinâmica)

---

**Última Atualização:** 28 de maio de 2026

