import sqlite3
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)


def init_db():
    conn = sqlite3.connect("messages.db")
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS messages (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            message TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()


init_db()

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        
        name = request.form['name']
        message = request.form['message']

        
        conn = sqlite3.connect("messages.db")
        cursor = conn.cursor()
        cursor.execute("INSERT INTO messages (name, message) VALUES (?, ?)", (name, message))
        conn.commit()
        conn.close()

        return f"<h1>Thanks, {name}!</h1><p>Your message has been saved.</p><a href='/'>Back to Home</a>"

    return render_template('contact.html')

@app.route('/messages')
def messages():
    conn = sqlite3.connect("messages.db")
    cursor = conn.cursor()
    cursor.execute("SELECT name, message FROM messages")
    all_messages = cursor.fetchall()
    conn.close()

    return render_template('messages.html', messages=all_messages)

@app.route('/clear-messages', methods=['POST'])
def clear_messages():
    conn = sqlite3.connect("messages.db")
    cursor = conn.cursor()
    cursor.execute("DELETE FROM messages")
    conn.commit()
    conn.close()

    return redirect(url_for('messages'))

if __name__ == '__main__':
    app.run(debug=True)
