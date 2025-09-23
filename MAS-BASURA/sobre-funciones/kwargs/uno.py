def suma(**kwargs):
    s = 0
    for key, value in kwargs.items():
        print(key, "=", value)
        s += value
    return s
    
suma(a=3, b=10, c=3)
#Salida
#a = 3
#b = 10
#c = 3
#16

def listar_campeones(**kwargs):
    for n, c in kwargs.items():
        print(n, c )
    

listar_campeones(name = "galio", carril = "mid", age=30) #clave , valor