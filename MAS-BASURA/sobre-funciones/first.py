x = [10, 20, 30]
print(id(x)) # 4422423560
def funcion(entrada):
    entrada.append(40)
    print(id(entrada)) # 4422423560

funcion(x)



print("\n -- -- otro ejemplo -- -- ")

nombres = ["saul","kim", "skyler", "hank"]
print(id(nombres))

n = "tilin"
print(f"id de tilin: {id(n)}")
nombres.append(n)
print(nombres)
print(id(nombres))
