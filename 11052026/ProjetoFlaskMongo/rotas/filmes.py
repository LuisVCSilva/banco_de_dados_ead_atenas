from flask import Blueprint, render_template, request, redirect, url_for
from db import ConexaoMongo
from bson.objectid import ObjectId

filmes_bp = Blueprint("filmes", __name__)

banco = ConexaoMongo().obter_banco()
colecao = banco["filmes"]

@filmes_bp.route("/", methods=["GET", "POST"])
def pagina_inicial():
    if request.method == "POST":
        colecao.insert_one({
            "filme": request.form["filme"],
            "opiniao": request.form["opiniao"]
        })
        return redirect(url_for("filmes.pagina_inicial"))

    filmes = colecao.find()
    return render_template("index.html", filmes=filmes)


@filmes_bp.route("/deletar/<id>/", methods=["POST"])
def deletar(id):
    colecao.delete_one({"_id": ObjectId(id)})
    return redirect(url_for("filmes.pagina_inicial"))
