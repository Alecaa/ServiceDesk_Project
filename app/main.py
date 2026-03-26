from fastapi import FastAPI
from app.controllers import auth_controller, ticket_comentario_controller
from app.controllers import emp_controller
from app.controllers import user_controller
from app.controllers import ticket_controller
from app.controllers import ticket_evidencia_controller
<<<<<<< HEAD
from fastapi.middleware.cors import CORSMiddleware
=======
>>>>>>> 7379ee4b923faa98f711bef2de9fc40e3642dfc2



app = FastAPI()
<<<<<<< HEAD
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)
=======
>>>>>>> 7379ee4b923faa98f711bef2de9fc40e3642dfc2

@app.get("/")
def root():
    return {"msg": "API funcionando"}

app.include_router(auth_controller.router)
app.include_router(emp_controller.router)
app.include_router(user_controller.router)  
app.include_router(ticket_controller.router)
app.include_router(ticket_comentario_controller.router)
app.include_router(ticket_evidencia_controller.router)


<<<<<<< HEAD
=======

















>>>>>>> 7379ee4b923faa98f711bef2de9fc40e3642dfc2
#Activar entorno virtual: venv\Scripts\activate
#Correr proyecto: uvicorn app.main:app --reload