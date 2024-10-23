from flask import Flask, render_template,redirect,request
import datetime
from pymongo import MongoClient
import os
from dotenv import load_dotenv


def crear_app():
    app = Flask(__name__)
    cliente = MongoClient(os.getenv('MONGODB_URI'))
    app.db = cliente.actividadesDB
    entradas = ""
    entradas = [entradas for entradas in app.db.contenidosCL.find({})]


    @app.route('/',  methods=["GET", "POST"])
    def home():
        if request.method == 'POST':
            titulo = request.form['actividad']
            contenido = request.form['contenido']
            fecha = datetime.datetime.today().strftime('%d-%m-%Y')
            parametros = {'titulo': titulo, 'contenido': contenido, 'fecha': fecha}
            entradas.append(parametros)
            app.db.contenidosCL.insert_one(parametros)
            return redirect('/')
        
        
        return render_template('index.html', entradas = entradas)    

    if __name__ == '__main__':
        app.run(debug=True)
        
crear_app()