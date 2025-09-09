from typing import Union

from fastapi import FastAPI
from src.mongo_db.conexion import iniciar_conexion
from src.mongo_db.models.characters_models import Character
from src.utils.generar_tiempo_real import generar_hora_y_fecha
app = FastAPI(
    title = "un crud con mongo",
    description = "un crud usando las rutas de fastapi"

)


@app.get("/")
def read_root():
    return {"message": "un video mas mi gente pa perder el tiempo"}

# Serializador para convertir documentos de MongoDB a JSON
def character_serializer(character) -> dict:
    return {
        "message": "campeon obtenido: ",
        "id personaje": str(character["_id"]), #Convierte el ObjectId en una cadena (str(champion["_id"])).
        "name personaje": character["name"],
        "last_name personaje": character["last_name"],
        "age personaje": character["age"]
    }

@app.post("/guardar_character")
def guardar_personaje(data: Character):
    character = iniciar_conexion()
    tiempo_generado = generar_hora_y_fecha()
    
    informacion = {
        "nombre": data.name,
        "apellido": data.last_name,
        "año": data.age,
        "se_creo_en": tiempo_generado
        
    }
    
    character.insert_one(informacion)
    
    
    return {
        "message": "se guardo el personaje con exito!!!",
        "nombre": data.name,
        "apellido": data.last_name,
        "año": data.age,
        "fecha_creacion": tiempo_generado
    }

@app.get("/obtener_todos_personajes")
def traer_todos_personajes():
    characters = iniciar_conexion()
    
    # def iniciar_bucle():
    #     for c in character.find():
    #         # print(c)
    #         return c
    # result = iniciar_bucle()
    # print(f"resultado del bucle: {result}")
    personajes = [character_serializer(char) for char in characters.find()] 
    print(f"\nall characters: {personajes}")
    # return {"message": "se trajo todos los personajes!!!",
    #         # "bucle": result
        
    # }
    return personajes