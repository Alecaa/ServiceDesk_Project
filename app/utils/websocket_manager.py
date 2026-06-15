from fastapi import WebSocket
import json

class ConnectionManager:
    def __init__(self):
        self.active_connections: list[WebSocket] = []

    async def connect(self, websocket: WebSocket):
        await websocket.accept()
        self.active_connections.append(websocket)

    def disconnect(self, websocket: WebSocket):
        if websocket in self.active_connections:
            self.active_connections.remove(websocket)

    async def broadcast_new_ticket(self, num_ticket: str, modulo: str):
        message = {
            "type": "NEW_TICKET",
            "num_ticket": num_ticket,
            "modulo": modulo,
            "mensaje": f"Nuevo ticket creado: {num_ticket}"
        }
        json_message = json.dumps(message)
        
        for connection in list(self.active_connections):
            try:
                await connection.send_text(json_message)
            except Exception:
                self.disconnect(connection)

manager = ConnectionManager()
