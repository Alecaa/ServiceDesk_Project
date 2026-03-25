from fastapi import FastAPI
from app.controllers import auth_controller, ticket_comentario_controller
from app.controllers import emp_controller
from app.controllers import user_controller
from app.controllers import ticket_controller
from app.controllers import ticket_evidencia_controller



app = FastAPI()

@app.get("/")
def root():
    return {"msg": "API funcionando"}

app.include_router(auth_controller.router)
app.include_router(emp_controller.router)
app.include_router(user_controller.router)  
app.include_router(ticket_controller.router)
app.include_router(ticket_comentario_controller.router)
app.include_router(ticket_evidencia_controller.router)



















#Activar entorno virtual: venv\Scripts\activate
#Correr proyecto: uvicorn app.main:app --reload