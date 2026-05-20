preco = 50
while preco > 0:
    print(f"Amount Due: {preco}")
    moeda = int(input("Insert Coin: "))
    if moeda in [25, 10, 5]:
        preco = preco - moeda
print(f"Change Owed: {abs(preco)}")
