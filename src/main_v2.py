#!/usr/bin/env python3
"""
Programa principal de la calculadora - Versión extendida
"""

from calculadora import suma, resta, multiplicacion, division
from operaciones_avanzadas import potencia, raiz_cuadrada, factorial

def mostrar_menu():
    """Muestra el menú de opciones extendido"""
    print("\n=== CALCULADORA PYTHON AVANZADA ===")
    print("Operaciones básicas:")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")
    print("\nOperaciones avanzadas:")
    print("5. Potencia")
    print("6. Raíz cuadrada")
    print("7. Factorial")
    print("8. Salir")

def main():
    """Función principal del programa extendido"""
    print("Bienvenido a la Calculadora Python Avanzada")
    
    while True:
        mostrar_menu()
        opcion = input("\nSeleccione una opción (1-8): ")
        
        if opcion == "8":
            print("¡Hasta luego!")
            break
        
        try:
            if opcion in ["1", "2", "3", "4", "5"]:
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
                elif opcion == "5":
                    resultado = potencia(num1, num2)
                    operacion = "^"
                
                print(f"\nResultado: {num1} {operacion} {num2} = {resultado}")
            
            elif opcion == "6":
                num = float(input("Ingrese número: "))
                resultado = raiz_cuadrada(num)
                print(f"\nRaíz cuadrada de {num} = {resultado}")
            
            elif opcion == "7":
                num = int(input("Ingrese número entero: "))
                resultado = factorial(num)
                print(f"\nFactorial de {num} = {resultado}")
            
            else:
                print("Opción no válida. Intente nuevamente.")
                
        except ValueError as e:
            print(f"Error: {e}")
        except Exception as e:
            print(f"Error inesperado: {e}")

if __name__ == "__main__":
    main()
