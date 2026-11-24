
import ollama
import time

# Sem doplň přesné názvy svých modelů
MODELY = [
    "llama3.2:1b",
    "lfm3-omni"
]

klient = ollama.Client(
    host="http://localhost:11434",
    trust_env=False
)

ulohy = [
    {
        "nazev": "Logické uvažování",
        "zadani": """
        Petr je vyšší než Pavel.
        Pavel je vyšší než Karel.
        Kdo je nejnižší a proč?
        """
    },
    {
        "nazev": "Matematika",
        "zadani": """
        Maminka koupila 3 trička za 250 Kč za kus
        a 2 kalhoty za 450 Kč za kus.
        V obchodě dostala slevu 15 % na celý nákup.
        Kolik zaplatila?
        Ukaž postup výpočtu.
        """
    },
    {
        "nazev": "Programování",
        "zadani": """
        Napiš Python funkci, která zjistí,
        zda je zadané číslo prvočíslo.
        Přidej také tři příklady použití.
        """
    },
    {
        "nazev": "Porozumění textu",
        "zadani": """
        Jana šla do obchodu koupit jablka.
        Měla 100 Kč, koupila jablka za 35 Kč
        a rohlíky za 20 Kč.
        Cestou domů našla 50 Kč.
        Kolik peněz jí zbylo po nákupu?
        """
    },
    {
        "nazev": "Kreativita",
        "zadani": """
        Napiš krátký příběh o robotovi,
        který se poprvé dostane do školy.
        Příběh musí mít maximálně 100 slov.
        """
    }
]

for model in MODELY:
    print("\n" + "=" * 60)
    print("TESTUJI MODEL:", model)
    print("=" * 60)

    for uloha in ulohy:
        print("\nÚLOHA:", uloha["nazev"])

        zacatek = time.time()

        try:
            odpoved = klient.chat(
                model=model,
                messages=[
                    {
                        "role": "user",
                        "content": uloha["zadani"]
                    }
                ]
            )

            konec = time.time()

            vysledek = odpoved["message"]["content"]

            print(vysledek)
            print("\nČas odpovědi:",
                  round(konec - zacatek, 2), "sekund")

        except Exception as chyba:
            print("CHYBA:", chyba)

        print("\n" + "-" * 60)
