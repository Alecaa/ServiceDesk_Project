from fastapi import FastAPI
from app.controllers import auth_controller, ticket_comentario_controller
from app.controllers import emp_controller
from app.controllers import user_controller
from app.controllers import ticket_controller
from app.controllers import ticket_evidencia_controller
from app.controllers import area_controller
from fastapi.middleware.cors import CORSMiddleware



app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

@app.get("/")
def root():
    return {"msg": "API funcionando"}

app.include_router(auth_controller.router)
app.include_router(emp_controller.router)
app.include_router(user_controller.router)  
app.include_router(ticket_controller.router)
app.include_router(ticket_comentario_controller.router)
app.include_router(ticket_evidencia_controller.router)
app.include_router(area_controller.router)

from fastapi import WebSocket, WebSocketDisconnect
from app.utils.websocket_manager import manager

@app.websocket("/ws/notificaciones")
async def websocket_endpoint(websocket: WebSocket):
    await manager.connect(websocket)
    try:
        while True:
            # Mantener la conexión viva, esperando recibir algo (ping/pong)
            data = await websocket.receive_text()
    except WebSocketDisconnect:
        manager.disconnect(websocket)

@app.get("/debug-rutas")
def listar_rutas():
    # Esto te dirá exactamente qué rutas existen y qué prefijos tienen
    return [{"path": route.path, "methods": list(route.methods)} for route in app.routes]


#Activar entorno virtual: venv\Scripts\activate
#Correr proyecto: uvicorn app.main:app --reload