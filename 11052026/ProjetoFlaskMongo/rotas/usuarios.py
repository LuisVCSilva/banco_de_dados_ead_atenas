from flask import Blueprint, request, jsonify
from uuid import uuid4
from db import ConexaoMongo

usuarios_bp = Blueprint("usuarios", __name__)

banco = ConexaoMongo().obter_banco()
colecao = banco["usuarios"]

@usuarios_bp.post("/usuario")
def criar_usuario():
    dados = request.json
    dados["_id"] = str(uuid4())
    colecao.insert_one(dados)
    return {"mensagem": "criado com sucesso"}

@usuarios_bp.get("/usuarios")
def listar_usuarios():
    usuarios = list(colecao.find())
    for u in usuarios:
        u["_id"] = str(u["_id"])
    return jsonify(usuarios)
