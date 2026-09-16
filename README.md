#exercicio17
print("ola mundo")

#dados 
produto = (str(input("digite o nome do produto: ")))
preco_unitario = float(input("digite o preco unitario: "))
quantidade = int(input("digite a quantidade: "))

#processamento
valor_total = float(preco_unitario) * int(quantidade)   

#saida 
print("produto:", produto)
print("preco unitario: R$ ", preco_unitario)
print("quantidade:", quantidade)        
print("valor total: R$ ", valor_total)   
