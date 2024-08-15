codigo = input("Digite o código do produto: ")
nome_produto = input("Digite o nome do produto: ")
quantidade = int(input("Digite a quantidade do produto: "))
preco = float(input("Digite o preço do produto: "))
valor_total = quantidade * preco

print("\n--- Informações do produto ---")
print("Código:", codigo)
print("Nome:", nome_produto)
print("Quantidade:", quantidade)
print("Preço:", preco)
print("Valor total da compra: R$", valor_total)