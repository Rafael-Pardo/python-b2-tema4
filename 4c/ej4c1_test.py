"""
Enunciado:
Desarrolla un test para la función implementada calculate_rectangle_area, la función recibe dos parámetros ancho y
alto, y devuelve el área del rectángulo, calculada como ancho * alto. utilizando el enfoque de Desarrollo Guiado
por Pruebas (TDD).

Instrucciones de Implementación:
- Realizar los test considerando los distintos casos de prueba descritos a continuación.
- Ejecutar las pruebas y verificar que la implementación sea correcta.

Casos de Prueba:
    Prueba con valores enteros positivos para ancho y alto.
    Prueba con ancho/alto negativo.
    Prueba con ancho/alto no numérico.

Ejemplo:
    area = calcular_area_rectangulo(5, a)
    print("Área del rectángulo:", area)

"""

import pytest
from ej4c1 import calculate_rectangle_area

def test_calculate_rectangle_area(): 
    # Prueba con valores enteros positivos para ancho y alto.   
    # Write here your code
    width = 3
    height = 7
    expected_area = 21
    # Change the following line
    assert calculate_rectangle_area(width, height) == expected_area
    print(" Area del rectangulo= ", calculate_rectangle_area(width, height))
    
def test_value_error_calculate_rectangle_area():
    # Prueba con ancho/alto negativo.
    # Write here your code
    width = -2
    height = 8
    # Change the following line
    with pytest.raises(ValueError):
        calculate_rectangle_area(width, height)
    print("se produjo un error: Uno de los datos es negativo")
    

def test_type_error_calculate_rectangle_area():
    # Prueba con ancho/alto no numérico.
    # Write here your code
    width = 'a'
    height = 5
    # Change the following line
    with pytest.raises(TypeError):
        calculate_rectangle_area(width, height)
    print("se produjo un error: Uno de los datos no es un numero")
