import tkinter as tk
from tkinter import ttk, messagebox
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import os

# Função para carregar os dados
def carregar_dados(caminho_arquivo):
    dados = np.loadtxt(caminho_arquivo, delimiter=',', skiprows=1)
    X = dados[:, 1:4]
    d = dados[:, 4]
    return X, d

# Função de treinamento do perceptron
def treinar_perceptron(X, d, taxa_aprendizado, max_epocas):
    num_amostras, num_features = X.shape
    x0 = -np.ones((num_amostras, 1))
    X_com_bias = np.hstack((x0, X))
    
    np.random.seed(42)
    w = np.random.uniform(-0.5, 0.5, size=num_features + 1)
    
    epocas_concluidas = 0
    for epoca in range(max_epocas):
        erros_na_epoca = 0
        for i in range(num_amostras):
            v = np.dot(w, X_com_bias[i])
            y = 1 if v >= 0 else -1
            erro = d[i] - y
            if erro != 0:
                w = w + taxa_aprendizado * erro * X_com_bias[i]
                erros_na_epoca += 1
                
        epocas_concluidas = epoca + 1
        if erros_na_epoca == 0:
            break
            
    return w, epocas_concluidas

class PerceptronApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Classificador Perceptron - Projeto IA")
        self.root.geometry("1000x700")
        
        # Configurar Estilo Básico
        style = ttk.Style()
        style.theme_use('clam')
        
        # Frame Lateral (Controles)
        control_frame = ttk.Frame(self.root, padding="15", width=300)
        control_frame.pack(side=tk.LEFT, fill=tk.Y)
        
        ttk.Label(control_frame, text="Hiperparâmetros", font=("Arial", 14, "bold")).pack(pady=10)
        
        ttk.Label(control_frame, text="Taxa de Aprendizado (η):").pack(anchor=tk.W, pady=5)
        self.entry_lr = ttk.Entry(control_frame)
        self.entry_lr.insert(0, "0.01")
        self.entry_lr.pack(fill=tk.X)
        
        ttk.Label(control_frame, text="Épocas Máximas:").pack(anchor=tk.W, pady=5)
        self.entry_epochs = ttk.Entry(control_frame)
        self.entry_epochs.insert(0, "1000")
        self.entry_epochs.pack(fill=tk.X)
        
        self.btn_treinar = ttk.Button(control_frame, text="Treinar Perceptron", command=self.executar_treinamento)
        self.btn_treinar.pack(pady=20, fill=tk.X)
        
        # Resultados
        self.lbl_status = ttk.Label(control_frame, text="", font=("Arial", 10))
        self.lbl_status.pack(pady=10)
        self.lbl_pesos = ttk.Label(control_frame, text="", font=("Arial", 10), justify=tk.LEFT)
        self.lbl_pesos.pack(pady=5)
        
        # Frame Principal (Gráfico)
        self.plot_frame = ttk.Frame(self.root, padding="5")
        self.plot_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)
        
        # Placeholder do Gráfico
        self.fig = plt.Figure(figsize=(6, 5), dpi=100)
        self.ax = self.fig.add_subplot(111, projection='3d')
        self.ax.set_title("Gráfico de Convergência (Entradas e Separação)")
        self.canvas = FigureCanvasTkAgg(self.fig, master=self.plot_frame)
        self.canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

    def executar_treinamento(self):
        try:
            lr_str = self.entry_lr.get().replace(',', '.')
            taxa_aprendizado = float(lr_str)
            max_epocas = int(self.entry_epochs.get())
        except ValueError:
            messagebox.showerror("Erro", "Valores inválidos nos campos.")
            return

        diretorio_atual = os.path.dirname(os.path.abspath(__file__))
        caminho_csv = os.path.join(diretorio_atual, 'treinamento.csv')
        
        if not os.path.exists(caminho_csv):
            messagebox.showerror("Erro", f"Arquivo {caminho_csv} não encontrado.")
            return
            
        # Treinamento
        X, d = carregar_dados(caminho_csv)
        self.lbl_status.config(text="Treinando...")
        self.root.update()
        
        w, epocas_gastas = treinar_perceptron(X, d, taxa_aprendizado, max_epocas)
        
        self.lbl_status.config(text=f"Convergência: Época {epocas_gastas}")
        self.lbl_pesos.config(text=f"Pesos Finais:\nw0 (bias): {w[0]:.4f}\nw1: {w[1]:.4f}\nw2: {w[2]:.4f}\nw3: {w[3]:.4f}")
        
        self.plotar_grafico(X, d, w)

    def plotar_grafico(self, X, d, w):
        self.ax.clear()
        
        # Separar classes para cores
        X_c1 = X[d == -1]
        X_c2 = X[d == 1]
        
        # Plotar entradas
        self.ax.scatter(X_c1[:, 0], X_c1[:, 1], X_c1[:, 2], color='red', label='Classe C1 (-1)', s=50)
        self.ax.scatter(X_c2[:, 0], X_c2[:, 1], X_c2[:, 2], color='blue', label='Classe C2 (+1)', s=50)
        
        # Criar plano de separação (Hiperplano)
        # Equação: -w0 + w1*x1 + w2*x2 + w3*x3 = 0  => x3 = (w0 - w1*x1 - w2*x2) / w3
        x1_range = np.linspace(X[:, 0].min() - 1, X[:, 0].max() + 1, 10)
        x2_range = np.linspace(X[:, 1].min() - 1, X[:, 1].max() + 1, 10)
        X1, X2 = np.meshgrid(x1_range, x2_range)
        
        # Evitar divisão por zero caso w[3] seja muito pequeno
        if abs(w[3]) > 1e-6:
            X3 = (w[0] - w[1]*X1 - w[2]*X2) / w[3]
            self.ax.plot_surface(X1, X2, X3, alpha=0.3, color='gray')
            
        self.ax.set_xlabel('Grandeza x1')
        self.ax.set_ylabel('Grandeza x2')
        self.ax.set_zlabel('Grandeza x3')
        self.ax.set_title("Separação Linear das Amostras de Óleo")
        self.ax.legend()
        
        self.canvas.draw()

if __name__ == "__main__":
    root = tk.Tk()
    app = PerceptronApp(root)
    root.mainloop()
