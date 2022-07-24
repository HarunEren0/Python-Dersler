print("""*********************************
Hesap Makinesi Programı

İşlemler;

1. Toplama İşlemi

2. Çıkarma İşlemi

3. Çarpma İşlemi

4. Bölme İşlemi

*********************************""")

a = int(input("1. sayı: "))
b = int(input("2. sayı: "))

işlem = input("İşlemi giriniz: ")

if işlem == "1":
    print("{} ile {}'ın toplamı {} dır".format(a,b,a + b))
elif işlem == "2":
    print("{} ile {}'ın farkı {} dır".format(a,b,a - b))
elif işlem == "3":
    print("{} ile {}'ın çarpımı {} dır".format(a,b,a * b))
elif işlem == "4":
    print("{} ile {}'ın bölümü {} dır".format(a,b,a / b))
else:
    print("İşlem Geçersiz")