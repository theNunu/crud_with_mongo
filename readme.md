# crear el entorno virtual

python -m venv venv

# activar el venv

venv\Scripts\activate

# instalar los requirimientos

pip install -r requirements.txt

# usando el port 3030
--port=3030

# correr el proyecto

fastapi dev src/routes/characters_routes.py 
