import sys
import os

# Aseguramos que se pueda importar "app" agregando el directorio actual al path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from app.config.db import get_db
from app.utils.security import hash_password
from app.repositories import emp_repo, user_repo, ticket_repo
from app.schemas.emp_schema import EmpresaCreate
from app.schemas.user_schema import UserCreate
from app.schemas.ticket_schema import TicketCreate
from datetime import datetime
import random

def run_seeder():
    print("Iniciando seeder de base de datos...")
    gen = get_db()
    db = next(gen)
    
    try:
        # 1. Crear Empresa de Prueba
        print("Creando empresa de prueba...")
        emp_data = EmpresaCreate(
            razon_social=f"Empresa de Pruebas {random.randint(100, 999)}",
            identificacion=f"NIT-{random.randint(100000, 999999)}",
            contacto="Contacto Test",
            correo=f"contacto{random.randint(100, 999)}@pruebas.com"
        )
        id_empresa = emp_repo.crear_empresa(db, emp_data)
        codigo_emp = f"EMP{id_empresa:04d}"
        emp_repo.actualizar_codigo(db, id_empresa, codigo_emp)
        db.commit()
        print(f"✅ Empresa creada (ID: {id_empresa}, Código: {codigo_emp})")

        # 2. Crear Usuarios (Admin, Cliente, Técnico)
        print("Creando usuarios de prueba...")
        pass_hash = hash_password("123456")
        
        # Admin
        admin_data = UserCreate(
            id_empresa=id_empresa,
            id_rol=2, # Admin
            username=f"admin_test_{id_empresa}",
            nombre="Administrador Test",
            password="fake_password", # Se reemplaza abajo
            contacto="3000000000",
            correo=f"admin{id_empresa}@test.com"
        )
        id_admin = user_repo.crear_usuario(db, admin_data, pass_hash)
        
        # Cliente
        cliente_data = UserCreate(
            id_empresa=id_empresa,
            id_rol=4, # Cliente
            username=f"cliente_test_{id_empresa}",
            nombre="Cliente Test",
            password="fake_password",
            contacto="3000000001",
            correo=f"cliente{id_empresa}@test.com"
        )
        id_cliente = user_repo.crear_usuario(db, cliente_data, pass_hash)

        # Tecnico (Área 1 = Soporte N1)
        tecnico_data = UserCreate(
            id_empresa=None,
            id_rol=3, # Tecnico
            id_area=1, 
            username=f"tecnico_test_{id_empresa}",
            nombre="Tecnico Test",
            password="fake_password",
            contacto="3000000002",
            correo=f"tecnico{id_empresa}@test.com"
        )
        id_tecnico = user_repo.crear_usuario(db, tecnico_data, pass_hash)

        db.commit()
        print(f"✅ Usuarios creados: Admin ({admin_data.username}), Cliente ({cliente_data.username}), Tecnico ({tecnico_data.username}) - [Contraseña: 123456]")

        # 3. Crear Tickets
        print("Creando tickets de prueba...")
        for i in range(1, 4):
            ticket_data = TicketCreate(
                id_empresa=id_empresa,
                modulo="Hardware",
                tipo_caso="Incidente",
                prioridad="Media",
                descripcion=f"Problema con equipo de prueba #{i}",
                comentario="Por favor ayuda"
            )
            # Simular que lo crea el cliente
            user_cliente = {"id": id_cliente, "id_empresa": id_empresa, "id_rol": 4}
            id_ticket = ticket_repo.crear_ticket(db, ticket_data, user_cliente, None)
            num_ticket = f"TKT-{id_ticket:06d}"
            ticket_repo.actualizar_numero_ticket(db, id_ticket, num_ticket)
            print(f"✅ Ticket creado: {num_ticket}")

        db.commit()
        print("\n🎉 Seeder ejecutado con éxito.")
        
    except Exception as e:
        db.rollback()
        print(f"❌ Error en seeder: {e}")
    finally:
        db.close()

if __name__ == "__main__":
    run_seeder()
