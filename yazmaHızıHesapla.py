from datetime import *
import time

while True:
        print("               ","-"*50)
        print("               ","-"*50)
        print("                         Yazma Hızını Hesaplama Uygulaması \n")

        print("10 saniye geriye sayıp hesaplamayı başlatacak !!\n")
        time.sleep(2)
        a=10
        while a>1:
            a-=1
            time.sleep(1)
            print(a)
        time.sleep(1)
        önce = datetime.now()
        yazı = input("\nBaşla: ")

        sonra = datetime.now()

        hız = sonra - önce

        saniye = hız.total_seconds()

        harf_bası_saniye = round(len(yazı) / saniye, 1)

        print("\n*Bitirdin.\n")
        time.sleep(1)
        print("*Yazma hızınız hesaplanıyor..........")
        time.sleep(2)
        print("*Toplam saniye: {}\n*Klavyeden girilen toplam tuş sayısı:{}".format(saniye,len(yazı)))
        time.sleep(1)
        print("*{} Harf başı saniye.\n\n".format(harf_bası_saniye))
        time.sleep(1)
        print("60 saniye sonra tekrar başlatılacak.")
        time.sleep(60)

