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
    def __init__(self, table: dict, check: int = 0):
        """
        Construye la representación de un grupo a partir de su tabla de multiplicar
        :param table: dict
            tabla de multiplicar
        """
        self.elements = list(set(table.values()))
        self.inverses = {}
        if check:
            self.table = table
            self._has_unity(table)
            self._has_inverses(table)
        else:
            if self._has_unity(table) and (self._has_inverses(table) and self._is_associative(table)):
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
        print('unity')
        n_of_units = 0
        unit = None
        for i in self.elements:
            is_unity = True
            for j in self.elements:
                if table[(i, j)] != j or table[(j, i)] != j:
                    is_unity = False
                    break
            if is_unity:
                n_of_units += 1
                unit = i
        if n_of_units == 1:
            self.unit = unit
            print('True')
            return True

        self.unit = None
        print('False')
        return False

    def _has_inverses(self, table: dict) -> bool:
        """
        Verifica si el grupo tiene inversos
        :param table: dict
            Tabla de multiplicar
        :return:
            True si existen todos los inversos, False en otro caso
        """
        print('inversos')
        for elto in self.elements:
            row = [r for r in table if r[0] == elto]
            row_values = [r[1] for r in row if table[r] == self.unit]
            if len(row_values) == 1:
                self.inverses[elto] = row_values[0]
            else:
                return False
        return True

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

    def subgroup(self, elements: tuple):
        if all([elto in self.elements for elto in elements]):
            if not self._is_subgroup(elements):
                raise Exception('Los elementos no forma un subgrupo')
            return Group({key: self.table[key] for key in product(elements, elements)}, check=1)
        return None

    def _is_subgroup(self, elements: tuple) -> bool:
        if self.unit not in elements or len(self.elements) % len(elements) != 0:
            #print('sin unidad o longitud no divide')
            return False
        if not all([self.inverses[elto] in elements for elto in elements]):
            #print('sin inversos')
            return False
        if not all([self.table[(x, y)] in elements for x, y in product(elements, elements)]):
            #print('no cerrado')
            return False
        return True

    def subgroups_list(self):
        sets_to_try = (chain(*[combinations(self.elements, n) for n, _ in enumerate(self.elements)
                               if n and len(self.elements) % n == 0]))
        #sets_with_unity = (filter(lambda x: self.unit in x, sets_to_try))
        #sets_with_inverses = (filter(lambda x: all([self.inverses[elto] in x for elto in x]), sets_with_unity))
        #sets_closed = list([g for g in sets_with_inverses if all([self.table[(x, y)] in g for x, y in product(g, g)])])
        subgroups = list(filter(self._is_subgroup, sets_to_try))
        return subgroups+[tuple(self.elements)]

    def normal_subgroups_list(self):
        candidates = self.subgroups_list()
        return [sg for sg in candidates
                if all({all({(self[x] + self[i] - self[x]).id in sg for x in self.elements}) for i in sg})]

    def __len__(self):
        return len(self.elements)

    def __getitem__(self, key):
        if key in self.elements:
            return GroupElement(key, self)
        return None

    def __repr__(self):
        res = []
        for x in self.elements:
            aux = []
            for y in self.elements:
                aux.append(self.table[(x, y)])
            res.append(aux)
        return str(res)

    def __str__(self):
        res = []
        res.append([0] + self.elements)
        for x in self.elements:
            aux = []
            aux.append(x)
            for y in self.elements:
                aux.append(self.table[(x, y)])
            res.append(aux)
        return '\n'.join(' '.join(map(str, row)) for row in res)

    def __eq__(self, other):
        return self.table == other.table

    def __mul__(self, other):
        table = {}
        for x, y in product(self.table, other.table):
            x1, x2 = x
            y1, y2 = y
            table[(x, y)] = (self.table[(x1, y1)], other.table[(x2, y2)])
        return Group(table, check=1)


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

    def __rmul__(self, other: int):
        aux = self
        for _ in range(1, other):
            aux = aux + self
        return aux

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
        return 0


def mult_cyclic(n: int) -> dict:
    """
    Crea la tabla de multiplicar de el grupo (Z/nZ, +)
    :param n: int
        Tamaño del grupo a crear
    :return:
        Diccionario con la tabla de multiplicar del grupo (Z/nZ, +)
    """
    elements = range(0, n)
    res = {}
    for x in elements:
        for y in elements:
            res[(x, y)] = (x + y) % n
    return res


def mult_units(n: int) -> dict:
    """
        Crea la tabla de multiplicar de el grupo (Z/nZ, *)
        :param n: int
            Entero con el cual se creara el grupo mod n
        :return:
            Diccionario con la tabla de multiplicar del grupo (Z/nZ, *)
        """
    elements = [x for x in range(0, n) if gcd(x, n) == 1]
    res = {}
    for x in elements:
        for y in elements:
            res[(x, y)] = (x * y) % n
    return res
