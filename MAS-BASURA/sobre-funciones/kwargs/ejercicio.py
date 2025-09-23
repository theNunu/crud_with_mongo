

parole_guardadas = []
def ver_parole(*args):
    for parola in args:
        # print(f"palabra ingresada numero {i}")
        print(f"la parola que ingresastes fue: {parola}")
        parole_guardadas.append(parola)
        print(f"\n lista actual: {parole_guardadas}")
        
    
    return f"cantidad de palabras ingresadas: {len(parole_guardadas)}"

    
while True:
    
    # Verificar si la lista tiene 3 palabras antes de pedir otra
    if len(parole_guardadas) >= 3:
        print("Se alcanzó el límite de 3 palabras.")
        break
    parola = input("ingrese una palabra: ")
    res = ver_parole(parola)
    print(res)