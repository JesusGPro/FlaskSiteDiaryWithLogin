import sqlite3

def db_factory():
    connection = sqlite3.connect("site_blog.db")
    cursor = connection.cursor()
    cursor.execute("""CREATE TABLE BLOG(
                        ID INTEGER PRIMARY KEY AUTOINCREMENT,
                        TITLE VARCHAR(20) UNIQUE NOT NULL,
                        CONTENT VARCHAR(500),
                        DATE_TIME) """)

    connection.close()
    return

db_factory()