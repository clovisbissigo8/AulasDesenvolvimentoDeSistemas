#3 numeros organizados de forma decrescente
n1 = float (input("1º número: "))
n2 = float (input("2º número: "))
n3 = float (input("3º número: "))
l = [n1,n2,n3]
l.sort()
l.reverse()
print(l)