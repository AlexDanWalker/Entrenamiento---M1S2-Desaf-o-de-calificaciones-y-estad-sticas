# Función que solicita al usuario una calificación válida entre 0 y 100
def obtener_calificacion():
    while True:  # Bucle para asegurar que la entrada sea válida
        try:
            calificacion = float(input("Ingrese una calificación del alumno (0 a 100): "))
            if 0 <= calificacion <= 100:
                return calificacion  # Devuelve la calificación válida
            else:
                print("La calificación debe estar entre 0 y 100")
        except ValueError:
            print("Entrada no válida. Debes ingresar un número")

# Función que verifica si una calificación es aprobatoria
def verificar_aprobacion(calificacion):
    if calificacion >= 60:
        print("El alumno fue APROBADO")
    else:
        print("El alumno fue REPROBADO")

# Función que permite ingresar una lista de calificaciones separadas por comas
def obtener_lista_calificaciones():
    while True:
        entrada = input("Ingresa una lista de calificaciones separadas por comas (0 a 100): ")
        try:
            # Divide la entrada y convierte cada parte a float
            lista = [float(x.strip()) for x in entrada.split(",")]
            if all(0 <= x <= 100 for x in lista):  # Valida cada valor en el rango
                return lista
            else:
                print("Todas las calificaciones deben estar entre 0 y 100.")
        except ValueError:
            print("Entrada no válida. Asegúrate de ingresar solo números separados por comas")

# Función que calcula el promedio usando un ciclo for
def calcular_lista_calificaciones(calificaciones):
    if calificaciones:
        suma = 0
        for cal in calificaciones:  # Recorre cada calificación
            suma += cal
        promedio = suma / len(calificaciones)
        print(f"El promedio de las calificaciones es {promedio:.2f}")
    else:
        print("No se ingresaron calificaciones")

# Función que cuenta cuántas calificaciones son mayores a un valor usando while
def contar_mayores_que(calificaciones):
    try:
        valor = float(input("Ingresa un valor para contar cuáles calificaciones son mayores: "))
        if 0 <= valor <= 100:
            contador = 0
            i = 0
            while i < len(calificaciones):  # Recorre con índice manual
                if calificaciones[i] > valor:
                    contador += 1
                i += 1
            print(f"Hay {contador} calificaciones mayores que {valor}.")
        else:
            print("El valor debe estar entre 0 y 100.")
    except ValueError:
        print("Entrada no válida.")

# Función que verifica si una calificación específica aparece y cuántas veces
def verificar_y_contar_calificacion(calificaciones):
    try:
        objetivo = float(input("Ingresa la calificación a buscar: "))
        if not (0 <= objetivo <= 100):
            print("La calificación debe estar entre 0 y 100.")
            return

        contador = 0
        for cal in calificaciones:
            if cal < 0 or cal > 100:
                continue  # Ignora valores fuera de rango (prevención)
            if cal == objetivo:
                contador += 1
        if contador > 0:
            print(f"La calificación {objetivo} aparece {contador} veces.")
        else:
            print(f"La calificación {objetivo} no está en la lista.")
    except ValueError:
        print("Entrada no válida. Debes ingresar un número.")

# Función principal del programa que muestra un menú y ejecuta opciones
def main():
    lista = []  # Lista vacía inicial para guardar calificaciones
    while True:
        # Menú de opciones
        print("\n--- MENÚ PRINCIPAL ---")
        print("1. Verificar estado de aprobación")
        print("2. Ingresar nueva lista de calificaciones")
        print("3. Calcular promedio de calificaciones")
        print("4. Contar calificaciones mayores a un valor")
        print("5. Buscar y contar una calificación específica")
        print("6. Salir")

        # Entrada del usuario
        opcion = input("Selecciona una opción (1-6): ")

        # Ejecución según opción seleccionada
        if opcion == '1':
            calificacion = obtener_calificacion()
            verificar_aprobacion(calificacion)
        elif opcion == '2':
            lista = obtener_lista_calificaciones()
        elif opcion == '3':
            calcular_lista_calificaciones(lista)
        elif opcion == '4':
            contar_mayores_que(lista)
        elif opcion == '5':
            verificar_y_contar_calificacion(lista)
        elif opcion == '6':
            print("Programa terminado.")
            break  # Finaliza el bucle y el programa
        else:
            print("Ingresa una opción válida.")  # Opción no reconocida

# Llamada inicial al programa
main()
