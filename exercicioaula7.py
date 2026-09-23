#exercicio 1 
#entrada
numero = int(input("digite o numero inteiro") )

#processamento
quociente = numero // 10
resto = numero % 10
ultimo_digito = numero % 10

#saida
print(f"a divisao inteira por 10 e: {quociente}")
print(f"o resto da divisao por 10 e: {resto}")
print(f"o ultimo algarismo é: {ultimo_digito}")




#exercicio 2
#entrada    
capital_investido = (float(input("digite o capital investido: ")))
taxa_juros = (float(input("digite a taxa de juros: ")))
meses = (int(input("digite o numero de meses: ")))

#processamento
juros = capital_investido * (taxa_juros / 100) * meses
montante = capital_investido + juros

#saida
print(f"o valor do juros e: R$ {juros:.2f}")
print(f"o valor do montante e: R$ {montante:.2f}")






#exercicio 3
#entrada    
orcamento_disponivel = (float(input("digite o orcamento disponivel: ")))
gasto = (float(input("digite o valor gastos: ")))

#processamento
saldo = orcamento_disponivel - gasto

print(gasto <= orcamento_disponivel)
print(f"o saldo disponivel e: R$ {saldo:.2f}")



#exercicio 4
#entrada
saldo_disponivel = (float(input("digite o saldo disponivel: ")))
valor_compra = (float(input("digite o valor da compra: ")))

#saida 
if valor_compra <= saldo_disponivel:
    print("compra realizada com sucesso")
else:
    print("compra nao realizada - saldo insuficiente")
