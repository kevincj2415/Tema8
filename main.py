from flask import Flask
from dotenv import load_dotenv
import os

# Cargar las variables de entorno del archivo .env
load_dotenv()

# Obtener las variables de entorno
PORT = os.getenv('PORT')
HOST = os.getenv('HOST')
SECRET_MESSAGE = os.getenv('SECRET_MESSAGE')
DEBUG = os.getenv('DEBUG')

app = Flask(__name__)

@app.route('/')
def main():
    return SECRET_MESSAGE

if __name__ == '__main__':
    app.run(port=PORT, host=HOST, debug=DEBUG)