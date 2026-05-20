resposta=input("What is the answer to the great question of life, the universe and everything? ")
resposta=resposta.lower()
resposta=resposta.strip()
if resposta == "42" or resposta =="forty-two" or resposta =="forty two":
    print("Yes")
else:
    print("No")
