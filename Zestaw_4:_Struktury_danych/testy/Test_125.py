import unittest
import sys
import io
import os

# Dodanie dynamicznej ścieżki do katalogu nadrzędnego
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.abspath(os.path.join(current_dir, os.pardir))
sys.path.append(parent_dir)
from Zadanie_125 import Zadanie_125

# testy pisze sie kopiujac jedna z tych funkcji i zmieniajac nazwe. trzeba zostawic przedrostek test_<tutaj dowolnosci> 
# jesli funkcja przyjmuje wartosci trzeba dodac do wywolan aby testy dzialaly

class Test_125(unittest.TestCase):
    def test_BrakTestow(self):  # po napisaniu testu usunac ta funkcje
        self.assertEqual("brak napisanych testow do tego zadania","")

    def test_wypisujacy(self):
        # te komendy przejmuja wyniki printa
        captured_output = io.StringIO()
        sys.stdout = captured_output  

        Zadanie_125()

        # przestajemy przejmowac wyniki printa i zwracamy jakie zmienne wypisalo po odpaleniu funkcji
        sys.stdout = sys.__stdout__
        wynik = captured_output.getvalue().strip()  

        prawdziwyWynik = ""
        self.assertEqual(wynik, prawdziwyWynik)

    def test_zwracajacy(self):
        wynik = Zadanie_125()
        prawdziwyWynik = None
        self.assertEqual(wynik, prawdziwyWynik)


if __name__ == "__main__":
    unittest.main()
