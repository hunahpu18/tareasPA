# This is a sample Python script.
""""
@author Jesus Ivan Rivera Ramirez
CDMX 27th april 2022
Representación de un grupo finito dada su tabla de multiplicación(Cayley)
"""


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
        #print(f'{table =}')
        if self._has_unity(table) and self._has_inverses(table) and self._is_associative(table):
            self.table = table

        else:
            raise Exception("La tabla de multiplicación no es de un grupo")

    def _is_associative(self, table: dict) -> bool:
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

        :param table:
        :return:
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
                print(f'{i} es unidad')
        if n_of_units == 1:
            print('unidad: yes')
            self.unit = unit
            return True
        else:
            print('unidad: no')
            return False

    def _has_inverses(self, table: dict) -> bool:
        for elto in self.elements:
            row = [r for r in table.keys() if r[0] == elto]
            row_values = [r[1] for r in row if table[r] == self.unit]
            if len(row_values) == 1:
                #print(f'{elto} tiene inverso')
                self.inverses[elto] = row_values[0]
            else:
                print(f'{elto} inv: no')
                return False
        print('inv: yes')
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
        for i, j in self.table.keys():
            if self.table[(i, j)] != self.table[(j, i)]:
                return False
        return True
    
    def __len__(self):
        return len(self.elements)

    def __getitem__(self, key):
        if key in self.elements:
            return GroupElement(key, self)


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
        aux = self.id
        for i in range(1, 1+len(self.group.elements)):
            aux = self.group.table[(self.id, aux)]
            if aux == self.group.unit:
                return i+1


def mult_table(n: int) -> dict:
    elements = range(0, n)
    res = dict()
    for x in elements:
        for y in elements:
            res[(x, y)] = (x + y) % n
    return res
