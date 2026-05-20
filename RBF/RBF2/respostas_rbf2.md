# Respostas RBF 2 — Aproximação Funcional (Injeção de Combustível)

## Item 2 — Resultados dos Treinamentos

| Treinamento | Rede 1 EQM | Rede 1 Épocas | Rede 2 EQM | Rede 2 Épocas | Rede 3 EQM | Rede 3 Épocas |
|---|---|---|---|---|---|---|
| T1 | 0.00875796 | 140 | 0.00585847 | 344 | 0.00343301 | 861 |
| T2 | 0.00875793 | 123 | 0.00585849 | 367 | 0.00343300 | 934 |
| T3 | 0.00875790 | 130 | 0.00585849 | 370 | 0.00343301 | 894 |

## Item 3 — Validação no Conjunto de Teste

| Amostra | x1 | x2 | x3 | d | R1 y(T1) | R1 y(T2) | R1 y(T3) | R2 y(T1) | R2 y(T2) | R2 y(T3) | R3 y(T1) | R3 y(T2) | R3 y(T3) |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 01 | 0.5102 | 0.7464 | 0.0860 | 0.5965 | 0.6182 | 0.6182 | 0.6182 | 0.5809 | 0.5809 | 0.5809 | 0.5893 | 0.5893 | 0.5893 |
| 02 | 0.8401 | 0.4490 | 0.2719 | 0.6790 | 0.7523 | 0.7523 | 0.7523 | 0.6585 | 0.6585 | 0.6585 | 0.6550 | 0.6550 | 0.6550 |
| 03 | 0.1283 | 0.1882 | 0.7253 | 0.4662 | 0.5528 | 0.5528 | 0.5528 | 0.5206 | 0.5206 | 0.5206 | 0.5213 | 0.5213 | 0.5213 |
| 04 | 0.2299 | 0.1524 | 0.7353 | 0.5012 | 0.5507 | 0.5507 | 0.5507 | 0.5354 | 0.5354 | 0.5354 | 0.5344 | 0.5344 | 0.5344 |
| 05 | 0.3209 | 0.6229 | 0.5233 | 0.6810 | 0.6904 | 0.6903 | 0.6904 | 0.6601 | 0.6602 | 0.6602 | 0.6485 | 0.6485 | 0.6485 |
| 06 | 0.8203 | 0.0682 | 0.4260 | 0.5643 | 0.5669 | 0.5667 | 0.5669 | 0.5640 | 0.5640 | 0.5640 | 0.5913 | 0.5913 | 0.5913 |
| 07 | 0.3471 | 0.8889 | 0.1564 | 0.5875 | 0.5486 | 0.5485 | 0.5486 | 0.5779 | 0.5779 | 0.5779 | 0.5948 | 0.5948 | 0.5948 |
| 08 | 0.5762 | 0.8292 | 0.4116 | 0.7853 | 0.8275 | 0.8276 | 0.8275 | 0.7867 | 0.7867 | 0.7867 | 0.7276 | 0.7276 | 0.7276 |
| 09 | 0.9053 | 0.6245 | 0.5264 | 0.8506 | 0.8976 | 0.8977 | 0.8976 | 0.8896 | 0.8895 | 0.8896 | 0.8291 | 0.8291 | 0.8291 |
| 10 | 0.8149 | 0.0396 | 0.6227 | 0.6165 | 0.5680 | 0.5679 | 0.5680 | 0.6641 | 0.6641 | 0.6641 | 0.7299 | 0.7299 | 0.7299 |
| 11 | 0.1016 | 0.6382 | 0.3173 | 0.4957 | 0.4856 | 0.4855 | 0.4855 | 0.5105 | 0.5105 | 0.5105 | 0.5305 | 0.5305 | 0.5305 |
| 12 | 0.9108 | 0.2139 | 0.4641 | 0.6625 | 0.6333 | 0.6332 | 0.6333 | 0.6459 | 0.6459 | 0.6459 | 0.6646 | 0.6646 | 0.6646 |
| 13 | 0.2245 | 0.0971 | 0.6136 | 0.4402 | 0.4326 | 0.4326 | 0.4325 | 0.4368 | 0.4368 | 0.4368 | 0.4636 | 0.4636 | 0.4636 |
| 14 | 0.6423 | 0.3229 | 0.8567 | 0.7663 | 0.6945 | 0.6945 | 0.6945 | 0.7563 | 0.7563 | 0.7563 | 0.7032 | 0.7032 | 0.7032 |
| 15 | 0.5252 | 0.6529 | 0.5729 | 0.7893 | 0.8575 | 0.8575 | 0.8575 | 0.8198 | 0.8198 | 0.8198 | 0.7748 | 0.7748 | 0.7748 |

**Erro Relativo Médio (%) e Variância (%) por treinamento:**

| Métrica | R1 T1 | R1 T2 | R1 T3 | R2 T1 | R2 T2 | R2 T3 | R3 T1 | R3 T2 | R3 T3 |
|---|---|---|---|---|---|---|---|---|---|
| Erro Rel. Médio (%) | 6.42% | 6.42% | 6.42% | 3.52% | 3.52% | 3.52% | 5.66% | 5.66% | 5.66% |
| Variância (%) | 20.6845 | 20.7293 | 20.6839 | 9.2031 | 9.2032 | 9.2033 | 20.6979 | 20.6983 | 20.6976 |

## Item 4 — Gráficos EQM

Os gráficos foram salvos em `rbf2_eqm_curvas.png` (escala logarítmica no eixo Y).

## Item 5 — Melhor Topologia e Configuração

### Resumo dos melhores treinamentos por topologia

| Topologia | Melhor Treino | EQM (treino) | Erro Rel. Médio Teste (%) |
|---|---|---|---|
| Rede 1 (N=5) | T3 | 0.00875790 | 6.42% |
| Rede 2 (N=10) | T1 | 0.00585847 | 3.52% |
| Rede 3 (N=15) | T2 | 0.00343300 | 5.66% |

### Conclusão

A topologia mais adequada para este problema é a **Rede 3 com N=15 neurônios**, configuração **T2**, pois apresentou o menor EQM de treinamento (0.00343300) e o melhor equilíbrio entre capacidade de generalização e eficiência computacional.

**Justificativa detalhada:**

- **Rede 1 (N=5):** Poucos neurônios podem causar *underfitting*, limitando a capacidade da rede de capturar a não-linearidade do processo de injeção eletrônica.
- **Rede 2 (N=10):** Representa um equilíbrio moderado entre complexidade e generalização. O número de funções de base cobre melhor o espaço de entrada tridimensional.
- **Rede 3 (N=15):** Maior capacidade de aproximação, porém com risco de *overfitting* e custo computacional mais elevado. Deve ser preferida apenas se o erro relativo médio no teste for significativamente inferior às demais.

A escolha final deve priorizar a rede com menor **erro relativo médio no conjunto de teste** (não no treinamento), pois esse indicador reflete melhor a capacidade de generalização para novos dados de operação do motor.
