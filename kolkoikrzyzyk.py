plansza = ["n", "o", "x", "n", "o", "n", "o", "x", "n"]
# plansza = ["o", "o", "x", "n", "o", "n", "o", "x", "o"]
# n - puste pole, o - kółko, x - krzyżyk

def wyswietl_plansze(plansza):
    for i in range(9):
        print(plansza[i], end=" ")
        if (i+1)%3 == 0:
            print()
    print()

# return x - wygrywa krzyżyk, o - wygrywa kołko, n - brak wygranego
def czy_wygrana(plansza):
    # na skos
    if plansza[4] == plansza[0] == plansza[8] or plansza[4] == plansza[2] == plansza[6]:
        if plansza[4] == "o":
            return "o"
        elif plansza[4] == "x":
            return "x"
    
    # pion 1
    if plansza[0] == plansza[3] == plansza[6]:
        if plansza[0] == "o":
            return "o"
        elif plansza[0] == "x":
            return "x"
    # pion 2
    if plansza[1] == plansza[4] == plansza[7]:
        if plansza[1] == "o":
            return "o"
        elif plansza[1] == "x":
            return "x"
    # pion 3
    if plansza[2] == plansza[5] == plansza[8]:
        if plansza[2] == "o":
            return "o"
        elif plansza[2] == "x":
            return "x"
    
    # wiersz 1
    if plansza[0] == plansza[1] == plansza[2]:
        if plansza[0] == "o":
            return "o"
        elif plansza[0] == "x":
            return "x"
    # wiersz 2
    if plansza[3] == plansza[4] == plansza[5]:
        if plansza[3] == "o":
            return "o"
        elif plansza[3] == "x":
            return "x"
    # wiersz 3
    if plansza[6] == plansza[7] == plansza[8]:
        if plansza[6] == "o":
            return "o"
        elif plansza[6] == "x":
            return "x"
    
    if "n" not in plansza:
        return "pat"

    return "n"

wyswietl_plansze(plansza)
# print(czy_wygrana(plansza))

wygrywa_x = []
wygrywa_o = []
remis = []

# True - x, False - o
def kolejny_ruch(plansza, kto):
    global wygrywa_o, wygrywa_x, remis
    if kto == True:
        dodaj = "x"
    else:
        dodaj = "o"

    for i in range(9):
        if plansza[i] == "n":
            temp_plansza = plansza.copy()

            temp_plansza[i] = dodaj

            temp_wynik = czy_wygrana(temp_plansza)

            # wyswietl_plansze(temp_plansza)
            # print(temp_wynik)
            
            if temp_wynik == "x":
                wygrywa_x.append(temp_plansza)
            elif temp_wynik == "o":
                wygrywa_o.append(temp_plansza)
            elif temp_wynik == "pat":
                remis.append(temp_plansza)
            else:
                kolejny_ruch(temp_plansza, not kto)
            

kolejny_ruch(plansza, True)

print("zaczyna x")

print("scenariusze wygrany o: ")
for i in wygrywa_o:
    wyswietl_plansze(i)

print("\nscenariusze wygrany x: ")
for i in wygrywa_x:
    wyswietl_plansze(i)

print("\nscenariusze remisu: ")
for i in remis:
    wyswietl_plansze(i)