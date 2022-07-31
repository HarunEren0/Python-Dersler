print("""
************************************
Atm Makinesine Hoşgeldiniz.

İşlemler;

1) Bakiye Sorgulama

2) Para Yatırma

3) Para Çekme

Programdan çıkmak için 'q' ya basın.
*************************************
""")


bakiye = 1000

while True:
    işlem = input("İşlemi Seçin: ")
    
    if işlem == "q":
        print("Yine Bekleriz")
        break
    elif işlem == "1" :
        print("bakiyeniz {} TL dir.".format(bakiye))

    elif işlem == "2":
        miktar = int(input("Miktarı Giriniz: "))
        bakiye += miktar

    elif işlem == "3":
        miktar = int(input("Miktarı Giriniz: "))
        
        if bakiye - miktar < 0 :
            print("Böyle bir miktar çekemezsiniz...")
            continue
        bakiye -= miktar
    else:
        print("Geçersiz işlem...")