"""
Unicaribe OpenData API
API para la consulta de datos de estudiantes de la Universidad del Caribe, 
obtenidos con su consentimiento del sistema SIGMAA.

Autor: Unicaribe OpenData
Versión: 0.0.1.dev
Contacto: admin@unicaribe.dev

Derechos Reservados © 2024 Unicaribe OpenData. Todos los derechos reservados.
"""

from fastapi import APIRouter

from models.users import StudentInfo

users = APIRouter(prefix="/users", tags=["users"])


@users.get("/me", status_code=200)
async def read_users_me() -> StudentInfo:
    """
    Obtiene los datos del usuario autenticado.

    Returns:

    """

    test_data = {
        "name": "Juan",
        "last_name": "Perez",
        "curp": "JUPL900101HDFRNN09",
        "rfc": "JUPL900101",
        "gender": "masculino",
        "email": "juan.perez@example.com",
        "phone": "9981234567",
        "civil_status": "soltero",
        "address_info": {
            "street": "Avenida Tulum",
            "number": "123",
            "neighborhood": "Centro",
            "city": "Cancun",
            "state": "Quintana Roo",
            "postal_code": "77500",
        },
        "birthplace_info": {
            "country": "MEXICO",
            "state": "Ciudad de Mexico",
            "city": "Ciudad de Mexico",
            "birthdate": "1990-01-01",
        },
        "high_school_info": {
            "country": "MEXICO",
            "state": "Quintana Roo",
            "city": "Cancun",
            "school_name": "Preparatoria Cancun",
            "regime": "público",
        },
    }

    return test_data
