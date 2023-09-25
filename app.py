from flask import Flask
from flask import render_template
import sqlite3

app = Flask(__name__)

def get_db_connection():
    conn = sqlite3.connect('app.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/pruebas")
def pruebas():
    conn = get_db_connection()
    pruebas = conn.execute('SELECT * FROM pruebas').fetchall()
    conn.close()
    return render_template('pruebas.html', pruebas=pruebas)



if __name__ == '__main__':
    app.run(debug=True)