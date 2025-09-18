from clases.areas import Areas

def main():
    calculadora = Areas()

    while True:
        print("=== Calculadora de Áreas ===")
        print("1. Área de un Triángulo")
        print("2. Área de un Rectángulo")
        print("3. Salir")
        opcion = input("Elige una opción (1-3): ")

        if opcion == "1":
            calculadora.leerDatos("triángulo")
            print(calculadora.areaTriangulo())
        elif opcion == "2":
            calculadora.leerDatos("rectángulo")
            print(calculadora.areaRectangulo())
        elif opcion == "3":
            print("Saliendo...")
            break
        else:
            print("Opción inválida, intenta de nuevo.")

if __name__ == "__main__":
    main()
