"""
Unicaribe OpenData API
API para la consulta de datos de estudiantes de la Universidad del Caribe, obtenidos con su consentimiento del sistema SIGMAA.

Autor: Unicaribe OpenData
Versión: 0.0.1.dev
Contacto: admin@unicaribe.dev

Derechos Reservados © 2024 Unicaribe OpenData. Todos los derechos reservados.

MIT License

Copyright (c) 2023 Unicaribe OpenData

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""
from datetime import datetime
from contextlib import asynccontextmanager
from fastapi import FastAPI

@asynccontextmanager
async def lifespan(the_app: FastAPI):
    """
    Administrador de contexto para el ciclo de vida de la aplicación.
    """
    print("Startup")
    yield
    print("Shutdown")

app = FastAPI(
    title="Unicaribe OpenData API",
    description="API para la consulta de datos de estudiantes de la Universidad del Caribe, obtenidos con su consentimiento del sistema SIGMAA",
    version="0.0.1.dev",
    lifespan=lifespan,
    contact={
        "name": "Unicaribe OpenData",
        "url": "https://info.unicaribe.dev"
    },
    license_info={
        "name": "MIT License",
        "url": "https://opensource.org/licenses/MIT"
    },
    terms_of_service="https://unicaribe.dev/terms",
)

@app.get("/", include_in_schema=True)
async def root():
    """
    Ruta de bienvenida.
    """
    message = {
        "message": "Welcome to Unicaribe OpenData API",
        "description": "Para acceder a la documentación de la API, visita /docs o /redoc",
        "datetime": datetime.now().isoformat()
    }
    return message

@app.get("/healthcheck", include_in_schema=False)
async def healthcheck():
    """
    Ruta de verificación de estado.
    """
    return {"status": "ok"}
