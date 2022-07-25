print(""""
**********************
EN BÜYÜK SAYIYI BULMA
**********************
""")


sayı1 = int(input("İlk sayıyı giriniz: "))
sayı2 = int(input("İkinci sayıyı giriniz: "))
sayı3 = int(input("Üçüncü sayıyı giriniz: "))

if sayı1 > sayı2 :
    print(sayı1)

elif sayı2 > sayı3 :
    print(sayı2)

elif sayı3 > sayı2 :
    print(sayı3)

elif sayı1 > sayı3 :
    print(sayı1)

elif sayı2 > sayı1 :
    print(sayı2)

elif sayı3 > sayı1 :
    print(sayı3)