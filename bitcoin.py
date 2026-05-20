import requests
import sys
import json

if len(sys.argv) != 2:
    sys.exit("Missing command-line argument")

try:
    quantidade = float(sys.argv[1])
except ValueError:
    sys.exit("Command-line argument is not a number")

try:
    bitcoin = requests.get("https://rest.coincap.io/v3/assets/bitcoin?apiKey=486e723d6af6140540af39b040900ffd089df13922a781ea788de78793ac25d4")
    preco = bitcoin.json()
    preco_bitcoin = float(preco["data"]["priceUsd"])

    valor_total = quantidade * preco_bitcoin
    print(f"${valor_total:,.4f}")

except requests.RequestException:
    sys.exit("Erro de conexão")
