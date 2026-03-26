<<<<<<< HEAD
# Service Desk API - FastAPI

Sistema backend de gestión de tickets (Service Desk) desarrollado con **FastAPI + MySQL**, orientado a empresas para el manejo de incidencias, asignación de técnicos y seguimiento de solicitudes.

---

# Características principales

* Autenticación con JWT
* Control de acceso por roles (RBAC)
* Multi-tenant (por empresa)
* Gestión completa de tickets
* Comentarios (internos y públicos)
* Escalamiento de tickets
* Evidencias (archivos reales)
* Resolución de tickets
* Reportes (SQL + PDF) --- Pronto

---

# Instalación rápida

```bash
git clone <repo>
cd servicedesk
pip install -r requirements.txt
uvicorn main:app --reload
```

Swagger:
http://localhost:8000/docs

---

# AUTENTICACIÓN

## Login (Super Admin)

```http
POST /auth/login
```

```json
{
  "username": "root",
  "password": "123456"
}
```

Copiar token:

```http
Authorization: Bearer <TOKEN>
```

---

# PRUEBAS EN POSTMAN (FUNCIONALES)

# === Ejecutar en este orden===

---

# 1. CREAR EMPRESA

```http
POST /empresa/
```

```json
{
  "razon_social": "Empresa Test",
  "identificacion": "900111222",
  "contacto": "Juan Perez",
  "correo": "empresa@test.com"
}
```

---

# 2. CREAR USUARIOS

## Admin empresa

```http
POST /usuarios/
```

```json
{
  "username": "admin1",
  "nombre": "Admin Empresa",
  "password": "123456",
  "correo": "admin@test.com",
  "contacto": "3000000000",
  "id_rol": 2,
  "id_empresa": 1
}
```

---

## Técnico

```json
{
  "username": "tec1",
  "nombre": "Tecnico N1",
  "password": "123456",
  "correo": "tec@test.com",
  "contacto": "3000000001",
  "id_rol": 3,
  "id_area": 1
}
```

---

## Cliente

```json
{
  "username": "cliente1",
  "nombre": "Cliente Demo",
  "password": "123456",
  "correo": "cliente@test.com",
  "contacto": "3000000002",
  "id_rol": 4,
  "id_empresa": 1
}
```

---

# 3. CREAR TICKET (LOGIN COMO CLIENTE)

```http
POST /auth/login
```

```json
{
  "username": "cliente1",
  "password": "123456"
}
```

---

```http
POST /tickets/
```

```json
{
  "modulo": "Facturación",
  "tipo_caso": "Error",
  "descripcion": "No genera factura",
  "prioridad": "Alta"
}
```

---

# 4. LISTAR TICKETS

```http
GET /tickets/
```

---

# 5. ASIGNAR TICKET (LOGIN ADMIN)

```http
POST /tickets/1/asignar?id_tec=3&id_area=1
```

---

# 6. COMENTARIOS

```http
POST /tickets/1/comentarios
```

```json
{
  "comentario": "Estamos revisando el caso",
  "tipo": "publico"
}
```

---

# 7. ESCALAR TICKET

```http
POST /tickets/1/escalar
```

```json
{
  "id_area": 4,
  "id_tec": 6,
  "motivo": "Requiere soporte nivel 2"
}
```

---

# 8. RESOLVER TICKET

```http
POST /tickets/1/solucion
```

```json
{
  "solucion": "Se reinició el servidor y quedó operativo"
}
```

---

# 9. SUBIR EVIDENCIA

```http
POST /tickets/1/evidencias
```

👉 En Postman:

* Body → form-data
* key: `file`
* tipo: File


---
# VALIDACIONES IMPORTANTES

* Cliente solo ve sus tickets
* Admin solo su empresa
* Técnico gestiona tickets asignados
* Comentarios internos no visibles para cliente
* Escalamiento genera historial
* Token obligatorio

---

# NOTAS IMPORTANTES

* El sistema usa **multi-tenant por empresa**
* Los tickets se relacionan por `codigo_empresa`
* Los números de ticket se generan automáticamente
* Evidencias se almacenan como archivos

---

# ESTADO DEL PROYECTO

✔ Sistema completamente funcional
✔ Flujo real de soporte técnico
✔ Listo para escalar

---

# FUTURO
* Reportes
* Dashboard con gráficas
* Notificaciones
* SLA
* Cloud storage (AWS S3)
=======
# servicedesk
>>>>>>> 7379ee4b923faa98f711bef2de9fc40e3642dfc2
