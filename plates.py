def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(s):
    final_placa = []

    if len(s) < 2 or len(s) > 6:
        return False

    if s[0].isalpha() and s[1].isalpha():
        for c in range(len(s)):
            if not s[c].isalnum():
                return False

            for i in range(2, len(s)):
                if s[i].isdigit():
                    if s[i] not in final_placa:
                        final_placa.append(s[i])

                    if final_placa[0] == "0":
                        return False

                    if not s[i:].isdigit():
                        return False

        return True

    else:
        return False



main()
