
# Gerenciador de Vendas Açai Paraense

Este é um sistema de controle de vendas para um negócio de açaí e produtos regionais. A aplicação permite gerenciar produtos, adicionar vendas, registrar dados dos clientes, calcular o preço total da venda e salvar todas as informações em uma planilha.

## Funcionalidades

- Seleção de produtos com unidades de medida específicas
- Entrada e cálculo de quantidade e preço unitário
- Registro de informações do cliente e forma de pagamento
- Listagem de produtos adicionados para cada venda
- Salva as vendas em uma planilha Excel (`crud_acai.xlsx`) com informações detalhadas
- Limpa os campos de entrada e exibe o valor total da venda
- Cancelamento de vendas para redefinir a lista de produtos e valores

## Requisitos

- **Python 3.x**
- **Bibliotecas Python necessárias**: 
  - `tkinter` (para interface gráfica)
  - `ttkbootstrap` (para temas de interface gráfica)
  - `pandas` (para manipulação de planilhas Excel)
  
Para instalar as bibliotecas necessárias, execute:

```bash
pip install pandas ttkbootstrap
```

## Estrutura do Código

- **Dicionário de Produtos:** Contém os produtos e suas unidades de medida específicas (como kg, litro, g).
- **Interface Gráfica:** Desenvolvida usando `tkinter` e `ttkbootstrap` para uma aparência moderna e intuitiva.
- **Manipulação de Dados:** O sistema calcula o preço total com base na quantidade e no preço unitário e armazena os dados em uma lista.
- **Exportação para Excel:** Usa `pandas` para salvar as vendas no arquivo `crud_acai.xlsx`.

## Instruções de Uso

1. **Selecione o Produto:** Escolha o produto desejado e a unidade de medida (é preenchida automaticamente com as unidades permitidas para cada produto).
2. **Insira a Quantidade e o Preço Unitário:** Preencha os campos com a quantidade e o preço unitário do produto.
3. **Dados do Cliente e Pagamento:** Insira o nome do cliente e escolha a forma de pagamento.
4. **Adicionar Produto:** Clique em "Adicionar Produto" para adicionar à lista de vendas.
5. **Salvar Vendas:** Ao concluir a adição dos produtos, clique em "Salvar Vendas" para registrar as informações na planilha Excel.
6. **Cancelar Venda:** Caso precise, o botão "Cancelar Venda" esvazia a lista de produtos e limpa os campos.

## Estrutura da Planilha Excel (`crud_acai.xlsx`)

Cada linha da planilha salva as seguintes informações sobre cada venda:
- Produto
- Quantidade
- Unidade de medida
- Preço unitário e total formatados (com prefixo `R$`)
- Forma de pagamento
- Cliente
- Data

## Executando o Projeto

Para iniciar o programa, basta executar o arquivo `main.py` (ou o nome que você deu ao seu código):

```bash
python main.py
```

Se desejar distribuir o programa como um executável, pode seguir as instruções para criar um executável com o **PyInstaller**:

```bash
pip install pyinstaller
pyinstaller --onefile --windowed main.py
```

## Interface

A interface possui:
- Campo de seleção de produtos e unidades de medida.
- Entradas para quantidade, preço unitário, cliente e forma de pagamento.
- Botões para adicionar produtos, salvar vendas, limpar campos e cancelar vendas.
- Tabela listando os produtos adicionados e total da venda atualizado.

## Licença

Este projeto é licenciado sob a [MIT License](LICENSE).
