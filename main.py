import sqlite3

import requests, bs4, time

conn = sqlite3.connect("mydatabase.db")  # или :memory: чтобы сохранить в RAM
cursor = conn.cursor()

# Создание таблицы
cursor.execute("""CREATE TABLE IF NOT EXISTS av_data
                  (item text, date text, view text)
               """)
# Вставляем данные в таблицу
cursor.execute("""INSERT INTO av_data
                  VALUES ('2152372823', '13 июля в 17:27', '872 (+9)')"""
               )

# Сохраняем изменения
conn.commit()
#
# Вставляем множество данных в таблицу используя безопасный метод "?"
av_data = [('2122700128', '13 июля в 17:11', '525 (+16)'),
          ('2122700129', '14 июля в 17:12', '625 (+16)'),
          ('2122700130', '15 июля в 17:13', '725 (+16)'),
          ('2122700131', '16 июля в 17:14', '825 (+16)')]

cursor.executemany("INSERT INTO av_data VALUES (?,?,?)", av_data)
conn.commit()

# test

rowstr = cursor.execute("""SELECT * FROM av_data""")
print (rowstr.rowcount)

a = ('2122700128', '13 июля в 17:11', '525 (+16)')
b = ('2122700128', '13 июля в 17:11', '525 (+16)')
print(a[0])

# # Вставляем множество данных в таблицу используя безопасный метод "?"
# albums = [('Exodus', 'Andy Hunter', '7/9/2002', 'Sparrow Records', 'CD'),
#           ('Until We Have Faces', 'Red', '2/1/2011', 'Essential Records', 'CD'),
#           ('The End is Where We Begin', 'Thousand Foot Krutch', '4/17/2012', 'TFKmusic', 'CD'),
#           ('The Good Life', 'Trip Lee', '4/10/2012', 'Reach Records', 'CD')]
#
# cursor.executemany("INSERT INTO albums VALUES (?,?,?,?,?)", albums)
# conn.commit()