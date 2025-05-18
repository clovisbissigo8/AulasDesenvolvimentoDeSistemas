#qual dos dois números é maior
n1 = float (input("Ensira o 1º número: "))
n2 = float (input("Ensira o 2º número: "))
if n1 > n2:
    print(f"O 1º número ({n1}) é maior que o 2º número ({n2}).")
elif n2 > n1:
    print(f"O 2º número ({n2}) é maior que o 1º número ({n1}).")
else:
    print(f"Os números são iguais {n1}, {n2} ")