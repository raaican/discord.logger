import sqlite3

def osu(conn, add):
    sql = ''' INSERT into osu(discord, profile_link)
              VALUES(?,?) '''

    cur = conn.cursor()
    cur.execute(sql, add)
    conn.commit()
    return cur.lastrowid

def add_osu(add):
    try: 
        with sqlite3.connect("main.db") as conn:
            osu(conn, add)
    except sqlite3.Error as error:
        print(error)
