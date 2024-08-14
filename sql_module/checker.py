import sqlite3

def osudbfind(find):
    conn = sqlite3.connect('main.db')
    cur = conn.cursor()
    cur.execute('SELECT profile_link FROM osu WHERE discord = ?', (find,))
    result = cur.fetchone()
    return result
