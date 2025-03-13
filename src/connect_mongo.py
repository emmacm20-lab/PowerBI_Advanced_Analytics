# 📂 src/connect_mongo.py - Conexión a MongoDB

from pymongo import MongoClient

def connect_mongo():
    client = MongoClient("mongodb://usuario:contraseña@tu_servidor:27017/")
    db = client["tu_base"]
    collection = db["ventas"]
    data = collection.find().limit(10)
    return list(data)

if __name__ == "__main__":
    print("Conexión a MongoDB exitosa:", connect_mongo())