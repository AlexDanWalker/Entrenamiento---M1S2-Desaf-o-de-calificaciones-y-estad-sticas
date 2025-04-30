# Función que solicita al usuario una calificación válida entre 0 y 100
def obtener_calificacion():
    while True:
        try: 
            calificacion = float(input("Ingrese una calificación del alumno (0 a 100): "))
            if 0 <= calificacion <= 100:
                return calificacion  # Devuelve la calificación válida
            else: 
                print("La calificación debe estar entre 0 y 100")
        except ValueError:
            print("Entrada no válida. Debes ingresar un número")

# Función que verifica si una calificación es aprobatoria (>= 60)
def verificar_aprobacion(calificacion):
    if calificacion >= 60:
        print("El alumno fue APROBADO")
    else:
        print("El alumno fue REPROBADO")

# Función que solicita una lista de calificaciones separadas por comas y valida que estén entre 0 y 100
def obtener_lista_calificaciones():
    while True:
        entrada = input("Ingresa una lista de calificaciones separadas por comas (0 a 100): ")
        try: 
            lista = [float(x.strip()) for x in entrada.split(",")]  # Convierte a float cada valor
            if all(0 <= x <= 100 for x in lista):  # Verifica que todas estén en el rango
                return lista
            else:
                print("Todas las calificaciones deben estar entre 0 y 100.")
        except ValueError:
            print("Entrada no válida. Asegúrate de ingresar solo números separados por comas")

# Función que calcula y muestra el promedio de una lista de calificaciones
def calcular_lista_calificaciones(calificaciones):
    if calificaciones:
        promedio = sum(calificaciones) / len(calificaciones)
        print(f"El promedio de las calificaciones es {promedio:.2f}")
    else:
        print("No se ingresaron calificaciones")

# Función que cuenta cuántas calificaciones son mayores que un valor proporcionado por el usuario
def contar_mayores_que(calificaciones):
    try:
        valor = float(input("Ingresa un valor para contar cuáles calificaciones son mayores: "))
        if 0 <= valor <= 100:
            contador = sum(1 for x in calificaciones if x > valor)
            print(f"Hay {contador} calificaciones mayores que {valor}.")
        else:
            print("El valor debe estar entre 0 y 100.")
    except ValueError:
        print("Entrada no válida.")

# Función principal que ejecuta el menú del programa
def main():
    while True:
        # Muestra el menú de opciones al usuario
        print("\n--- MENÚ PRINCIPAL ---")
        print("1. Verificar estado de aprobación")
        print("2. Obtener lista de calificaciones")
        print("3. Contar calificaciones mayores a un valor")
        print("4. Salir")

        # Solicita al usuario que seleccione una opción del menú
        opcion = input("Selecciona una opción (1-4): ")

        # Verifica qué opción eligió el usuario y ejecuta la función correspondiente
        if opcion == '1':
            calificacion = obtener_calificacion()
            verificar_aprobacion(calificacion)
        elif opcion == '2':
            lista = obtener_lista_calificaciones()
            calcular_lista_calificaciones(lista)
        elif opcion == '3': 
            lista = obtener_lista_calificaciones()
            contar_mayores_que(lista)
        elif opcion == '4':
            print("Programa terminado.")
            break  # Finaliza el programa
        else:
            print("Ingresa una opción válida.")  # Opción no válida

# Llamada inicial para ejecutar el programa
main()
