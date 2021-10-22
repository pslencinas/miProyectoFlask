from flask import Flask
from flask import request
app = Flask(__name__)

@app.route('/')
def hola_mundo():
    return 'Hola mundo desde Flask'


@app.route('/test')
def test():
    return 'Hola mundo desde Flask, ruta /test'

@app.route('/saludar')
def saludar():
    param = request.args.get('q', 'no tengo parametros')
    return 'Hola {}'.format(param)

@app.route('/cargarUsuario/<name>/<int:id>')
def cargar(name, id):
    
    return 'Hola {} con id: {}'.format(name, id)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')