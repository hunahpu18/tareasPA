# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

class Group:
    def __init__(self, table: dict):
        self.elements = list(set(table.values()))
        print(f'{table =}')
        if self._has_unity(table) and self._has_inverses(table) and self._is_asociative(table):
            self.table = table
        else:
            raise Exception("La tabla de multiplicación no es de un grupo")

    def _is_asociative(self, table: dict) -> bool:
        for i in self.elements:
            for j in self.elements:
                for k in self.elements:
                    if table[(table[(i, j)], k)] != table[(i, table[(j, k)])]:
                        print('asoc: no')
                        return False
        print('asoc: yes')
        return True

    def _has_unity(self, table: dict) -> bool:
        n_of_units = 0
        for i in self.elements:
            is_unity = True
            for j in self.elements:
                if not (table[(i, j)] == j and table[(j, i)] == j):
                    is_unity = False
                    break
            if is_unity:
                n_of_units += 1
                print(f'{i} es unidad')
        if n_of_units == 1:
            print('unidad: yes')
            return True
        else:
            print('unidad: no')
            return False

    def _has_inverses(self, table: dict) -> bool:
        for elto in self.elements:
            row = [r for r in table.keys() if r[0] == elto]
            row_values = [table[r] for r in row]
            if ('e' in row_values) or (0 in row_values):
                print(f'{elto} tiene inverso')
            else:
                print(f'{elto} inv: no')
                return False
        print('inv: yes')
        return True

    def show(self):
        res = list()
        for _ in self.elements:
            aux = list()
            for y in self.elements:
                aux.append(y)
            res.append(aux)
        print(res)

    def is_commutative(self) -> bool:
        for i,j in self.table.keys():
            if self.table[(i, j)]!=self.table[(j, i)]:
                return False
        return True
    def order(self, elto) -> int:
        if not elto in self.elements:
            return -1
        else:
            aux=elto
            for i in range(1,1+len(self.elements)):
                aux = self.table[(elto,aux)]
                if (aux == 0 or aux == 'e'):
                    return i+1

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.

def multtable(n):
    elements = range(0,n)
    res = dict()
    for x in elements:
        for y in elements:
            res[(x,y)]=(x+y)%n;
    return res;
test = {(0, 0): 0, (0, 1): 1, (1, 0): 1, (1, 1): 0}
test1 = {('e', 'e'): 'e', ('e', 'a'): 'a', ('a', 'e'): 'a', ('a', 'a'): 'e'}
testd = {(0, 0): 0, (0, 1): 1, (0, 2): 2, (0, 3): 3, (0, 4): 4, (0, 5): 5,
         (1, 0): 1, (1, 1): 2, (1, 2): 3, (1, 3): 4, (1, 4): 5, (1, 5): 0,
         (2, 0): 2, (2, 1): 3, (2, 2): 4, (2, 3): 5, (2, 4): 0, (2, 5): 1,
         (3, 0): 3, (3, 1): 4, (3, 2): 5, (3, 3): 0, (3, 4): 1, (3, 5): 2,
         (4, 0): 4, (4, 1): 5, (4, 2): 0, (4, 3): 1, (4, 4): 2, (4, 5): 3,
         (5, 0): 5, (5, 1): 0, (5, 2): 1, (5, 3): 2, (5, 4): 3, (5, 5): 4}

print(multtable(2))
## validate_multiplication_table(test)
G = Group(multtable(5))
G.show()
print(f'G es conmutativo: {G.is_commutative()}')
print(G.order(2))
# Press the green button in the gutter to run the script.
## if __name__ == '__main__':
##    print_hi('PyCharm')
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
