# Montecarlo: intersección elipse - hipérbola

Programa en Python que estima, con el método de Montecarlo, el área de la parte de una elipse que también cumple la condición de una hipérbola.
Evaluación Final de *Análisis de Algoritmos y Estrategias de Programación*.

## Fórmulas

- Elipse: `x² / a² + y² / b² <= 1`
- Hipérbola: `x² / c² - y² / d² >= 1`
- Área de la elipse: `π · a · b`

## Cómo funciona

1. Se piden por consola `a`, `b` (elipse), `c`, `d` (hipérbola) y la cantidad de puntos.
2. Se generan puntos `(x, y)` con decimales aleatorios: `x` en `[-a, a]` e `y` en `[-b, b]`.
3. Se cuentan los puntos que caen **dentro de la elipse**.
4. De esos, se cuentan los que también cumplen la condición de la **hipérbola** (la intersección).
5. El área aproximada de la intersección es:

```
área_intersección ≈ (puntos_intersección / puntos_elipse) · π · a · b
```

## Requisitos

- Python 3.8 o superior. No requiere librerías externas (solo `random` y `math`).

## Ejecución

```bash
python montecarlo_elipse_hiperbola.py
```

El programa valida que cada valor sea un número mayor que cero y, al final, muestra:

- cuántos puntos cayeron dentro de la elipse,
- cuántos cayeron en la intersección con la hipérbola,
- el área de la elipse y el área aproximada de la intersección.

## Ejemplo de uso

```
Ingrese el valor de a (elipse): 10
Ingrese el valor de b (elipse): 5
Ingrese el valor de c (hiperbola): 4
Ingrese el valor de d (hiperbola): 4
Ingrese la cantidad de puntos: 1000



```
.
├── montecarlo_elipse_hiperbola.py   # programa principal
└── README.md
```
