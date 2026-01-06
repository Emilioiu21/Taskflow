# Tests manuales para Thunder Client

Base URL (asumiendo servidor en local): `http://localhost:5000`

1) Health
- Método: GET
- URL: `/api/health`
- Respuesta esperada: `{ "status": "ok", "message": "TaskFlow API v1.0" }`

2) Listar usuarios
- Método: GET
- URL: `/api/users`

3) Obtener usuario por ID
- Método: GET
- URL: `/api/users/1`

4) Crear usuario
- Método: POST
- URL: `/api/users`
- Body (JSON):

```
{
  "name": "Carlos"
}
```

Respuesta esperada: código `201` y el objeto creado, por ejemplo `{ "id": 3, "name": "Carlos" }`.

5) Actualizar usuario
- Método: PUT
- URL: `/api/users/2`
- Body (JSON):

```
{
  "name": "Juan Pérez"
}
```

Respuesta esperada: `200` y el objeto actualizado.

6) Eliminar usuario
- Método: DELETE
- URL: `/api/users/2`

Notas:
- Asegúrate de arrancar el servidor backend (ver instrucciones abajo) antes de ejecutar las peticiones.

Instrucciones para preparar entorno y arrancar (PowerShell):

```
cd backend
# Crear entorno virtual (requiere Python instalado)
python -m venv venv

# Activar el entorno (PowerShell)
.\venv\Scripts\Activate.ps1

# Instalar dependencias
pip install -r requirements.txt

# Ejecutar el servidor
python app.py
```

Si no tienes Python instalado, instala Python 3.11+ desde https://www.python.org/downloads/windows/ y marca "Add Python to PATH" durante la instalación.
