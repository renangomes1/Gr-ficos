import tkinter as tk
import pandas as pd
import matplotlib.pyplot as plt




def ler_dados():
    df = pd.read_csv('dados.csv')
    return df

def plotar_grafico_barras(df):
    plt.figure(figsize=(8, 6), edgecolor='black')
    plt.bar(df['vendedor'], df['vendas'],edgecolor='black')
    plt.title('Vendas por Vendedor')
    plt.xlabel('Vendedor')
    plt.ylabel('Vendas')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.grid(True, color= 'black')
    plt.show()

def plotar_grafico_pizza(df):
    plt.figure(figsize=(8, 6))
    plt.pie(df['vendas'], labels=df['vendedor'], autopct='%1.1f%%')
    plt.title('Distribuição de Vendas')
    plt.tight_layout()
   
    plt.show()




def plotar_grafico_linha(df):
    plt.figure(figsize=(8, 6))
    plt.plot(df['vendedor'], df['vendas'], marker='o')
    plt.title('Evolução das Vendas')
    plt.xlabel('Vendedor')
    plt.ylabel('Vendas')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()
    plt.grid(True)

def plotar_grafico_dispersao(df):
    
    plt.scatter(df['vendedor'], df['vendas'])
    plt.title('Dispersão de Vendas')
    plt.grid(True)
    plt.xlabel('Vendedor')
    plt.ylabel('Vendas')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()
    


def plotar_grafico_barras_horizontais(df):
    plt.figure(figsize=(8, 6), edgecolor= 'black')
    plt.barh(df['vendedor'], df['vendas'], edgecolor= 'black')
    plt.title('Vendas por Vendedor (Horizontal)')
    plt.xlabel('Vendas')
    plt.ylabel('Vendedor')
    plt.grid(True, color= 'black')
    plt.tight_layout()
    plt.show()
    

# Função para criar a interface gráfica com Tkinter
def criar_interface():
    # Inicialização da janela principal
    root = tk.Tk()
    root.title('Análise de Vendas')

    # Leitura dos dados
    df = ler_dados()

    # Botões para os tipos de gráficos
    btn_barra = tk.Button(root, text='Gráfico de Barras', command=lambda: plotar_grafico_barras(df))
    btn_barra.pack(pady=10)

    btn_pizza = tk.Button(root, text='Gráfico de Pizza', command=lambda: plotar_grafico_pizza(df))
    btn_pizza.pack(pady=10)

    btn_linha = tk.Button(root, text='Gráfico de Linha', command=lambda: plotar_grafico_linha(df))
    btn_linha.pack(pady=10)

    btn_dispersao = tk.Button(root, text='Gráfico de Dispersão', command=lambda: plotar_grafico_dispersao(df))
    btn_dispersao.pack(pady=10)

    btn_barras_horizontais = tk.Button(root, text='Gráfico de Barras Horizontais', command=lambda: plotar_grafico_barras_horizontais(df))
    btn_barras_horizontais.pack(pady=10)

   
    root.mainloop()


criar_interface()
