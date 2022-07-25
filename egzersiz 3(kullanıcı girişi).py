print("""
****************************
Kullanıcı girişi
****************************
""")

sys_kullanıcı_adı = "mmurat"

sys_parola = "12345"

kullanıcı_adı = input("Kullanıcı Adı: ")
parola = input("Parola: ")

if kullanıcı_adı == sys_kullanıcı_adı and sys_parola != parola :
    print("Parola Hatalı...")

elif kullanıcı_adı != sys_kullanıcı_adı and parola == sys_parola :
    print("Kullanıcı Adı Hatalı...")

elif kullanıcı_adı != sys_kullanıcı_adı and parola != sys_parola :
    print("Kullanıcı adı ve parola hatalı...")

else :
    print("Sisteme başarıyla giriş yapıldı")