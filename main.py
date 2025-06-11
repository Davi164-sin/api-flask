from flask import Flask, request, jsonify
from werkzeug.utils import secure_filename
import os

# Crear la carpeta uploads si no existe
UPLOAD_FOLDER = 'uploads'
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Ruta para cargar archivos
@app.route('/upload', methods=['POST'])
def upload_file():
    file = request.files['file']
    filename = secure_filename(file.filename)
    file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
    return jsonify({'message': 'Archivo cargado con éxito'})
@app.route('/info', methods=['GET'])
def get_info():
    info = {
        'mensaje': 'Hola, mundo!',
        'version': '1.0'
    }
    return jsonify(info)
if __name__ == '__main__':
    app.run(port=5003)
