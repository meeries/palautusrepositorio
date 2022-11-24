from tuote import Tuote
from ostos import Ostos

class Ostoskori:
    def __init__(self):
        self.kori = {}
        # ostoskori tallettaa Ostos-oliota, yhden per korissa oleva Tuote

    def tavaroita_korissa(self):
        maara = 0
        for tuote in self.kori.values():
            maara += tuote.lukumaara()

        return maara

    def hinta(self):
        hinta = 0
        for tuote in self.kori.values():
            hinta += tuote.hinta()
        return hinta

    def lisaa_tuote(self, lisattava: Tuote):
        if lisattava.nimi in self.kori:
            self.kori[lisattava.nimi].muuta_lukumaaraaa(1)
        else:
            self.kori[lisattava.nimi] = Ostos(lisattava)

    def poista_tuote(self, poistettava: Tuote):
        # poistaa tuotteen
        pass

    def tyhjenna(self):
        pass
        # tyhjentää ostoskorin

    def ostokset(self):
        pass
        # palauttaa listan jossa on korissa olevat ostos-oliot
        # kukin ostos-olio siis kertoo mistä tuotteesta on kyse JA kuinka monta kappaletta kyseistä tuotetta korissa on
