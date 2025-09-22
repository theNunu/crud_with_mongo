from pydantic import BaseModel


class Character(BaseModel):
    name: str
    last_name: str
    age: int
    state: int = 1
    
# models.py 

# class  ApiUserBase ( SQLModel ): 
#     __tablename__ = 'api_users'
    
#      active: bool = Field(..., description= "Si el usuario está activo o no" ) 
#     api_key: uuid.UUID = Field(default_factory=uuid.uuid4, description= "La clave API para el usuario" , unique= True ) 
#     monthly_credits: int = Field(..., description= "La cantidad de créditos que el usuario tiene para el mes" ) 
#     curr_credits: int = Field(..., description= "La cantidad de créditos que le quedan al usuario para el mes" ) 
#     created_at: datetime = Field(..., description= "La fecha y hora en que se creó el usuario" ) 
#     is_internal: bool = Field(..., description= "Si el usuario es interno o no" )

import uuid 
class ApiUserBase(BaseModel):
    api_key: uuid.uuid4
    active: bool
    curr_credits: int
    pass
    