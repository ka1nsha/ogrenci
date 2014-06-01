# -*- coding:utf-8 -*-

__author__ = 'ka1nsha'
import os
import sqlite3
dbkontrol = os.path.exists("db.db3")


def yetkiliolustur():
    db = sqlite3.connect("db.db3")
    cursor = db.cursor()
    cursor.execute("""CREATE TABLE yetkili(kadi text,
    sifre text)""")
    cursor.execute("""CREATE TABLE ogrenciler(isim text,okulno integer,tel integer)""")
    yonetici_adi = input("Yönetici ad¿:")
    yonetici_sifre = input("Yönetici ¿ifresi:")
    cursor.execute("""INSERT INTO yetkili values(?,?)""", (yonetici_adi, yonetici_sifre))
    db.commit()
if not dbkontrol:
    yetkiliolustur()
else:
    print("Yetkilendirme i¿lemi zaten yap¿lm¿¿")

