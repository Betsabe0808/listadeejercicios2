#1. Crear un menu iterativo con las siguientes opciones 
#2. opcion 1 'Saludar' , pedir datos personales
def saludar():
    nombre = input("Por favor, ingresa tu nombre: ")
    edad = input("Por favor, ingresa tu edad: ")
    print(f"\nHola {nombre}, gracias por proporcionar tus datos. Tienes {edad} años.\n")

def mostrar_menu():
    print("¡Bienvenido al programa!")
    print("1. Saludar")
    print("2. Otra opción")
    print("3. Salir")

def main():
    while True:
        mostrar_menu()
        opcion = input("Selecciona una opción: ")
        if opcion == '1':
            saludar()
        elif opcion == '2':
            print("Has seleccionado la opción 2")
            # Aquí puedes agregar más funcionalidades para otras opciones
        elif opcion == '3':
            print("Gracias por usar el programa. ¡Hasta luego!")
            break
        else:
            print("Opción inválida. Por favor, selecciona una opción válida.")

if __name__ == "__main__":
    main()
#3. opcion 2 Realizar una operacion matematica pedir 2 numeros 
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
#4. opcion 3 Agregar a lista un diccionario que tenga (nombre ,edad ,correo,cursos). Los cursos sera a su vez una lista de diccionario que tendra las llaves de nombre de curso y listado de notas
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

def mostrar_estudiantes(lista_estudiantes):
    for estudiante in lista_estudiantes:
        print("\nNombre:", estudiante["nombre"])
        print("Edad:", estudiante["edad"])
        print("Correo:", estudiante["correo"])
        print("Cursos:")
        for curso in estudiante["cursos"]:
            print("  Nombre del curso:", curso["nombre_curso"])
            print("  Notas:", curso["notas"])

def main():
    lista_estudiantes = []

    while True:
        print("\n¡Bienvenido al sistema de gestión de estudiantes!")
        print("1. Agregar estudiante")
        print("2. Mostrar estudiantes")
        print("3. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            agregar_estudiante(lista_estudiantes)
        elif opcion == '2':
            if lista_estudiantes:
                mostrar_estudiantes(lista_estudiantes)
            else:
                print("No hay estudiantes registrados.")
        elif opcion == '3':
            print("Gracias por usar el sistema. ¡Hasta luego!")
            break
        else:
            print("Opción inválida. Por favor, seleccione una opción válida.")
if __name__ == "__main__":
    main()
#5. opcion 4 calcular el promedio de las notas y agregar las notas finales a una lista  
#6. opcion 5 mostrar listado de alumnos aprobados 
def calcular_promedio(notas):
    if notas:
        return sum(notas) / len(notas)
    else:
        return 0

def mostrar_alumnos_aprobados(lista_estudiantes, promedio_minimo=6.0):
    print("\nListado de alumnos aprobados:")
    for estudiante in lista_estudiantes:
        for curso in estudiante["cursos"]:
            promedio_curso = calcular_promedio(curso["notas"])
            if promedio_curso >= promedio_minimo:
                print(f"Nombre: {estudiante['nombre']}, Curso: {curso['nombre_curso']}, Promedio: {promedio_curso}")

def main():
    lista_estudiantes = []

    while True:
        print("\n¡Bienvenido al sistema de gestión de estudiantes!")
        print("1. Agregar estudiante")
        print("2. Mostrar estudiantes")
        print("3. Mostrar listado de alumnos aprobados")
        print("4. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            agregar_estudiante(lista_estudiantes)
        elif opcion == '2':
            if lista_estudiantes:
                mostrar_estudiantes(lista_estudiantes)
            else:
                print("No hay estudiantes registrados.")
        elif opcion == '3':
            if lista_estudiantes:
                mostrar_alumnos_aprobados(lista_estudiantes)
            else:
                print("No hay estudiantes registrados.")
        elif opcion == '4':
            print("Gracias por usar el sistema. ¡Hasta luego!")
            break
        else:
            print("Opción inválida. Por favor, seleccione una opción válida.")

if __name__ == "__main__":
    main()
#7. opcion 6 mostrar listado de alumnos desaprobados
#8. opcion 7 Generar una funcion rango hasta un numero grande (10^10) con un step y agregar a una lista los numeros que cumplan la condicion de ser multiplo de 2 ,  5 y de 7.Finalmente mostrar el tamaño de esa lista.
#9. opcion 8 llamar a una funcion que devuelva el mayor de 2 numeros ingresados por teclado.
#10. opcion 9 Salir. 