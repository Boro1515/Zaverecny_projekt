from seznam import seznam_lidi

class Uzivatele:
    def __init__(self, jmeno, prijmeni, vek, telefon):
        self.jmeno = jmeno
        self.prijmeni = prijmeni
        self.vek = vek
        self.telefon = telefon


    def __str__(self):
        return f"{self.jmeno, self.prijmeni, self.vek, self.telefon}"


    def uloz_do_seznamu(self):
        seznam_lidi.append((self.jmeno, self.prijmeni, self.vek, self.telefon))


    def vypsat_vsechny(self):
        for jm, pr, ve, tel in seznam_lidi:
            print(f"\nJméno: {jm}, Příjmení: {pr}, Věk: {ve}, Telefoní číslo: {tel}")


    def vyhledat(self, jmeno, prijmeni):
        nalezeno = False
        for osoba in seznam_lidi:
            if osoba[0] == jmeno and osoba[1] == prijmeni:
                print(f"\nJméno: {osoba[0]}, Příjmení: {osoba[1]}, Věk: {osoba[2]}, Telefon: {osoba[3]}")
                nalezeno = True
        if not nalezeno:
            print("Pojištenec nenalezen")


    def konec(self):
        print("\nPřejeme krásný den, nashledanou")






