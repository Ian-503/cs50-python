import emoji

entrada=input("Input: ")

resultado=emoji.emojize(entrada, language='alias')

print(f"Output: {resultado}")
