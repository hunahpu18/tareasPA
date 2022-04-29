# This is a sample Python script.
""""
@author Jesus Ivan Rivera Ramirez
CDMX 27th april 2022
Representación de un grupo finito dada su tabla de multiplicación(Cayley)
"""

from math import gcd
from itertools import combinations, chain, product

class Group:
    """
        Clase que representa un grupo.

        ...

        Attributes
        ----------
        table : dict
            Tabla de multiplicar del grupo
        inverses : dict
            Inversos del grupo
        elements : list
            Elementos del grupo
        unit:
            Unidad del grupo
    """
    def __init__(self, table: dict):
        """
        Construye la representación de un grupo a partir de su tabla de multiplicar
        :param table: dict
            tabla de multiplicar
        """
        self.elements = list(set(table.values()))
        self.inverses = dict()
        if self._has_unity(table) and self._has_inverses(table) and self._is_associative(table):
            self.table = table

        else:
            raise Exception("La tabla de multiplicación no es de un grupo")

    def _is_associative(self, table: dict) -> bool:
        """
        Verfica si el grupo satisface la propiedad asociativa, es decir,
        (i+j)+k = i+(j+k)
        :param table:std
            tabla de multiplicación
        :return:
            True si se satisface la propiedad asociativa, False en otro caso
        """
        """"for i in self.elements:
            for j in self.elements:
                for k in self.elements:
                    if table[(table[(i, j)], k)] != table[(i, table[(j, k)])]:
                        print('asoc: no')
                        return False
        print('asoc: yes')
        return True"""""
        return all([table[(table[(i, j)], k)] == table[(i, table[(j, k)])]
                    for i in self.elements for j in self.elements for k in self.elements])

    def _has_unity(self, table: dict) -> bool:
        """
        Verfica si el grupo tiene unidad
        :param table:dict
            tabla de multiplicar
        :return:
            True si el grupo tiene unidad, False en otro caso
        """
        n_of_units = 0
        unit = None
        for i in self.elements:
            is_unity = True
            for j in self.elements:
                if not (table[(i, j)] == j and table[(j, i)] == j):
                    is_unity = False
                    break
            if is_unity:
                n_of_units += 1
                unit = i
        if n_of_units == 1:
            self.unit = unit
            return True
        else:
            return False

    def _has_inverses(self, table: dict) -> bool:
        """
        Verifica si el grupo tiene inversos
        :param table: dict
            Tabla de multiplicar
        :return:
            True si existen todos los inversos, False en otro caso
        """
        for elto in self.elements:
            row = [r for r in table if r[0] == elto]
            row_values = [r[1] for r in row if table[r] == self.unit]
            if len(row_values) == 1:
                self.inverses[elto] = row_values[0]
            else:
                return False
        return True

    def __repr__(self):
        res = list()
        for x in self.elements:
            aux = list()
            for y in self.elements:
                aux.append(self.table[(x, y)])
            res.append(aux)
        return str(res)

    def __str__(self):
        res = list()
        res.append([0] + self.elements)
        for x in self.elements:
            aux = list()
            aux.append(x)
            for y in self.elements:
                aux.append(self.table[(x, y)])
            res.append(aux)
        return '\n'.join(' '.join(map(str, row)) for row in res)

    def is_commutative(self) -> bool:
        """
        Verifica si un grupo es conmutativo
        :return:
            True si el grupo es conmutativo, False en otro caso
        """
        for i, j in self.table:
            if self.table[(i, j)] != self.table[(j, i)]:
                return False
        return True
    
    def __len__(self):
        return len(self.elements)

    def __getitem__(self, key):
        if key in self.elements:
            return GroupElement(key, self)

    def subgroups_list(self):
        sets_to_try = (chain(*[list(combinations(self.elements, n))for n, _ in enumerate(self.elements)]))
        sets_with_unity = (filter(lambda x: self.unit in x and len(self.elements) % len(x) == 0, sets_to_try))
        sets_with_inverses = (filter(lambda x: all([self.inverses[elto] in x for elto in x]), sets_with_unity))
        sets_closed = list([g for g in sets_with_inverses if all([self.table[(x,y)] in g for x, y in product(g, g)])])
        return sets_closed+[tuple(self.elements)]

    def normal_subgroups_list(self):
        candidates = self.subgroups()
        return [sg for sg in candidates if all({all({(self[x] + self[i] - self[x]).id in sg for x in self.elements}) for i in sg})]


class GroupElement:
    def __init__(self, elto, group):
        self.id = elto
        self.group = group

    def __str__(self):
        return str(self.id)

    def __repr__(self):
        return str(self.id)

    def __add__(self, other):
        if self.group == other.group:
            return GroupElement(self.group.table[(self.id, other.id)], self.group)
        return None

    def __sub__(self, other):
        if self.group == other.group:
            return self + (-other)
        return None

    def __neg__(self):
        return GroupElement(self.group.inverses[self.id], self.group)

    def order(self) -> int:
        """
        Devuelve el orden de un elemento
        :return:
            El orden de un elemento
        """
        aux = self.id
        for i in range(1, 1+len(self.group.elements)):
            aux = self.group.table[(self.id, aux)]
            if aux == self.group.unit:
                return i+1


def mult_table(n: int) -> dict:
    """
    Crea la tabla de multiplicar de el grupo (Z/nZ, +)
    :param n: int
        Tamaño del grupo a crear
    :return:
        Diccionario con la tabla de multiplicar del grupo (Z/nZ, +)
    """
    elements = range(0, n)
    res = dict()
    for x in elements:
        for y in elements:
            res[(x, y)] = (x + y) % n
    return res


def mult_cyclic(n: int) -> dict:
    """
        Crea la tabla de multiplicar de el grupo (Z/nZ, *)
        :param n: int
            Entero con el cual se creara el grupo mod n
        :return:
            Diccionario con la tabla de multiplicar del grupo (Z/nZ, *)
        """
    elements = [x for x in range(0, n) if gcd(x, n) == 1]
    res = dict()
    for x in elements:
        for y in elements:
            res[(x, y)] = (x * y) % n
    return res
