from flask import Flask, render_template, request, redirect, url_for, jsonify
from bson.objectid import ObjectId
from pymongo import MongoClient
from uuid import uuid4
import os
from dotenv import load_dotenv

load_dotenv()

# =====================================
# APP
# =====================================
app = Flask(__name__)

# =====================================
# MONGO
# =====================================
cliente = MongoClient(os.getenv("MONGO_URI"))
banco = cliente["filme_app"]

colecao_filmes = banco["filmes"]
colecao_usuarios = banco["usuarios"]

# =====================================
# HOME (FILMES)
# =====================================
@app.route("/", methods=["GET", "POST"])
def pagina_inicial():
    if request.method == "POST":
        colecao_filmes.insert_one({
            "filme": request.form["filme"],
            "opiniao": request.form["opiniao"]
        })
        return redirect(url_for("pagina_inicial"))

    filmes = colecao_filmes.find()
    return render_template("index.html", filmes=filmes)

# =====================================
# DELETAR FILME
# =====================================
@app.post("/deletar/<id>/")
def deletar_filme(id):
    colecao_filmes.delete_one({"_id": ObjectId(id)})
    return redirect(url_for("pagina_inicial"))

# =====================================
# CRIAR USUÁRIO (JSON API)
# =====================================
@app.post("/usuario")
def criar_usuario():
    dados = request.json

    if not dados:
        return {"erro": "JSON obrigatório"}, 400

    dados["_id"] = str(uuid4())
    colecao_usuarios.insert_one(dados)

    return {
        "mensagem": "Usuário criado",
        "id": dados["_id"]
    }, 201

# =====================================
# LISTAR USUÁRIOS
# =====================================
@app.get("/usuarios")
def listar_usuarios():
    usuarios = list(colecao_usuarios.find())

    for u in usuarios:
        u["_id"] = str(u["_id"])

    return jsonify(usuarios), 200

# =====================================
# BUSCAR USUÁRIO
# =====================================
@app.get("/usuario/<id>")
def buscar_usuario(id):
    usuario = colecao_usuarios.find_one({"_id": id})

    if not usuario:
        return {"erro": "não encontrado"}, 404

    usuario["_id"] = str(usuario["_id"])
    return jsonify(usuario)

# =====================================
# ATUALIZAR USUÁRIO
# =====================================
@app.put("/usuario/<id>")
def atualizar_usuario(id):
    dados = request.json

    resultado = colecao_usuarios.update_one(
        {"_id": id},
        {"$set": dados}
    )

    if resultado.matched_count == 0:
        return {"erro": "usuário não encontrado"}, 404

    return {"mensagem": "atualizado com sucesso"}

# =====================================
# DELETAR USUÁRIO
# =====================================
@app.delete("/usuario/<id>")
def deletar_usuario(id):
    resultado = colecao_usuarios.delete_one({"_id": id})

    if resultado.deleted_count == 0:
        return {"erro": "não encontrado"}, 404

    return {"mensagem": "removido"}

# =====================================
# RUN
# =====================================
if __name__ == "__main__":
    print(app.url_map)  # DEBUG ROTAS
    app.run(debug=True)
