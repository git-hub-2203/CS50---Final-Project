import sqlite3

def get_db_connection():
    connection = sqlite3.connect('info.db')
    connection.row_factory = sqlite3.Row
    return connection

def init_db():
    db = get_db_connection()
    cursor = db.cursor()
    cursor.execute('CREATE TABLE IF NOT EXISTS users (link TEXT, name TEXT, login TEXT, password TEXT, note TEXT)')
    db.commit()
    cursor.close()
    db.close()

def using_db(command):
    db = get_db_connection()
    cursor = db.cursor()
    cursor.execute(command)
    db.commit()
    cursor.close()
    db.close()

def update_data(link, **kwargs):
    """Update user data by link"""
    db = get_db_connection()
    cursor = db.cursor()
    
    # Build the SET clause dynamically
    set_clause = ", ".join([f"{key} = ?" for key in kwargs.keys()])
    values = list(kwargs.values()) + [link]
    
    cursor.execute(f'UPDATE users SET {set_clause} WHERE link = ?', values)
    db.commit()
    cursor.close()
    db.close()

def get_data():
    db = get_db_connection()
    cursor = db.cursor()
    cursor.execute('SELECT * FROM users')
    data = cursor.fetchall()
    cursor.close()
    db.close()
    return data


