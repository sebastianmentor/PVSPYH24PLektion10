# Vad definierar en fruk?

fruktkorg = []

class Frukt:
    def __init__(self, namn, färg, kalorier_per_kilo=None) -> None:
        self.namn = namn
        self.färg = färg
        self.kalorier_per_kilo = kalorier_per_kilo

    def visa_färg(self):
        print(f"Min färg är {self.färg}")
    
    def vilken_frukt_är_du(self):
        print(f"Jag är en {self.namn}")

vår_frukt = Frukt('Banan', 'Gul', 250)
# vår_frukt.vilken_frukt_är_du()
# vår_frukt.visa_färg()
fruktkorg.append(vår_frukt)

if __name__ == "__main__":
    while True:
        print("1. Skapa frukt och lägg i fruktkorgen")
        print("2. Vad finns i fruktkorgen?")
        print("3. Uppdatera kalorier per kilo!")
        print("4. Avsluta")

        val = input("Gör ett val")

        if val == "1":
            frukt_namn = input("Ange fruktnamn: ")
            frukt_färg = input("Ange färg på frukten: ")

            vet_kalorier = input("Vet du kalorier per kilo frukt? (y/n)")

            if vet_kalorier == 'y':
                while True:
                    kalorier_per_kilo = input("Ange kcal/kg: ")

                    if kalorier_per_kilo.isdigit():
                        ny_frukt = Frukt(frukt_namn, frukt_färg, int(kalorier_per_kilo))
                        fruktkorg.append(ny_frukt)
                        break
                    else:
                        print("Inte giltligt heltal! ")
            
            else:
                ny_frukt = Frukt(frukt_namn, frukt_färg)
                fruktkorg.append(ny_frukt)


        elif val == "2":
            for frukt in fruktkorg:
                frukt.vilken_frukt_är_du()
                frukt.visa_färg()
                print(f"Kcal/kg : {frukt.kalorier_per_kilo}")


        elif val == "3":
            frukt_namn = input("Ange fruknamn du vill ändra/lägga till kalorier på: ")

            frukt_att_ändra = None

            for frukt in fruktkorg:
                if frukt_namn == frukt.namn:
                    print("Frukten finns!!")
                    frukt_att_ändra = frukt

            if frukt_att_ändra != None:
                kalorier = input(f"Ange kalorier per kilo för {frukt_att_ändra.namn}: ")

                if kalorier.isdigit():
                    frukt_att_ändra.kalorier_per_kilo = int(kalorier)
                else:
                    print("Ogiltligt tal!! Går tillbaka till menyn!")
            
            else:
                print(f"Finns ingen frukt med namn {frukt_namn}")

        elif val == "4":
            break
        else:
            print("Ogiltligt val!!")
    #   # hit hoppar vi    