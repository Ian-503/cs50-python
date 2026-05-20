comprimento=input("how you doing?: ")
comprimento=comprimento.lower()
comprimento=comprimento.strip()
if comprimento.startswith("hello"):
    print("$0")
elif comprimento.startswith("h"):
     print("$20")
else:
     print("$100")
