#media de 3 notas é 7 ou >
n1 = float (input("1ª nota: "))
n2 = float (input("2ª nota: "))
n3 = float (input("3ª nota: "))
if (n1+n2+n3)/3 >= 7:
    print(f"Aprovado. Sua média é: {(n1+n2+n3)/3}")
else:
    print(f"Reprovado. Sua média é: {(n1+n2+n3)/3}")