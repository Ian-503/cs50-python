arquivo=input("name of a file: ")
arquivo=arquivo.strip()
arquivo=arquivo.lower()


if arquivo.endswith(".gif"):
    print("image/gif")
elif arquivo.endswith(".jpeg"):
    print("image/jpeg")
elif arquivo.endswith(".jpeg"):
    print("image/jpeg")
elif arquivo.endswith(".jpg"):
    print("image/jpeg")
elif arquivo.endswith(".png"):
    print("image/png")
elif arquivo.endswith(".pdf"):
    print("application/pdf")
elif arquivo.endswith(".txt"):
    print("text/plain")
elif arquivo.endswith(".zip"):
    print("application/zip")
else:
    print("application/octet-stream")
