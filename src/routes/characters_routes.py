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
    tiempo_generado = generar_hora_y_fecha()
    return {
        "message": "campeon obtenido: ",
        "id personaje": str(character["_id"]), #Convierte el ObjectId en una cadena (str(champion["_id"])).
        "name personaje": character["nombre"],
        "last_name personaje": character["apellido"],
        "age personaje": character["año"],
        "se obtuvo en": tiempo_generado
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
    
    #en este return se basa los nombres para llamarlos en otras operaciones
    # LOQ QUE ESTA DENTRO " "
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
    return personajes

@app.get("/find_by_name")
def encontrar_por_nombre():
    characters = iniciar_conexion()
    
    personajes = [character_serializer(c) for c in characters.find({"nombre": "string" })]
    return personajes


@app.put("/editar_personaje/{id_personaje}")
def edit_character(id_personaje: str, data: Character):
    characters = iniciar_conexion()
    personaje_encontrado = characters.find_one({"_id": id_personaje})
    
    personaje_encontrado = {
        "_id": id_personaje,
        "nombre": data.name,
        "apellido": data.last_name,
        "año": data.age,
    }
    print(f"personaje encontrado: {personaje_encontrado}")
    
    return {"message": "id obtenido con exito",
            "id": id_personaje,
            "personaje_encontrado": personaje_encontrado}