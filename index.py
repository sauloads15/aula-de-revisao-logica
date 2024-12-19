
# idade = int(input("Por favor, informe a sua idade: "))

# if idade < 12:
#     print("Criança")
# elif 12 <= idade <= 17:
#     print("Adolescente")
# elif 18 <= idade <= 59:
#     print("Adulto")
# else:
#     print("Idoso")

# num1 = float(input("Digite o primeiro número: "))
# num2 = float(input("Digite o segundo número: "))
# num3 = float(input("Digite o terceiro número: "))
# maior = max(num1, num2, num3)

# menor = min(num1, num2, num3)

# print(f"O maior número é: {maior}")
# print(f"O menor número é: {menor}")
# atv 3
# pares = 0
# impares = 0
# for i in range(10):
#     numero = int(input(f"Digite o {i+1}º número inteiro: "))
    
#     if numero % 2 == 0:
#         pares += 1
#     else:
#         impares += 1

# print(f"Quantidade de números pares: {pares}")
# print(f"Quantidade de números ímpares: {impares}")

# atv 4
# idades = []

# while True:
#     idade = input("Digite a idade (ou 'sair' para finalizar): ")
#     if idade.lower() == 'sair':  # Condição de saída
#         break
#     try:
#         idades.append(int(idade))  # Adiciona a idade à lista
#     except ValueError:
#         print("Por favor, digite um número válido ou 'sair'.")

# if not idades:
#     print("Nenhuma idade foi informada.")
# else:

#     media_idades = sum(idades) / len(idades)
#     if media_idades <= 25:
#         categoria = "Jovem"
#     elif media_idades <= 60:
#         categoria = "Adulta"
#     else:
#         categoria = "Idosa"
#     print(f"\nA média de idade da turma é {media_idades:.2f}.")
#     print(f"A turma é classificada como: {categoria}")


# #atv5
# numeros = []

# n = int(input("Quantos números você deseja inserir? "))

# if n <= 0:
#     print("O número de entradas deve ser maior que zero.")
# else:
#     for i in range(n):
#         numero = float(input(f"Digite o {i+1}º número: "))
#         numeros.append(numero)
#     menor = min(numeros)
#     maior = max(numeros)
#     soma = sum(numeros)
#     print(f"O menor valor é: {menor}")
#     print(f"O maior valor é: {maior}")
#     print(f"A soma dos valores é: {soma}")

total_gasto = 0
contador_produtos_acima_1000 = 0
nome_produto_mais_barato = ""
preco_produto_mais_barato = float('inf')  
while True:
    nome = input("Digite o nome do produto: ")
    preco = float(input(f"Digite o preço do produto {nome}: R$ "))
    total_gasto += preco
    if preco > 1000:
        contador_produtos_acima_1000 += 1
    if preco < preco_produto_mais_barato:
        preco_produto_mais_barato = preco
        nome_produto_mais_barato = nome
    continuar = input("Deseja continuar inserindo produtos? (sim/não): ").strip().lower()
    if continuar != 'sim':
        break
print("\nResumo da compra:")
print(f"Total gasto: R$ {total_gasto:.2f}")
print(f"Quantidade de produtos acima de R$ 1000: {contador_produtos_acima_1000}")
print(f"Produto mais barato: {nome_produto_mais_barato} - R$ {preco_produto_mais_barato:.2f}")
