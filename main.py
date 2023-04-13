from seznam import seznam_lidi
from uzivatele import Uzivatele

while True:

    print("----------------------------\nEvidence pojištěných\n----------------------------\n")
    vyber_akce = input("Vyberte si akci:\n"
                        "1 - Přidat nového pojištěného\n"
                        "2 - Vypsat všechny pojištěné\n"
                        "3 - Vyhledat pojištěného\n"
                        "4 - Konec\n")

    if not vyber_akce.isdigit():
        print("Musíte zadat číslo!")
        continue

    vyber_akce = int(vyber_akce)

    if vyber_akce < 1 or vyber_akce > 4:
        print("Musíte zadat číslo od 1 do 4!")
        continue


    elif vyber_akce == 1:
        while True:
            jmeno = input("\nZadejte jméno pojištěného:\n")
            if not jmeno.isalpha():
                print("Jméno může obsahovat pouze písmena!")
                continue
            break
        while True:
            prijmeni = input("Zadejte příjmení:\n")
            if not prijmeni.isalpha():
                print("Příjmení může obsahovat pouze písmena!")
                continue
            break
        while True:
            try:
                vek = int(input("Zadejte věk:\n"))
                break
            except ValueError:
                print("Musíte zadat číslice!")
        while True:
            telefon = input("Zadejte telefonní číslo:\n")
            if not telefon.isdigit():
                print("Telefonní číslo musí obsahovat pouze číslice!")
            elif len(telefon) != 9:
                print("Telefonní číslo musí obsahovat 9 číslic!")
            else:
                telefon = int(telefon)
                break
        registrace = Uzivatele(jmeno.strip().capitalize(), prijmeni.strip().capitalize(), vek, telefon)
        registrace.uloz_do_seznamu()
        pokracovat = input("\nData byla uložena. Pokračujte klávesou \"Enter\"...")


    elif vyber_akce == 2:
        vypise_vsechny = Uzivatele
        vypise_vsechny.vypsat_vsechny(seznam_lidi)
        pokracovat = input("\nPokračujte klávesou \"Enter\"...")

    elif vyber_akce == 3:
        vyhleda_pojisteneho = Uzivatele("", "", 0, "")
        vyhleda_pojisteneho.vyhledat(input("\nZadejte jméno pojištěného:\n"),input("Zadejte příjmení pojištěného:\n"))
        pokracovat = input("\nPokračujte klávesou \"Enter\"...")

    elif vyber_akce == 4:
        rozlouceni = Uzivatele
        rozlouceni.konec(seznam_lidi)
        break