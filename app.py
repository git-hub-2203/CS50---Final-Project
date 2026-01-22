from flask import Flask, render_template, redirect, request, session
from db import init_db, get_data, get_db_connection, using_db, update_data
import re

DATA = {}


#Configure app
app = Flask(__name__)


def main():
    init_db()
    
    for index, row in enumerate(get_data(), 1):
        DATA[index] = dict(row)

    app.run(debug=True)


@app.route('/add_password', methods=['GET', 'POST'])
def add_password():
    link = request.form['link']
    name = request.form['name']
    login = request.form['login']
    password = request.form['password']
    note = request.form['note']

    db = get_db_connection()
    cursor = db.cursor()
    cursor.execute('INSERT INTO users (link, name, login, password, note) VALUES (?, ?, ?, ?, ?)', 
    (link, name, login, password, note))

    db.commit()
    cursor.close()
    db.close()
    
    new_id = max(DATA.keys()) + 1 if DATA else 1
    DATA[new_id] = {'link': link, 'name': name, 'login': login, 'password': password, 'note': note}
    
    return redirect('/')

@app.route('/delete_password', methods=['POST'])
def delete_password():
    link = request.form.get('link')
    using_db(f"DELETE FROM users WHERE link = '{link}'")
    
    for key, value in list(DATA.items()):
        if value['link'] == link:
            del DATA[key]
            break
    
    return redirect('/')

@app.route('/update_password', methods=['POST'])
def update_password():
    link = request.form.get('link')
    name = request.form.get('name')
    login = request.form.get('login')
    password = request.form.get('password')
    note = request.form.get('note')
    
    update_data(link, name=name, login=login, password=password, note=note)
    
    for key, value in DATA.items():
        if value['link'] == link:
            DATA[key] = {'link': link, 'name': name, 'login': login, 'password': password, 'note': note}
            break
    
    return redirect('/')


@app.route('/', methods=['GET', 'POST'])
def home():
    enumerated_data = list(DATA.items())
    return render_template('home.html', data=enumerated_data, rows=len(DATA))


if __name__ == '__main__':
    main()


