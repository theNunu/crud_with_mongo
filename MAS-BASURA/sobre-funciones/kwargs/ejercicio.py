

parole_guardadas = []
def ver_parole(*args):
    
    
    for parola in args:
        # print(f"palabra ingresada numero {i}")
        print(f"la parola que ingresastes fue: {parola}")
        parole_guardadas.append(parola)
        print(parole_guardadas)
        
        
        if len(parole_guardadas) == 3: 
            print("y si hacemos un muñeco?")
            break  # Rompe el bucle cuando el número es 0
           
            # return"te excediste de palabras"
            
       
    
    return f"cantidad de palabras ingresadas: {len(parole_guardadas)}"

    
while True:
    parola = input("ingrese una palabra: ")
    res = ver_parole(parola)
    print(res)