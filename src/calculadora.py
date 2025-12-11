"""
Módulo de calculadora básica
"""

def suma(a, b):
    """Retorna la suma de dos números"""
    return a + b

def resta(a, b):
    """Retorna la resta de dos números"""
    return a - b

def multiplicacion(a, b):
    """Retorna la multiplicación de dos números"""
    return a * b

def division(a, b):
    """Retorna la división de dos números"""
    if b == 0:
        raise ValueError("No se puede dividir por cero")
    return a / b

if __name__ == "__main__":
    # Ejemplos de uso
    print("Calculadora Básica")
    print(f"5 + 3 = {suma(5, 3)}")
    print(f"10 - 4 = {resta(10, 4)}")
