# Tarea 10
> Jesus Ivan Rivera Ramirez

## Ejecución de Pylint

La salida de ejecutar pylint en la tarea 9 es### 
```shell
************* Module main
main.py:10:0: W0105: String statement has no effect (pointless-string-statement)
main.py:31:0: W0105: String statement has no effect (pointless-string-statement)
main.py:83:0: W0105: String statement has no effect (pointless-string-statement)
main.py:120:0: W0105: String statement has no effect (pointless-string-statement)
main.py:136:0: W0105: String statement has no effect (pointless-string-statement)
main.py:161:0: W0105: String statement has no effect (pointless-string-statement)
main.py:186:0: W0105: String statement has no effect (pointless-string-statement)
main.py:212:0: W0105: String statement has no effect (pointless-string-statement)
main.py:220:34: W0613: Unused argument 'data' (unused-argument)
main.py:258:0: W0105: String statement has no effect (pointless-string-statement)
main.py:299:0: W0105: String statement has no effect (pointless-string-statement)

------------------------------------------------------------------
Your code has been rated at 8.10/10 (previous run: 8.10/10###  +0.00)
```

Al eliminar las lineas de comentarios que separan los ejercicios se puede obtener una calificación mayor###  mostrada a continuación### 

```shell

************* Module main
main.py:178:34: W0613: Unused argument 'data' (unused-argument)

------------------------------------------------------------------
Your code has been rated at 9.79/10 (previous run: 9.79/10###  +0.00)
```

## Métodos de file

A continuación se describen los métodos para operar con archivos

### close
Cierra el archivo abierto.

### closed
Devuelve `True` si un archivo ha sido cerrado, `False` en otro caso.

###  encoding
Devuelve el *encoding* utilizado para abrir y escribir sobre el archivo.

###  fileno
Devuelve el entero usado como descriptor del archivo internamente.

###  flush
Vacia y escribe los búfers sobre el archivo. En caso de que se use el modo lectura este metodo no hace nada.

###  isatty
Devuelve `True` si el archivo es interactivo, es decir, esta conectado a una terminal o a un dispositivo tty.

###  mode
Devuelve el modo con el que fue abierto el archivo.

###  name
Devuelve el nombre del archivo abierto.

###  newlines
Devuelve el tipo de `newlines` que se han econtrado durante la lectura del archivo.

###  next
Cuando el archivo se usa como un iterador, devuelve el siguiente elemento, por ejemplo, la siguiente linea.

### read
Permite leer un archivo, tambien se pueden especificar un cierto numero de bytes que se quieren leer del archivo.


###  readline
Lee una linea del archivo y la devuelve como `str`.

###  readlines
Lee todos las lineas del archivo y devuelve un iterador con todas las lineas.

###  seek
Mueve la posición(interna) desde donde se comienza a leer el archivo.

###  softspace
Devuelve un booleano que indica si es necesario imprimir un carácter de espacio antes de otro cuando se utiliza la sentencia print.

###  tell
Devuelve la posición de la posición(interna) desde donde se esta leyendo el archivo.

###  truncate
Cambia el tamaño del archivo al numero de bytes dado.
###  write
Escribe un objeto, por ejemplo, una cadena de texto sobre nuestro archivo.

###  writelines
Escribe una lista de objetos, por ejemplo, una lista de cadenas de texto sobre nuestro archivo.

###  xreadlines.
Este metodo esta obsoleto desde python 2.3