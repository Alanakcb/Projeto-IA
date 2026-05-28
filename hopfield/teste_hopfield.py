"""
Script de Teste Interativo da Rede de Hopfield
Demonstra a recuperação de um padrão específico com visualização passo-a-passo
"""

import numpy as np
import matplotlib.pyplot as plt
from hopfield import HopfieldNetwork, create_patterns, visualize_pattern

def demonstrate_recovery_step_by_step():
    """
    Demonstra passo-a-passo a recuperação de um padrão com visualização iterativa
    """
    # Cria e treina a rede
    patterns = create_patterns()
    network = HopfieldNetwork(num_neurons=45)
    network.train(patterns)
    
    print("=" * 80)
    print("DEMONSTRAÇÃO INTERATIVA: RECUPERAÇÃO DE PADRÃO COM HOPFIELD")
    print("=" * 80)
    
    # Seleciona o padrão "3" como exemplo
    pattern_idx = 2
    original_pattern = patterns[pattern_idx]
    pattern_names = ["1", "2", "3", "4"]
    pattern_name = pattern_names[pattern_idx]
    
    print(f"\nPadrão Selecionado: '{pattern_name}'")
    print("-" * 80)
    
    # Adiciona ruído (20%)
    noisy_pattern = network.add_noise(original_pattern, noise_percentage=0.20)
    num_corrupted = np.sum(noisy_pattern != original_pattern)
    
    print(f"Pixels corrompidos: {num_corrupted}/45 ({num_corrupted/45*100:.1f}%)")
    print(f"\nIniciando processo de recuperação...")
    print("-" * 80)
    
    # Executa passo-a-passo com visualização
    state = noisy_pattern.copy()
    
    # Cria figura com múltiplas iterações
    fig, axes = plt.subplots(2, 6, figsize=(16, 6))
    fig.suptitle(f"Recuperação Iterativa do Padrão '{pattern_name}' \n(Rede de Hopfield com 45 Neurônios)", 
                fontsize=14, fontweight='bold')
    
    # Mostra padrão original
    visualize_pattern(original_pattern, f"Original", axes[0, 0])
    
    # Mostra padrão com ruído
    visualize_pattern(noisy_pattern, f"Entrada\n({num_corrupted} erros)", axes[1, 0])
    
    iteration_count = 0
    iterations_to_show = [1, 2, 5, 10, 20, 50]
    
    for iteration in range(100):
        iteration_count += 1
        
        # Calcula entrada ponderada
        h = np.dot(network.weights, state)
        
        # Aplica tangente hiperbólica
        new_state = np.tanh(100.0 * h)
        
        # Quantiza para -1 ou +1
        new_state = np.sign(new_state)
        new_state[new_state == 0] = 1
        
        # Verifica convergência
        converged = np.array_equal(new_state, state)
        
        # Mostra iterações específicas
        if iteration_count in iterations_to_show:
            col_idx = iterations_to_show.index(iteration_count) + 1
            num_errors = np.sum(new_state != original_pattern)
            visualize_pattern(new_state, 
                            f"Iteração {iteration_count}\n({num_errors} erros)", 
                            axes[0, col_idx])
            axes[1, col_idx].axis('off')
        
        if converged:
            print(f"✓ Convergência após {iteration_count} iterações")
            break
        
        state = new_state
    
    # Mostra resultado final
    num_errors_final = np.sum(state != original_pattern)
    
    if num_errors_final == 0:
        print(f"✓ SUCESSO! Padrão recuperado perfeitamente")
    else:
        print(f"✗ FALHA! {num_errors_final} pixels ainda com erro")
    
    print("\nEstatísticas da Recuperação:")
    print(f"  - Iterações até convergência: {iteration_count}")
    print(f"  - Pixels corrompidos na entrada: {num_corrupted}")
    print(f"  - Pixels com erro na saída: {num_errors_final}")
    
    plt.tight_layout()
    plt.savefig('teste_recuperacao_interativa.png', dpi=150, bbox_inches='tight')
    print(f"\n✓ Figura salva: teste_recuperacao_interativa.png")
    
    return state


def compare_all_patterns():
    """
    Compara a recuperação de todos os 4 padrões com o mesmo ruído
    """
    patterns = create_patterns()
    network = HopfieldNetwork(num_neurons=45)
    network.train(patterns)
    
    pattern_names = ["1", "2", "3", "4"]
    
    print("\n" + "=" * 80)
    print("COMPARAÇÃO: RECUPERAÇÃO DE TODOS OS PADRÕES COM 20% DE RUÍDO")
    print("=" * 80)
    
    fig, axes = plt.subplots(4, 3, figsize=(12, 14))
    fig.suptitle('Recuperação Comparativa de Todos os Padrões (20% de Ruído)', 
                fontsize=14, fontweight='bold')
    
    results_summary = []
    
    for p_idx, pattern_name in enumerate(pattern_names):
        original = patterns[p_idx]
        
        # Adiciona ruído
        noisy = network.add_noise(original, noise_percentage=0.20)
        
        # Recupera
        recovered = network.activate(noisy, iterations=100, beta=100.0)
        
        # Calcula estatísticas
        corrupted = np.sum(noisy != original)
        errors = np.sum(recovered != original)
        success = "✓ OK" if errors == 0 else f"✗ {errors}"
        
        results_summary.append({
            'pattern': pattern_name,
            'corrupted': corrupted,
            'errors': errors,
            'success': errors == 0
        })
        
        # Visualiza
        visualize_pattern(original, f"Original '{pattern_name}'", axes[p_idx, 0])
        visualize_pattern(noisy, f"Ruído: {corrupted} pixels", axes[p_idx, 1])
        visualize_pattern(recovered, f"Recuperado {success}", axes[p_idx, 2])
        
        print(f"\nPadrão '{pattern_name}':")
        print(f"  - Pixels corrompidos: {corrupted}")
        print(f"  - Pixels com erro: {errors}")
        print(f"  - Status: {'✓ SUCESSO' if errors == 0 else f'✗ FALHA ({errors} erros)'}")
    
    plt.tight_layout()
    plt.savefig('comparacao_padroes.png', dpi=150, bbox_inches='tight')
    print(f"\n✓ Figura salva: comparacao_padroes.png")
    
    # Resumo
    successes = sum(1 for r in results_summary if r['success'])
    total = len(results_summary)
    print("\n" + "=" * 80)
    print(f"RESUMO: {successes}/{total} padrões recuperados com sucesso ({successes/total*100:.1f}%)")
    print("=" * 80)
    
    return results_summary


def test_individual_pattern(pattern_idx: int, noise_percent: float = 0.20):
    """
    Testa um padrão individual com visualização detalhada
    
    Args:
        pattern_idx: Índice do padrão (0=L, 1=T, 2=O, 3=X)
        noise_percent: Percentual de ruído
    """
    patterns = create_patterns()
    network = HopfieldNetwork(num_neurons=45)
    network.train(patterns)
    
    pattern_names = ["1", "2", "3", "4"]
    pattern_name = pattern_names[pattern_idx]
    
    print("\n" + "=" * 80)
    print(f"TESTE DETALHADO DO PADRÃO '{pattern_name}' COM {noise_percent*100:.0f}% DE RUÍDO")
    print("=" * 80)
    
    original = patterns[pattern_idx]
    
    # Múltiplos testes
    num_tests = 5
    results = []
    
    for test_num in range(num_tests):
        noisy = network.add_noise(original, noise_percentage=noise_percent)
        recovered = network.activate(noisy, iterations=100, beta=100.0)
        
        corrupted = np.sum(noisy != original)
        errors = np.sum(recovered != original)
        
        results.append({
            'test': test_num + 1,
            'corrupted': corrupted,
            'errors': errors,
            'success': errors == 0
        })
        
        print(f"\nTeste {test_num + 1}:")
        print(f"  - Pixels corrompidos: {corrupted}/45")
        print(f"  - Pixels com erro: {errors}/45")
        print(f"  - Status: {'✓ SUCESSO' if errors == 0 else f'✗ FALHA'}")
    
    # Visualiza os 5 testes
    fig, axes = plt.subplots(5, 3, figsize=(12, 16))
    fig.suptitle(f"Teste Repetido: Padrão '{pattern_name}' com {noise_percent*100:.0f}% de Ruído", 
                fontsize=14, fontweight='bold')
    
    for test_num in range(num_tests):
        noisy = network.add_noise(original, noise_percentage=noise_percent)
        recovered = network.activate(noisy, iterations=100, beta=100.0)
        
        corrupted = np.sum(noisy != original)
        errors = np.sum(recovered != original)
        status = "✓ OK" if errors == 0 else f"✗ {errors}"
        
        visualize_pattern(original, f"Original", axes[test_num, 0])
        visualize_pattern(noisy, f"Ruído: {corrupted}", axes[test_num, 1])
        visualize_pattern(recovered, f"Recuperado {status}", axes[test_num, 2])
    
    plt.tight_layout()
    plt.savefig(f'teste_padrao_{pattern_name}.png', dpi=150, bbox_inches='tight')
    print(f"\n✓ Figura salva: teste_padrao_{pattern_name}.png")
    
    # Resumo
    successes = sum(1 for r in results if r['success'])
    print(f"\nRESUMO: {successes}/{num_tests} testes bem-sucedidos ({successes/num_tests*100:.1f}%)")
    
    return results


if __name__ == "__main__":
    import os
    
    # Define seed
    np.random.seed(42)
    
    # Criar diretório de testes se não existir
    os.makedirs('testes', exist_ok=True)
    os.chdir('testes')
    
    print("\n" + "=" * 80)
    print("TESTES DA REDE DE HOPFIELD - SUITE COMPLETA")
    print("=" * 80)
    
    # Teste 1: Recuperação passo-a-passo
    print("\n\n>>> TESTE 1: Recuperação Iterativa Passo-a-Passo")
    demonstrate_recovery_step_by_step()
    
    # Teste 2: Comparação de todos os padrões
    print("\n\n>>> TESTE 2: Comparação de Todos os Padrões")
    compare_all_patterns()
    test_individual_pattern(2, noise_percent=0.20)
    
    print("\n" + "=" * 80)
    print("TODOS OS TESTES CONCLUÍDOS!")
    print("=" * 80)
    print("\nArquivos gerados em ./testes/:")
    print("  - teste_recuperacao_interativa.png")
    print("  - comparacao_padroes.png")
    print("  - teste_padrao_3.png")
    print("\n")
