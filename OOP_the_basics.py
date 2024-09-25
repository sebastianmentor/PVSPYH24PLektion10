class Bil:
    def __init__(self, märke, modell, årsmodell) -> None:
        self.märke = märke
        self.modell = modell
        self.årsmodell = årsmodell

    def brumbrum(self):
        print("Brum brum låter bilen!")

    def skriv_ut_info(self):
        print(self.märke, self.modell, self.årsmodell, id(self))

    


volvo = Bil('Volvo', 'XC90', 2020)
volvo2 = Bil('Volvo', 'XC90', 2020)
bmv = Bil('Bmw','M3', 2021 )

bilar = [volvo, volvo2, bmv]

print(volvo.modell)
print(volvo2.modell)
print(f"{volvo is volvo2=}")
print(f"{volvo is volvo=}")
print(f"{volvo == volvo=}")
print(f"{volvo == volvo2=}")
print(f"{bilar[0]}") # <--- vad skrivs ut?
print(f"{volvo is bilar[0]=}")
print(f"{volvo is bilar[1]=}")
print(f"{volvo is bilar[2]=}")
print('@'*20)
print(id(volvo))
print(id(volvo2))
volvo2 = volvo
print(id(volvo))
print(id(volvo2))
print(f"{volvo is volvo2=}")
print('@'*20)
print(id(bilar[0]))
print(id(bilar[1]))
print(id(bilar[2]))
print('@'*20)
volvo.årsmodell = 2022
print(volvo2.årsmodell) # <-- Vad blir det här? 2020 eller 2022?
print('@'*20)
volvo.skriv_ut_info()
volvo2.skriv_ut_info()
bmv.skriv_ut_info()
print('@'*20)
for bil in bilar:
    bil.skriv_ut_info()

# print(bmv.modell)
