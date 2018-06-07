import sqlite3
import sys
conn = sqlite3.connect("pranav.db")  # or use :memory: to put it in RAM
data = " ".join(sys.argv[2:])
cursor = conn.cursor()


def new():
    # create a table
    cursor.execute("""CREATE TABLE notes
                      (id INTEGER PRIMARY KEY AUTOINCREMENT, note text) 
                   """)


def add():
    query = 'INSERT INTO notes (note) VALUES (\''+data+'\')'
    cursor.execute(query)
    conn.commit()


def view():
    cursor.execute("SELECT * FROM notes")
    rows = cursor.fetchall()
    for a in rows:
        print(a)


def rm():
    query = 'DELETE FROM notes WHERE ID ='+data
    cursor.execute(query)
    conn.commit()


if(sys.argv[1] == 'add'):
    add()
elif(sys.argv[1] == 'view'):
    view()
elif(sys.argv[1] == 'new'):
    new()
elif(sys.argv[1] == 'rm'):
    rm()
