
print("meu primeiro programa aplicado a negocios")
#pratica 02
#primeiro programa aplicado a negocios

#dados
produto = "notebook"
preco = 3500.00
quantidade = 4
cliente_ativo = True
percentual_desconto = 10
percentual_comissao = 4
custo_unitario = 2600.00

#processamento
total_venda = preco * quantidade
valor_desconto = total_venda * percentual_desconto / 100
valor_final = total_venda - valor_desconto
valor_comissao = total_venda * percentual_comissao / 100
custo_total = custo_unitario * quantidade
lucro_bruto = total_venda - custo_total 

#saida
print("produto:", produto)
print("preco unitario:", preco)
print("quantidade:", quantidade)
print("total da venda:", total_venda)
print("valor do desconto:", valor_desconto)
print("valor final:", valor_final)
print("valor da comissao:", valor_comissao)
print("custo total:", custo_total)
print("lucro bruto:", lucro_bruto)


produto = "monitor" 
preco = 1800.00
quantidade = 7
percentual_desconto = 12
percentual_comissao = 5
custo_unitario = 1250

print("produto:", produto)
print("preco unitario:", preco)
print("quantidade:", quantidade)
print("total da venda:", total_venda)
print("valor do desconto:", valor_desconto)
print("valor final:", valor_final)
print("valor da comissao:", valor_comissao)
print("custo total:", custo_total)
print("lucro bruto:", lucro_bruto)


