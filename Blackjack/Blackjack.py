import random
kolory = ["Pik","Kier","Trefl","Karo"]
numery = ["Dwa","Trzy","Cztery","Piec","Szesc","Siedem","Osiem","Dziewiec","Dziesiec","Walet","Dama","Krol","As"]
wartosci = {"Dwa":2,"Trzy":3,"Cztery":4,"Piec":5,"Szesc":6,"Siedem":7,"Osiem":8,"Dziewiec":9,"Dziesiec":10,"Walet":10,"Dama":10,"Krol":10,"As":11}

class Karta():

    def __init__(self,kolor,numer) -> None:
        
        self.kolor = kolor
        self.numer = numer
        self.wartosc = wartosci[numer]
    
    def __str__(self) -> str:
        
        return self.numer + " " + self.kolor

class Talia():

    def __init__(self) -> None:
        self.deck = []

        for kolor in kolory:
            for num in numery:
                nowa_karta = Karta(kolor,num)
                self.deck.append(nowa_karta)
    
    def shuffle(self):

        random.shuffle(self.deck)

    def oddanie_kart(self):

        return self.deck.pop()
    
    def __str__(self):

        return self.deck

class Reka():

    def __init__(self):
        self.karty = []
        self.wartosc = 0
        self.asy = 0

    def dodanie_karty(self,karta):
        self.karty.append(karta)
        self.wartosc += wartosci[karta.numer]
        if karta.numer == "As":
            self.asy += 1
            
            
    def wyjatek_as(self):
        while self.wartosc > 21 and self.asy:
            self.wartosc -= 10
            self.asy -= 1

class Chips():

    def __init__(self,total=100):
        self.total = total
        self.bet = 0
    
    def wygrana(self):
        self.total += self.bet

    def przegrana(self):
        self.total -= self.bet

def branie_zakladu(chips):
    
    while True:
        try:
            chips.bet = int(input("Podaj stawke: "))
        except ValueError:
            print("To nie jest liczba")
        else:
            if chips.bet > chips.total:
                print("Nie masz tyle zetonow")
            else:
                break

def hit(deck,reka):
    reka.dodanie_karty(deck.oddanie_kart())
    reka.wyjatek_as()

def hit_lub_stand(deck,reka):
    global game_on
    while True:
        play = input("Czy chcesz dobrac karte czy pasowac ? (wpisz d - dobranie, p - pas): ")

        if play[0].lower() == "d":
            hit(deck,reka)
        elif play[0].lower() == "p":
            print("Gracz spasowal, zagrywa krupier")
            game_on = False
        else:
            print("Podales zle odpowiedz, sprobuj ponownie")
            continue
        break

def show_some(gracz, krupier):
    print("\nReka krupiera:")
    print("<ukryta karta>")
    print(krupier.karty[1])
    print("\nReka gracza: ",*gracz.karty, sep="\n")

def show_all(gracz,krupier):
    print("\nReka krupiera:",*krupier.karty, sep="\n")
    print("Wartosc reki krupiera: ",krupier.wartosc)
    print("\nReka gracza:",*gracz.karty, sep="\n")
    print("Wartosc reki gracza: ",gracz.wartosc)

def wygrana_gracza(gracz,krupier,chips):
    print("\nGracz wygral")
    chips.wygrana()

def przebicie_gracza(gracz,krupier,chips):
    print("\nGracz bust")
    chips.przegrana()

def wygrana_krupiera(gracz,krupier,chips):
    print("\nKrupier wygral")
    chips.przegrana()

def przebicie_krupiera(gracz,krupier,chips):
    print("\nKrupier bust")
    chips.wygrana()

def remis(gracz,krupier):
    print("\nMamy remis")

if __name__ == "__main__":
    game_on = True

    while True:

        print("Witam w grze Blackjack! Krupier podbija do wartosci 17")

        deck = Talia()
        deck.shuffle()

        gracza_reka=Reka()
        gracza_reka.dodanie_karty(deck.oddanie_kart())
        gracza_reka.dodanie_karty(deck.oddanie_kart())

        krupiera_reka=Reka()
        krupiera_reka.dodanie_karty(deck.oddanie_kart())
        krupiera_reka.dodanie_karty(deck.oddanie_kart())

        gracza_zetony=Chips()

        branie_zakladu(gracza_zetony)

        show_some(gracza_reka,krupiera_reka)

        while game_on:

            hit_lub_stand(deck,gracza_reka)

            show_some(gracza_reka,krupiera_reka)

            if gracza_reka.wartosc > 21:
                przebicie_gracza(gracza_reka,krupiera_reka,gracza_zetony)
                break

        if gracza_reka.wartosc <= 21:

            while krupiera_reka.wartosc < 17:
                hit(deck,krupiera_reka)

            show_all(gracza_reka,krupiera_reka)

            if krupiera_reka.wartosc > 21:
                przebicie_krupiera(gracza_reka,krupiera_reka,gracza_zetony)
            elif krupiera_reka.wartosc > gracza_reka.wartosc:
                wygrana_krupiera(gracza_reka,krupiera_reka,gracza_zetony)
            elif krupiera_reka.wartosc < gracza_reka.wartosc:
                wygrana_gracza(gracza_reka,krupiera_reka,gracza_zetony)
            else:
                remis(gracza_reka,krupiera_reka)

        print("\nIlosc zetonow graca po rundzie: ",gracza_zetony.total)
        
        reset_gry = input("CZy chcesz zagrac ponownie? Wpisz tak lub nie: ")

        if reset_gry[0].lower() == 't':
            game_on = True
        else:
            print("Dzieki za gre")
            break