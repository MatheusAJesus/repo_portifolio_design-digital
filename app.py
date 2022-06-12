from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route("/") 
def index(): 
    return render_template('home.html')

@app.route("/biografia") 
def biografia(): 
    return render_template('biografia.html')

@app.route("/projetos") 
def projetos(): 
    return render_template('projetos.html')

@app.route("/contatos") 
def contatos(): 
    return render_template('contatos.html')