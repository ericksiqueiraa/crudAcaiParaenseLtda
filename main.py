import tkinter as tk
from tkinter import messagebox
import pandas as pd

def formatarPreco(preco):
    """Converte o valor em um formato de moeda (Real)."""
    try:
        preco_float = float(preco)  # Converte o preço para float
        return f'R$ {preco_float:.2f}'  # Formata o preço como string de moeda
    except ValueError:
        messagebox.showerror("Erro", "Preço inválido. Por favor, insira um número.")
        return None  # Retorna None se houver erro na conversão

def adicionarProduto(nome, qtd, preco):
    if not nome or not qtd or not preco:  # Verifica se os campos não estão vazios
        messagebox.showerror("Erro", "Todos os campos devem ser preenchidos.")
        return

    preco_formatado = formatarPreco(preco)  # Formata o preço
    if preco_formatado is None:  # Se houve um erro, retorna
        return
    
    # Lê o DataFrame existente
    try:
        df = pd.read_excel("crud_acai.xlsx")
    except FileNotFoundError:
        df = pd.DataFrame(columns=["Produto", "Quantidade", "Preço"])
    
    # Cria um novo DataFrame com o novo produto
    novo_produto = pd.DataFrame({"Produto": [nome], "Quantidade": [qtd], "Preço": [preco_formatado]})
    
    # Concatena o DataFrame existente com o novo
    df = pd.concat([df, novo_produto], ignore_index=True)
    
    # Salva o DataFrame atualizado no arquivo Excel
    df.to_excel("crud_acai.xlsx", index=False)
    messagebox.showinfo("✅ Venda feita!", f"O produto '{nome}' foi adicionado com sucesso!")

def interfaceGrafica():
    root = tk.Tk()
    root.title("🌟 Gerenciador Açaí Paraense 🌟")
    
    # Definindo o tamanho da janela
    root.geometry("400x350")
    root.configure(bg="#f0f8ff")  # Cor de fundo

    # Estilo dos rótulos
    label_style = {'bg': "#f0f8ff", 'font': ('Arial', 12, 'bold')}
    
    tk.Label(root, text="🌟 Gerenciador de Açaí 🌟", font=('Arial', 16, 'bold'), bg="#f0f8ff", fg="#333").pack(pady=10)

    # Criando um frame para organizar os campos
    frame = tk.Frame(root, bg="#f0f8ff")
    frame.pack(pady=10)

    tk.Label(frame, text="Nome do Produto 🥤", **label_style).grid(row=0, column=0, padx=10, pady=5)
    entry_nome = tk.Entry(frame, width=30)
    entry_nome.grid(row=0, column=1, padx=10, pady=5)

    tk.Label(frame, text="Quantidade 📦", **label_style).grid(row=1, column=0, padx=10, pady=5)
    entry_qtd = tk.Entry(frame, width=30)
    entry_qtd.grid(row=1, column=1, padx=10, pady=5)

    tk.Label(frame, text="Preço 💲", **label_style).grid(row=2, column=0, padx=10, pady=5)
    entry_preco = tk.Entry(frame, width=30)
    entry_preco.grid(row=2, column=1, padx=10, pady=5)

    tk.Button(root, text="✅ Adicionar Produto", 
              command=lambda: adicionarProduto(entry_nome.get(), entry_qtd.get(), entry_preco.get()),
              bg="#4CAF50", fg="white", font=('Arial', 12, 'bold')).pack(pady=20)  # Botão

    tk.Label(root, text="📈 Controle de Vendas 📈", font=('Arial', 12, 'italic'), bg="#f0f8ff", fg="#333").pack(pady=10)

    root.mainloop()

if __name__ == "__main__":
    interfaceGrafica()
