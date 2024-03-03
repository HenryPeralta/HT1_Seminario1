from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

# Respuesta default
respuesta = {
    'Instancia': 'Instancia #1 - API #1',
    'Curso': 'Seminario de sistemas 1',
    'Estudiante': 'Estudiante - 201712289'
}

respuestaOK = {
    'codigo': '200',
    'status': 'OK'
}

# Ruta para obtener las imagenes
@app.route('/', methods=['GET'])
def obtener_productos():
    return jsonify(respuesta)

@app.route('/check', methods=['GET'])
def obtener_check():
    return jsonify(respuestaOK)

#python consultasFlask.py    --PARA LEVANTAR SERVIDOR
if __name__ == '__main__':
    app.run(port=4000, debug=True)