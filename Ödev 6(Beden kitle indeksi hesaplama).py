


print("""
*****************************
BEDEN KİTLE İNDEKSİ HESAPLAMA
*****************************
""")


boy = float(input("Boyunuzu girin(m): "))
kilo = int(input("Kilonuzu girin: "))

indeks = kilo / boy**2


if indeks <= 18.5 :
    print("Zayıf")

elif indeks <= 25 :
    print("Normal")

elif indeks <= 30 :
    print("Fazla kilolu")

else:
    print("Obez")