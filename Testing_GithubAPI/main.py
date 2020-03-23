from person import Person
from hello_world import Hello_World

def main():
    # tworzymy dwa obiekty klasy Osoba
    Jan = Person("Jan", "Nowak", 48)
    Adam = Person("Adam", "Mickiewicz", 220)

    # wywołujemy metodę przedstaw_sie() na każdym z nich
    Jan.przedstaw_sie()
    Adam.przedstaw_sie()

    wiek_Adama_przed = Adam.urodziny()
    Adam.przedstaw_sie()
    print(f"Wiek Adama sprzed urodzin: {wiek_Adama_przed}")

    # odwołujemy się do pól, modyfikujemy je
    Jan.imie = "Hugo"
    Jan.nazwisko = "Gumis"
    Jan.wiek = 5

    Jan.przedstaw_sie()

    hello = Hello_World("Ania")
    hello.przywitaj_sie()


if __name__ == "__main__":
    main()
