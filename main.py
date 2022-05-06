from flask import Flask, jsonify, request
from controladores import *

import json

app = Flask(__name__)


@app.route("/livros", methods=['GET', 'POST', 'DELETE'])
def livros():
    if request.method == 'GET':
        objetos = []
        books_db = listar()
        for livro in books_db:
            a = {'id':livro[0], 'autor':livro[1], 'livro' : livro[2]}
            objetos.append(a)
        return jsonify(objetos)
    
    if request.method == 'POST':
        data = request.get_data().decode('utf-8')
        data = json.loads(data)
        add_livro(data['titulo'], data['autor'])
        return '200'
    
    if request.method == 'DELETE':
        data = request.get_data()
        data = json.loads(data)
        id = data['id_livro']
        remover_livro(id)
        return '200'


@app.route("/livros/<id>", methods=['GET'])
def book_by_id(id):
    if selecionar_livro(id):
        livro = selecionar_livro(id)
        a = {'id':livro[0], 'autor':livro[1], 'livro' : livro[2]}
        return a
    else:
        return 'Livro não encontrado'
app.config['JSON_AS_ASCII'] = False
app.run()
