"""Validaciones de datos de entrada para los usuarios."""


class ErrorValidacion(ValueError):
    """Excepción controlada para datos de usuario no válidos."""


def validar_nombre(nombre: str) -> str:
    """Limpia y valida que el nombre no esté vacío y solo use letras y espacios."""
    nombre_limpio = nombre.strip()
    if not nombre_limpio:
        raise ErrorValidacion("El nombre no puede estar vacío.")
    if not all(caracter.isalpha() or caracter.isspace() for caracter in nombre_limpio):
        raise ErrorValidacion("El nombre solo puede contener letras y espacios.")
    return nombre_limpio.title()


def validar_edad(edad: str) -> int:
    """Convierte la edad y comprueba que sea un entero entre 0 y 120."""
    try:
        edad_entera = int(edad)
    except ValueError as error:
        raise ErrorValidacion("La edad debe ser un número entero.") from error

    if not 0 <= edad_entera <= 120:
        raise ErrorValidacion("La edad debe estar entre 0 y 120 años.")
    return edad_entera
