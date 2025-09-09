# Importar la biblioteca PyMongo
import pymongo

# Conexión al servidor MongoDB local

def iniciar_conexion():
    cliente = pymongo.MongoClient("mongodb://localhost:27017/")

    # Crear una nueva base de datos llamada "mydatabase"
    database = cliente["crud_mongo"]
    
     # Acceder a una colección
    coleccion = database["character"]

    return coleccion

    # print(cliente.list_database_names())  # Lista de nombres de bases de datos
