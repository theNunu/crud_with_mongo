
#  -------  ------ ----- ----- ---- auth.py --- ---- ---- ---- -- ---- 

from fastapi import Security, HTTPException, status, Request, Depends
from fastapi.security import APIKeyHeader
from motor.motor_asyncio import AsyncIOMotorClient
from src.mongo_db.models.characters_models import ApiUserBase
# Encabezado para la clave API
api_key = APIKeyHeader(name="x-api-key")

# Lista de rutas internas
internal_routes = [
    '/users'
]

# Dependencia para obtener el cliente de MongoDB
async def get_mongo_client():
    client = AsyncIOMotorClient("mongodb://localhost:27017")
    try:
        yield client
    finally:
        client.close()

# Dependencia para obtener la colección de MongoDB
async def get_mongo_collection():
    client = AsyncIOMotorClient("mongodb://localhost:27017")
    db = client["crud_mongo"]
    collection = db["character"]
    try:
        yield collection
    finally:
        client.close()
        

# Función de autenticación adaptada para MongoDB
async def handle_api_key(req: Request, collection=Depends(get_mongo_collection), key: str = Security(api_key)):
    # Buscar el usuario en MongoDB por la clave API y estado activo
    api_key_data = await collection.find_one({"api_key": key, "active": True})

    # No se encontró una clave API activa
    if not api_key_data:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Clave API no encontrada o inválida"
        )

    # Convertir el documento de MongoDB a un modelo Pydantic
    api_user = ApiUserBase(**api_key_data)

    # Verificar si el usuario intenta acceder a una ruta interna
    for path in internal_routes:
        if path in req.url.path and not api_user.is_internal:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="No tienes permiso para acceder a esta ruta"
            )

    # Verificar si el usuario tiene créditos disponibles
    if api_user.curr_credits <= 0:
        raise HTTPException(
            status_code=status.HTTP_402_PAYMENT_REQUIRED,
            detail="No tienes créditos disponibles para este mes"
        )

    # Decrementar los créditos del usuario
    await collection.update_one(
        {"api_key": key},
        {"$set": {"curr_credits": api_user.curr_credits - 1}}
    )

    yield api_user