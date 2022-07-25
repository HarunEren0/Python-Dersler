vize1 = int(input("Vize 1 notu: "))
vize2 = int(input("Vize 2 notu: "))
final = int(input("Final notu: "))

not1 = (vize1 * 30) / 100 
not2 = (vize2 * 30) / 100
not3 = (final * 40) / 100

toplam_not = not1 + not2 + not3

if toplam_not >= 90 :
    print("AA")

elif toplam_not >= 85 :
    print("BA")

elif toplam_not >= 80 :
    print("BB")

elif toplam_not >= 75 :
    print("CB")

elif toplam_not >= 70 :
    print("CC") 

elif toplam_not >= 65 :
    print("Dc")

elif toplam_not >= 60 :
    print("DD")

elif toplam_not >= 55 :
    print("FD")

else:
    print("FF")