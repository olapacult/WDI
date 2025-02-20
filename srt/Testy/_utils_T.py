RAMKA = "# ====================================================================================================>\n"

NAGLOWEK = "class testy(unittest.TestCase):\n"

IMPORTY = "import unittest\nimport io\nimport os\nimport sys\nfrom contextlib import redirect_stdout\nimport importlib\n"

ODPAL_TESTY = "def odpal_testy():\n    suite = unittest.TestLoader().loadTestsFromTestCase(testy)\n    unittest.TextTestRunner(verbosity=2).run(suite)\n"

KOMENDA = f"""
def komenda(k: str, *args, **kwargs):
    \"\"\"
    Wykonuje zadaną komendę z przekazanymi argumentami.
    Dodanie wlasnej komendy ogranicza sie do dodania pliku z funkcja o tej samej nazwie
    w folderze glownym projektu src/Komendy
    Wiecej informacji o dodaniu wlasnej komendy jak i lista komend w ReadMe projektu

    Args:
        k (str): Komenda do wykonania.
        *args: Dodatkowe argumenty do komendy.
        **kwargs: Dodatkowe argumenty kluczowe do komendy.
    \"\"\"
    sciezka_pliku_wykonalnego = os.path.abspath(sys.argv[0])
    srt_dir = os.path.join( os.path.dirname(sciezka_pliku_wykonalnego), "../../srt")
    sys.path.append(srt_dir)
    nr_zadania = os.path.dirname(sciezka_pliku_wykonalnego)
    return importlib.import_module("WykonajKomende").wykonaj_komende(
        k, sciezka_pliku_wykonalnego, nr_zadania, *args, **kwargs
    )
"""


def dynamiczny_import_funkcji(nr_zadania, funkcje):
    funkcjeStr = ", ".join(funkcja.__name__ for funkcja in funkcje)
    return f"from szablon{nr_zadania} import {funkcjeStr}\n"


def nazwi_zmienne(zmienne):
    def przetworz_zmienna(z):
        nazwa = ""
        if isinstance(z, (int, float)):
            nazwa = f"minus_{abs(z)}" if z < 0 else str(z)
            if isinstance(z, float):
                nazwa = nazwa.replace(".", "_")
                nazwa += "f"

        elif isinstance(z, list):
            # Sprawdzamy, czy to zagnieżdżona lista
            nazwa = "tablica"
        return nazwa

    zmienne_nazwa = [przetworz_zmienna(z) for z in zmienne]
    return zmienne_nazwa


def metoda_zwracajaca_testow_zaokraglona(
    NazwaTestu, numerTestu, zmienne, wynikWywolania
):
    zmienne_nazwa = nazwi_zmienne(zmienne)
    return f"""    def test_Nr{numerTestu}_{NazwaTestu}_argumenty_{'_'.join(zmienne_nazwa)}(self):
        wynik  = {NazwaTestu}({', '.join(map(str, zmienne))})

        oczekiwany_wynik = { wynikWywolania }
        self.assertAlmostEqual(wynik, oczekiwany_wynik, places=4)\n"""


def metoda_nasluchujaca_testow_zaokraglona(
    NazwaTestu, numerTestu, zmienne, wynikWywolania
):
    zmienne_nazwa = nazwi_zmienne(zmienne)

    return f"""    def test_Nr{numerTestu}_{NazwaTestu}_argumenty_{'_'.join(zmienne_nazwa)}(self):
        f = io.StringIO()
        with redirect_stdout(f):
            {NazwaTestu}({', '.join(map(str, zmienne))})
        wynik = f.getvalue().strip()

        oczekiwany_wynik = { wynikWywolania }
        self.assertAlmostEqual(wynik, oczekiwany_wynik, places=4)\n"""


def metoda_zwracajaca_testow(NazwaTestu, numerTestu, zmienne, wynikWywolania):
    zmienne_nazwa = nazwi_zmienne(zmienne)
    return f"""    def test_Nr{numerTestu}_{NazwaTestu}_argumenty_{'_'.join(zmienne_nazwa)}(self):
        wynik  = {NazwaTestu}({', '.join(map(str, zmienne))})

        oczekiwany_wynik = [{ wynikWywolania }]
        self.assertIn(wynik, oczekiwany_wynik)\n"""


def metoda_nasluchujaca_testow(NazwaTestu, numerTestu, zmienne, wynikWywolania):
    zmienne_nazwa = nazwi_zmienne(zmienne)

    return f"""    def test_Nr{numerTestu}_{NazwaTestu}_argumenty_{'_'.join(zmienne_nazwa)}(self):
        f = io.StringIO()
        with redirect_stdout(f):
            {NazwaTestu}({', '.join(map(str, zmienne))})
        wynik = f.getvalue().strip()

        oczekiwany_wynik = [{ wynikWywolania }]
        self.assertIn(wynik, oczekiwany_wynik)\n"""
