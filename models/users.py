"""
Unicaribe OpenData API
API para la consulta de datos de estudiantes de la Universidad del Caribe, 
obtenidos con su consentimiento del sistema SIGMAA.

Autor: Unicaribe OpenData
Versión: 0.0.1.dev
Contacto: admin@unicaribe.dev

Derechos Reservados © 2024 Unicaribe OpenData. Todos los derechos reservados.
"""

from enum import Enum
from datetime import date
from pydantic import BaseModel

from models.internationalization import CountryEnum


class GenderEnum(str, Enum):
    """
    Enumeración de géneros
    """

    MALE = "masculino"
    FEMALE = "femenino"


class CivilStatusEnum(str, Enum):
    """
    Enumeración de estados civiles
    """

    SINGLE = "soltero"
    MARRIED = "casado"
    DIVORCED = "divorciado"
    WIDOW = "viudo"
    FREE_UNION = "unión libre"

class StudentBirthInfo(BaseModel):
    """
    Modelo de clase para la información de nacimiento de un estudiante.
    """

    country: CountryEnum
    state: str
    city: str
    birthdate: date


class StudentAdressInfo(BaseModel):
    """
    Modelo de clase para la información de dirección de un estudiante.
    """

    street: str
    number: str
    neighborhood: str
    city: str
    state: str
    postal_code: str


class HighSchoolRegimeEnum(str, Enum):
    """
    Enumeración de regímenes escolares
    """

    PUBLIC = "público"
    PRIVATE = "privado"


class StudentHighSchoolInfo(BaseModel):
    """
    Modelo de clase para la información de preparatoria de un estudiante.
    """

    country: CountryEnum
    state: str
    city: str
    school_name: str
    regime: HighSchoolRegimeEnum


class AccessibilityInfo(BaseModel):
    """
    Modelo de clase para la información de accesibilidad de un estudiante.
    """

    disability: bool
    sign_language: bool
    braille: bool
    wheelchair: bool
    guide_dog: bool
    other: str


class StudentInfo(BaseModel):
    """
    Modelo de clase para la información de un estudiante.
    """

    name: str
    last_name: str
    curp: str
    rfc: str
    gender: GenderEnum
    email: str
    phone: str
    civil_status: CivilStatusEnum
    address_info: StudentAdressInfo
    birthplace_info: StudentBirthInfo
    high_school_info: StudentHighSchoolInfo



class StudentWorkInfo(BaseModel):
    """
    Modelo de clase para la información laboral de un estudiante.
    """

    company: str
    position: str
    start_date: date
    end_date: date


class StudentRelativeInfo(BaseModel):
    """
    Modelo de clase para la información de un familiar de un estudiante.
    """

    name: str
    last_name: str
    phone: str
