def convert(frase):
    frase=frase.replace(":)", "🙂")
    frase=frase.replace(":(", "🙁")
    return frase
def main():
    palavra=str(input("say somenting with a smilying face: "))
    corrigido=convert(palavra)
    print(corrigido)


main()
