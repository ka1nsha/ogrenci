# -*- coding:cp857 -*-
__author__ = 'ka1nsha'
from tkinter import *
import sqlite3
from tkinter.messagebox import *
from tkinter import ttk
# ###### Veritaban¿ ba¿lant¿s¿ #######
db = sqlite3.connect("db.db3")
cursor = db.cursor()
# ####### Veritaban¿ ba¿lant¿s¿ ######


def kgirisi():
    global db
    global cursor
    global veriler1

    veriler1 = kadi.get()
    veriler2 = sifre.get()
    sorgu = cursor.execute("SELECT * FROM yetkili")
    fsorgu = sorgu.fetchall()

    for k, v in fsorgu:
        if veriler1 == k and veriler2 == v:
            lBilgi.destroy()
            anapencere()
        else:
            kadi.delete(0, END)
            sifre.delete(0, END)
            showwarning("Hata", "E¿le¿tirilemedi,Lütfen tekrar deneyiniz!")

# ##Ana i¿lemler #####
mainwindow = Tk()
mainwindow.geometry("1000x600+200+50")
mainwindow.resizable(width=False, height=False)
pencere = Frame(mainwindow)
mainwindow.wm_title("Ö¿renci Otomasyon Sistemi")
pencere.pack()
lBilgi = Label(pencere, text="Lütfen giri¿ yap¿n¿z", font="Arial 30 bold")
lBilgi.pack()
# ## Ana i¿lemler ####
# ########### Ana pencere ###################


def anapencere():
    login.destroy()

    arac = LabelFrame(pencere, text="Yetkili", width="600")

    bilgi = Label(arac, text="Giri¿ yapan yönetici : %s" % veriler1)
    bilgi.pack(side=LEFT)
    arac.pack(side=LEFT)
    sorgu1 = cursor.execute("select * from ogrenciler order by isim desc")
    sorgucek = sorgu1.fetchall()
    # ######## TTK ################
    container = Frame(width="600")
    tablokismi = LabelFrame(container, text="Kay¿tlar")

    tablo = ttk.Treeview(tablokismi, columns=("isim", "okulno", "tel"))

    tablo.heading("isim", text="Ad ve Soyad :")
    tablo.heading("okulno", text="Numaras¿ :")
    tablo.heading("tel", text="Ebeveyn Telefon numaras¿ :")

    tablo["show"] = "headings"

    for c in sorgucek:
        tablo.insert("", 0, values=(c[0], c[1], c[2]))

    scrollbar = Scrollbar(tablokismi, orient=VERTICAL, command=tablo.yview)
    tablo.configure(yscrollcommand=scrollbar.set)
    scrollbar.pack(side=LEFT, fill=BOTH)

    tablo.pack(side=RIGHT, expand=YES)
    tablokismi.pack(side=RIGHT, padx="20", expand=YES, fill=BOTH)
    # ### Sol Butonlar ###

    oEkle = Button(container, text="Ö¿renci Ekle").pack(padx="20", pady="20")

    container.pack(side=TOP)
    # ### Sol butonlar ###
# ########## Ana pencere #####################

# ####Kullan¿c¿ Giri¿i #######
login = Toplevel()
login.wm_title("Yetkili giri¿i")
login.geometry("200x130+400+200")
login.resizable(width=False, height=False)
bilgi1 = Label(login, text="Kullan¿c¿ Ad¿:")
bilgi1.pack()
kadi = Entry(login)
kadi.pack()
bilgi2 = Label(login, text="Parola:")
bilgi2.pack()
sifre = Entry(login, show="*")
sifre.pack()
onay = Button(login, text="Giri¿", command=kgirisi)
onay.pack()
login.transient(pencere)
# ####### Kullan¿c¿ Giri¿i ######


mainloop()
