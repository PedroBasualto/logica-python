#dados 
produto = "mouse"
preco = 120.00
quantidade = 25
custo_unitario = 75.00
percentual_desconto = 5

#processamento
total_venda = preco * quantidade
valor_desconto = total_venda * percentual_desconto / 100
valor_final = total_venda - valor_desconto  
custo_total = custo_unitario * quantidade
lucro_bruto = valor_final - custo_total

#saida
print("produto:", produto)
print("preco unitario:", preco)
print("quantidade:", quantidade)
print("total da venda:", total_venda)   
print("valor do desconto:", valor_desconto)
print("valor final:", valor_final)
print("custo total:", custo_total)
print("lucro bruto:", lucro_bruto)  