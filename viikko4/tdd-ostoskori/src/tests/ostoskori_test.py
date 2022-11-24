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