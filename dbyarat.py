#-*- coding:cp857 -*-

__author__ = 'ka1nsha'
import os
import sqlite3
dbkontrol = os.path.exists("db.db3")
def yetkiliolustur():
    db  = sqlite3.connect("db.db3")
    cursor = db.cursor()
    cursor.execute("""CREATE TABLE yetkili(kadi text,
    sifre text)"""
    )
    cursor.execute("""CREATE TABLE ogrenciler(isim text,okulno integer,tel integer)""")
    yAdi = input("Yînetici adç:")
    ySifre = input("Yînetici üifresi:")
    cursor.execute("""INSERT INTO yetkili values(?,?)""", (yAdi,ySifre))
    db.commit()
if dbkontrol == False:
    yetkiliolustur()
else:
    print("Yetkilendirme iülemi zaten yapçlmçü")

