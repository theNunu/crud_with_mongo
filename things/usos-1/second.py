parole = ["garen", "nautilus", "brand", "dr mundo", "Brand", "brand"]
parole_repetidas = []
for i, p in enumerate(parole):
    print(i +1, p)
    if p.lower() == "brand":
        # print("veces que se repitio brand")
        parole_repetidas.append(p)
        # print(p)
        
        
print(parole_repetidas)
# print(parole_repetidas.upper())

print(f"la palabra se repitio {len(parole_repetidas)} veces")