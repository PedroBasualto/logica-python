#parte 1 variaveis e tipos de dados           
#dados 
nome = "Pedro"
idade = 19
cidade = "Piracicaba"

#saida
print(f"Meu nome é {nome}")
print(f"Eu tenho {idade} anos")
print(f"atualmente morando em {cidade}")

#dados 02 
produto = "caderno"
preco = 5.99
quantidade = 10

#saida 02
print(f"Produto: {produto}")
print(f"Preço: R$ {preco:.2f}")
print(f"Quantidade: {quantidade}")

#dados 03
pontos = 10 
pontos = 20
#saida 03
print(f"Pontos: {pontos}")

#dados 04
nome = "Pedro"
idade = 25
altura = 1.78
ano_nascimento = 2026
#saida 04
print(type(nome))
print(type(idade))
print(type(altura))
print(type(ano_nascimento))

#parte 2 calculo com variaveis
#dados 5
num1 = 10
num2 = 5

#processamento 5 
soma = num1 + num2
subtracao = num1 - num2
multiplicacao = num1 * num2
divisao = num1 / num2   

#saida 5
print(f"Soma: {soma}")
print(f"Subtração: {subtracao}")
print(f"Multiplicação: {multiplicacao}")
print(f"Divisão: {divisao}")    

#dados 6 
nota = 8.5
nota2 = 7.0
nota3 = 9.0 

#processamento 6
media = (nota + nota2 + nota3) / 3

#saida 6
print(f"Média: {media:.2f}")    

#dados 7
preco_produto = 19.99
quantidade_produto = 3

#processamento 7
total = preco_produto * quantidade_produto

#saida 7
print(f"Total: R$ {total:.2f}")    


#dados 8
salario = 2500.00
bonus = 500.00

#processamento 8
salario_total = salario + bonus

#saida 8
print(f"Salário total: R$ {salario_total:.2f}")

#parte 3 entrada de dados com input
#dados 9
nome = input("Digite seu nome: ")

#saida 9
print(f"Olá, {nome}! Bem-vindo ao Python!")

#dados 10
nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))    
curso = input("Digite seu curso: ")

#saida 10
print(f"Olá, {nome}! Você tem {idade} anos.")
print(f"Você está matriculado no curso de {curso}.")

#dados 11
num1 = int(input("Digite o primeiro número inteiro: ")) 
num2 = int(input("Digite o segundo número inteiro: "))

#processamento 11
soma = num1 + num2

#saida 11
print(f"A soma de {num1} e {num2} é {soma}")    

#dados 12
num1 = float(input("Digite o primeiro número decimal: "))
num2 = float(input("Digite o segundo número decimal: "))

#processamento 12
soma = num1 + num2
subtracao = num1 - num2
multiplicacao = num1 * num2
divisao = num1 / num2

#saida 12
print(f"Soma: {soma}")
print(f"Subtração: {subtracao}")    
print(f"Multiplicação: {multiplicacao}")
print(f"Divisão: {divisao}")

#parte 4 problemas aplicados
#dados 13
nome = input("Digite seu nome: ")
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: ")) 

#processamento 13
media = (nota1 + nota2) / 2

#saida 13
print(f"{nome}, bem vindo(a)!")
print(f"sua nota 1 e nota 2 são {nota1} e {nota2}, respectivamente.")
print(f"Sua média é {media:.2f}")

#dados 14
produto = input("Digite o nome do produto: ")
preco_unitario = float(input("Digite o preço unitário do produto: "))
quantidade = int(input("Digite a quantidade do produto: "))

#processamento 14
total = preco_unitario * quantidade

#saida 14
print(f"Produto: {produto}")
print(f"Preço unitário: R$ {preco_unitario:.2f}")
print(f"Quantidade: {quantidade}")
print(f"Total: R$ {total:.2f}")

#dados 15
nome_do_funcionario = input("Digite o nome do funcionário: ")
salario_base = float(input("Digite o salário base do funcionário: "))
bonus = float(input("Digite o bônus do funcionário: "))

#processamento 15
salario_total = salario_base + bonus    

#saida 15
print(f"Funcionário: {nome_do_funcionario}")
print(f"Salário base: R$ {salario_base:.2f}")
print(f"Bônus: R$ {bonus:.2f}")
print(f"Salário total: R$ {salario_total:.2f}")     

#dados 16
preco_produto = float(input("Digite o preço do produto: "))
valor_desconto = float(input("Digite o valor do desconto: "))

#processamento 16
preco_final = preco_produto - valor_desconto

#saida 16
print(f"Preço do produto: R$ {preco_produto:.2f}")
print(f"Valor do desconto: R$ {valor_desconto:.2f}")
print(f"Preço final: R$ {preco_final:.2f}")

#desafio final 
nome = input("Digite seu nome: ")
produto = input("Digite o nome do produto: ")
preco_unitario = float(input("Digite o preço unitário do produto: "))
quantidade = int(input("Digite a quantidade do produto: "))

#processamento desafio final
total = preco_unitario * quantidade

#saida desafio final
print("======pedido======")
print(f"Nome: {nome}")
print(f"Produto: {produto}")
print(f"Preço unitário: R$ {preco_unitario:.2f}")
print(f"Quantidade: {quantidade}")
print(f"Total: R$ {total:.2f}")
print("===================")