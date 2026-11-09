import random
import math


def calcular_interseccion(a, b, c, d, cantidad):
    """
    Estima el area de la parte de la elipse que tambien pertenece
    a la region definida por la hiperbola, usando Montecarlo.
    """
    puntos_elipse = 0
    puntos_interseccion = 0

    for _ in range(cantidad):
        # Generar un punto uniforme dentro del rectangulo [-a,a] x [-b,b]
        x = random.uniform(-a, a)
        y = random.uniform(-b, b)

        # Comprobar si el punto pertenece a la elipse
        dentro_elipse = (x**2 / a**2) + (y**2 / b**2) <= 1

        if dentro_elipse:
            puntos_elipse += 1

            # Comprobar si tambien pertenece a la region de la hiperbola
            dentro_hiperbola = (x**2 / c**2) - (y**2 / d**2) >= 1

            if dentro_hiperbola:
                puntos_interseccion += 1

    area_elipse = math.pi * a * b

    if puntos_elipse > 0:
        area_interseccion = area_elipse * (puntos_interseccion / puntos_elipse)
    else:
        area_interseccion = 0.0

    return puntos_elipse, puntos_interseccion, area_elipse, area_interseccion


def leer_numero_positivo(mensaje, tipo=float):
    while True:
        try:
            valor = tipo(input(mensaje))
            if valor > 0:
                return valor
            print("Error: ingrese un valor mayor que cero.")
        except ValueError:
            print("Error: ingrese un numero valido.")


def main():
    print("=" * 58)
    print("  METODO DE MONTECARLO: INTERSECCION ELIPSE-HIPERBOLA")
    print("=" * 58)

    a = leer_numero_positivo("Ingrese el valor de a (elipse): ")
    b = leer_numero_positivo("Ingrese el valor de b (elipse): ")
    c = leer_numero_positivo("Ingrese el valor de c (hiperbola): ")
    d = leer_numero_positivo("Ingrese el valor de d (hiperbola): ")
    cantidad = leer_numero_positivo("Ingrese la cantidad de puntos: ", int)

    puntos_elipse, puntos_interseccion, area_elipse, area_interseccion = (
        calcular_interseccion(a, b, c, d, cantidad)
    )

    print("\n--------------- RESULTADOS ---------------")
    print(f"Puntos aleatorios dentro de la elipse: {puntos_elipse}")
    print(f"Puntos en la interseccion: {puntos_interseccion}")
    print(f"Area de la elipse: {area_elipse:.6f}")
    print(f"Area aproximada de la interseccion: {area_interseccion:.6f}")
    print("------------------------------------------")


if __name__ == "__main__":
    main()
