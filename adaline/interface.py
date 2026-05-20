import tkinter as tk
from tkinter import ttk, messagebox
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import os

from core import carregar_dados, treinar_adaline

class AdalineApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Classificador ADALINE - Projeto IA")
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
        self.entry_lr.insert(0, "0.0025")
        self.entry_lr.pack(fill=tk.X)
        
        ttk.Label(control_frame, text="Precisão de Parada:").pack(anchor=tk.W, pady=5)
        self.entry_precisao = ttk.Entry(control_frame)
        self.entry_precisao.insert(0, "0.000001")
        self.entry_precisao.pack(fill=tk.X)
        
        ttk.Label(control_frame, text="Épocas Máximas:").pack(anchor=tk.W, pady=5)
        self.entry_epochs = ttk.Entry(control_frame)
        self.entry_epochs.insert(0, "10000")
        self.entry_epochs.pack(fill=tk.X)
        
        self.btn_treinar = ttk.Button(control_frame, text="Treinar ADALINE", command=self.executar_treinamento)
        self.btn_treinar.pack(pady=20, fill=tk.X)
        
        # Resultados
        self.lbl_status = ttk.Label(control_frame, text="", font=("Arial", 10), foreground="blue")
        self.lbl_status.pack(pady=10)
        self.lbl_pesos = ttk.Label(control_frame, text="", font=("Arial", 10), justify=tk.LEFT)
        self.lbl_pesos.pack(pady=5)
        
        # Frame Principal (Gráfico)
        self.plot_frame = ttk.Frame(self.root, padding="5")
        self.plot_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)
        
        # Placeholder do Gráfico
        self.fig, self.ax = plt.subplots(figsize=(6, 5), dpi=100)
        self.ax.set_title("Curva de Erro Quadrático Médio (EQM)")
        self.ax.set_xlabel("Épocas")
        self.ax.set_ylabel("EQM")
        self.ax.grid(True)
        self.canvas = FigureCanvasTkAgg(self.fig, master=self.plot_frame)
        self.canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

    def executar_treinamento(self):
        try:
            lr_str = self.entry_lr.get().replace(',', '.')
            prec_str = self.entry_precisao.get().replace(',', '.')
            taxa_aprendizado = float(lr_str)
            precisao = float(prec_str)
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
        self.lbl_status.config(text="Treinando... Aguarde.")
        self.root.update()
        
        w, epocas_gastas, historico_eqm = treinar_adaline(X, d, taxa_aprendizado, precisao, max_epocas)
        
        self.lbl_status.config(text=f"Convergência atingida: Época {epocas_gastas}")
        texto_pesos = (f"Pesos Finais:\n"
                       f"w0 (bias): {w[0]:.4f}\n"
                       f"w1: {w[1]:.4f}\n"
                       f"w2: {w[2]:.4f}\n"
                       f"w3: {w[3]:.4f}\n"
                       f"w4: {w[4]:.4f}\n\n"
                       f"EQM Final: {historico_eqm[-1]:.6f}")
        self.lbl_pesos.config(text=texto_pesos)
        
        self.plotar_grafico(historico_eqm)

    def plotar_grafico(self, historico_eqm):
        self.ax.clear()
        self.ax.plot(range(len(historico_eqm)), historico_eqm, color='purple', linewidth=2)
        self.ax.set_title("ADALINE - Curva de Decaimento do Erro (EQM)")
        self.ax.set_xlabel('Épocas')
        self.ax.set_ylabel('Erro Quadrático Médio')
        self.ax.grid(True, linestyle='--', alpha=0.7)
        self.canvas.draw()

if __name__ == "__main__":
    root = tk.Tk()
    app = AdalineApp(root)
    root.mainloop()
