"""Registro, consulta y listado de usuarios en memoria."""

from app.usuarios.validaciones import ErrorValidacion, validar_edad, validar_nombre


class GestorUsuarios:
    """Administra una colección de usuarios durante la ejecución del programa."""

    def __init__(self) -> None:
        self._usuarios: list[dict[str, int | str]] = []

    def registrar_usuario(self, nombre: str, edad: str) -> dict[str, int | str]:
        """Valida y registra un usuario; no permite nombres repetidos."""
        nombre_validado = validar_nombre(nombre)
        edad_validada = validar_edad(edad)

        if any(usuario["nombre"].casefold() == nombre_validado.casefold() for usuario in self._usuarios):
            raise ErrorValidacion(f"Ya existe un usuario llamado {nombre_validado}.")

        usuario = {"nombre": nombre_validado, "edad": edad_validada}
        self._usuarios.append(usuario)
        return usuario

    def listar_usuarios(self) -> list[dict[str, int | str]]:
        """Devuelve una copia de los usuarios registrados."""
        return self._usuarios.copy()

    def buscar_usuario(self, nombre: str) -> dict[str, int | str] | None:
        """Busca un usuario por nombre, sin distinguir mayúsculas."""
        nombre_buscado = validar_nombre(nombre).casefold()
        return next(
            (usuario for usuario in self._usuarios if usuario["nombre"].casefold() == nombre_buscado),
            None,
        )
