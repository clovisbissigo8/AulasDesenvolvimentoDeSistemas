# 1. Soma de 5 números
soma = 0
for i in range(5):
    num = int(input("Digite um número: "))
    soma += num
print("A soma é:", soma)

# 2. Maior e menor de 4 números
numeros = []
for i in range(4):
    num = int(input("Digite um número: "))
    numeros.append(num)
print("Maior número:", max(numeros))
print("Menor número:", min(numeros))

# 3. Quantas vogais tem uma palavra
palavra = input("Digite uma palavra: ")
vogais = "aeiouAEIOU"
quantidade = 0
for letra in palavra:
    if letra in vogais:
        quantidade += 1
print("A palavra tem", quantidade, "vogais")

# 4. Pares entre 6 digitados
pares = []
for i in range(6):
    num = int(input("Digite um número: "))
    if num % 2 == 0:
        pares.append(num)
print("Números pares digitados:", pares)

# 5. Média 
soma = 0
for i in range(4):
    nota = float(input("Digite a nota da prova: "))
    soma += nota
media = soma / 4
print("A média é:", media)

# 6. Tabuada até 10x
num = int(input("Digite um número para ver a tabuada: "))
for i in range(1, 11):
    print(numero, "x", i, "=", num * i)

# 7. Mostrar números de 1 até N
n = int(input("Digite um número N: "))
for i in range(1, n + 1):
    print(i)

# 8. Palavra ao contrário
palavra = input("Digite uma palavra: ")
print("Palavra ao contrário:", palavra[::-1])

# 9. Múltiplo de 3
num = int(input("Digite um número: "))
if num % 3 == 0:
    print("É múltiplo de 3")
else:
    print("Não é múltiplo de 3")

# 10. Mostrar 3 nomes em ordem alfabética
nomes = []
for i in range(3):
    nome = input("Digite o nome: ")
    nomes.append(nome)
nomes.sort()
print("Nomes em ordem alfabética:", nomes) 
