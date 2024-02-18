#1. Crear un menu iterativo con las siguientes opciones 
#2. opcion 1 'Saludar' , pedir datos personales
#3. opcion 2 Realizar una operacion matematica pedir 2 numeros 
#4. opcion 3 Agregar a lista un diccionario que tenga (nombre ,edad ,correo,cursos). Los cursos sera a su vez una lista de diccionario que tendra las llaves de nombre de curso y listado de notas
#5. opcion 4 calcular el promedio de las notas y agregar las notas finales a una lista  
#6. opcion 5 mostrar listado de alumnos aprobados 
#7. opcion 6 mostrar listado de alumnos desaprobados
#8. opcion 7 Generar una funcion rango hasta un numero grande (10^10) con un step y agregar a una lista los numeros que cumplan la condicion de ser multiplo de 2 ,  5 y de 7.Finalmente mostrar el tamaño de esa lista.
#9. opcion 8 llamar a una funcion que devuelva el mayor de 2 numeros ingresados por teclado.
#10. opcion 9 Salir. 
def saludar():
    nombre = input("Por favor, ingresa tu nombre: ")
    edad = input("Por favor, ingresa tu edad: ")
    print(f"\nHola {nombre}, un placer saludarte. Tienes {edad} años.\n")

def realizar_operacion():
    try:
        num1 = float(input("Ingrese el primer número: "))
        num2 = float(input("Ingrese el segundo número: "))
        operacion = input("Ingrese la operación a realizar (+, -, *, /): ")

        if operacion == '+':
            resultado = num1 + num2
        elif operacion == '-':
            resultado = num1 - num2
        elif operacion == '*':
            resultado = num1 * num2
        elif operacion == '/':
            if num2 != 0:
                resultado = num1 / num2
            else:
                print("No se puede dividir por cero.")
                return

        print(f"\nEl resultado de {num1} {operacion} {num2} es: {resultado}\n")
    except ValueError:
        print("Por favor, ingrese números válidos.")

def agregar_estudiante(lista_estudiantes):
    nombre = input("Ingrese el nombre del estudiante: ")
    edad = input("Ingrese la edad del estudiante: ")
    correo = input("Ingrese el correo del estudiante: ")
    cursos = []

    while True:
        curso_nombre = input("Ingrese el nombre del curso (o 'fin' para terminar): ")
        if curso_nombre.lower() == 'fin':
            break
        notas = input("Ingrese las notas del curso separadas por comas: ").split(',')
        cursos.append({"nombre_curso": curso_nombre, "notas": [float(nota) for nota in notas]})

    estudiante = {"nombre": nombre, "edad": edad, "correo": correo, "cursos": cursos}
    lista_estudiantes.append(estudiante)
    print("Estudiante agregado exitosamente.\n")

def calcular_promedio(notas):
    if notas:
        return sum(notas) / len(notas)
    else:
        return 0

def mostrar_alumnos(lista_estudiantes, aprobado=True):
    if aprobado:
        print("\nListado de alumnos aprobados:")
    else:
        print("\nListado de alumnos desaprobados:")
    for estudiante in lista_estudiantes:
        for curso in estudiante["cursos"]:
            promedio_curso = calcular_promedio(curso["notas"])
            if (promedio_curso >= 11.0 and aprobado) or (promedio_curso < 11.0 and not aprobado):
                print(f"Nombre: {estudiante['nombre']}, Curso: {curso['nombre_curso']}, Promedio: {promedio_curso}")

def obtener_mayor():
    num1 = float(input("Ingrese el primer número: "))
    num2 = float(input("Ingrese el segundo número: "))
    print(f"El mayor número ingresado es: {max(num1, num2)}")

def mostrar_menu():
    print("\nMostrar_Menú:")
    print("1. Saludar y pedir datos personales")
    print("2. Realizar una operación matemática con dos números")
    print("3. Agregar un estudiante a la lista")
    print("4. Calcular el promedio de las notas y agregar las notas finales a una lista")
    print("5. Mostrar listado de alumnos aprobados")
    print("6. Mostrar listado de alumnos desaprobados")
    print("8. Obtener el mayor de dos números ingresados")
    print("9. Salir")

def main():
    lista_estudiantes = []
    notas_finales = []

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            saludar()
        elif opcion == '2':
            realizar_operacion()
        elif opcion == '3':
            agregar_estudiante(lista_estudiantes)
        elif opcion == '4':
            for estudiante in lista_estudiantes:
                for curso in estudiante["cursos"]:
                    notas_finales.append(calcular_promedio(curso["notas"]))
            print("Notas finales calculadas y agregadas a la lista.")
        elif opcion == '5':
            mostrar_alumnos(lista_estudiantes, aprobado=True)
        elif opcion == '6':
            mostrar_alumnos(lista_estudiantes, aprobado=False)
        elif opcion == '8':
            obtener_mayor()
        elif opcion == '9':
            print("¡Hasta luego!")
            break
        else:
            print("Opción inválida. Por favor, seleccione una opción válida.")

if __name__ == "__main__":
    main()
