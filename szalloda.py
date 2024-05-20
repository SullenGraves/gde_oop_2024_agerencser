## Import modules
from datetime import datetime

## Initialize classes
# Room Parent
# Szoba(szobaszam, ar)
class Szoba:
    def __init__(self, szobaszam, ar):
        self.szobaszam = szobaszam
        self.ar = ar

# Egyagyas class
# EgyagyasSzoba(szobaszam, tv)
class EgyagyasSzoba(Szoba):
    def __init__(self, szobaszam, tv):
        super().__init__(szobaszam, 4500)
        self.tv = tv

# Ketagyas class
# KetagyasSzoba(szobaszam, francia)
class KetagyasSzoba(Szoba):
    def __init__(self, szobaszam, francia):
        super().__init__(szobaszam, 6000)
        self.francia = francia

# Foglalas class
# Foglalas(szoba, datum)
class Foglalas:
    def __init__(self, szoba, datum):
        self.szoba = szoba
        self.datum = datum

# Szalloda class
# Szalloda(nev, csillag)
class Szalloda:
    def __init__(self, nev, csillag):
        self.nev = nev
        self.csillag = csillag
        self.szobak = []
        self.foglalas = []

## Szalloda functions
    # Add room to hotel
    # Szalloda.szobaHozzaad(EgyagyasSzoba(szobaszam, tv))
    # Szalloda.szobaHozzaad(KetagyasSzoba(szobaszam, francia))
    def szobaHozzaad(self, szoba):
        self.szobak.append(szoba)

    # Reserve room on date
    # Szalloda.foglal(szobaszam, datum)
    def foglal(self, szobaszam, datum):
        for foglal in self.foglalas:
            # Check if room is already reserved
            if foglal.szoba.szobaszam == szobaszam and foglal.datum == datum:
                print(" A szoba foglalt ezen a napon!")
                return
        for szoba in self.szobak:
            # Add room to reserved list and return price
            if szoba.szobaszam == szobaszam:
                self.foglalas.append(Foglalas(szoba, datum))
                return szoba.ar

    # Remove reservation
    def lemond(self, szobaszam, datum):
        for foglal in self.foglalas:
            # Check is room is actually reserved
            if foglal.szoba.szobaszam == szobaszam and foglal.datum == datum:
                self.foglalas.remove(foglal)
                return True
        return False

    # List Reservations
    def foglalLista(self):
        for foglal in self.foglalas:
            print(f"\n Szobaszám: {foglal.szoba.szobaszam} - Dátum: {foglal.datum}")

## Initialize class objects
# Initialize Szalloda object
szalloda = Szalloda("The Overlook", 4)

# Initialize and add room objects
szalloda.szobaHozzaad(EgyagyasSzoba("11", True))
szalloda.szobaHozzaad(EgyagyasSzoba("12", False))
szalloda.szobaHozzaad(KetagyasSzoba("21", True))

## Room reservation test
szalloda.foglal("11", datetime(2025, 3, 11))
szalloda.foglal("12", datetime(2025, 4, 12))
szalloda.foglal("21", datetime(2025, 5, 13))

# User interface and controls
while True:
    print("\nVálasszon az alábbi opciók közül:")
    print("1. Szoba foglalása")
    print("2. Foglalás lemondása")
    print("3. Foglalások listázása")
    print("4. Kilépés")
    case = input("Választott opció (1/2/3/4): ")

# 1. Szoba foglalása
    if case == "1":
        szobaszam = input("\nAdja meg a választott szoba számát: ")
        datum = input("Adja meg a foglalás dátumát (ÉÉÉÉ.HH.NN): ")
        try:
            datum = datetime.strptime(datum, "%Y.%m.%d")
            if datum < datetime.now():
                print("\nVálasszon jövőbeni időpontot!")
            else:
                ar = szalloda.foglal(szobaszam, datum)
                if ar:
                    print(f"Sikeres foglalás! A szoba ára: {ar} HUF")
                else:
                    print("A szobaszám nem létezik!")
        except ValueError:
            print("\nHibás formátum!")

# 2. Foglalás lemondása
    elif case == "2":
        szam = input("\nAdja meg a szoba számát: ")
        datum = input("Adja meg a lemondandó dátumot (ÉÉÉÉ.HH.NN): ")
        try:
            datum = datetime.strptime(datum, "%Y.%m.%d")
            valid = szalloda.lemond(szam, datum)
            if valid:
                print("\nFoglalás lemondva.")
            else:
                print("\nNem létezik ilyen foglalás.")
        except ValueError:
            print("\nHibás formátum!")

# 3. Foglalások listázása
    elif case == "3":
        szalloda.foglalLista()

# 4. Kilépés
    elif case == "4":
        break
    # > 4 - Invalid choice
    else:
        print("All work and no play makes Jack a dull boy")
