"""
Rede de Hopfield para recuperação de padrões de imagens
Implementação de uma memória associativa com 45 neurônios
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from typing import Tuple, List
import os

class HopfieldNetwork:
    """
    Rede de Hopfield para armazenamento e recuperação de padrões
    """
    
    def __init__(self, num_neurons: int = 45):
        """
        Inicializa a rede de Hopfield
        
        Args:
            num_neurons: Número de neurônios (45 para imagens 9x5)
        """
        self.num_neurons = num_neurons
        self.weights = None
        self.patterns = None
        
    def train(self, patterns: np.ndarray):
        """
        Treina a rede com os padrões usando a regra do produto externo
        
        Args:
            patterns: Array de forma (num_patterns, num_neurons)
                     Valores devem ser -1 (branco) ou +1 (escuro)
        """
        self.patterns = patterns
        num_patterns = patterns.shape[0]
        
        # Inicializa matriz de pesos com zeros
        self.weights = np.zeros((self.num_neurons, self.num_neurons))
        
        # Aplica a regra do produto externo para cada padrão
        for pattern in patterns:
            self.weights += np.outer(pattern, pattern)
        
        # Define diagonal como zero (sem auto-conexões)
        np.fill_diagonal(self.weights, 0)
        
        # Normaliza pelos pesos
        self.weights = self.weights / num_patterns
        
    def activate(self, input_pattern: np.ndarray, iterations: int = 100, 
                 beta: float = 100.0) -> np.ndarray:
        """
        Ativa a rede e recupera o padrão
        
        Args:
            input_pattern: Padrão de entrada (distorcido)
            iterations: Número de iterações
            beta: Parâmetro de inclinação da tangente hiperbólica (muito grande)
        
        Returns:
            Padrão recuperado
        """
        state = input_pattern.copy()
        
        for _ in range(iterations):
            # Calcula a entrada ponderada: h = W @ x
            h = np.dot(self.weights, state)
            
            # Aplica tangente hiperbólica com β muito grande
            # Quando β → ∞, tanh(β*h) → sign(h)
            new_state = np.tanh(beta * h)
            
            # Quantiza para -1 ou +1
            new_state = np.sign(new_state)
            new_state[new_state == 0] = 1  # Trata zeros como +1
            
            # Verifica convergência
            if np.array_equal(new_state, state):
                break
            
            state = new_state
        
        return state
    
    def add_noise(self, pattern: np.ndarray, noise_percentage: float = 0.2) -> np.ndarray:
        """
        Adiciona ruído aleatório a um padrão
        
        Args:
            pattern: Padrão original
            noise_percentage: Percentual de pixels a corromper (default 20%)
        
        Returns:
            Padrão com ruído
        """
        noisy_pattern = pattern.copy()
        num_corrupted = int(self.num_neurons * noise_percentage)
        
        # Seleciona índices aleatórios para corrupção
        corrupted_indices = np.random.choice(self.num_neurons, 
                                            num_corrupted, 
                                            replace=False)
        
        # Inverte os bits nos índices selecionados
        noisy_pattern[corrupted_indices] *= -1
        
        return noisy_pattern


def create_patterns() -> np.ndarray:
    """
    Cria 4 padrões diferentes em formato 9x5 (45 bits)
    Representam os números: 1, 2, 3, 4
    -1 = pixel branco (background)
    +1 = pixel escuro (foreground)
    """
    
    # Padrão 1: Número "1" (desespelhado)
    pattern1 = np.array([
        -1, -1, +1, -1, -1,  # linha 1
        -1, -1, +1, +1, -1,  # linha 2
        -1, -1, +1, -1, -1,  # linha 3
        -1, -1, +1, -1, -1,  # linha 4
        -1, -1, +1, -1, -1,  # linha 5
        -1, -1, +1, -1, -1,  # linha 6
        -1, -1, +1, -1, -1,  # linha 7
        -1, +1, +1, +1, -1,  # linha 8
        -1, +1, +1, +1, -1,  # linha 9
    ], dtype=np.float32)
    
    # Padrão 2: Número "2" (desespelhado)
    pattern2 = np.array([
        -1, +1, +1, +1, -1,  # linha 1
        +1, +1, -1, +1, +1,  # linha 2
        +1, +1, -1, -1, -1,  # linha 3
        -1, +1, +1, -1, -1,  # linha 4
        -1, -1, +1, +1, -1,  # linha 5
        -1, -1, -1, +1, +1,  # linha 6
        -1, -1, -1, -1, +1,  # linha 7
        +1, +1, +1, +1, +1,  # linha 8
        +1, +1, +1, +1, +1,  # linha 9
    ], dtype=np.float32)
    
    # Padrão 3: Número "3"
    pattern3 = np.array([
        +1, +1, +1, +1, -1,  # linha 1
        +1, +1, -1, +1, +1,  # linha 2
        -1, -1, -1, +1, +1,  # linha 3
        -1, +1, +1, +1, -1,  # linha 4
        -1, -1, -1, +1, +1,  # linha 5
        +1, +1, -1, +1, +1,  # linha 6
        +1, +1, -1, +1, +1,  # linha 7
        +1, +1, +1, +1, -1,  # linha 8
        -1, +1, +1, +1, -1,  # linha 9
    ], dtype=np.float32)
    
    # Padrão 4: Número "4" (corrigido - virado para cima)
    pattern4 = np.array([
        +1, -1, -1, +1, -1,  # linha 1
        +1, -1, -1, +1, -1,  # linha 2
        +1, -1, -1, +1, -1,  # linha 3
        +1, -1, -1, +1, -1,  # linha 4
        +1, +1, +1, +1, +1,  # linha 5 (horizontal no meio)
        +1, +1, +1, +1, +1,  # linha 6 (horizontal no meio)
        -1, -1, -1, +1, -1,  # linha 7
        -1, -1, -1, +1, -1,  # linha 8
        -1, -1, -1, +1, -1,  # linha 9
    ], dtype=np.float32)
    
    return np.array([pattern1, pattern2, pattern3, pattern4])


def visualize_pattern(pattern: np.ndarray, title: str = "Padrão", ax=None) -> None:
    """
    Visualiza um padrão como grade de pixels/células
    
    Args:
        pattern: Padrão de 45 bits
        title: Título da visualização
        ax: Eixo matplotlib
    """
    if ax is None:
        fig, ax = plt.subplots(figsize=(4, 6))
    
    # Reshape para 9x5
    image = pattern.reshape(9, 5)
    
    # Normaliza para 0-1 para visualização
    # -1 (branco) → 1 (branco)
    # +1 (preto) → 0 (preto)
    image_display = (1 - image) / 2  # +1→0 (preto), -1→1 (branco)
    
    # Exibe com interpolação nearest para manter aparência de grade
    ax.imshow(image_display, cmap='gray', interpolation='nearest', extent=[0, 5, 0, 9])
    
    # Adiciona grid de células
    for i in np.arange(0, 5.1, 1):
        ax.axvline(i, color='black', linewidth=1.5)
    for i in np.arange(0, 9.1, 1):
        ax.axhline(i, color='black', linewidth=1.5)
    
    ax.set_xlim(-0.1, 5.1)
    ax.set_ylim(-0.1, 9.1)
    ax.set_aspect('equal')
    ax.invert_yaxis()
    ax.set_xticks([])
    ax.set_yticks([])
    ax.set_title(title, fontsize=10, fontweight='bold')
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['bottom'].set_visible(False)
    ax.spines['left'].set_visible(False)


def run_simulations():
    """
    Executa 12 simulações (3 para cada padrão) com 20% de ruído
    """
    # Cria os 4 padrões
    patterns = create_patterns()
    
    # Cria e treina a rede
    network = HopfieldNetwork(num_neurons=45)
    network.train(patterns)
    
    # Prepara figuras para visualização
    num_simulations = 12
    simulations_per_pattern = 3
    
    results = []
    
    print("=" * 80)
    print("REDE DE HOPFIELD PARA RECUPERAÇÃO DE PADRÕES")
    print("=" * 80)
    print(f"\nTreinamento concluído com {len(patterns)} padrões de 45 neurônios")
    print("\nSimulando 12 transmissões (3 para cada padrão)...\n")
    
    pattern_names = ["1", "2", "3", "4"]
    
    for pattern_idx, pattern_name in enumerate(pattern_names):
        print(f"\n{'='*80}")
        print(f"PADRÃO {pattern_idx + 1}: '{pattern_name}'")
        print(f"{'='*80}")
        
        original_pattern = patterns[pattern_idx]
        
        for sim in range(simulations_per_pattern):
            print(f"\nSimulação {pattern_idx * 3 + sim + 1}/12 - Padrão '{pattern_name}' (teste {sim + 1})")
            print("-" * 80)
            
            # Adiciona ruído (20%)
            noisy_pattern = network.add_noise(original_pattern, noise_percentage=0.20)
            
            # Recupera o padrão
            recovered_pattern = network.activate(noisy_pattern, iterations=100, beta=100.0)
            
            # Calcula estatísticas
            num_corrupted = np.sum(noisy_pattern != original_pattern)
            num_errors = np.sum(recovered_pattern != original_pattern)
            
            print(f"Pixels corrompidos: {num_corrupted}/45 ({num_corrupted/45*100:.1f}%)")
            print(f"Pixels com erro após recuperação: {num_errors}/45 ({num_errors/45*100:.1f}%)")
            
            if num_errors == 0:
                print("✓ Padrão recuperado com SUCESSO!")
            else:
                print("✗ Padrão NÃO foi completamente recuperado")
            
            results.append({
                'pattern_idx': pattern_idx,
                'pattern_name': pattern_name,
                'simulation': sim + 1,
                'original': original_pattern,
                'noisy': noisy_pattern,
                'recovered': recovered_pattern,
                'num_corrupted': num_corrupted,
                'num_errors': num_errors
            })
    
    return results, patterns


def save_visualizations(results: List, patterns: np.ndarray):
    """
    Salva visualizações das simulações
    """
    # Cria diretório para resultados
    os.makedirs('resultados', exist_ok=True)
    
    # Padrão 1: Todos os resultados em uma figura grande
    fig = plt.figure(figsize=(18, 16))
    fig.suptitle('Rede de Hopfield: Recuperação de Padrões com Ruído (20%)', 
                 fontsize=16, fontweight='bold', y=0.995)
    
    for idx, result in enumerate(results):
        # Original
        ax = plt.subplot(12, 3, idx*3 + 1)
        visualize_pattern(result['original'], 
                         f"Padrão Original\n'{result['pattern_name']}'", ax=ax)
        
        # Com ruído
        ax = plt.subplot(12, 3, idx*3 + 2)
        visualize_pattern(result['noisy'], 
                         f"Com Ruído (20%)\n{result['num_corrupted']} pixels corrompidos", ax=ax)
        
        # Recuperado
        ax = plt.subplot(12, 3, idx*3 + 3)
        status = "✓ OK" if result['num_errors'] == 0 else f"✗ {result['num_errors']} erros"
        visualize_pattern(result['recovered'], 
                         f"Recuperado\n{status}", ax=ax)
    
    plt.tight_layout()
    plt.savefig('resultados/hopfield_recuperacao_completa.png', dpi=150, bbox_inches='tight')
    print("\n✓ Figura completa salva: resultados/hopfield_recuperacao_completa.png")
    
    # Padrão 2: Uma figura por padrão
    pattern_names = ["1", "2", "3", "4"]
    for p_idx in range(4):
        fig, axes = plt.subplots(3, 3, figsize=(12, 12))
        fig.suptitle(f"Padrão '{pattern_names[p_idx]}': 3 Simulações com 20% de Ruído", 
                    fontsize=14, fontweight='bold')
        
        for sim_idx in range(3):
            result = results[p_idx * 3 + sim_idx]
            
            # Original
            visualize_pattern(result['original'], f"Original", axes[sim_idx, 0])
            # Com ruído
            visualize_pattern(result['noisy'], 
                             f"Ruído: {result['num_corrupted']} pixels", 
                             axes[sim_idx, 1])
            # Recuperado
            status = "✓ OK" if result['num_errors'] == 0 else f"✗ {result['num_errors']} erros"
            visualize_pattern(result['recovered'], f"Recuperado\n{status}", 
                             axes[sim_idx, 2])
        
        plt.tight_layout()
        plt.savefig(f'resultados/hopfield_padrao_{pattern_names[p_idx]}.png', 
                   dpi=150, bbox_inches='tight')
        print(f"✓ Figura salva: resultados/hopfield_padrao_{pattern_names[p_idx]}.png")
    
    plt.close('all')


def test_noise_levels():
    """
    Testa diferentes níveis de ruído para analisar o comportamento da rede
    """
    patterns = create_patterns()
    network = HopfieldNetwork(num_neurons=45)
    network.train(patterns)
    
    noise_levels = np.arange(0, 0.51, 0.05)  # 0% a 50%
    success_rates = []
    
    print("\n" + "=" * 80)
    print("ANÁLISE: EFEITO DO NÍVEL DE RUÍDO NA RECUPERAÇÃO")
    print("=" * 80)
    print("\nTestando diferentes níveis de ruído...\n")
    print(f"{'Ruído':<10} {'Sucesso':<15} {'Taxa de Acerto':<20}")
    print("-" * 80)
    
    for noise_level in noise_levels:
        successes = 0
        num_tests = 10
        
        for _ in range(num_tests):
            # Testa com primeiro padrão
            pattern = patterns[0]
            noisy_pattern = network.add_noise(pattern, noise_percentage=noise_level)
            recovered_pattern = network.activate(noisy_pattern, iterations=200, beta=100.0)
            
            if np.array_equal(recovered_pattern, pattern):
                successes += 1
        
        success_rate = successes / num_tests * 100
        success_rates.append(success_rate)
        
        status = "✓" if success_rate >= 80 else "✗" if success_rate < 20 else "~"
        print(f"{noise_level*100:6.0f}%    {successes:2d}/{num_tests}           {success_rate:6.1f}%          {status}")
    
    # Cria gráfico
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.plot(noise_levels * 100, success_rates, 'b-o', linewidth=2, markersize=8)
    ax.axhline(y=50, color='r', linestyle='--', label='50% (ponto crítico)')
    ax.set_xlabel('Nível de Ruído (%)', fontsize=12, fontweight='bold')
    ax.set_ylabel('Taxa de Sucesso (%)', fontsize=12, fontweight='bold')
    ax.set_title('Efeito do Nível de Ruído na Recuperação de Padrões', 
                fontsize=14, fontweight='bold')
    ax.grid(True, alpha=0.3)
    ax.set_ylim([-5, 105])
    ax.set_xlim([-2, 52])
    ax.legend()
    
    os.makedirs('resultados', exist_ok=True)
    plt.savefig('resultados/analise_ruido.png', dpi=150, bbox_inches='tight')
    print(f"\n✓ Gráfico salvo: resultados/analise_ruido.png")
    
    plt.close('all')
    
    return noise_levels, success_rates


if __name__ == "__main__":
    # Define seed para reprodutibilidade
    np.random.seed(42)
    
    # Executa as simulações
    results, patterns = run_simulations()
    
    # Salva visualizações
    save_visualizations(results, patterns)
    
    # Testa diferentes níveis de ruído
    noise_levels, success_rates = test_noise_levels()
    
    print("\n" + "=" * 80)
    print("SIMULAÇÕES CONCLUÍDAS COM SUCESSO!")
    print("=" * 80)
    print("\nArquivos gerados:")
    print("  - resultados/hopfield_recuperacao_completa.png")
    print("  - resultados/hopfield_padrao_1.png")
    print("  - resultados/hopfield_padrao_2.png")
    print("  - resultados/hopfield_padrao_3.png")
    print("  - resultados/hopfield_padrao_4.png")
    print("  - resultados/analise_ruido.png")
    print("\n")
