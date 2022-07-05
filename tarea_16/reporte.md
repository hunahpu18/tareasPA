# Tarea 16
> Jesus Ivan Rivera Ramirez

# Funcionamiento de los métodos
### is_pareto_efficient_dumb

```python
def is_pareto_efficient_dumb(costs):
"""
  Find the pareto-efficient points
  :param costs: An (n_points, n_costs) array
  :return: A (n_points, ) boolean array, indicating whether each point is Pareto efficient
"""
  is_efficient = np.ones(costs.shape[0], dtype=bool)
  for i, c in enumerate(costs):
    is_efficient[i] = np.all(np.any(costs[:i] > c, axis=1)) \
               and np.all(np.any(costs[i + 1:] > c, axis=1))
  return is_efficient
```

       Durante la instrucción `for` se revisa si existe algún elemento que domine al i-esimo elemento primero en el rango [0,i) y luego en el rango [i+1,n] donde n es la longitud del arreglo
       utilizando `np.any` pare revisar si algún elemento lo domina y combinandolo con `np.all` para obtener `True` si no es dominado o `False` en caso contrario.

### is_pareto_efficient_simple

       ```python
def is_pareto_efficient_simple(costs):
"""
 Find the pareto-efficient points
 :param costs: An (n_points, n_costs) array
 :return: A (n_points, ) boolean array, indicating whether each point is Pareto efficient
"""
  is_efficient = np.ones(costs.shape[0], dtype=bool)
  for i, c in enumerate(costs):
    if is_efficient[i]:
    # Keep any point with a lower cost
      is_efficient[is_efficient] = np.any(costs[is_efficient] < c, axis=1)
      is_efficient[i] = True  # And keep self
  return is_efficient
  ```
  
En este caso se procede de manera similar, se crea un arreglo para guardar que elementos son dominantes,
la mejora de este es que solo se utilizan los indices de elementos que aún no han sido dominados, por
lo que el numero de comparaciones es menor que en el metodo anterior.

### is_pareto_efficient

```python
def is_pareto_efficient(costs, return_mask=True):
    """
    Find the pareto-efficient points
    :param costs: An (n_points, n_costs) array
    :param return_mask: True to return a mask
    :return: An array of indices of pareto-efficient points.
        If return_mask is True, this will be an (n_points, ) boolean array
        Otherwise it will be a (n_efficient_points, ) integer array of indices.
    """
    is_efficient = np.arange(costs.shape[0])
    n_points = costs.shape[0]
    next_point_index = 0  # Next index in the is_efficient array to search for
    while next_point_index < len(costs):
        nondominated_point_mask = np.any(costs < costs[next_point_index], axis=1)
        nondominated_point_mask[next_point_index] = True
        is_efficient = is_efficient[nondominated_point_mask]  # Remove dominated points
        costs = costs[nondominated_point_mask]
        next_point_index = np.sum(nondominated_point_mask[:next_point_index]) + 1
    if return_mask:
        is_efficient_mask = np.zeros(n_points, dtype=bool)
        is_efficient_mask[is_efficient] = True
        return is_efficient_mask
    return is_efficient

```
La mejora de este metodo sobre el anterior es que ahora en ves de iterar sobre todos los elementos,
solo se itera sobre aquellos que aún no han sido dominados, al utilizar la variable `next_point_index.

## Observaciones
Al ejecutar los algoritmos anteriores se puede notar que son sensibles al orden en que aparecen los elementos
de los que se desea calcular el frentre de pareto, por ejemplo, con los datos de prueba que estan ordenados
de menor a mayor todos los metodos son más lentos, sin embargo si se ordenan previo a la ejecucíon del método
esto logra que el tiempo de ejecución sea menor. Además si los datos se revuelven se alcanza un tiempo similar al tiempo 
con los datos ordenados, los tiempos obtenidos son los siguientes.

|algoritmo| tiempo|
| --- | --- |
|my_pareto| 0.709723375638001|
|my_pareto shuffled| 0.022174418277001676|
|my_pareto sorted| 0.03820451881700137|
|pareto_front| 0.03167189165237505|
|is_pareto_efficient_dumb | 0.28316227411599904|
|is_pareto_efficient_simple | 0.001527363470999262|
|is_pareto_efficient | 0.0006262909170000057|
|is_pareto_efficient_dumb sorted| 0.3100833442969997|
|is_pareto_efficient_simple sorted| 0.0009105862689975765|
|is_pareto_efficient sorted| 0.00015902138800083775|
|is_pareto_efficient_dumb shuffled| 0.32333724023020477|
|is_pareto_efficient_simple shuffled| 0.0009358590092051599|
|is_pareto_efficient shuffled| 0.00018442580020928273|

