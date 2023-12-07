preco = float(input("PREÇO UNITARIO DO PRODUTO: "))
qtd = int(input("QUANTIDADE COMPRADA: "))
dinheiro = float(input("DINHEIRO RECEBIDO "))

troco = dinheiro - (preco * qtd)

print(f"TROCO: {troco:.2f}")