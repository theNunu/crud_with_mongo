parole = ["garen", "nautilus", "brand", "dr mundo", "brand", "brand"]
parole_repetidas = []
for i, p in enumerate(parole):
    print(i +1, p)
    if p == "brand":
        # print("veces que se repitio brand")
        parole_repetidas.append(p)
        # print(p)
        
        
print(parole_repetidas)
print(f"la palabra se repitio {len(parole_repetidas)} veces")