#creamos una clase llamada registro 

class Registro:

    #donde usamos un metodo constructor donde usa un diccionario para los registros de las personas y una lista para los votos 
    def __init__(self):
        self.registros = {}  # Diccionario para almacenar el estado del registro de los usuarios
        self.votos = []  # Lista para almacenar los votos de los usuarios

    #creamos un metodo donde principalmente usamos el self, un id.. y un nombre
    def registrar_usuario(self, id, nombre):
        #donde creamos un donde si el id esta en el diccionario de registros.. va a imprimir que ya esta registrado
        if id in self.registros:
            print("El ID ya está registrado")
            return False
        else:
            #aca marca al usuario como no registrado y e imprime la informacion
            self.registros[id] = False
            print("Usuario registrado exitosamente")
            return True
    #aca creamos un metodo para votar... donde si id no esta en el diccionario o si en el diccionario no hay un id en especeifico que si sea igual a True (significando que ya voto)... le imprime lo siguiente
    def votar(self, id):
        if id not in self.registros or self.registros[id]:
            print("El usuario no está registrado o ya votó anteriormente")
            return False
        #si eso es al contrario... crea un menu para los votantes 
        else:
            while True:
                cajita = input("Ingrese el número del candidato: 1 - Pepito, 2 - Tilin, 3 - Rodriguez, 4 - En Blanco ")
                #donde usamos un condicional con el metodo isdigit que lo que hace es poner a la variable cajita como dijito
                if cajita.isdigit():
                    #y lo confimarmos haciendo que sol reciba numeros 
                    cajita = int(cajita)
                    #aca queriamos hacer que no se cogiera otro candidato inexistente 
                    if cajita >= 1 and cajita <= 4:
                        #donde independiente del candidato se agrega cajita dentro de la lista votos... solo el numero
                        self.votos.append(cajita) 
                        self.registros[id] = True  # y marca el usuario como ya votado
                        print("Gracias por votar")
                        return True
                    else:
                        print("Por favor, elija un número válido de candidato.")
                else:
                    print("Entrada inválida. Por favor, ingrese un número.")

    #gracias starckoverflow... aca creamos el metodo para mostrar los resultados... donde creamos un contador tipo lista (nunca se me ocurrio la verdad) donde va a coger los votos en cada direccion 
    def mostrar_resultados(self):
        contador = [0, 0, 0, 0]
        #aca creamos un bucle para los votos 
        for voto in self.votos:
            #donde el contador por cada indice... osea lo que hace es acordar el indice de los votos por el indice del contador y se le suma +1 al indice que estamos votando
            contador[voto - 1] += 1
        #aca generamos el maximo de los votos 
        max_votos = max(contador)
        #aca creamos el ganador donde sacamos el indice correspondiente a los candidatos donde creamos un bucle donde buscamos por indice y elemento iterando el contador con enumerate y si v es igual al maximo de votos hace lo siguiente
        ganadores = [i + 1 for i, v in enumerate(contador) if v == max_votos]

        #aca se hace una lectura de la lista ganadores donde si ganadores es igual ==1 sigue con lo siguiente 
        if len(ganadores) == 1:
            # donde ganador ahora es a 0 y busca a los candidatos por los contadores y encuentra al ganador 
            ganador = ganadores[0]
            print("Resultados de la votación:")
            print(f"Candidato 1 (Pepito): {contador[0]} votos")
            print(f"Candidato 2 (Tilin): {contador[1]} votos")
            print(f"Candidato 3 (Rodriguez): {contador[2]} votos")
            print(f"En Blanco: {contador[3]} votos")
            print(f"Ganador: Candidato {ganador}")
            #si no encuentra en un bucle al que empato
        else:
            print("Hubo un empate entre los siguientes candidatos:")
            for ganador in ganadores:
                print(f"Candidato {ganador} empata con {max_votos} votos")

#aca creamos el menu
def mostrar_menu():
    print("\n--- Menú ---")
    print("1. Registrarse")
    print("2. Votar")
    print("3. Ver Resultados")
    print("4. Salir")
#aca llamamos el objeto y hacemos un main 
def main():
    registro = Registro()

    while True:
        mostrar_menu()
        opcion = input("\nSeleccione una opción: ")

        if opcion == '1':
            id = int(input("Ingrese su ID: "))
            nombre = input("Ingrese su nombre: ")
            registro.registrar_usuario(id, nombre)
        elif opcion == '2':
            id = int(input("Ingrese su ID: "))
            registro.votar(id)
        elif opcion == '3':
            registro.mostrar_resultados()
        elif opcion == '4':
            print("Gracias por participar")
            break
        else:
            print("Opción no válida, por favor elija una opción correcta")

#se utiliza en Python para asegurarse de que el código dentro de este bloque se ejecute solo si el archivo Python se está ejecutando como el programa principal.
#esto tambien lo supe por stackoverflow

if __name__ == "__main__":
    main()
