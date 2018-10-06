import itertools
import time
import sys


print("+"*70)
print("        Fatih YOLCU"*25,"        Fatih YOLCU","")
print("+"*70)
print("         Contact Me : fatihh[dot]yolcu[at]gmail[dot]com")
print(" "*7,"*" * 50)
print(" "*7,"*" * 50)
print(" "*10,"Wordlist Oluşturma Programı'na Hoşgeldiniz")

while True:
    print("\n1-Harf Wordlisti ")
    print("2-Kelime Wordlisti \n")
    #KELİME WORDLİSTİ :-->
    #2'li , 3'lü yapıda wordlist oluşturmak amacı ile yapılmıştır.
    #örnek: fatih 1071 anadolu #3'lü yapı
    #pass:1071anadolufatih
    a = int(input("Oluşturmak istediğiniz wordlist'in numarasını giriniz : "))
    if a==1:
        print("")
        karakter = input("[+] Wordlist'in içinde hangi karakterler bulunsun? :>> ")
        print("")
        alt = int(input("[+]  En az kaç kelime olsun ?  : >>  "))
        k = alt
        print("")
        ust = int(input("[+] En fazla kaç kelime olsun ?  : >>  "))
        n = ust + 1
        print("")
        uzunluk = len(karakter)
        list = []
        kayıtdois = input("[+] Olusturulacak wordlist'in ismini giriniz  :>>> ")
        for ltp in range(k, n):
            ans = uzunluk ** ltp
            list.append(ans)
        topsatır = sum(list)
        time.sleep(1)
        print("[+] Toplam satır sayısı : ", topsatır)
        time.sleep(1)

        time.sleep(1)
        print("\n\n+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n")
        zaman = time.asctime()
        basla = time.time()

        kayıtyeri = open("c:\\new\\harf"+kayıtdois+".txt", 'a')
        for i in range(k, n):
            r = i * 100 / n
            alt = str(r) + ' percent '
            sys.stdout.write("\r%s" % alt)
            sys.stdout.flush()
            kayıtyeri.flush()
            for xs in itertools.product(karakter, repeat=i):
                kayıtyeri.write(''.join(xs) + '\n')
        kayıtyeri.flush()
        kayıtyeri.close()
        sys.stdout.write("\rBaşarı ile tamamlandı...\n")
        time.sleep(1)
        print("\nRapor Oluşturuluyor....")
        time.sleep(2)
        print('\n+++++++++++++++++++++++++ Oluşturma Raporu +++++++++++++++++++++++++++++++++++++\n')
        print('\t [+] Oluşturma başlatıldı                 :   ', zaman)
        son = time.time()
        print('\t [+] Tamamlandı                           :   ', time.asctime())
        toplamzaman = son - basla
        print('\t [+] Oluşturma zamanı                     :   ', toplamzaman, 'saniye')
        print('\n++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
        print("")
        #input("[*] Çıkmak için Enter'e basınız.")
    elif a==2:
        print("\n***Kelimeleri aralarında boşluk bırakarak giriniz\n"
              "aksi taktirde wordlist'iniz hatalı oluşur!!!!")
        print("")
        time.sleep(1)
        karakter = input("[+] Kelimeleri aralarında boşluk bırakarak giriniz  :>> ").split(" ")
        print("")
        alt = int(input("[+]  En az kaç kelime yan yana olsun ?  : >>  "))
        k = alt
        print("")
        ust = int(input("[+] En fazla kaç kelime yan yana olsun ?  : >>  "))
        n = ust + 1
        print("")
        uzunluk = len(karakter)
        list = []
        kayıtdois = input("[+] Olusturulacak wordlist'in ismini giriniz  :>>> ")
        for ltp in range(k, n):
            ans = uzunluk ** ltp
            list.append(ans)
        topsatır = sum(list)
        time.sleep(1)
        print("[+] Toplam satır sayısı : ", topsatır)
        time.sleep(1)

        time.sleep(1)
        print("\n\n+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n")
        zaman = time.asctime()
        basla = time.time()
        kayıtyeri = open("c:\\new\\kelime" + kayıtdois + ".txt", 'a')

        for i in range(k, n):
            r = i * 100 / n
            alt = str(r) + ' percent '
            sys.stdout.write("\r%s" % alt)
            sys.stdout.flush()
            kayıtyeri.flush()
            for xs in itertools.product(karakter, repeat=i):
                kayıtyeri.write(''.join(xs) + '\n')

        kayıtyeri.flush()
        kayıtyeri.close()
        sys.stdout.write("\rBaşarı ile tamamlandı...\n")
        time.sleep(1)
        print("\nRapor Oluşturuluyor....")
        time.sleep(2)
        print('\n+++++++++++++++++++++++++ Oluşturma Raporu +++++++++++++++++++++++++++++++++++++\n')
        print('\t [+] Oluşturma başlatıldı                 :   ', zaman)
        son = time.time()
        print('\t [+] Tamamlandı                           :   ', time.asctime())
        toplamzaman = son - basla
        print('\t [+] Oluşturma zamanı                     :   ', toplamzaman, 'saniye')
        print('\n++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
        print("")



    else:
        print('\n++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n')
        print("Lütfen Belirtilen rakamlardan birini giriniz ! ")
