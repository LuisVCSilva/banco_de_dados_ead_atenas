from pymongo import MongoClient
import os
from dotenv import load_dotenv

load_dotenv()

class ConexaoMongo:
    def __init__(self):
        self.cliente = MongoClient(os.getenv("MONGO_URI"))
        self.banco = self.cliente["filme_app"]

    def obter_banco(self):
        return self.banco
