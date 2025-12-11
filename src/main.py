#!/usr/bin/env python3
"""
Programa principal de la calculadora
"""

from calculadora import suma, resta, multiplicacion, division

def mostrar_menu():
    """Muestra el menú de opciones"""
    print("\n=== CALCULADORA PYTHON ===")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")
    print("5. Salir")

def main():
    """Función principal del programa"""
    print("Bienvenido a la Calculadora Python")
    
    while True:
        mostrar_menu()
        opcion = input("\nSeleccione una opción (1-5): ")
        
        if opcion == "5":
            print("¡Hasta luego!")
            break
        
        if opcion not in ["1", "2", "3", "4"]:
            print("Opción no válida. Intente nuevamente.")
            continue
        
        try:
            num1 = float(input("Ingrese primer número: "))
            num2 = float(input("Ingrese segundo número: "))
            
            if opcion == "1":
                resultado = suma(num1, num2)
                operacion = "+"
            elif opcion == "2":
                resultado = resta(num1, num2)
                operacion = "-"
            elif opcion == "3":
                resultado = multiplicacion(num1, num2)
                operacion = "*"
            elif opcion == "4":
                resultado = division(num1, num2)
                operacion = "/"
            
            print(f"\nResultado: {num1} {operacion} {num2} = {resultado}")
            
        except ValueError as e:
            print(f"Error: {e}")
        except Exception as e:
            print(f"Error inesperado: {e}")

if __name__ == "__main__":
    main()
