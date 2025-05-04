def cargar_matriz(matriz):
    for i in range(11):
        print(f"\nJugador {i + 1}:")
        matriz[i] = [
            input("Nombre: "),
            input("Apellido: "),
            input("Posición: "),
            int(input("Goles: "))
        ]


def mostrar_matriz(matriz):
    print("\n--- Equipo ---")
    for i in range(11):
        print(f" {i + 1}: {matriz[i]}")


def modificar_matriz(matriz):
    mostrar_matriz(matriz)
    fila = int(input("Fila a modificar (1-11): ")) - 1
    columna = int(input("Columna a modificar (1-4): ")) - 1
    matriz[fila][columna] = input("Nuevo dato: ")
    print("Modificado.")


def menu():
    matriz = [None] * 11
    opcion = ""
    while opcion != "4":
        print("\n1. Cargar jugadores")
        print("2. Mostrar equipo")
        print("3. Modificar jugador")
        print("4. Salir")
        opcion = input("Opción: ")

        if opcion == "1":
            cargar_matriz(matriz)
        elif opcion == "2":
            mostrar_matriz(matriz)
        elif opcion == "3":
            modificar_matriz(matriz)
        elif opcion == "4":
            print("¡Adiós!")
        else:
            print("Opción inválida.")