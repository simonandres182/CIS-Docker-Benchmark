from flask import Flask
from flask import render_template, request
import sqlite3
import time

app = Flask(__name__)

def get_db_connection():
    conn = sqlite3.connect('app.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/pruebas", methods=['GET','POST'])
def pruebas():
    if request.method == 'GET':
        conn = get_db_connection()
        pruebas = conn.execute('SELECT * FROM pruebas').fetchall()
        conn.close()
        return render_template('pruebas.html', pruebas=pruebas)
    else:
        data = request.json
        prueba_id = data.get('prueba_id')
        time.sleep(3)
        return {'id':prueba_id}



if __name__ == '__main__':
    app.run(debug=True)