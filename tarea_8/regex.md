 Tarea 8

> Jesús Iván Rivera Ramírez
> 

Una expresión regular(**regex**) es una secuencia de caracteres que define un patrón de búsqueda, son una herramienta poderosa al trabajar con cadenas de texto. Las regex no son una herramienta propia de Python, sin embargo esta herramienta esta implementada en la la biblioteca *re* de Python.

Antes de introducir el funcionamiento de la biblioteca *re,* repasaremos un poco las regex

## Meta caracteres

Los metacaracteres son los bloques de construcción para nuestras expresiones regulares. Los caracteres en una regex se dividen en dos tipos un metecaracter con un significado especial o un carácter regular con un significado literal. Los metacaracteres usados en Python son

```python
`. ^ $ * + ? { } [ ] \ | ( )
```

Veamos con más detalle cada uno de ellos

### Backslash \

Al igual que en Python, el backslash \ nos sirve para escapar los metacaracteres, es decir para poder usarlos de forma literal en las regex, por ejemplo si queremos buscar un `\` o `{` los precedemos por un backslash para anular su significado especial, es decir, `\\` o `\{`.

Otros usos del backslash es indicar secuencias especiales de caracteres, para esto usamos varios caracteres después del backslash, algunos ejemplos de estas secuencias son,

- `\d` para buscar dígitos.
- `\D` para buscar caracteres que no sean dígitos.
- `\s` para buscar espacios, saltos de linea, tabuladores.
- `\S` para buscar caracteres que no sean espacios, saltos de linea, tabuladores.
- `\w` para buscar caracteres alfanumericos.
- `\W` para buscar caracteres no alfanumericos.
- `\uXXXX` para buscar caracteres con codigo unicode XXXX.


### Cuantificadores

Podemos agrupar varios metacaracteres dentro del de grupo cuantificadores, es decir, estos caracteres especifican cuantos veces estamos buscando un carácter , secuencia de caracteres, etc. Los cuantificadores son los siguientes 


| Cuantificador  | Descripción   |
|---|---|
|  * |  coincide con el carácter  0 o más veces. |
|  + |  coincide con el carácter  1 o más veces. |
|  ? |  coincide con el carácter  0 o 1 vez. |
| **{** n **}**  |  coincide exactamente *n* veces. |
| **{** n **, }**  |  coincide al menos *n* veces. |
| **{** n **,** m **}**  | coincide de *n* a *m* veces.  |

### De posición

Estos metacaracteres nos ayudan a identificar posiciones dentro de la cadena donde debe suceder la ocurrencia. Los metacaracteres que nos ayudan a esto son,

|carácter  | Descripción |
|---|---|
| ^| La coincidencia debe ser al inicio de la linea | 
| $|  La coincidencia debe ser al inicio de la linea | 

### Conjuntos de Caracteres

Los metacaracteres `[` y `]`, nos permiten definir conjuntos de caracteres para buscar coincidencias, ya sea listandolos indivudualmente o usango rangos, los cuales se indican como dos caracteres separados por un `-`. Por ejemplo `[abc]` coincide con cualquiera de los caracteres `a`, `b`, o `c`. Podemos obtener el mismo resultado usando rangos `[a-c]`.

El metacaracter `^` al usarse al principio de un conjunto funciona como el complemento, es decir la expresioón `[^abc]` coincidira con cualquiera carácter  distinto de `a`, `b`, o `c`. Al usarse en cualquier otra parte funciona como un carácter normal, es decir, `[a^]` coindice con `a` o con `^`.

### Grupos de Caracteres
Los metacaracteres `(` y `)`, nos permiten agrupar cualquier expresión regular, y se puden utilizar posteriormente usando la referencia `\number` donde `number` hace referencia al orden en el que se crearon las referencias.

Tambien se pueden nombrar los grupos para referenciarlos mas tarde e incluso poder obtenerlos desde Python, para ello se utiliza `?P<name>` al principio del grupo, es decir, `(?P<name>...)` y utilizamos `(?P=name)` para referencias al grupo.

### Otros

El metacaracter `.` se utiliza para buscar cualquier caracter que no sea un nueva linea(`\n`)

El metacaracter `|` se utiliza como un *OR* logico entre expreciones regulares


## Expreciones regulares en python

Para utilizar expresiones regualres utilizamos la biblioteca **re**. Esta nos permite realizar busquedas y obtener substrings con condiciones más complejas, algunas de las funciones más utilizadas son las siguientes

### match

La función re.match() buscará la regex y devolverá la primera ocurrencia. El método Match de Python busca una coincidencia sólo al principio de la cadena. Así, si se encuentra una coincidencia en la primera línea, devuelve el objet, pero si se encuentra una coincidencia en alguna otra línea, ldevuelve None.

### search

La función re.search() busca el patrón dado por la expresión regular y devolverá la primera ocurrencia. A diferencia de Python re.match(), probará todas las líneas de la cadena. La función re.search() de Python devuelve None si no se encuentra la regex.

## Referencias

[Documentación de Python](https://docs.python.org/3/library/re.html)
[Regular Expresions Info](https://www.regular-expressions.info/)
[RegExr](https://regexr.com/)

