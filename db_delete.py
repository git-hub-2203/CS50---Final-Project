import sqlite3
import os

db = sqlite3.connect('info.db')
cursor = db.cursor()
cursor.execute('DELETE FROM users')
db.commit()
cursor.close()
db.close()

os.remove('info.db')
