import time

votos = []

class Registro:
    registros = {}

    def __init__(self, id, nombre):
        self.id = id
        self.nombre = nombre
        self.registros[id] = False

    def registrarse(self):
        if self.registros[self.id] == False:
            self.registros[self.id] = True
            print("Usuario registrado exitosamente")
        else:
            print("El id ya está registrado")

    def votar(self):
        if self.registros[self.id] == True:
            if self.id in votos:
                print("Lo siento, ya está registrado y no puede votar")
            else:
                cajita = int(input("Ingrese candidato al cual quiere votar:\n '1' para Pepito, \n '2' para Tilin, \n '3' Rodriguez. \n '4' En Blanco "))
                votos.append(self.id)
                print("Gracias por votar")
        else:
            print("El id no está registrado")

    def ganadoresPerdedoresYempates(self):
        self.contadorPepito=0
        self.contadorTilin=0
        self.contadorRodrigez=0
        self.contadorBlanco=0
        self.totalVotos = self.contadorPepito + self.contadorTilin + self.contadorRodrigez 

        for voto in votos:
            if voto == 1:
                print('Votaste Por pepito')
                self.contadorPepito+=1
            elif voto == 2:
                print('votaste por tilin')
                self.contadorTilin+=1
            elif voto == 3:
                print('votaste por rodriguez')
                self.contadorRodrigez+=1
            elif voto == 4:
                print('votaste por el blanco')
                self.contadorBlanco+=1


        if self.contadorPepito > self.contadorTilin and self.contadorPepito > self.contadorRodrigez and self.contadorPepito > self.contadorBlanco:
            print('Gano Pepito')
        elif self.contadorTilin > self.contadorPepito and self.contadorTilin > self.contadorRodrigez and self.contadorTilin > self.contadorBlanco:
            print('Gano Tilin')
        elif self.contadorRodrigez > self.contadorPepito and self.contadorRodrigez > self.contadorTilin and self.contadorRodrigez > self.contadorBlanco:
            print('Gano Rodriguez')
        elif self.contadorBlanco > self.contadorPepito and self.contadorBlanco > self.contadorTilin and self.contadorBlanco > self.contadorRodrigez:
            print('Gano el blanco porque los negros nunca ganan :C')
        elif self.contadorPepito == self.contadorTilin or self.contadorPepito == self.contadorRodrigez or self.contadorPepito == self.contadorBlanco:
            print('Hubo un empate')
        else: 
            print('El blanco gano porque no votaste por él :(')

def mostrar_Menu():
    print("\n--- Menú ---")
    print("1. Registrarse")
    print("2. Votar")
    print("3. Salir...")

while True:
    mostrar_Menu()
    opcion = int(input("\nSeleccione una opción: "))
    if opcion == 1:
        print("Ingrese su id:")
        id = int(input())
        print("Ingrese su nombre:")
        nombre = input()
        registro = Registro(id, nombre)
        registro.registrarse()
    elif opcion == 2:
        registro.votar()
    elif opcion == 3:
        registro.ganadoresPerdedoresYempates()
        print("Gracias por participar")
        time.sleep(3)
        break
    else:
        print("Error: la opción no es válida")