"""Carga centralizada de variables de entorno desde el archivo .env."""

import os
from pathlib import Path

from dotenv import load_dotenv

RAIZ_PROYECTO = Path(__file__).resolve().parents[2]
load_dotenv(RAIZ_PROYECTO / ".env")

APP_NAME = os.getenv("APP_NAME", "Sistema de Usuarios")
APP_VERSION = os.getenv("APP_VERSION", "1.0")
ADMIN_USER = os.getenv("ADMIN_USER", "admin")
