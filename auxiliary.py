from datetime import datetime

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

# Export to excell----------------------------------------------------------------------------------------------
"""
import sqlite3
import pandas as pd


connection = sqlite3.connect("site_diary.db")
cursor = connection.cursor()
data_frame = pd.read_sql('SELECT ID, TITLE, CONTENT FROM USER_JGP', connection)

file_name = "site_diary.xlsx"

data_frame.to_excel(file_name, index=False)
"""

