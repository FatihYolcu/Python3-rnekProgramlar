import os
import time
import threading

cevap = None
print("\n\n-----------PC KAPATILIYOR----------\n")
time.sleep(1)
print("*30 saniye içinde kapatma gerçekleşecektir\n")
time.sleep(1)
print("*İlk 15 saniye içinde cevap verme hakkınız vardır")
time.sleep(2)
print("\n*Sayaç son 15 saniye saymaya başlayacak.\n")
time.sleep(1)
print("*Çok geç olmadan cevabınızı veriniz.\n")
time.sleep(1)


def kontrol():
    time.sleep(15)

    if cevap =="y":
        print("\nİptal işleminiz başarılı..... ")
        exit()
    elif  cevap == "n":
        print("\nKapatılma işlemine geçiliyor......\n")
        sayac = 15
        while sayac != 0:
            sayac -= 1
            time.sleep(1)
            print(sayac)
        print("\nKapatılma işlemi başarılı bir şekilde başlatıldı. . . ")
        time.sleep(2)
        os.system("shutdown /s /t 1")
    else:
        print("\nKapatılma işlemine geçiliyor......\n")
        sayac = 15
        while sayac != 0:
            sayac -= 1
            time.sleep(1)
            print(sayac)
        print("\nKapatılma işlemi başarılı bir şekilde başlatıldı. . . ")
        time.sleep(2)
        os.system("shutdown /s /t 1")

threading.Thread(target=kontrol).start()
cevap = input("***Kapatmayı iptal etmek istermisiniz ? (y/n):")
