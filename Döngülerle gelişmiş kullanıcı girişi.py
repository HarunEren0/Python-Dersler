print("""
***************************
Kullanıcı Girişi Programı
***************************
""")


sys_kullanıcı_adı = "mmurat"

sys_parola = "12345"
giriş_hakkı = 3

while True:
    kullanıcı_adı = input("Kullanıcı adı: ")
    parola = input("parola: ")

    if (kullanıcı_adı != sys_kullanıcı_adı and parola == sys_parola):
        print("Kullanıcı adı hatalı...")
        giriş_hakkı -= 1
    
    elif (kullanıcı_adı == sys_kullanıcı_adı and parola != sys_parola):
        print("Parola hatalı...")
        giriş_hakkı -= 1
    
    elif (kullanıcı_adı != sys_kullanıcı_adı and parola != sys_parola):
        print("Kullanıcı adı ve parola hatalı...")
        giriş_hakkı -= 1
    
    else:
        print("Sisteme giriş yapıldı...")
        break
    
    if (giriş_hakkı == 0 ):
        print("Giriş hakkınız bitti...")
        break


