from tinydb import TinyDB

class ConexaoTinyDB:
    def __init__(self):
        self.db = TinyDB("db.json")

    def obter_db(self):
        return self.db
