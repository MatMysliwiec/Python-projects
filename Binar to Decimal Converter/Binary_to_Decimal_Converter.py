def bintodec(number: int):
    result = int(number, 2)
    return result


def dectobin(number: int):
    result = bin(number).replace("0b", "")
    return result


print("Zamiana liczby bin na dec - 1", end="\n")
print("Zamiana liczby dec na bin - 2", end="\n")
print("Wyjście z programu - 3", end="\n")

while True:
    choice = input("Podaj opcję: ")

    if choice == "1":
        numberbin = input("Podaj liczbe binarną: ")
        try:
            bin_to_dec = bintodec(numberbin)
            print("Wynik: ", bin_to_dec, end="\n")
        except TypeError:
            print("Nieprawidłowa wprowadzona liczba\n")
        except ValueError:
            print("Nieprawidłowa wprowadzona liczba\n")

    elif choice == "2":
        numberdec = int(input("Podaj liczbe dzesietna: "))
        try:
            dec_to_bin = dectobin(numberdec)
            print("Wynik: ", dec_to_bin, end='\n')
        except TypeError:
            print("Nieprawidłowa wprowadzona liczba\n")
        except ValueError:
            print("Nieprawidłowa wprowadzona liczba\n")

    elif choice == "3":
        print("Wyjście")
        break
