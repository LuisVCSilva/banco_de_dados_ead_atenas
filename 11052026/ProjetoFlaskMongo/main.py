from flask import Flask

app = Flask(__name__)

from rotas.filmes import filmes_bp
from rotas.usuarios import usuarios_bp

app.register_blueprint(filmes_bp)
app.register_blueprint(usuarios_bp)

if __name__ == "__main__":
    app.run(debug=True)
