def main():
    hora=input(("what time is it? ")).strip()
    tempo=convert(hora)

    if 7 <= tempo <=8:
        print("breakfast time")
    elif 12 <= tempo <=13:
        print("lunch time")
    elif 18 <= tempo <=19:
        print("dinner time")

def convert(time):
    time=time.replace(":",".")
    hora, min = time.split(".")
    hora=float(hora)
    min=float(min)
    min=min/60
    total=hora+min
    total=float(total)
    return total


if __name__ == "__main__":
    main()
