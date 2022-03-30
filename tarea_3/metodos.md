# Tarea 3
> Jesus Ivan Rivera Ramirez 

Descripción de los metodos mostrados al ejecutar lo siguiente en python
```python
>>> aux = [1, 2, 3]
>>> help(type(aux))
```

## \_\_add\_\_

```python
__add__
    Return self+value.
```
Permite concatenar una lista al final de otra lista, y devuelve la concatenación 
de las listas, su funcionamiento es igual a el operador `+`.

**Ejemplo**
```python
>>> aux = [1,2,3]
>>> aux2 = aux.add([4]) # aux2 = aux+[4] 
>>> aux2 
[1, 2, 3, 4]
```

## \_\_contains\_\_

```python
__contains__(self, key, /)
    Return key in self.
```

Indica si un elemento es *key* esta contenido en una lista,
su funcionamiento es igual a `in`.

**Ejemplo**
```python
>>> aux = [1, 2, 3]
>>> aux.__contains__(2) # 2 in aux
True
```

## \_\_delitem\_\_

```python
__delitem__(self, key, /)
    Delete self[key].
```
Elimina el elemento de la lista con indice *key*, funciona similiar a `del aux[key]`.

**Ejemplo**
```python
>>> aux = [1, 2, 3]
>>> aux.__delitem__(2) # del aux[2]
>>> aux 
[1, 2]
```

## \_\_eq\_\_

```python
__eq__(self, value, /)
    Return self==value.
```
Indica si un dos listas son iguales, es decir, tienen los mismos elementos,
en cada indice. Funciona similar a `lista1 == lista2`.

**Ejemplo**
```python
>>> aux = [1, 2, [3]]
>>> aux2 = [1, 2, 3]
>>> aux.__eq__(aux2) # aux == aux2
False
```

## \_\_ge\_\_

```python
__ge__(self, value, /)
    Return self>=value.
```
Nos permite comparar cuando una lista es **mayor** o igual a otra, la comparación se hace usando el orden lexicográfico 
su funcionamiento es similar a `lista1 >= lista2`.

**Ejemplo**
```python
>>> aux = [1, 2, 3]
>>> aux2 = [1, 1, 2]
>>> aux.__ge__(aux2) # aux >= aux2
True
>>> aux2.__ge__(aux) # aux2 >= aux
False
 
```

## \_\_getattribute\_\_

```python
__getattribute__(self, name, /)
    Return getattr(self, name).
```

Nos permite obtener el valor de un atributo con nombre *name*,
funciona como 'lista.name'.

**Ejemplo**
```python
>>> aux = [1, 2, 3]
>>> aux.__getattribute__('append') # aux.append
<built-in method append of list object at 0x7f25d4d14240>
```

## \_\_getitem\_\_
```python
__getitem__(...)
    x.__getitem__(y) <==> x[y]
```
Permite obtener el elemento con indice *y*, funciona igual que `lista[y]`.

**Ejemplo**
```python
>>> aux = [1, 2, 3, 4]
>>> aux.__getitem__(2) # aux[2]
3
```

## \_\_gt\_\_
```python
__gt__(self, value, /)
    Return self>value.
```
Nos permite comparar cuando una lista es **mayor** a otra usando el orden
lexicográfico, funciona igual que `lista1 > lista2`.

**Ejemplo**
```python
>>> aux = [1, 2, 3]                                                               
>>> aux2 = [1, 1, 2]
>>> aux.__gt__(aux2) # aux > aux2
True
>>> aux2.__gt__(aux) # aux2 > aux
False
>>> aux.__gt__(aux) # aux > aux
False

```

## \_\_iadd\_\_
```python
__iadd__(self, value, /)
    Implement self+=value.
```
Implementa la funcionalidad `+=`, es decir concatena la lista *value* y asigna el
valor a nuestra lista.

**Ejemplo**
```python
>>> aux = [1, 2, 3]
>>> aux.__iadd__([4, 5, 6]) # aux += [4, 5, 6] o aux = aux + [4, 5, 6]
>>> aux
[1, 2, 3, 4, 5, 6]
```

## \_\_imul\_\_
```python
__imul__(self, value, /)
    Implement self*=value.
```

Implementa la funcionalidad `*=` , es decir, repite *value*-veces la lista y la
asigna a nuestra lista.

**Ejemplo**
```python
>>> aux = [1, 2, 3]
>>> aux.__imul__(2) # aux *= 2
>>> aux
[1, 2, 3, 1, 2, 3]
```

## \_\_init\_\_
```python
__init__(self, /, *args, **kwargs)
    Initialize self.  See help(type(self)) for accurate signature.
```
Incializa nuestra lista, si este metodo se llama sin parametros, nuestra lista
se vuelve vacia, en caso contrario la inicializa con el valor del parametro.

**Ejemplo**
```python
>>> aux = [1, 2, 3]
>>> aux.__init__()
>>> aux
[]
>>> aux.__init__([4, 5, 6])
>>> aux
[4, 5, 6]
```

## \_\_iter\_\_
```python
__iter__(self, /)
    Implement iter(self).
```
Nos devuelve un **iteredor** nuestra lista, para ser usado por ejemplo en ciclos.
Funciona igual que `iter(lista)`.

**Ejemplo**
```python
>>> aux = [1, 2, 3, 4, 5, 6]
>>> mi_iter = aux.__iter__() # mi_iter = iter(aux)
>>> for elem in mi_iter:
...     print(x)
...
1
2
3
4
5
6

```

## \_\_le\_\_
```python
__le__(self, value, /)
    Return self<=value.
```
Nos permite comparar cuando una lista es **menor** o igual a otra usando el orden
lexicográfico, funciona igual que `lista1 <= lista2`.

**Ejemplo**
```python
>>> aux = [1, 2, 3]                                                               
>>> aux2 = [1, 1, 2]
>>> aux.__le__(aux2) # aux <= aux2
False
>>> aux2.__le__(aux) # aux2 <= aux
True
>>> aux.__le__(aux) # aux <= aux
True
```

## \_\_len\_\_
```python
__len__(self, /)
    Return len(self).
```
Devuelve la cantidad de elementos de nuestra lista.

**Ejemplo**
```python
>>> aux = [1, 2, 3]
>>> aux.__len__()
3
>>> aux = [1, 2, 3, 4, 5, 6]
>>> aux.__len__()
6
```

## \_\_lt\_\_
```python
__lt__(self, value, /)
    Return self<value.
```

Nos permite comparar cuando una lista es **menor**  otra usando el orden
lexicográfico, funciona igual que `lista1 < lista2`.

**Ejemplo**
```python
>>> aux = [1, 2, 3]                                                               
>>> aux2 = [1, 1, 2]
>>> aux.__lt__(aux2) # aux < aux2
False
>>> aux2.__lt__(aux) # aux2 < aux
True
>>> aux.__lt__(aux) # aux < aux
False
```

## \_\_mul\_\_
```python
__mul__(self, value, /)
    Return self*value.
```
Implementa la multiplicación `*` de una lista por un numero, es decir,
repite la lista *value* veces. A diferencia de `__imul__` no modifica la lista,
en su lugar devuelve la repetición de esta.

**Ejemplo**
```python
>>> aux = [1, 2]
>>> aux.__mul__(5) # aux * 5
[1, 2, 1, 2, 1, 2, 1, 2, 1, 2]
```

## \_\_ne\_\_
```python
__ne__(self, value, /)
    Return self!=value.
```
Indica cuando dos listas son distintas, es decir, tienen al menos un elemento,
distinto en el mismo indice. Funciona igual que `!=`.

**Ejemplo**
```python
>>> aux = [1, 2, 3]
>>> aux2 = [1, 2, 4]
>>> aux.__ne__(aux2) # aux != aux2 
True
>>> aux.__ne__(aux)
False
```

## \_\_repr\_\_
```python
__repr__(self, /)
    Return repr(self).
```
Representa a nuestra lista como un cadena. funciona igual que `repr()`.

**Ejemplo**
```python
>>> aux = [1, 2, 3]
>>> aux.__repr__() # repr(aux)
'[1, 2, 3]'
```

## \_\_reversed\_\_
```python
__reversed__(self, /)
    Return a reverse iterator over the list.
```
Devuelve un **iterador** en sentido opuesto de nuestra lista.
Funciona igual que `reversed`.

**Ejemplo**
```python
>>> aux = [1, 2, 3, 4, 5, 6]
>>> mi_iter = aux.__reversed__() # mi_iter = iter(aux)
>>> for elem in mi_iter:
...     print(x)
...
6
5
4
3
2
1
```

## \_\_rmul\_\_
```python
__rmul__(self, value, /)
    Return value*self.
```
Implementa la multiplicación derecha, esto sucede, cuando el el primer multiplicando
no puede multiplicarse por una lista, en esta caso se invoca `__rmul__` en vez de `__mul__`.

**Ejemplo**
```python
>>> aux = [1, 2, 3]
>>> aux.__rmul__(3) # 3 * aux 
[1, 2 ,3, 1, 2, 3, 1, 2, 3]
```

## \_\_setitem\_\_
```python
__setitem__(self, key, value, /)
    Set self[key] to value.
```
Nos permite modificar el valor del elmento con indice *key* y asignarle el valor *value*.
Es igual que `lista[key] = value`

**Ejemplo**
```python
>>> aux = [1, 2, 3]
>>> aux.__setitem__(2,10) # aux[2] = 10
>>> aux
[1, 2, 10]
```

## \_\_sizeof\_\_

```python
__sizeof__(self, /)
    Return the size of the list in memory, in bytes.
```
Devuele el numero de bytes que nuestra lista ocupa en memoria.

**Ejemplo**
```python
>>> aux = [1, 2, 3]
>>> aux.__sizeof__();
104
```

## append

```python
append(self, object, /)
    Append object to the end of the list.
```
Agregar el *object* al final de la lista.

**Ejemplo**
```python
>>> aux = [1, 2, 3]
>>> aux.append(2)
[1, 2, 3, 2]
>>> aux.append([1, 2])
>>> aux
[1, 2, 3, 2, [1, 2]]
```

## clear

```python
clear(self, /)
    Remove all items from list.
```
Elimina todos los elementos de la lista, dejando una lista vacia.

**Ejemplo**
```python
>>> aux = [1, 2, 3]
>>> aux.clear()
>>> aux
[]

```

## copy

```python
copy(self, /)
    Return a shallow copy of the list.
```
Crea una copia *shallow* de nuestra lista, esto es, crea una nueva lista e inserta
**referencias** a los elementos de la lista original.

**Ejemplo**
```python
>>> aux = [1, 2 ,3]
>>> copia = aux.copy()
>>> copia
[1, 2, 3]
```

## count

```python
count(self, value, /)
    Return number of occurrences of value.
```
Cuenta el numero de ocurrencias de *value* en nuestra lista

**Ejemplo**
```python
>>> aux = [1, 2, 3, 1, 2, 1, 1]
>>> aux.count(1)
4

```

## extend

```python
extend(self, iterable, /)
    Extend list by appending elements from the iterable.
```
Concatena un *iterable* al final de la lista.

**Ejemplo**
```python
>>> aux=[1, 2, 3]
>>> aux.extend([1,2,[3,4]])
>>> aux
[1, 2, 3, 1, 2, [3, 4]]
```

## index

```python
index(self, value, start=0, stop=9223372036854775807, /)
    Return first index of value.
    
    Raises ValueError if the value is not present.
```
Indica el el indice de la primera ocurrencia de *value*, en la lista entre
los indices *start* y *end*

**Ejemplo**
```python
>>> aux = [1, 2, 3, 2, 5]
>>> aux.index(2)
1
>>> aux.index(2,3)
3
```

## insert

```python
insert(self, index, object, /)
    Insert object before index.
```
Inserta un objeto en la lista antes de la posición *index*.

**Ejemplo**
```python
>>> aux = [1, 2, 3]
>>> aux.insert(1,4)
>>> aux
[1, 4, 2, 3]
>>> aux.insert(3,5)
>>> aux
[1, 4, 2, 5, 3]

```

## pop

```python
pop(self, index=-1, /)
    Remove and return item at index (default last).
    
    Raises IndexError if list is empty or index is out of range.
```
Elimina y devuelve el elemento en el indice *index*, en caso de no especificar un indice
elimina y devuelve el ultimo elemento.

**Ejemplo**
```python
>>> aux = [1 , 2, 3, [4,5]]
>>> aux.pop()
[4, 5]
>>> aux
[1, 2, 3]
>>> aux.pop(0)
1
>>> aux
[2, 3]
```

## remove

```python
remove(self, value, /)
    Remove first occurrence of value.
    
    Raises ValueError if the value is not present.
```
Elimina la primera ocurrencia de *value* en la lista

**Ejemplo**
```python
>>> aux = [1, 2, 1, 2, 1]
>>> aux.remove(2)
>>> aux
[1, 1, 2, 1]
```

## reverse

```python
reverse(self, /)
    Reverse *IN PLACE*.
```
Invierte el orden de la lista.

**Ejemplo**
```python
>>> aux = [1, 2, 3]
>>> axu.reverse()
>>> aux
[3, 2, 1]
```

## sort

```python
sort(self, /, *, key=None, reverse=False)
    Sort the list in ascending order and return None.
    
    The sort is in-place (i.e. the list itself is modified) and stable (i.e. the
    order of two equal elements is maintained).
    
    If a key function is given, apply it once to each list item and sort them,
    ascending or descending, according to their function values.
    
    The reverse flag can be set to sort in descending order.
```

Ordena la lista, se puede especifcar si el orden es acentende o descendente usando
el parametro *reverse*, asi como ordener con algún criterio *key*.

**Ejemplo**
```python
>>> aux = [5, 7, 2, 3]
>>> aux.sort()
>>> aux
[2, 3, 5, 7]
>>> aux.sort(reverse=True)
>>> aux
[7, 5, 3, 2]
```


```python
>>> aux = ['ABC', 'ACDB', 'XZ' ] 
>>> aux.sort()
>>> aux
['ABC', 'ACDB', 'XZ']    
>>> aux.sort(key = len) # Ordenamos usando la longitud de las cadenas
>>> aux
['XZ', 'ABC', 'ACDB']
```
