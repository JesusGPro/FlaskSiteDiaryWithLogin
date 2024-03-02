import sqlite3
from record import Record
from flask import flash, session
from datetime import datetime

x = datetime.now()
fecha = x.strftime("%c")

      
def add_record(record):
    table_name = str(session['username'])
    connection = sqlite3.connect("site_diary.db")
    cursor = connection.cursor()
    query = cursor.execute(f"INSERT INTO {table_name} (TITLE, CONTENT, DATE_TIME) VALUES (?, ?, ?)", (record.title, record.content, record.date_recorded))
    connection.commit()
    record_key = query.lastrowid
    flash("Report added")
    return record_key
    

def update_record(record_key, record):
    table_name = str(session['username'])
    connection = sqlite3.connect("site_diary.db")
    cursor = connection.cursor()
    data = [record.title, record.content, record_key,]
    cursor.execute(f"UPDATE {table_name} SET TITLE = ?, CONTENT = ? WHERE (ID = ?)", (data))
    connection.commit()
    flash("Report updated")

def delete_record(record_key):
    table_name = str(session['username'])
    connection = sqlite3.connect("site_diary.db")
    cursor = connection.cursor()
    cursor.execute(f"DELETE FROM {table_name} WHERE (ID = ?)", (record_key,))
    connection.commit()
    connection.close()
    flash("Field deleted successfully")

def get_record(record_key):
    table_name = str(session['username'])
    record_key = [record_key]
    connection = sqlite3.connect("site_diary.db")
    cursor = connection.cursor()
    query = cursor.execute(f"SELECT ID, TITLE, CONTENT, DATE_TIME FROM {table_name} WHERE (ID = ?)", (record_key)).fetchall()
    id, title, content, date_recorded = query[0][0], query[0][1], query[0][2], query[0][3]
    record_ =Record(title, content, date_recorded)
    connection.close()
    return record_, id
   
    
def get_records():
    table_name = str(session['username'])
    records = []
    connection = sqlite3.connect("site_diary.db")
    cursor = connection.cursor()
    query = cursor.execute(f"SELECT ID, TITLE, CONTENT, DATE_TIME FROM {table_name} ORDER BY ID").fetchall()
    for record_key, title, content, date_recorded in query:
        records.append((record_key, Record(title, content, date_recorded)))
    connection.close()
    return records

def get_sql_search(key_word):
    table_name = str(session['username'])
    records = []
    connection = sqlite3.connect("site_diary.db")
    cursor = connection.cursor()
    query = cursor.execute(f"SELECT * FROM {table_name} WHERE CONTENT like '%{key_word}%' ORDER BY ID").fetchall()
    for record_key, title, content, date_recorded in query:
        records.append((record_key, Record(title, content, date_recorded)))
    connection.close()
    return records

