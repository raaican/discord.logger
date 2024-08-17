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

def add_exp(discord, amount):
    conn = sqlite3.connect("main.db")
    cur = conn.cursor()
    cur.execute('SELECT exp, level FROM levels WHERE discord = ?', (discord,))
    result = cur.fetchone()

    if result:
        exp, previous_level = result
        new_exp = exp + amount
        new_level = previous_level
    else:
        new_exp = amount
        new_level = 1
        previous_level = 1
        cur.execute('INSERT INTO levels(discord, exp, level) VALUES(?, ?, ?)', (discord, new_exp, new_level))


    level_up_threshold = 100 * new_level
    while new_exp >= level_up_threshold:
        new_exp -= level_up_threshold
        new_level += 1
        level_up_threshold = 100 * new_level

    cur.execute('UPDATE levels SET exp = ?, level = ? WHERE discord = ?', (new_exp, new_level, discord))

    conn.commit()
    conn.close()

    return new_level, previous_level
