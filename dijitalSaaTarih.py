from tkinter import *
import time
import win32gui
import win32console

window = win32console.GetConsoleWindow()
win32gui.ShowWindow(window,0)

root = Tk()
zaman1 = ''

saat = Label(root, font=('times', 55, 'bold'),fg="green",bg='white')
saat.pack(fill=BOTH, expand=1)

tarih = Label(root, font=('times', 45, 'bold'),fg="green",bg='light blue')
tarih.pack(fill=BOTH, expand=1)
baba = Label(root, font=('vladimir script', 30, 'bold'),fg="green",bg='white')
baba.pack(fill=BOTH, expand=1)
def tick():
    global zaman1
    zaman2 = time.strftime('%H:%M:%S')  # local
    tarih_txt = time.strftime('%d/%m/%Y')

    if zaman2 != zaman1:  # if time string has changed, update it
        zaman1 = zaman2
        saat.config(text=zaman2)
        tarih.config(text=tarih_txt)
        baba.config(text="Fatih YOLCU")


    saat.after(200, tick)

tick()
root.mainloop()
