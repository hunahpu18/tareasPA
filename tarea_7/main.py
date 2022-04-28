from group import *
test = {('e', 'e'): 'e', ('e', 'a'): 'a', ('a', 'e'): 'a', ('a', 'a'): 'e'}


dieh = {('e', 'e'): 'e', ('e', 'a'): 'a', ('e', 'b'): 'b', ('e', 'c'): 'c', ('e', 'd'): 'd', ('e', 'f'): 'f',
        ('a', 'e'): 'a', ('a', 'a'): 'b', ('a', 'b'): 'e', ('a', 'c'): 'd', ('a', 'd'): 'f', ('a', 'f'): 'c',
        ('b', 'e'): 'b', ('b', 'a'): 'e', ('b', 'b'): 'a', ('b', 'c'): 'f', ('b', 'd'): 'c', ('b', 'f'): 'd',
        ('c', 'e'): 'c', ('c', 'a'): 'f', ('c', 'b'): 'd', ('c', 'c'): 'e', ('c', 'd'): 'b', ('c', 'f'): 'a',
        ('d', 'e'): 'd', ('d', 'a'): 'c', ('d', 'b'): 'f', ('d', 'c'): 'a', ('d', 'd'): 'e', ('d', 'f'): 'b',
        ('f', 'e'): 'f', ('f', 'a'): 'd', ('f', 'b'): 'c', ('f', 'c'): 'b', ('f', 'd'): 'a', ('f', 'f'): 'e'}

test = mult_table(6)
g = Group(dieh)
print(f'El grupo tiene orden: {len(g)}')
print(f'El grupo tiene unidad: {g.unit}')
print(f'El grupo es conmutativo {g.is_commutative()}')
print(f'La operación de c - a es {g["c"] + g["a"]}')
print(f'el orden de a es {g["a"].order()}')
print(f'{g}')
