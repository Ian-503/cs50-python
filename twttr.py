palavra=input("diga uma frase: ")
NovaPalavra=""
vogal=["a","e","i","o","u","A","E","I","O","U"]
for letra in palavra:
    if letra not in vogal:
        NovaPalavra=NovaPalavra+letra
print(NovaPalavra)
