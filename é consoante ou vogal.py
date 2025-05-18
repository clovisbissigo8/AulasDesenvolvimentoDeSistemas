#é consoante ou vogal
letra = input("Ensira a letra: ").strip().casefold()
if letra == 'a' and 'e' and 'i' and 'o' and 'u':
    print("Sua letra é uma vogal.")
else:
    print("Sua letra é uma consoante.")

#obs: se caso algo for digitado deferente de uma letra, será considerado vogal.