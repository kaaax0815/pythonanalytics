from datetime import date
import sqlite3
from flask import *
con = sqlite3.connect('database/fortnitepy.db')
cur = con.cursor()

update = ''' UPDATE Analytics
              SET hits = hits + 1
              WHERE date = ?'''

def analytics():
    today = str(date.today())
    try:
        cur.execute("insert into Analytics values(?,0)",(today,))
    except sqlite3.IntegrityError:
        pass # Date already exists
    cur.execute(update, (today,)) # increase hits by one
    con.commit() # commit changes
    return jsonify(status='200'), 200 # return 200