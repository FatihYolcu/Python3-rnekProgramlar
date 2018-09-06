from datetime import *
import time

while True:
    print("               ", "-" * 50)
    print("               ", "-" * 50)
    print("                         Okuma Hızını Hesaplama Uygulaması \n")
    time.sleep(1)
    print("***Okuyacağınız metin iki parağraf şeklinde olmamalıdır."
          "\n***Eğer iki parağraf şeklinde ise parağrafları birleştirdikten sonra ekleyiniz.")
    print("***Sayaç 5'i gösterdikten sonra , yazınız ekrana basıldığı anda "
          "\nokuma hızınız ölçülmeye başlayacaktır!!\n")
    time.sleep(1)
    yazı=input("Okumak istediğiniz metni buraya giriniz :")

    while True:
        a = 0
        time.sleep(2)
        a=int(input("\n*Okuma metnini , başlatmak için 1'i tuşlayınız:"))
        if a==1:
            print("\nBaşlatılıyor....")
            for i in range(0,5):
                i+=1
                print(i)
                time.sleep(1)
            time.sleep(1)
            print("\nMETİN :",yazı,"\n")
            yaz=yazı.split(" ")
            ilk=datetime.now()
            b=int(input("Tamamladığınızda hesaplamaya geçmek için 2'yi tuşlayınız."))
            if b==2:
                son=datetime.now()
                hız = son - ilk
                saniye=hız.total_seconds()
                kelime_bası_saniye =round(len(yaz)/saniye,1)
                dakika=saniye/60
                dakikada_topkelime=round(((60*len(yaz))/saniye),1)
                print("\nBaşarı ile durduruldu.\n")
                time.sleep(1)
                print("Okuma hızınız hesaplanıyor....\n")
                time.sleep(1)
                print("*{} Saniyede \n*{} Kelime okuduz".format(saniye, len(yaz)))
                print("*{} kelime başı harcadığınız saniye.".format(kelime_bası_saniye))
                time.sleep(1)
                print("*1 Dakikada ortalama {} kelime okuma hızına sahipsiniz.\n".format(dakikada_topkelime))
                time.sleep(1)
                print("***Seviyenizi Belirleyiniz***\n")
                time.sleep(1)
                print("1-)80-160 k/dk")
                time.sleep(1)
                print("2-)160-220 k/dk")
                time.sleep(1)
                print("3-)220–320 k/dk")
                time.sleep(1)
                print("3-)320-500 k/dk")
                time.sleep(1)
                print("4-)500–800 k/dk")
                time.sleep(1)
                print("5-)800–1300 k/dk\n")
                time.sleep(1)
                seviye = int(input("Seviyenizi seçiniz:"))
                if seviye==1:
                    time.sleep(1)
                    print("\nYavaş okuyucu.Böyle çok yavaş bir hızda , düşük bir\n "
                          "konsantrasyon vardır. bu hızdaki okuyucuların genellikle\n"
                          " anlama oranları da düşüktür.\n")
                    time.sleep(1)
                    print("Başa döndürülüyor....")
                    time.sleep(1)
                    break
                elif seviye==2:
                    time.sleep(1)
                    print("\nBu değer Türkiye ortalamasıdır.Bu hızdaki konsantrasyon"
                          "\nve anlama oranı da genellikle düşüktür.\n")
                    time.sleep(1)
                    print("Başa döndürülüyor....")
                    time.sleep(1)
                    break
                elif seviye == 3:
                    time.sleep(1)
                    print("\nBu aralık Türkiye’de hemen hemen ortalama üstü iken, bu değer"
                          "\nbirçok batı ülkesinde sadece ortalamadır.\n")
                    time.sleep(1)
                    print("Başa döndürülüyor....")
                    time.sleep(1)
                    break
                elif seviye == 4:
                    time.sleep(1)
                    print("\nBu değer hem Türkiye, hem de gelişmiş batı ülkeler "
                          "\nokuma hızı ortalamalarına göre hızlı bir okuma değeridir."
                          "\nBu hız aralığında okuyan çoğu kişinin interaktif ve doğru"
                          "\nbir hızlı okuma eğitimine veya kursuna katıldığı"
                          "\nanlaşılmaktadır. Bu guruptaki okuyucuların okuma"
                          "\nhızlarıyla birlikte anlama oranları da yüksektir.\n")
                    time.sleep(1)
                    print("Başa döndürülüyor....")
                    time.sleep(1)
                    break
                elif seviye == 5:
                    time.sleep(1)
                    print("\nFiziksel açıdan dakikada 1300 kelime üzerine çıkmak"
                          "\nteorik olarak imkansızdır. Bu aralıkta çok hızlı okuyan"
                          "\nokuyucular genellikle dakikada 500 - 800 aralığındaki okuma"
                          "\nhızına oranla, bir miktar anlama kaybına uğrarlar. Ancak"
                          "\nbazı çok özel hızlı okuma eğitimlerinde dakikada 800 kelimenin"
                          "\nüzerindeki okumalarda da anlama oranını yüksek tutmayı sağlayan"
                          "\nözel stratejiler öğretilmektedir.\n")
                    time.sleep(1)
                    print("Başa döndürülüyor....")
                    time.sleep(1)
                    break
                else:
                    time.sleep(1)
                    print("Hatalı değer girdiniz.\n\nBaşa döndürülüyor.....")
                    break
            else:
                time.sleep(1)
                print("Hatalı değer girdiniz.\n\nBaşa döndürülüyor.....")
                break
        else:
            time.sleep(1)
            print("Hatalı değer girdiniz.\n\nBaşa döndürülüyor.....")
            break
"""ÖRNEK METİN ==Gregor Samsa bir sabah huzursuz düşlerinden uyandığında,kendini yatağında korkunç bir haşereye dönüşmüş buldu.Zırha benzeyen kaskatı sırtı üzerinde uzanmıştı, kafasınıbiraz kaldırınca kemersi çizgilerle bölünmüş kabarık kahverengi karnını gördü, karnının tepesindeki yorgan zar zor tutunabiliyordu,tamamen sıyrılıp düşmek üzereydi. Geri kalan cüssesine oranla acınacak kadar sıska olan sıra sıra bacakları, gözleri önünde çaresizce parıldıyordu. “Bana ne oldu?” diye düşündü. Bu bir düş değildi. Odası doğru düzgün, sadece biraz ufak bir insan odasıydı bu– gayet iyi bildiği dört duvarın arasında sakince duruyordu. Tuhafiye ürünleri numunelerinin serili bulunduğu –Samsa gezici satış mümessiliydi masanın üzerinde, kısa zaman önce   resimli bir dergiden kesip hoş bir altın varaklı çerçeveye yerleştirdiği resim asılıydı. Resim, kürklü bir şapka ve kürk boyunluk takınmış, dik oturan ve kolunun alt kısmını tamamen kapatan ağır bir el kürkünü izleyene doğru kaldıran bir hanımı tasvir ediyordu. Gregor’un bakışı sonra pencereye yöneldi, puslu hava  yağmur damlalarının pencerenin sac pervazına vurduğu""""
