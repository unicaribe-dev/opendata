"""
Unicaribe OpenData API
API para la consulta de datos de estudiantes de la Universidad del Caribe, 
obtenidos con su consentimiento del sistema SIGMAA.

Autor: Unicaribe OpenData
Versión: 0.0.1.dev
Contacto: admin@unicaribe.dev

Derechos Reservados © 2024 Unicaribe OpenData. Todos los derechos reservados.
"""

from datetime import datetime
from pydantic import BaseModel


class Welcome(BaseModel):
    """
    Clase de modelo para la respuesta de bienvenida.
    """

    message: str
    description: str
    detetime: datetime
