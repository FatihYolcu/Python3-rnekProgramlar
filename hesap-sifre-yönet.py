import random
import shelve
import time


print("+"*30)
print(" Fatih YOLCU","Fatih YOLCU","")
print("    Fatih YOLCU","Fatih YOLCU","")
print(" Fatih YOLCU","Fatih YOLCU","")
print("    Fatih YOLCU","Fatih YOLCU","")
print("+"*30)
print("Contact Me:>>fatihh[dot]yolcu[at]gmail[dot]com")
print ("\n***HESAP&ŞİFRE programına hoş geldiniz**** \n")
a=input("ŞİFRENİZİ GİRİNİZ(22 basamak):>>>")
print("\nŞifre kontrol ediliyor.........\n")
time.sleep(1)
if a=="1q2w3e4r5t6y7u8ı9o0p*ğ":
    print("***Hoş geldiniz Fatih Bey\n")
    def random_password():
        """Yeni şifre oluştur"""
        print('\n')
        hesadı = input("Hesap adı:>> ")
        kullaniciadi = input("Kullanıcı adı:>> ")
        passuzunluk = input("Şifre uzunluğu:>> ")
        while not passuzunluk.isdigit():
            print ("Hatalı giriş!")
            passuzunluk = input("Şifre uzunluğu:>> ")
        password = pass_olustur(int(passuzunluk))
        baslık = yeni_hes_tamam(hesadı, password, kullaniciadi)
        print (baslık + '\n')


    def manual_input():
        """Manuel hesap/şifre girişi"""
        print('\n')
        hesadı = input("Hesap adı :>> ")
        kullaniciadi = input("Kullanıcı adı :>>")
        password = input("Şifre :>> ")
        baslık = yeni_hes_tamam(hesadı, password, kullaniciadi)
        print (baslık + '\n')


    def find_account():
        """Var olan hesabı bul"""
        print ('\n')
        ara = input("Hangi hesabı arıyorsunuz :>> ")
        f = shelve.open("c:\\new\\winhs\\system32.dat")
        if ara in f:
            hesadı = f[ara]
            print (hesadı)
        else:
            print ("Böyle bir hesap bulunamadı " + ara)
        print ('\n')
        f.close()


    def yeni_hes_tamam(hesadı, password, kullaniciadi):
        """gönder basşlık kayıt etmeye ve return mesaj"""
        baslık = baslık_olustur(hesadı, password, kullaniciadi)
        kayıt(hesadı, baslık)
        return "\nKayıt başarılı.\n" + "\n" + str(baslık) + "\n"


    def baslık_olustur(hesadı, password, kullaniciadi):
        """Başlık oluştur"""
        return "Hesap adı:>> " + hesadı + "\nKullanıcı adı:>> " + kullaniciadi + "\nŞifre:>> " + password


    def kayıt(hesadı, baslık):
        """Kaydedilen hesaplar"""
        f = shelve.open("c:\\new\\winhs\\system32.dat") #kayıt yeri sistem dosyası gibi görünmesi amaçlanmıştır.
        kayıtlar = [baslık]
        f[hesadı] = kayıtlar
        f.sync()
        f.close()


    def silinen_hesaplar():
        """Silinen Hesaplar"""
        print('\n')
        hesadı = input("Hangi hesabı silmek istiyorsunuz?:>> ")
        f = shelve.open("c:\\new\\winhs\\system32.dat") #kayıt yeri sistem dosyası gibi görünmesi amaçlanmıştır.
        if hesadı in f:
            confirm_deletion = input("Simek istediğinize emin misiniz (e/h)? " + hesadı + "?: ")
            if confirm_deletion.lower() in ('evet', 'e','EVET','E'):
                del f[hesadı]
                print ("Hesap silindi.")
            else:
                print ("Silme işlemi iptal edildi. ")
        else:
            print ("Hesap bulunamadı " + hesadı)
        print ('\n')
        f.close


    def tum_hesaplar():
        """Tüm hesapları yazdır : gizli komut"""
        f = shelve.open("c:\\new\\winhs\\system32.dat") #kayıt yeri sistem dosyası gibi görünmesi amaçlanmıştır.
        tumhesaplar = f.keys()
        f.close()
        print (tumhesaplar)
        print ("\n")


    def pass_olustur(passuzunluk):
        """Rastgele  pass karakterleri döndür"""
        alphanumeric_chars = ["0123456789",
                              "abcçdefgğhijklmnoöpqrsştuüvwxyz",
                              "ABCÇDEFGĞHIİJKLMNOÖPQRSŞTUÜVWXYZ"]
        return make_password(passuzunluk, *alphanumeric_chars)


    def make_password(length, *collections_of_characters):
        """Rasgele pass oluştur"""
        characters = set()
        for collection in collections_of_characters:
            characters.update(str(c) for c in collection)
        characters = list(characters)

        password = [random.choice(characters) for _ in range(0, length)]
        return "".join(password)


    def program_start():
        time.sleep(1)
        """Temel"""
        choice = ''
        while choice != "5":
            choice = input("""1-Hesap girişi için 1'
2-Şifre oluşturmak için 2'yi
3-Varolan bir heap için 3'ü
4-Hesap silmek için 4'ü
5-Çıkmak için 5'i tuşlayınız :>>
    """)
            if choice == "1":
                manual_input()
            elif choice == "2":
                random_password()
            elif choice == "3":
                find_account()
            elif choice == "4":
                silinen_hesaplar()
            elif choice == "tüm hesaplar":
                tum_hesaplar()
            else:
                print ("Çıkılıyor...")
                time.sleep(1)
    program_start()
else:
    print("\nDış kapıya yönlendiriliyorsunuz.......")
    time.sleep(2)
