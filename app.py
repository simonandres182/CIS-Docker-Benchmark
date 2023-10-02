from flask import Flask
from flask import render_template, request
import sqlite3
import subprocess
import time
import os

app = Flask(__name__)

def get_db_connection():
    conn = sqlite3.connect('app.db')
    conn.row_factory = sqlite3.Row
    return conn

def registrar_resultado(prueba_id, resultado, msg):
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("""UPDATE pruebas SET pass='%s', result='%s' WHERE id=%s""" % (resultado, msg, prueba_id))
    conn.commit()
    cur.close()
    conn.close()

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
        if (prueba_id == 1):
            result = subprocess.run(['mountpoint', '/var/lib/docker'], stdout=subprocess.PIPE)
            respuesta = result.stdout.decode('utf-8').replace('\n','')
            time.sleep(1) #damos tiempo para capturas la salida
            if "no" in respuesta:
                registrar_resultado(prueba_id, "N", respuesta)
                return {'prueba':'fail'}
            else:
                registrar_resultado(prueba_id, "S", respuesta)
                return {'prueba':'pass'}
        
        elif (prueba_id == 2):
            comando = "stat -c %U:%G /usr/lib/systemd/system/docker.service | grep -v root:root"
            resultado = subprocess.getoutput(comando)
            lineas = resultado.split('\n')
            primera_linea = lineas[0]
            time.sleep(1) #damos tiempo para capturas la salida
            if primera_linea == "":
                registrar_resultado(prueba_id, "S", primera_linea)
                return {'prueba':'pass'}
            else:
                registrar_resultado(prueba_id, "N", primera_linea)
                return {'prueba':'fail'}
            
        elif (prueba_id == 3):
            comando = "stat -c %a /usr/lib/systemd/system/docker.socket"
            resultado = subprocess.getoutput(comando)
            lineas = resultado.split('\n')
            primera_linea = lineas[0]
            time.sleep(1) #damos tiempo para capturas la salida
            if primera_linea == "644":
                registrar_resultado(prueba_id, "S", primera_linea)
                return {'prueba':'pass'}
            else:
                registrar_resultado(prueba_id, "N", primera_linea)
                return {'prueba':'fail'}
            
        elif (prueba_id == 4):
            comando = "stat -c %U:%G /etc/docker | grep -v root:root"
            resultado = subprocess.getoutput(comando)
            lineas = resultado.split('\n')
            primera_linea = lineas[0]
            time.sleep(1) #damos tiempo para capturas la salida
            if primera_linea == "":
                registrar_resultado(prueba_id, "S", primera_linea)
                return {'prueba':'pass'}
            else:
                registrar_resultado(prueba_id, "N", primera_linea)
                return {'prueba':'fail'}

        elif (prueba_id == 5):
            comando = "stat -c %a /etc/docker"
            resultado = subprocess.getoutput(comando)
            lineas = resultado.split('\n')
            primera_linea = lineas[0]
            time.sleep(1) #damos tiempo para capturas la salida
            if primera_linea == "755":
                registrar_resultado(prueba_id, "S", primera_linea)
                return {'prueba':'pass'}
            else:
                registrar_resultado(prueba_id, "N", primera_linea)
                return {'prueba':'fail'}
            
        elif (prueba_id == 6):
            comando = "stat -c %U:%G /var/run/docker.sock | grep -v root:docker"
            resultado = subprocess.getoutput(comando)
            lineas = resultado.split('\n')
            primera_linea = lineas[0]
            time.sleep(1) #damos tiempo para capturas la salida
            if primera_linea == "":
                registrar_resultado(prueba_id, "S", primera_linea)
                return {'prueba':'pass'}
            else:
                registrar_resultado(prueba_id, "N", primera_linea)
                return {'prueba':'fail'}
            
        elif (prueba_id == 7):
            comando = "stat -c %a /var/run/docker.sock"
            resultado = subprocess.getoutput(comando)
            lineas = resultado.split('\n')
            primera_linea = lineas[0]
            time.sleep(1) #damos tiempo para capturas la salida
            if primera_linea == "660":
                registrar_resultado(prueba_id, "S", primera_linea)
                return {'prueba':'pass'}
            else:
                registrar_resultado(prueba_id, "N", primera_linea)
                return {'prueba':'fail'}

        elif (prueba_id == 8):
            comando = "stat -c %U:%G /run/containerd/containerd.sock | grep -v root:root"
            resultado = subprocess.getoutput(comando)
            lineas = resultado.split('\n')
            primera_linea = lineas[0]
            time.sleep(1) #damos tiempo para capturas la salida
            if primera_linea == "":
                registrar_resultado(prueba_id, "S", primera_linea)
                return {'prueba':'pass'}
            else:
                registrar_resultado(prueba_id, "N", primera_linea)
                return {'prueba':'fail'}
            
        elif (prueba_id == 9):
            comando = "stat -c %a /run/containerd/containerd.sock"
            resultado = subprocess.getoutput(comando)
            lineas = resultado.split('\n')
            primera_linea = lineas[0]
            time.sleep(1) #damos tiempo para capturas la salida
            if primera_linea == "660":
                registrar_resultado(prueba_id, "S", primera_linea)
                return {'prueba':'pass'}
            else:
                registrar_resultado(prueba_id, "N", primera_linea)
                return {'prueba':'fail'}
            
        elif (prueba_id == 10):
            comando = "stat -c %a /usr/lib/systemd/system/docker.service"
            resultado = subprocess.getoutput(comando)
            lineas = resultado.split('\n')
            primera_linea = lineas[0]
            time.sleep(1) #damos tiempo para capturas la salida
            if primera_linea == "644":
                registrar_resultado(prueba_id, "S", primera_linea)
                return {'prueba':'pass'}
            else:
                registrar_resultado(prueba_id, "N", primera_linea)
                return {'prueba':'fail'}

        else:
            return {'prueba':''}



if __name__ == '__main__':
    app.run(debug=True)