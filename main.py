# Project name: PassForge

from flask import Flask, render_template, request, url_for
import sqlite3
import string
import secrets
import datetime

app = Flask(__name__, template_folder='temps') 


with sqlite3.connect('savelist.db') as conn:
    cursor = conn.cursor()
    create_insert_db = """
        CREATE TABLE IF NOT EXISTS passwords (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL CHECK(length(title) <= 32),
        password TEXT NOT NULL,
        created_at TEXT NOT NULL
        );
    """
    conn.execute(create_insert_db)
    conn.commit()

@app.route('/')
def home():
    return render_template('index.html', send_msg=None)

@app.route('/', methods=['POST'])
def generate_password():
    try:
        length = int(request.form.get('length', 16))
    except ValueError:
        return render_template('index.html', send_msg="Invalid length. Please enter a number.")

    uppercase = request.form.get('uppercase') == 'on'
    lowercase = request.form.get('lowercase') == 'on'
    digits = request.form.get('numbers') == 'on'
    symbols = request.form.get('symbols') == 'on'

    if not uppercase and not lowercase:
        return render_template('index.html', send_msg="Please seletc uppercase or lowercase chrachter.")

    # بررسی انتخاب حداقل یک نوع کاراکتر
    if not (uppercase or lowercase or digits or symbols):
        return render_template('index.html', send_msg="Please select at least one character type.")

    # ساخت مجموعه کاراکترها
    characters = ""
    if uppercase:
        characters += string.ascii_uppercase
    if lowercase:
        characters += string.ascii_lowercase
    if digits:
        characters += string.digits
    if symbols:
        characters += '!@#$%^&*()_'

    # تولید رمز
    password = "".join(secrets.choice(characters) for _ in range(length))

    return render_template('index.html', send_msg=password)

@app.route('/save')
def save():
    pass

if __name__ == '__main__':
    app.run(debug=True)