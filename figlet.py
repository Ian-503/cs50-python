import sys
from pyfiglet import Figlet
import random

figlet=Figlet()
fontes=figlet.getFonts()

if len(sys.argv)==1:
    figlet.setFont(font=random.choice(fontes))
elif len(sys.argv)==3:
    if sys.argv[1]=="-f":
        if sys.argv[2] in fontes:
            figlet.setFont(font=sys.argv[2])
        else:
            sys.exit("Invalid usage")
    elif sys.argv[1]=="--font":
        if sys.argv[2] in fontes:
            figlet.setFont(font=sys.argv[2])
        else:
            sys.exit("Invalid usage")
    else:
        sys.exit("Invalid usage")

else:
    sys.exit("Invalid usage")

texto=input("Input: ")

print("Output:")
print(figlet.renderText(texto))
