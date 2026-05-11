from flask import Flask, request, jsonify
from uuid import uuid4
from db import ConexaoMongo

app = Flask(__name__)

banco = ConexaoMongo().obter_banco()
colecao = banco["usuarios"]

# =====================================
# CRIAR USUÁRIO
# =====================================
@app.post("/usuario")
def criar_usuario():
    dados = request.json
    id_usuario = str(uuid4())

    dados["_id"] = id_usuario

    resultado = colecao.insert_one(dados)

    if not resultado.inserted_id:
        return {"mensagem": "Erro ao inserir"}, 500

    return {
        "mensagem": "Sucesso",
        "id": str(resultado.inserted_id)
    }, 200


# =====================================
# LISTAR USUÁRIOS
# =====================================
@app.get("/usuarios")
def listar_usuarios():
    usuarios = list(colecao.find({}))

    for u in usuarios:
        u["_id"] = str(u["_id"])

    return jsonify(usuarios), 200


# =====================================
# BUSCAR USUÁRIO
# =====================================
@app.get("/usuario/<id_usuario>")
def buscar_usuario(id_usuario):
    usuario = colecao.find_one({"_id": id_usuario}, {"_id": 0})

    if not usuario:
        return {"mensagem": "Não encontrado"}, 404

    return {"dados": usuario}, 200


# =====================================
# ATUALIZAR USUÁRIO
# =====================================
@app.put("/usuario/<id_usuario>")
def atualizar_usuario(id_usuario):
    dados = {"$set": dict(request.json)}

    resultado = colecao.update_one({"_id": id_usuario}, dados)

    if not resultado.matched_count:
        return {"mensagem": "Usuário não encontrado"}, 404

    return {"mensagem": "Atualizado com sucesso"}, 200


# =====================================
# DELETAR USUÁRIO
# =====================================
@app.delete("/usuario/<id_usuario>")
def deletar_usuario(id_usuario):
    resultado = colecao.delete_one({"_id": id_usuario})

    if not resultado.deleted_count:
        return {"mensagem": "Erro ao deletar"}, 500

    return {"mensagem": "Removido com sucesso"}, 200


if __name__ == "__main__":
    app.run(port=5000, debug=True)
