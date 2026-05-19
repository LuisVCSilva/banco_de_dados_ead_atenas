from flask import Flask, render_template, request, redirect, url_for, jsonify
from uuid import uuid4
from db import ConexaoTinyDB
from tinydb import Query

app = Flask(__name__)

db = ConexaoTinyDB().obter_db()

filmes = db.table("filmes")
usuarios = db.table("usuarios")
User = Query()

#Exemplo de ORM -- Object Relation Mapping
class Usuario:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        self.ativo = True

    def to_dict(self):
        return {"_id":str(uuid4()),"nome":self.nome,"idade":self.idade,"ativo":self.ativo} 


@app.post("/usuario/classe")
def criar_usuario_classe ():
   dados = request.json
   if not dados:
      return {"erro":"cade o pacote?"},400
   if "nome" not in dados or "idade" not in dados:
      return {"erro":"faltou nome ou idade no pacote..."}, 400
   usuario = Usuario(nome=dados["nome"],idade=dados["idade"])
   doc = usuario.to_dict()
   usuarios.insert(doc)
   return {"mensagem":"Usuario criado com sucesso usando a classe Usuario","usuario":doc},201

u = Usuario("Kaik", 23)
print(u.__dict__)



@app.get("/usuarios/ativos")
def usuarios_ativos():
    return jsonify(usuarios.search(User.ativo == True))
# =====================================
# HOME
# =====================================
@app.route("/", methods=["GET", "POST"])
def pagina_inicial():
    if request.method == "POST":
        filmes.insert({
            "_id": str(uuid4()),
            "filme": request.form["filme"],
            "opiniao": request.form["opiniao"]
        })
        return redirect(url_for("pagina_inicial"))

    return render_template("index.html", filmes=filmes.all())

# =====================================
# DELETAR FILME
# =====================================
@app.post("/deletar/<id>/")
def deletar_filme(id):
    filmes.remove(User._id == id)
    return redirect(url_for("pagina_inicial"))

# =====================================
# CRIAR USUÁRIO
# =====================================
@app.post("/usuario")
def criar_usuario():
    dados = request.json

    if not dados:
        return {"erro": "JSON obrigatório"}, 400

    dados["_id"] = str(uuid4())
    usuarios.insert(dados)

    return {"mensagem": "Usuário criado", "id": dados["_id"]}, 201

# =====================================
# LISTAR USUÁRIOS
# =====================================
@app.get("/usuarios")
def listar_usuarios():
    return jsonify(usuarios.all()), 200

@app.get("/usuario/email/<email>")
def buscar_por_email(email):
    user = usuarios.get(User.email == email)

    if not user:
        return {"erro": "não encontrado"}, 404

    return jsonify(user)

# =====================================
# BUSCAR USUÁRIO
# =====================================
@app.get("/usuario/<id>")
def buscar_usuario(id):
    user = usuarios.get(User._id == id)

    if not user:
        return {"erro": "não encontrado"}, 404

    return jsonify(user)

# =====================================
# ATUALIZAR USUÁRIO
# =====================================
@app.put("/usuario/<id>")
def atualizar_usuario(id):
    dados = request.json

    if not usuarios.contains(User._id == id):
        return {"erro": "usuário não encontrado"}, 404

    usuarios.update(dados, User._id == id)

    return {"mensagem": "atualizado com sucesso"}

# =====================================
# DELETAR USUÁRIO
# =====================================
@app.delete("/usuario/<id>")
def deletar_usuario(id):
    removed = usuarios.remove(User._id == id)

    if not removed:
        return {"erro": "não encontrado"}, 404

    return {"mensagem": "removido"}

# =====================================
# RUN
# =====================================
if __name__ == "__main__":
    print(app.url_map)
    app.run(debug=True)
