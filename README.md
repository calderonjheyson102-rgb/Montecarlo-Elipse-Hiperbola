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

--------------- RESULTADOS ---------------
Puntos aleatorios dentro de la elipse: 788
Puntos en la interseccion: 335
Area de la elipse: 157.079633
Area aproximada de la interseccion: 66.778778
------------------------------------------
```

## Resultados de las pruebas

| Prueba | a | b | c | d | Puntos | En la elipse | En la intersección | Área aprox. |
|---|---|---|---|---|---|---|---|---|
| 1 | 10 | 5 | 4 | 4 | 1,000 | 788 | 335 | 66.78 |
| 2 | 12 | 7 | 5 | 4 | 10,000 | 7,873 | 2,862 | 95.93 |
| 3 | 10 | 5 | 4 | 4 | 100,000 | 78,595 | 33,518 | 66.99 |

Como valor de referencia (calculado aparte con integración numérica, no forma parte del programa):

- Prueba 1: área aproximada **66.78** vs. referencia **67.34** (diferencia 0.56, 0.8 %).
- Prueba 2: área aproximada **95.93** vs. referencia **95.81** (diferencia 0.12, 0.1 %).
- Prueba 3: área aproximada **66.99** vs. referencia **67.34** (diferencia 0.35, 0.5 %).

## Comentario de los resultados

- En las tres pruebas cerca del 78.5 % de los puntos cae dentro de la elipse. Es lo esperado, porque el área de la elipse (`π·a·b`) es `π/4 ≈ 78.5 %` del área del rectángulo `4·a·b` donde se generan los puntos.
- Con pocos puntos (1000) la estimación es menos estable; con muchos (100 000) es más precisa, ya que el error del método disminuye aproximadamente con la raíz de la cantidad de puntos.
- Al ser aleatorio, cada ejecución da valores distintos. En una sola ejecución el error puede salir mayor o menor de lo típico, por lo que la mejora se aprecia mejor repitiendo las pruebas.

## Estructura

```
.
├── montecarlo_elipse_hiperbola.py   # programa principal
└── README.md
```
