import inflect
texto=inflect.engine()

nomes=[]
while True:
    try:
        nome=input("Name: ")
        nomes.append(nome)
    except EOFError:
        print()
        break

frase=texto.join(nomes)
print(f"Adieu, adieu, to {frase}")
