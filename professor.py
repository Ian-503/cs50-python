import random

def main():
    score=0
    level=get_level()
    for i in range(10):
        x=generate_integer(level)
        y=generate_integer(level)
        resposta=x+y
        vidas=3
        while True:
            try:
                tentativa=int(input(f"{x} + {y} = "))
                if tentativa==resposta:
                    score+=1
                    break
                else:
                    vidas-=1
                    print("EEE")

            except ValueError:
                vidas-=1
                print("EEE")
            if vidas==0:
                print(f"{x} + {y} = {resposta}")
                break
    print(f"Score: {score}")

def get_level():
    while True:
        try:
            level=int(input("Level: "))
            if level>=1 and level<=3:
                return level
        except ValueError:
            pass

def generate_integer(level):
    if level == 1:
        return random.randint(0, 9)
    elif level == 2:
        return random.randint(10, 99)
    elif level == 3:
        return random.randint(100, 999)
    else:
        raise ValueError

if __name__ == "__main__":
    main()
