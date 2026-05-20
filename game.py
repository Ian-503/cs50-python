import random
while True:
    try:
        nivel=int(input("Level: "))
        if nivel>0:
            break
    except ValueError:
        pass
escolhido=random.randint(1,nivel)

while True:
    try:
        palpite=int(input("Guess: "))
        if palpite<=0:
            continue

        if palpite==escolhido:
            print("Just right!")
            break
        elif palpite>escolhido:
            print("Too large!")
        elif palpite<escolhido:
            print("Too small!")
    except ValueError:
        pass
