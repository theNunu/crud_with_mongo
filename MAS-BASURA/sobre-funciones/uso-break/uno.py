names = ["John", "Jane", "Doe"]
for i in names:
    print(i)
    if i == "Jane":
        break
    
    
print("""\n
      
El código anterior imprime un rango de números del 0 al 9. Pero podemos evitar
que este ciclo imprima todos los números; en su lugar, podemos detenernos en un número en particular. Así es cómo:""")

for i in range(10):
  print(i)
  if i == 5:
      break