import random, time, keyboard
kolory = ["Pik","Kier","Trefl","Karo"]
numery = ["Dwa","Trzy","Cztery","Piec","Szesc","Siedem","Osiem","Dziewiec","Dziesiec","Walet","Dama","Krol","As"]
wartosci = {"Dwa":2,"Trzy":3,"Cztery":4,"Piec":5,"Szesc":6,"Siedem":7,"Osiem":8,"Dziewiec":9,"Dziesiec":10,"Walet":11,"Dama":12,"Krol":13,"As":14}

class Karta():
    def __init__(self,kolor,numer):
        self.kolor = kolor
        self.numer = numer
        self.wartosc = wartosci[numer]
    def __str__(self):
        return self.numer + " " + self.kolor

class Talia():
    def __init__(self) -> None:
        self.deck = []
        for kolor in kolory:
            for numer in numery:
                nowa_karta = Karta(kolor,numer)
                self.deck.append(nowa_karta)

    def shuffle(self):
        random.shuffle(self.deck)
    
    def rozdanie_karty(self):
        return self.deck.pop()

class Gracz():

    def __init__(self,name) -> None:
        self.name = name
        self.reka = []

    def wykladanie_karty(self):
        return self.reka.pop(0)

    def odbieranie_kart(self,nowe_karty):
        if type(nowe_karty) == type([]):
            self.reka.extend(nowe_karty)
        else:
            self.reka.append(nowe_karty)

def przerwanie_gry():
    if len(gracz_1.reka) > len(gracz_2.reka):
        print(f"Gracz {gracz_1.name} wygrywa przez większą ilość kart")
    elif len(gracz_1.reka) < len(gracz_2.reka):
        print(f"Gracz {gracz_2.name} wygrywa przez większą ilość kart")
    else:
        print("Jest remis")

if __name__ == "__main__":
    print("Witajcie w grze WOJNA!!")
    print("Zasady: Pierwszy i drugi zawodnik równocześnie wykładają po jednej karcie i porównują ich wartości (względem starszeństwa – kolory nie odgrywają roli).") 
    print("Gracz mający kartę o wyższej wartości odbiera karty i kładzie je pod spodem swojej talii. Jeśli karty mają taką samą siłę (as na asa, król na króla, itp.), rozpętuje się wojna")
    print("Wyciągane są pięc kart. Ostatnia wyciągnieta karta o wyższej wartości wygrywa, a zwycięzca wojny odbiera wszystkie karty wykorzystane w wojnie. Proces jest powtarzany, jeśli w okresie wojny znowu nie można wyłonić zwycięzcy. ")
    print("Przy pytaniu o kontynuacji gry wpisanie 'q' kończy grę i wyznacza zwycięzcę na podstawie ilości kart graczy")
    print(" ")
    gracz_1 = Gracz(input("Podaj swoje imię pierwszy graczu: "))
    gracz_2 = Gracz(input("Podaj swoje imię drugi graczu: "))
    nowa_talia=Talia()
    nowa_talia.shuffle()
    ilosc_wojn = 0

    for i in range(26):
        gracz_1.odbieranie_kart(nowa_talia.rozdanie_karty())
        gracz_2.odbieranie_kart(nowa_talia.rozdanie_karty())
    
    game_on = True
    Ilosc_rund = 0

    while game_on:
        print(" ")
        Ilosc_rund += 1
        print(f'Runda {Ilosc_rund}')
        
        if len(gracz_1.reka) == 0:
            print(f"Gracz {gracz_1.name} nie ma kart \nWygrawa Gracz {gracz_2.name}")
            print(f'Ilosc wojn w rozgrywce {ilosc_wojn}')
            game_on = False
            break
        if len(gracz_2.reka) == 0:
            print(f"Gracz {gracz_2.name} nie ma kart \nWygrawa Gracz {gracz_1.name}")
            print(f'Ilosc wojn w rozgrywce {ilosc_wojn}')
            game_on = False
            break

        gracz_1_karty = []
        gracz_1_karty.append(gracz_1.wykladanie_karty())
        gracz_2_karty = []
        gracz_2_karty.append(gracz_2.wykladanie_karty())
        
        print(f"Gracz {gracz_1.name}")
        time.sleep(0.5)
        print(gracz_1_karty[0])
        print("")
        print(f"Gracz {gracz_2.name}")
        time.sleep(0.5)
        print(gracz_2_karty[0])
        print("")
        jest_wojna = True
        while jest_wojna:
            if gracz_1_karty[-1].wartosc > gracz_2_karty[-1].wartosc:
                gracz_1.odbieranie_kart(gracz_1_karty)
                gracz_1.odbieranie_kart(gracz_2_karty)
                print(f"Potyczkę wygrał {gracz_1.name}")
                jest_wojna = False

            elif gracz_1_karty[-1].wartosc < gracz_2_karty[-1].wartosc:
                gracz_2.odbieranie_kart(gracz_1_karty)
                gracz_2.odbieranie_kart(gracz_2_karty)
                print(f"Potyczkę wygrał {gracz_2.name}")
                jest_wojna = False

            else:
                print(" ")
                print("Wojna!!")
                print(" ")
                ilosc_wojn +=1
                if len(gracz_1.reka) < 3:
                    print(f"Gracz {gracz_1.name} nie jest w stanie wypowiedziec wojny \nGracz {gracz_2.name} wygrywa")
                    print(f'Ilosc wojn w rozgrywce {ilosc_wojn}')
                    game_on = False
                    break
                elif len(gracz_2.reka) < 3:
                    print(f"Gracz {gracz_2.name} nie jest w stanie wypowiedziec wojny \nGracz {gracz_1.name} wygrywa")
                    print(f'Ilosc wojn w rozgrywce {ilosc_wojn}')
                    game_on = False
                    break
                else:
                    for num in range(5):
                        gracz_1_karty.append(gracz_1.wykladanie_karty())
                        gracz_2_karty.append(gracz_2.wykladanie_karty())
                        time.sleep(0.2)
                        print(gracz_1_karty[-1], gracz_2_karty[-1],sep = " vs ")
        print(" ")
        print(f"Gracz {gracz_1.name} ma {len(gracz_1.reka)} kart")
        print(f"Gracz {gracz_2.name} ma {len(gracz_2.reka)} kart")

        while True: 
            koniec = input("Wciśnij enter aby kontynuować lub q aby zakończyć gre: ")
            if koniec == "":
                break
            elif koniec == 'q':    
                game_on = False
                przerwanie_gry()
                break
            else:
                print("Pamiętaj używaj tylko enter lub q")
