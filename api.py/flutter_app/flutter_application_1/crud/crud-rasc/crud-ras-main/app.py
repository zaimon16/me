from flask import Flask, jsonify
from flask_cors import CORS
import pymysql

app = Flask(__name__)
CORS(app)

def conectar():
    return pymysql.connect(host='localhost', user='root', passwd='', db='ras', charset='utf8mb4')

@app.route("/consulta_anfibios")
def consulta_anfibios():
    try:
        conn = conectar()
        cur = conn.cursor()
        cur.execute("""SELECT nombre, nombre_cientifico, veneno, habitos, habitat FROM anfibios""")
        datos = cur.fetchall()
        cur.close()
        conn.close()

        registros = []
        for dato in datos:
            registros.append({
                'nombre': dato[0],
                'nombre_cientifico': dato[1],
                'veneno': dato[2],
                'habitos': dato[3],
                'habitat': dato[4]
            })
        return jsonify({'registros': registros})
    except Exception as ex:
        print("Error en la consulta a la base de datos:", ex)
        return jsonify({'mensaje': 'Error'})

if __name__ == '__main__':
    app.run(debug=True)
