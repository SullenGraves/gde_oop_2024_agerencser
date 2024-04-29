from abc import ABC, abstractmethod


class Szoba(ABC):
    def __init__(self, ar, szobaszam):
        self.ar = ar
        self.szobaszam = szobaszam

        @property
        def ar(self):
            return self.ar


class EgyagyasSzoba(Szoba):
    def __init__(self, ar, szobaszam):
        super().__init__(szobaszam)
        self.ar = 4500


class KetagyasSzoba(Szoba):
    def __init__(self, ar, szobaszam):
        super().__init__(szobaszam)
        self.ar = 6000


class Szalloda:
    def __init__(self, szobak: list[Szoba], nev, csillag):
        self.nev = nev
        self.csillag = csillag

    def foglalas(self):
        pass


class Foglalas:
    def __init__(self, szobak: list[Szoba], datum):
        self.datum = []

    def lemondas(self):
        pass


egyagyas_szobak = [EgyagyasSzoba(EgyagyasSzoba.ar, 1), EgyagyasSzoba(EgyagyasSzoba.ar, 2),
                   KetagyasSzoba(KetagyasSzoba.ar, 3)]
szalloda = Szalloda(egyagyas_szobak, 'the Overlook', 4)