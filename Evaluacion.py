import time  # Importa el módulo 'time' para manejar el tiempo
votos = []  # Lista para almacenar los votos de los usuarios

class Registro:
    registros = {}  # Diccionario para almacenar el estado del registro de los usuarios

    def __init__(self, id, nombre):
        self.id = id
        self.nombre = nombre
        self.registros[id] = False  # Inicializa el estado del usuario como no registrado

    def registrarse(self):
        # Registra a un usuario si aún no está registrado
        if self.registros[self.id] == False:
            self.registros[self.id] = True  # Marca al usuario como registrado
            print("Usuario registrado exitosamente")
        else:
            print("El ID ya está registrado")  # Indica que el ID ya está en uso

    def votar(self):
        # Permite a un usuario votar por un candidato si está registrado y no ha votado antes
        if self.registros[self.id] == True:
            if self.id in votos:
                print("Ya votó anteriormente, no puede votar de nuevo")
            else:
                # Pide al usuario que elija un candidato y registra su voto
                cajita = int(input("Ingrese el número del candidato: 1 - Pepito, 2 - Tilin, 3 - Rodriguez, 4 - En Blanco "))
                votos.append(cajita)  # Agrega el voto a la lista de votos
                print("Gracias por votar")
        else:
            print("El usuario no está registrado")  # Indica que el usuario no está registrado

    def ganadoresPerdedoresYempates(self):
        # Inicializa contadores para cada candidato y votos en blanco
        self.contadorPepito = 0
        self.contadorTilin = 0
        self.contadorRodrigez = 0
        self.contadorBlanco = 0

        # Cuenta los votos para cada candidato
        for voto in votos:
            if voto == 1:
                self.contadorPepito += 1
            elif voto == 2:
                self.contadorTilin += 1
            elif voto == 3:
                self.contadorRodrigez += 1
            elif voto == 4:
                self.contadorBlanco += 1

        # Compara los votos para determinar el ganador, perdedor o empate
        if self.contadorPepito > self.contadorTilin and self.contadorPepito > self.contadorRodrigez and self.contadorPepito > self.contadorBlanco:
            print('Ganó Pepito')
        # Resto de las comparaciones para determinar el resultado de la votación...

def mostrar_Menu():
    # Muestra el menú de opciones para el usuario
    print("\n--- Menú ---")
    print("1. Registrarse")
    print("2. Votar")
    print("3. Salir...")

while True:  # Bucle principal del programa
    mostrar_Menu()  # Muestra el menú
    opcion = int(input("\nSeleccione una opción: "))  # Solicita al usuario que elija una opción

    if opcion == 1:
        print("Ingrese su ID:")
        id = int(input())
        print("Ingrese su nombre:")
        nombre = input()
        registro = Registro(id, nombre)  # Crea un nuevo objeto Registro para el usuario
        registro.registrarse()  # Llama al método para registrar al usuario
    elif opcion == 2:
        registro.votar()  # Llama al método para que el usuario vote
    elif opcion == 3:
        registro.ganadoresPerdedoresYempates()  # Llama al método para mostrar los resultados de la votación
        print("Gracias por participar")
        time.sleep(3)  # Espera 3 segundos antes de salir del programa
        break
    else:
        print("Opción no válida, por favor elija una opción correcta")  # Indica que la opción seleccionada no es válida
