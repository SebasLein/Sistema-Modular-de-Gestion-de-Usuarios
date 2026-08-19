# Sistema Modular de Configuración y Gestión de Usuarios

Proyecto integrador para la evidencia **GA1-220501093-04-AA1-EV06** de Python avanzado (SENA). La aplicación de consola registra, lista y busca usuarios; usa un entorno virtual, dependencias, variables de entorno y paquetes de Python.

## Requisitos

- Python 3.10 o superior.
- Terminal de Windows, macOS o Linux.

## Instalación y ejecución

Desde la carpeta `sistema_usuarios`, cree y active el entorno virtual:

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
```

En macOS/Linux use `python3 -m venv .venv` y `source .venv/bin/activate`.

Instale las dependencias y ejecute el sistema:

```powershell
python -m pip install -r requirements.txt
python main.py
```

Para salir del entorno virtual use `deactivate`.

## Uso

Al iniciar se muestra el nombre, versión y administrador configurados. El menú permite:

1. Registrar un usuario con nombre y edad.
2. Listar los usuarios registrados durante la ejecución.
3. Buscar un usuario por nombre.
4. Salir.

El programa valida nombres vacíos, caracteres no válidos, edades no numéricas o fuera de 0 a 120 y nombres repetidos. Los errores se controlan con la excepción `ErrorValidacion`, sin cerrar la aplicación.

## Estructura y modularización

```text
sistema_usuarios/
├── app/
│   ├── config/
│   │   └── settings.py       # Carga las variables del archivo .env
│   └── usuarios/
│       ├── gestor.py         # Registro, listado y búsqueda
│       └── validaciones.py   # Validación de nombre y edad
├── .env                      # Configuración local (no se publica)
├── .env.example              # Plantilla segura de configuración
├── main.py                   # Menú y punto de entrada
└── requirements.txt          # Dependencias exactas
```

Los archivos `__init__.py` convierten `app`, `config` y `usuarios` en paquetes. Así cada módulo tiene una responsabilidad concreta y puede importarse claramente desde `main.py`.

## Variables de entorno

El módulo `app/config/settings.py` usa `python-dotenv` para cargar `.env` y leer:

| Variable      | Propósito                             | Valor de ejemplo   |
| ------------- | ------------------------------------- | ------------------ |
| `APP_NAME`    | Nombre mostrado por la aplicación     | `Sistema Usuarios` |
| `APP_VERSION` | Versión mostrada al iniciar           | `1.0`              |
| `ADMIN_USER`  | Saludo personalizado al administrador | `admin`            |

`.env` está en `.gitignore`; para compartir la configuración sin datos reales se versiona solamente `.env.example`.

## Evidencias para el README / repositorio

Antes de entregar, agregue capturas reales en una carpeta `capturas/` y enlácela aquí:

- Creación del entorno virtual: comando `py -m venv .venv` y la carpeta creada.
- Instalación: `python -m pip install -r requirements.txt`.
- Ejecución: menú con un registro, listado y búsqueda exitosos.
- Variables de entorno: contenido no sensible de `.env` y el saludo inicial personalizado.

![Evidencia de terminal y creación del entorno parte 1](images/Evidencia1.png)

![Evidencia de terminal, uso de variables e intalación de dependencias parte 2](images/Evidencia2.png).

## Guion para la socialización (máximo 5 minutos)

1. **30 s — Objetivo:** presentar el sistema de consola y sus tres operaciones.
2. **1 min — Organización:** mostrar `main.py`, `gestor.py`, `validaciones.py` y `settings.py`; cada uno tiene una responsabilidad.
3. **1 min — Entorno y dependencias:** explicar que `.venv` aísla `python-dotenv` y que `requirements.txt` permite reproducir la instalación.
4. **1 min — Configuración segura:** explicar `.env`, `.env.example` y `.gitignore`.
5. **1 min — Demostración:** registrar, listar, buscar y provocar una validación de edad.
6. **30 s — Reflexión:** modularizar facilita probar, mantener y reutilizar; el entorno virtual evita conflictos entre proyectos; las variables de entorno separan configuración y código, evitando publicar datos sensibles.

## Video de reflexión

Pendiente de agregar tras publicarlo: `[Ver video de reflexión](PEGAR_AQUI_EL_ENLACE_DE_YOUTUBE)`.
