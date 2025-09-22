from typing import Union

from fastapi import FastAPI, HTTPException
from src.mongo_db.conexion import iniciar_conexion
from src.mongo_db.models.characters_models import Character
from src.utils.generar_tiempo_real import generar_hora_y_fecha

from bson import ObjectId

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
        "state": character["state"],
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
        "state": data.state,
        "se_creo_en": tiempo_generado,
 
    }
    
    character.insert_one(informacion)
    
    #en este return se basa los nombres para llamarlos en otras operaciones
    # LO QUE ESTA DENTRO " "
    return {
        "message": "se guardo el personaje con exito!!!",
        "nombre": data.name,
        "apellido": data.last_name,
        "año": data.age,
        "state": data.state,
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
    personajes = [character_serializer(char) for char in characters.find({"state": 1})] 
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
    # personaje_encontrado = characters.find_one({"_id": id_personaje})
    
    # Validar que el ID sea un ObjectId válido
    try:
        object_id = ObjectId(id_personaje)
    except Exception:
        raise HTTPException(status_code=400, detail="ID de personaje inválido")
    
    # Preparar los datos actualizados
    tiempo_generado = generar_hora_y_fecha()
    informacion_actualizada = {
        "nombre": data.name,
        "apellido": data.last_name,
        "año": data.age,
        "se_actualizo_en": tiempo_generado  # Actualiza la fecha de creación (puedes omitir esto si no deseas cambiarla)
    }

    # Actualizar el documento en MongoDB
    resultado = characters.update_one(
        {"_id": object_id},  # Filtro para encontrar el documento por ID
        {"$set": informacion_actualizada}  # Datos a actualizar
    )

    # Verificar si se actualizó algún documento
    if resultado.matched_count == 0:
        raise HTTPException(status_code=404, detail="Personaje no encontrado")
    
    # Devolver una respuesta con los datos actualizados
    
    return {"message": "id actualizado con exito",
            "id_personaje": id_personaje,
            "nombre": data.name,
            "apellido": data.last_name,
            "año": data.age,
            }  
    
@app.put("/eliminar_personaje/{id_personaje}")
def delete_charcater(id_personaje: str, data: Character):
    characters = iniciar_conexion()
        # Validar que el ID sea un ObjectId válido
    try:
        object_id = ObjectId(id_personaje)
    except Exception:
        raise HTTPException(status_code=400, detail="ID de personaje inválido")
    
        # Preparar los datos actualizados
    tiempo_generado = generar_hora_y_fecha()
    informacion_actualizada = {
        # "nombre": data.name,
        # "apellido": data.last_name,
        # "año": data.age,
        "state": data.state,
        "se_elimino_en": tiempo_generado  # Actualiza la fecha de creación (puedes omitir esto si no deseas cambiarla)
    }

    # Actualizar el documento en MongoDB
    resultado = characters.update_one(
        {"_id": object_id},  # Filtro para encontrar el documento por ID
        {"$set": {"state": 0}}  # Datos a actualizar
    )
    
    nuevos_valores = {
        "$set": { "state": False}
    }
        # Verificar si se actualizó algún documento
    if resultado.matched_count == 0:
        raise HTTPException(status_code=404, detail="Personaje no encontrado")
    
    # Devolver una respuesta con los datos actualizados
    
    return {"message": "id eliminado con exito",
            "id_personaje": id_personaje,
            "nombre": data.name,
            "apellido": data.last_name,
            "año": data.age,
            }  
    
    
    
@app.get("/obtener_personajes_eliminados")
def traer_personajes_borrados():
    characters = iniciar_conexion()
    # def iniciar_bucle():
    #     for c in character.find():
    #         # print(c)
    #         return c
    # result = iniciar_bucle()
    # print(f"resultado del bucle: {result}")
    personajes = [character_serializer(char) for char in characters.find({"state": 0})] 
    print(f"\nall characters: {personajes}")
    return personajes
