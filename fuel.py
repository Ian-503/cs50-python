while True:
    try:
        quantidade=input("qual a porcentagem?")
        a,b=quantidade.split("/")
        a=int(a)
        b=int(b)
        if a>b:
            continue
        elif a<0:
            continue
        resultado=round((a/b)*100)
        break
    except (ValueError, ZeroDivisionError):
        pass
if resultado>=99:
    print("F")
elif resultado<=1:
    print("E")
else:
    print(f"{resultado}%")
