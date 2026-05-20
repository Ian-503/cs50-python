expressao = input("Expression: ").strip()
x, y, z = expressao.split(" ")
x=float(x)
z=float(z)

if y == "+":
    conta=x+z
    print(f"{conta:.1f}")

elif y == "-":
    conta=x-z
    print(f"{conta:.1f}")

elif y == "*":
    conta=x*z
    print(f"{conta:.1f}")

elif y == "/":
    conta=x/z
    print(f"{conta:.1f}")
