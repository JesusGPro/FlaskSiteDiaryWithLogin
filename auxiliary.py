import sqlite3
from record import Record, Search
import database
from datetime import datetime
from flask import session

def get_records():
    records = []
    connection = sqlite3.connect("site_diary.db")
    cursor = connection.cursor()
    query = cursor.execute("SELECT ID, TITLE, CONTENT, DATE_TIME FROM USER_JGP ORDER BY ID").fetchall()
    for record_key, title, content, date_recorded in query:
        records.append((record_key, Record(title, content, date_recorded)))
    connection.close()
    return records

def delete_record(record_key):
    connection = sqlite3.connect("site_diary.db")
    cursor = connection.cursor()
    cursor.execute("DELETE FROM USER_JGP WHERE (ID = ?)", (record_key,)).fetchall()
    connection.commit()
    connection.close()
    # flash("Field deleted successfully")
    
def record_edit_page(record_key):
    record = database.get_record(record_key)
    values = {"title": record[0].title, "content": record[0].content}
        
    print(values)  

def get_record(record_key):
    record_key = [record_key]
    connection = sqlite3.connect("site_diary.db")
    cursor = connection.cursor()
    query = cursor.execute("SELECT ID, TITLE, CONTENT, DATE_TIME FROM USER_JGP WHERE (ID = ?)", (record_key)).fetchall()
    id, title, content, date_recorded = query[0][0], query[0][1], query[0][2], query[0][3]
    record_ = Record(title, content, date_recorded)
    connection.close()
    return record_, id

def reverse_list(lista):
    inicio = 0
    fin = len(lista) - 1
    while inicio < fin:
        lista[inicio], lista[fin] = lista[fin], lista[inicio]
        print(lista)
        inicio += 1
        fin -= 1
        
    return lista

# lista = [5, 7, 9, 4, 3, 2]
# print(reverse_list(lista))

x = datetime.now()
fecha = [x. day,'/', x.month,'/', x.year,'/', x.hour, ':', x.minute, x.strftime("%A")]

# print(x.strftime("%c"))

# print(user.username)

def get_sql_search(key_word):
    records = []
    connection = sqlite3.connect("site_diary.db")
    cursor = connection.cursor()
    query = cursor.execute(f"SELECT * FROM USER_JGP WHERE CONTENT like '%{key_words.search_1}%' AND CONTENT like '%{key_words.search_2}%' ORDER BY ID").fetchall()
    for record_key, title, content, date_recorded in query:
        records.append((record_key, Record(title, content, date_recorded)))
    connection.close()
    return records

key_words=Search('C29', 'Gantry')
print(get_sql_search(key_words))