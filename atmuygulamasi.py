_kartsifresi = 1234
_bakiye = 500
sifre_sayac = 3
login = False

while sifre_sayac > 0:
    if not login:
        sifre = int(input("Lütfen şifrenizi giriniz: "))
        if sifre == _kartsifresi:
            login = True
            print("""
            1. Para Çek    
            2. Para Yatır
            3. Bakiye Sorgulama
            4. Kart İade    
            """)
        else:
            sifre_sayac -= 1
            if sifre_sayac == 0:
                print("Kartınız bloke olmuştur. Lütfen bankanıza başvurunuz!")
                break
    else:
        secim = int(input("\nHangi işlemi yapmak istiyorsunuz: "))
        if secim == 1:
            miktar = int(input("Kaç TL çekmek istiyorsunuz?: "))
            if _bakiye < miktar:
                print("Yeterli bakiyeniz bulunmamaktadır.")
            else:
                _bakiye -= miktar
        elif secim == 2:
            miktar = int(input("Kaç TL yatırmak istiyorsunuz?: "))
            _bakiye += miktar
        elif secim == 3:
            print("Bakiyeniz: {} TL".format(_bakiye))
        elif secim == 4:
            print("Yine bekleriz!")
            break
        else:
            print("Lütfen 1-4 arasında bir değer giriniz!")
else:
    print("Kartınız bloke olmuştur. Lütfen bankanıza başvurunuz!")














