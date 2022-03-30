# Tarea 2
Al llegar a la línea 98

```python
data = data_json.json()
```

El programa convierte un objeto de tipo JSON el cual es un diccionario con dos elementos, los cuales tienen por llaves “meta“ y ”objects”, donde el valor de “meta” es un diccionario y “objects” una lista de diccionarios

La línea 99

```python
data = [[datetime.datetime.strptime(d['date'],"%Y-%m-%d"),
				d['frequency'],
				float(d['happiness'])]
 for d in data['objects']] 
```

Hace lo siguiente, primero vamos a crear una lista por comprensión para esto, iteramos sobre la lista `data[“objects”]` y llamamos `d` a nuestra variable auxiliar, posteriormente creamos una lista con los siguientes objetos 

1. Un objeto de tipo `datetime` el cual creamos con la fecha `d[’date’]` 
2. La frecuencia 
3. El valor de la llave ‘felicidad‘ convertido a un dato de tipo `float`