import tkinter as tk
from ttkbootstrap import Style
from ttkbootstrap.constants import *
from tkinter import ttk, messagebox
import pandas as pd
from datetime import datetime

# Dicionário com os produtos e suas unidades de medida
PRODUTOS = {
    "Polpa Açaí Parlamaz": "kg",
    "Polpa Açaí Xingu": "kg",
    "Açaí Preparado": "litro",
    "Farinha": ["kg", "litro"],
    "Combo": "unidade",
    "Taperebá": "kg",
    "Cupuaçu": "kg",
    "Tapioca": "kg",
    "Pimenta": "ml",
    "Camarão": ["g", "kg"],
    "Peixe": ["kg", "g"],
    "Conserva": "unidade",
    "Charque": ["kg", "g"],
    "Maniva": "kg",
    "Tucupi": "litro"
}

class SistemaControleVendas:
    def __init__(self, root):
        self.root = root
        self.root.title("Gerenciador de Vendas Açai Paraense")
        self.root.geometry("900x600")
        self.vendas = []
        
        # Interface do sistema
        self.criar_interface()

    def adicionar_produto(self):
        produto = self.produto_selecionado.get()
        unidade = self.entry_unidade.get()
        cliente = self.entry_cliente.get()
        pagamento = self.pagamento_selecionado.get()
        
        try:
            qtd = float(self.entry_qtd.get().replace(",", "."))
            preco_unitario = float(self.entry_preco.get().replace("R$ ", "").replace(",", "."))
        except ValueError:
            messagebox.showerror("Erro", "Digite valores válidos para quantidade e preço.")
            return

        preco_total = round(qtd * preco_unitario, 2)
        self.vendas.append([produto, qtd, unidade, preco_unitario, preco_total, pagamento, cliente])
        
        # Atualiza o total e lista de vendas
        self.lbl_total_venda.config(text=f"Total da Venda: R$ {preco_total:.2f}")
        self.atualizar_lista_vendas()
        self.limpar_campos()

    def atualizar_lista_vendas(self):
        self.lista_vendas.delete(*self.lista_vendas.get_children())
        for venda in self.vendas:
            self.lista_vendas.insert('', 'end', values=venda)

    def salvar_vendas(self):
        try:
            df = pd.read_excel("crud_acai.xlsx")
        except FileNotFoundError:
            df = pd.DataFrame(columns=["Produto", "Quantidade", "Unidade", "Preço Unitário", "Preço Total", "Forma de Pagamento", "Cliente", "Data"])
        
        data_atual = datetime.now().strftime("%d/%m/%Y")
        
        for venda in self.vendas:
            df = pd.concat([df, pd.DataFrame({
                "Produto": [venda[0]],
                "Quantidade": [venda[1]],
                "Unidade": [venda[2]],
                "Preço Unitário": [f"R$ {venda[3]:.2f}".replace('.', ',')],
                "Preço Total": [f"R$ {venda[4]:.2f}".replace('.', ',')],
                "Forma de Pagamento": [venda[5]],
                "Cliente": [venda[6]],
                "Data": [data_atual]
            })], ignore_index=True)

        df.to_excel("crud_acai.xlsx", index=False)
        self.lbl_total_venda.config(text="Total da Venda: R$ 0,00")
        self.vendas.clear()
        self.atualizar_lista_vendas()
        messagebox.showinfo("Sucesso", "Vendas salvas com sucesso!")

    def atualizar_unidades(self, event):
        # Atualiza o Combobox de unidades de medida de acordo com o produto selecionado
        produto = self.produto_selecionado.get()
        unidades = PRODUTOS.get(produto, [])
        self.entry_unidade['values'] = unidades
        self.entry_unidade.set('')  # Limpa o valor selecionado anteriormente

    def limpar_campos(self):
        self.produto_selecionado.set('')
        self.entry_qtd.delete(0, tk.END)
        self.entry_preco.delete(0, tk.END)
        self.entry_unidade.set('')
        self.entry_cliente.delete(0, tk.END)
        self.pagamento_selecionado.set('')

    def cancelar_venda(self):
        self.vendas.clear()
        self.atualizar_lista_vendas()
        self.lbl_total_venda.config(text="Total da Venda: R$ 0,00")
        self.limpar_campos()
        messagebox.showinfo("Cancelamento", "Venda cancelada com sucesso!")

    def criar_interface(self):
        style = Style()
        style.configure('TButton', font=('Helvetica', 14))

        # Frame para seleção de produto
        frame_produto = ttk.Labelframe(self.root, text="🛒 Dados do Produto", padding=20, bootstyle="info")
        frame_produto.pack(fill=X, padx=20, pady=10)

        # Produto e preço
        ttk.Label(frame_produto, text="Produto:", font=("Helvetica", 12)).grid(row=0, column=0, sticky="w", padx=5)
        self.produto_selecionado = ttk.Combobox(frame_produto, values=list(PRODUTOS.keys()), font=("Helvetica", 12), state="readonly")
        self.produto_selecionado.grid(row=0, column=1, padx=10, pady=5)
        self.produto_selecionado.bind("<<ComboboxSelected>>", self.atualizar_unidades)

        ttk.Label(frame_produto, text="Quantidade:", font=("Helvetica", 12)).grid(row=1, column=0, sticky="w", padx=5)
        self.entry_qtd = ttk.Entry(frame_produto, font=("Helvetica", 12))
        self.entry_qtd.grid(row=1, column=1, padx=10, pady=5)

        ttk.Label(frame_produto, text="Preço Unitário:", font=("Helvetica", 12)).grid(row=2, column=0, sticky="w", padx=5)
        self.entry_preco = ttk.Entry(frame_produto, font=("Helvetica", 12))
        self.entry_preco.grid(row=2, column=1, padx=10, pady=5)
        self.entry_preco.insert(0, "R$ ")

        ttk.Label(frame_produto, text="Unidade:", font=("Helvetica", 12)).grid(row=3, column=0, sticky="w", padx=5)
        self.entry_unidade = ttk.Combobox(frame_produto, font=("Helvetica", 12), state="readonly")
        self.entry_unidade.grid(row=3, column=1, padx=10, pady=5)


        # Frame para cliente e pagamento
        frame_cliente = ttk.Labelframe(self.root, text="👤 Dados do Cliente", padding=20, bootstyle="info")
        frame_cliente.pack(fill=X, padx=20, pady=10)

        ttk.Label(frame_cliente, text="Cliente:", font=("Helvetica", 12)).grid(row=0, column=0, sticky="w", padx=5)
        self.entry_cliente = ttk.Entry(frame_cliente, font=("Helvetica", 12))
        self.entry_cliente.grid(row=0, column=1, padx=10, pady=5)

        ttk.Label(frame_cliente, text="Forma de Pagamento:", font=("Helvetica", 12)).grid(row=1, column=0, sticky="w", padx=5)
        self.pagamento_selecionado = ttk.Combobox(frame_cliente, values=["Dinheiro", "Cartão", "Pix", "Vale", "Cheque", "Fiado"], font=("Helvetica", 12), state="readonly")
        self.pagamento_selecionado.grid(row=1, column=1, padx=10, pady=5)

        # Lista de produtos adicionados
        frame_lista = ttk.Frame(self.root)
        frame_lista.pack(fill=X, padx=20, pady=10)
        
        self.lista_vendas = ttk.Treeview(frame_lista, columns=("Produto", "Quantidade", "Unidade", "Preço Unitário", "Preço Total", "Forma de Pagamento", "Cliente"), show='headings', height=8)
        for col in self.lista_vendas["columns"]:
            self.lista_vendas.heading(col, text=col)
            self.lista_vendas.column(col, width=100, anchor="center")
        self.lista_vendas.grid(row=0, column=0, sticky="nsew")

        # Botões alinhados ao lado direito
        frame_botoes = ttk.Frame(frame_lista)
        frame_botoes.grid(row=0, column=1, padx=10, sticky="ns")
        
        btn_add_produto = ttk.Button(frame_botoes, text="Adicionar Produto", command=self.adicionar_produto, bootstyle="success-outline")
        btn_add_produto.pack(pady=5)
        
        btn_salvar = ttk.Button(frame_botoes, text="Salvar Vendas", command=self.salvar_vendas, bootstyle="primary-outline")
        btn_salvar.pack(pady=5)
        
        btn_limpar = ttk.Button(frame_botoes, text="Limpar Campos", command=self.limpar_campos, bootstyle="danger-outline")
        btn_limpar.pack(pady=5)

        btn_cancelar = ttk.Button(frame_botoes, text="Cancelar Venda", command=self.cancelar_venda, bootstyle="warning")
        btn_cancelar.pack(pady=5)

        # Label de total de vendas
        self.lbl_total_venda = ttk.Label(self.root, text="Total da Venda: R$ 0,00", font=("Helvetica", 14))
        self.lbl_total_venda.pack(pady=10)

# Inicialização do sistema
root = tk.Tk()
app = SistemaControleVendas(root)
root.mainloop()
