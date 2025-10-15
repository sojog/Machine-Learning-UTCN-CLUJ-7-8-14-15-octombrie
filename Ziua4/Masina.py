
class Masina:
    def __init__(self, an_fabricatie, cai_putere):
        self.an_fabricatie = an_fabricatie
        self.cai_putere = cai_putere

    def __str__(self):
        return f"Masina din {self.an_fabricatie}  are {self.cai_putere}"
    

if __name__ == "__main__":
    masina1 = Masina(2015, 150)
    masina2 = Masina(2020, 70)

    print(masina1)
    print(masina2)

        