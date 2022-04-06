# Funciones Map, Filter y Reduce
> Jesús Iván Rivera Ramiréz

## Map
La función `map()` nos permite transformar cada elemento de un *iterable*(lista, tuplas, conjuntos, diccionarios, etc) y obtener un nuevo
*iterable*. La función `map` suele ser más eficiente para transformar una lista en ves de usar un ciclo `for`.
La sintaxis de la función map es la siguiente,
    
```python
    map(function, iterable, [iterable 2, iterable 3, ...])
``` 

El primer argumento de la función map, es otra función la cual se aplicara a cada uno de los elementos de nuestro iterable, las funciones que se usan principalmente
pueden dividirse en tres grupos

    - Funciones Lambda.
    - Funciones definidas por el desarrollador.
    - Funciones propias de python

Vemos cada una de estas con mas detalle,

### Funciones Lambda

Las funciones lambda son funciones anonimas, es decir, que no tienen nombre, solo definición y usualmente son de una solo linea, la sintaxis
de estas funciones es la siguiente

```python
    lambda argumento(s) : expresión
```

una función de este tipo evalua la expresión usando los argumentos, por ejemplo podemos elevar un numero al cuadrado usando la siguiente función

```python
    lambda x : x**2
```

o sumar dos numeros

```python
    lambda x,y : x   + y
```

al combinar estas funciones con la función `map()`, por ejemplo para sumar `15` a cada elemento de una lista,
```python
>>> lista = [1, 2, 3, 4, 5]
>>> nueva_lista =list(map(lambda x : x + 15, lista))
>>> nueva_lista
[16, 17, 18, 19, 20]
```

podemos usar mas de un iterable por ejemplo repetir cada palabra en una lista un numero distinto de veces,
```python
>>> palabras = ["Perro", "Gato", "Cerdo"]
>>> repeticion = [3, 4, 2]
>>> palabras_repetidas = list(map(lambda x,y: x*y, palabras, repeticion))
>>> palabras_repetidas  
['PerroPerroPerro', 'GatoGatoGatoGato', 'CerdoCerdo']
```

### Funciones definidas por el desarrollador

Podemos usar funciones más complejas que las funciones lambda, por ejemplo
```python
def mi_funcion(x,y):
    if x>y:
        return 'Más grande.'
    elif x<y:
        return 'Más chico.'
    else:
        return 'iguales'

lista1 = [1, 10, 4, 6]
lista2 = [1, 9, 8, 7]
resultado = list(map(mi_funcion,lista1,lista2))
print(resultado)
#['iguales', 'Más grande.', 'Más chico.', 'Más chico.']
```

### Funciones Propias de Python
También es posible usar las funciones propias de python por ejemplo la función `pow`, para elevar cada elemento de una lista a
una potencia distinta
```python
>>> base = [2, 4, 6, 8, 10, 12, 14, 16]
>>> exponente = [1, 2, 3, 4, 5]
>>> potencias = list(map(pow, base, exponente))
>>> potencias
[2, 16, 216, 4096, 100000]
```

## Filter

Al igual que `map()`, `filter()` es una función que se aplica a *iterables*,
a diferencia de `map()` que transforma los elementos de un *iterable*m esta los escoge
usando una función. La sintaxis es la siguiente

```python
filter(function or None, iterable)
```

De forma similar podemos usar funciones lambda o funciones definidas por el usuario,
a continuación se presentan algunos ejemplos, además del caso especial `None`

### Funciones lambda
```python
>>> nums = [5, 10, 23, 64, 42, 53, 93, 2, 0, -14, 6, -22, -13]
>>> impar = list(filter(lambda p : p%2 != 0, nums))
>>> par = list(filter(lambda p: p%2 == 0, nums))
>>> par
[10, 64, 42, 2, 0, -14, 6, -22]
>>> impar
[5, 23, 53, 93, -13]
```

### Funciones propias
```python
def mi_funcion(letter):
  vocales = ['a', 'e', 'i', 'o', 'u']
    if letter in list_of_vowels:
        return True
    else:
        return False
letras = ['u', 'a', 'q', 'c', 'i', 'd', 'z', 'p', 'e']
filtradas = list(filter(mi_funcion, letras))
print(filtradas)
#['u', 'a', 'i', 'e']
```

### None
Al utilizar `None` como parametro, en vez de una función, `filter()` eliminara
cada elemento que se condisere falso, por ejemplo, `0`, `""`, `False`, `{}` o `[]`

```python
>>> lista = [5, -23, "", True, False, 0, 0.0, {}, []]
>>> resultado = list(filter(None, lista))
>>> resultado
[5, 23, True]
```

## Reduce

Aplica una función de dos parametros de forma acumulada a los elementos de un *iterable* de izquierda a derecha hasta obtener un solo valor, por ejemplo para
obtener la suma de los elementos de una lista

```python
>>> from functools import reduce
>>> lista = [1, 2, 4, 9]
>>> res = reduce(lambda x,y: x+y, lista)
>>> res
16
```

al igual que las funciones descritas anteriormente se pueden utilzar funciones de tipo
lambda y definidas por el usuario, por ejemplo, para obtener el maximo de una lista,

```python
>>> from functools import reduce

>>> # Minimum
>>> def my_min_func(a, b):
...     return a if a < b else b
>>> lista = [10, 21, 3, 12, 1]
>>> reduce(my_min_func, numbers)
1
```
