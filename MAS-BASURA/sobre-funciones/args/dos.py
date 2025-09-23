def suma(*args):
    s = 0
    for arg in args:
        s += arg
    return s

suma(1, 3, 4, 2)
#Salida 10

suma(1, 1)
#Salida 2
""" 
args*  = tupla
kwargs** = diccionarios

"""

def listar_palabras(*args):
    la_lista = []
    for a in args:
        la_lista.append(a)
        print(a)
    return la_lista

paroles = listar_palabras("waza", "lingaguri", "mi gente", "pa perder el tiempo")
print(paroles)