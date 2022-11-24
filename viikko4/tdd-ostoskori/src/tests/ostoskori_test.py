import unittest
from ostoskori import Ostoskori
from tuote import Tuote

class TestOstoskori(unittest.TestCase):
    def setUp(self):
        self.kori = Ostoskori()

    def test_ostoskorin_hinta_ja_tavaroiden_maara_alussa(self):
        self.assertEqual(self.kori.hinta(), 0)
        self.assertEqual(self.kori.tavaroita_korissa(), 0)

    def test_korissa_yksi_tavara_yhden_lisaamisen_jalkeen(self):
        kakku = Tuote("Kakku", 5)
        self.kori.lisaa_tuote(kakku)
        self.assertEqual(self.kori.tavaroita_korissa(), 1)

    def test_yhden_tuotteen_jalkeen_hinta_oikein(self):
        kakku = Tuote("Kakku", 5)
        self.kori.lisaa_tuote(kakku)
        self.assertEqual(self.kori.hinta(), 5)

    def test_kahden_erituotteen_jalkeen_maara_oikein(self):
        kakku = Tuote("Kakku", 5)
        omena = Tuote("Omena", 5)
        self.kori.lisaa_tuote(kakku)
        self.kori.lisaa_tuote(omena)
        self.assertEqual(self.kori.tavaroita_korissa(), 2)

    def test_kahden_erituotteen_jalkeen_hinta_oikein(self):
        kakku = Tuote("Kakku", 5)
        omena = Tuote("Omena", 5)
        self.kori.lisaa_tuote(kakku)
        self.kori.lisaa_tuote(omena)
        self.assertEqual(self.kori.hinta(), 10)

    def test_kahden_samantuotteen_jalkeen_maara_oikein(self):
        kakku = Tuote("Kakku", 5)
        self.kori.lisaa_tuote(kakku)
        self.kori.lisaa_tuote(kakku)
        self.assertEqual(self.kori.tavaroita_korissa(), 2)

    def test_kahden_samantuotteen_jalkeen_hinta_oikein(self):
        kakku = Tuote("Kakku", 5)
        self.kori.lisaa_tuote(kakku)
        self.kori.lisaa_tuote(kakku)
        self.assertEqual(self.kori.hinta(), 10)

    def test_yhden_tuotteen_jalkeen_yksi_olio(self):
        kakku = Tuote("Kakku", 5)
        self.kori.lisaa_tuote(kakku)
        ostokset = self.kori.ostokset()
        self.assertEqual(len(ostokset), 1)

    def test_yhden_jalkeen_yksi_olio_oikea_nimi(self):
        kakku = Tuote("Kakku", 5)
        self.kori.lisaa_tuote(kakku)
        ostos = self.kori.ostokset()[0]
        self.assertEqual(ostos.tuotteen_nimi(), "Kakku")

    def test_kahden_erituotteen_jalkeen_kaksi_oliota(self):
        kakku = Tuote("Kakku", 5)
        omena = Tuote("Omena", 5)
        self.kori.lisaa_tuote(kakku)
        self.kori.lisaa_tuote(omena)
        ostokset = self.kori.ostokset()
        self.assertEqual(len(ostokset), 2)

    def test_kahden_samantuotteen_jalkeen_yksi_olio(self):
        kakku = Tuote("Kakku", 5)
        self.kori.lisaa_tuote(kakku)
        ostokset = self.kori.ostokset()
        self.assertEqual(len(ostokset), 1)