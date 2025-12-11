"""
Módulo de operaciones matemáticas avanzadas
"""

import math

def potencia(base, exponente):
    """Calcula la potencia de un número"""
    return base ** exponente

def raiz_cuadrada(numero):
    """Calcula la raíz cuadrada de un número"""
    if numero < 0:
        raise ValueError("No se puede calcular raíz de número negativo")
    return math.sqrt(numero)

def factorial(n):
    """Calcula el factorial de un número"""
    if n < 0:
        raise ValueError("Factorial no definido para números negativos")
    if n == 0:
        return 1
    return n * factorial(n - 1)
