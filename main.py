"""Punto de entrada del Sistema Modular de Gestión de Usuarios."""

from app.config.settings import ADMIN_USER, APP_NAME, APP_VERSION
from app.usuarios.gestor import GestorUsuarios
from app.usuarios.validaciones import ErrorValidacion


def mostrar_menu() -> None:
    print("\n1. Registrar usuario")
    print("2. Listar usuarios")
    print("3. Buscar usuario")
    print("4. Salir")


def registrar(gestor: GestorUsuarios) -> None:
    usuario = gestor.registrar_usuario(input("Nombre: "), input("Edad: "))
    print(f"Usuario {usuario['nombre']} registrado correctamente.")


def listar(gestor: GestorUsuarios) -> None:
    usuarios = gestor.listar_usuarios()
    if not usuarios:
        print("Aún no hay usuarios registrados.")
        return
    print("\nUsuarios registrados:")
    for indice, usuario in enumerate(usuarios, start=1):
        print(f"{indice}. {usuario['nombre']} - {usuario['edad']} años")


def buscar(gestor: GestorUsuarios) -> None:
    usuario = gestor.buscar_usuario(input("Nombre a buscar: "))
    if usuario is None:
        print("Usuario no encontrado.")
        return
    print(f"Usuario encontrado: {usuario['nombre']} - {usuario['edad']} años.")


def main() -> None:
    gestor = GestorUsuarios()
    print(f"Bienvenido a {APP_NAME} v{APP_VERSION}, {ADMIN_USER}.")

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ").strip()
        try:
            if opcion == "1":
                registrar(gestor)
            elif opcion == "2":
                listar(gestor)
            elif opcion == "3":
                buscar(gestor)
            elif opcion == "4":
                print("Gracias por usar el sistema. Hasta pronto.")
                break
            else:
                print("Opción no válida. Intente nuevamente.")
        except ErrorValidacion as error:
            print(f"Error de validación: {error}")
        except (EOFError, KeyboardInterrupt):
            print("\nEjecución cancelada por el usuario.")
            break


if __name__ == "__main__":
    main()
