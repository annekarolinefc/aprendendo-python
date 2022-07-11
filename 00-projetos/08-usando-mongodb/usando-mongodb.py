#pip install pymongo
import datetime
from pymongo import MongoClient

#CONECTAR BANCO
client = MongoClient('mongodb://localhost:27817')

#ACESSAR AO BANCO
db = client['nome-do-banco']

#ACESSAR UMA COLLECTION
users = db.users

#CRIAR UM OBJETO
user = {
    "nome": "André",
    "sobrenome": "Lopes",
    "data": datetime.datetime.utcnow()
}

#INSERIR NA COLLECTION
user_id = users.insert_one(user).inserted_id