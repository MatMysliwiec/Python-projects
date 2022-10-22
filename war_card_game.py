import random, time
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

if __name__ == "__main__":
    
    gracz_1 = Gracz("1")
    gracz_2 = Gracz("2")
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
        print(gracz_1_karty[0], gracz_2_karty[0],sep = " vs ")
        time.sleep(0.2)
        jest_wojna = True
        while jest_wojna:
            if gracz_1_karty[-1].wartosc > gracz_2_karty[-1].wartosc:
                gracz_1.odbieranie_kart(gracz_1_karty)
                gracz_1.odbieranie_kart(gracz_2_karty)
                jest_wojna = False

            elif gracz_1_karty[-1].wartosc < gracz_2_karty[-1].wartosc:
                gracz_2.odbieranie_kart(gracz_1_karty)
                gracz_2.odbieranie_kart(gracz_2_karty)
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
                    for num in range(3):
                        gracz_1_karty.append(gracz_1.wykladanie_karty())
                        gracz_2_karty.append(gracz_2.wykladanie_karty())
                        print(gracz_1_karty[-1], gracz_2_karty[-1],sep = " vs ")
                        time.sleep(0.2)
