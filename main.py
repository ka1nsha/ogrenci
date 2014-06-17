#-*- coding:utf-8 -*-
__author__ = 'ka1nsha'
from tkinter import *
import sqlite3
from tkinter.messagebox import *
from tkinter import ttk
####### Veritabanı bağlantısı #######
db = sqlite3.connect("db.db3")
cursor = db.cursor()
######## Veritabanı bağlantısı ######
def kgirisi():
    global db
    global cursor
    global veriler1
    global veriler2
    veriler1 = kadi.get()
    veriler2 = sifre.get()
    sorgu = cursor.execute("""SELECT * FROM yetkili WHERE kadi="%s"  """ %veriler1)
    fsorgu = sorgu.fetchall()
    for k,v in fsorgu:
        if veriler1 == k and veriler2 == v:
            lBilgi.destroy()
            anapencere()
        else:
            kadi.delete(0, END)
            sifre.delete(0, END)
            showwarning("Hata", "Eşleştirilemedi,Lütfen tekrar deneyiniz!")

###Ana işlemler #####
mainwindow = Tk()
mainwindow.geometry("1000x400+200+50")
mainwindow.resizable(width=False,height=False)
pencere = Frame(mainwindow)

mainwindow.wm_title("Öğrenci Otomasyon Sistemi")
pencere.pack()
lBilgi = Label(pencere,text="Lütfen giriş yapınız",font="Arial 30 bold")
lBilgi.pack()
### Ana işlemler ####
############ Ana pencere ###################

def anapencere():


    ##### Menü #####
    ustmenu = Menu(pencere)
    yetkilimenu = Menu(ustmenu,tearoff=0)
    yetkilimenu.add_command(label="Yetkili ekle",command=yetkiekle)

    ustmenu.add_cascade(label="Yetkili işlemleri",menu=yetkilimenu)
    oturumenusu = Menu(ustmenu,tearoff=0)
    oturumenusu.add_command(label="Şifre değiştir",command=sifredegistir)
    oturumenusu.add_command(label="Kapat",command=mainwindow.quit)
    ustmenu.add_cascade(label="Oturum ayarları",menu=oturumenusu)




    mainwindow.config(menu=ustmenu)
    #### Menü #####
    login.destroy()
    ######### Yetkili kısmı ####
    arac = LabelFrame(pencere, text="Yetkili")

    bilgi = Label(arac, text="""Giriş yapan yönetici : """ + veriler1)
    bilgi.pack(side=LEFT,fill=BOTH)
    arac.pack(side=LEFT,fill=BOTH)

    ### Yetkili kısmı ####



    dtable()

def dtable():
    sorgu1 = cursor.execute("""select * from ogrenciler order by isim desc""")
    sorgucek = sorgu1.fetchall()

    ######### TTK ################
    global tablo,tablokismi,container

    container = Frame()
    tablokismi = LabelFrame(container,text="Kayıtlar")

    tablo = ttk.Treeview(tablokismi,columns=("isim","okulno","tel"))


    tablo.heading("isim",text="Ad ve Soyad :")
    tablo.heading("okulno",text="Numarası :")
    tablo.heading("tel",text="Ebeveyn Telefon numarası :")


    tablo["show"] = "headings"

    for c in sorgucek:
        tablo.insert("",0,values=(c[0],c[1],c[2]))
    scrollbar = Scrollbar(tablokismi,orient=VERTICAL,command=tablo.yview)
    tablo.configure(yscrollcommand=scrollbar.set)
    scrollbar.pack(side=LEFT,fill=BOTH)


    tablo.pack(side=RIGHT,expand=YES)
    tablokismi.pack(side=RIGHT,padx="20",expand=YES,fill=BOTH)
    #### Sol Butonlar ###

    oEkle = Button(container,text="Kayıt Ekle",command=kayitekle).pack(padx="20",pady="20")
    oSil = Button(container,text="Kayıt sil",command=kayitsil).pack()

    #### Sol butonlar ###
    container.pack(side=TOP,pady="50")
def kayitsil():
    if askyesno("Eminmisiniz?","Seçilen kayıt silinicek eminmisiniz?"):
        secilen = tablo.item(tablo.selection())
        numarasi = secilen["values"][1]
        slsorgu = cursor.execute("""DELETE FROM ogrenciler WHERE okulno=%s""" %numarasi)
        db.commit()
        showinfo("Başarılı!","Kayıt silindi!")
        container.destroy()
        dtable()
    else:
        showinfo("","Kayıt silinmedi")

def yetkiekle():
    global Eyetkiliadi
    global Eyetkilisifre
    yetkipencere= Toplevel()
    yetkipencere.wm_title("Yetkili Ekle")
    yetkipencere.geometry("170x130")
    yetkipencere.resizable(width=False,height=False)
    yetkipencere.transient(pencere)

    yetkiliadi = Label(yetkipencere,text="Yetkili adı:").grid(row=1,column=1)
    Eyetkiliadi = Entry(yetkipencere)
    Eyetkiliadi.grid(row=2,column=1)

    yetkilisifre = Label(yetkipencere,text="Yetkili parolası:").grid(row=3,column=1)
    Eyetkilisifre = Entry(yetkipencere)
    Eyetkilisifre.grid(row=4,column=1)

    yetkilionay = Button(yetkipencere,text="Onayla",command=addyetkili).grid(row=5,column=1)
    yetkipencere.grid()
def addyetkili():

    yadi = Eyetkiliadi.get()
    ysifre = Eyetkilisifre.get()
    ekle = cursor.execute("""INSERT INTO yetkili VALUES(?,?) """, (yadi,ysifre))
    db.commit()
def sifredegistir():
    global sifrekrani
    sifrekrani = Toplevel()
    sifrekrani.wm_title("Şifre değiştir!")
    sifrekrani.geometry("168x130")
    sifrekrani.resizable(width=False,height=False)
    sifrekrani.transient(pencere)
    bkadi =  Label(sifrekrani,text="Kullanıcı adınız : %s" %veriler1)
    bkadi.grid(row=1,column=1,columnspan="2")

    beskisifre=Label(sifrekrani,text="Eski şifreniz : ")
    beskisifre.grid(row=2,column=1,columnspan="2")

    global eeskisifre
    eeskisifre = Entry(sifrekrani,show="*")
    eeskisifre.grid(row=3,column=1,columnspan="2")

    byenisifre = Label(sifrekrani,text="Yeni Şifreniz : ")
    byenisifre.grid(row=4,column=1,columnspan="2")

    global eyenisifre
    eyenisifre = Entry(sifrekrani,show="*")
    eyenisifre.grid(row=5,column=1,columnspan="2")

    stamam = Button(sifrekrani,text="Onayla!",command=sifresorgu)
    stamam.grid(row=6,column=1,columnspan="2")
def sifresorgu():
    eskisifre = eeskisifre.get()
    yenisifre = eyenisifre.get()

    eskisifresorgu = cursor.execute("""SELECT * from yetkili WHERE kadi="%s" """ %veriler1)
    kntrl=eskisifresorgu.fetchall()

    if eskisifre == "" and yenisifre == "":
        showerror("Hata","Lütfen şifre kısımlarını boş bırakmayınız!")

    else:
        for k,v in kntrl:
            if v == eskisifre:
                print(k,v)
                cursor.execute("""UPDATE yetkili SET sifre=%s""" %yenisifre)
                showinfo("İşlem başarılı","Şifreniz  değiştirildi.")
                db.commit()
                sifrekrani.destroy()
            else:
                showwarning("Hata","Eski şifrenizi lütfen doğru yazınız!")
                eeskisifre.delete(0,END)
                eyenisifre.delete(0,END)
def kayitekle():
    global kayitformu
    kayitformu = Toplevel()
    kayitformu.wm_resizable(width=False,height=False)
    kayitformu.wm_title("Yeni kayıt")
    kayitformu.geometry("169x200")
    kayitformu.transient(pencere)
    global Eisim,Eno,Etel
    Lisim = Label(kayitformu,text="İsim ve Soyisim ")
    Eisim = Entry(kayitformu)
    Lno = Label(kayitformu,text="Numarası")
    Eno = Entry(kayitformu)
    Ltel = Label(kayitformu,text="Veli Tel")
    Etel = Entry(kayitformu)

    onay = Button(kayitformu,text="Kaydı Ekle",)

    Lisim.grid(row=1,column=2)
    Eisim.grid(row=2,column=2)
    Lno.grid(row=3,column=2)
    Eno.grid(row=4,column=2)
    Ltel.grid(row=5,column=2)
    Etel.grid(row=6,column=2)
    onay.grid(row=7,column=2)
def kayit():
    advesoyad = Eisim.get()
    numara = Eno.get()
    telefon = Etel.get()
    ktsorgu = cursor.execute("""SELECT * FROM ogrenciler WHERE okulno=%s""" %numara)
    ktsorguf = ktsorgu.fetchall()

    if len(ktsorguf) > 0:
        showwarning("Hata","Böyle bir kayıt zaten bulunuyor")
    else:
        if advesoyad == "" and numara == "" and telefon == "":
            showwarning("Hata","Lütfen boş alan bırakmayınız")
        else:
            advesoyad = advesoyad.capitalize()
            cursor.execute("""INSERT INTO ogrenciler VALUES(?,?,?)""", (advesoyad,numara,telefon))

            db.commit()

            showinfo("Başarılı","Kayıt Eklendi")
            kayitformu.destroy()
            container.destroy()
            dtable()

########### Ana pencere #####################



#####Kullanıcı Girişi #######
login = Toplevel()
login.wm_title("Yetkili girişi")
login.geometry("200x130+400+200")
login.resizable(width=False,height=False)
bilgi1 = Label(login, text="Kullanıcı Adı:")
bilgi1.pack()
kadi = Entry(login)
kadi.pack()
bilgi2 = Label(login, text="Parola:")
bilgi2.pack()
sifre = Entry(login, show="*")
sifre.pack()
onay = Button(login, text="Giriş", command=kgirisi)
onay.pack()
login.transient(pencere)
######## Kullanıcı Girişi ######


mainloop()
