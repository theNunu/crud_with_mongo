texto = """  
Abriste una ventana despertando una ilusión
Cegando por completo mi razón
Mantuve la esperanza conociendo tu interior
Sintiendo tan ajeno tu calor, probé de la manzana por amor
Quiero ya no amarte y enterrar este dolor
Quiero, que mi corazón te olvide
Quiero ser como tú, quiero ser yo la fuerte
Solo te he pedido a cambio tu sinceridad
Quiero, que el amor al fin conteste
¿Por qué siempre soy yo la de la mala suerte?
Tú vienes me acaricias y te marchas con el sol
Me duele solo ser tu diversión
Dices que me amas, que no hay nadie como yo
Que soy la dueña de tu corazón
Pero alguien más está en tu habitación
Quiero ya no amarte y enterrar este dolor
Quiero, que mi corazón te olvide
Quiero ser como tú, quiero ser yo la fuerte
Solo te he pedido a cambio tu sinceridad
Quiero, que el amor al fin conteste
¿Por qué siempre soy yo la de la mala suerte?
Y no, no pasa nada si el amor, no es perfecto
Siempre y cuando sea honesto
Y no, ya para qué pedir perdón, no es correcto
No puedo compartir lo que no se me dio
No soy la dueña de tu corazón
Yo soy quien sobra en esta habitación, no
Quiero ya no amarte y enterrar este dolor
Quiero, que mi corazón te olvide
Quiero ser como tú, quiero ser yo la fuerte
Solo te he pedido a cambio tu sinceridad
Quiero, que el amor por fin conteste
¿Por qué siempre soy yo la de la mala suerte?
"""
print(f"longitud de texto: {len(texto)}")
palabras_repetidas  = []
texto_split = texto.split()
print(texto_split)

print("\n -- -- USANDO UN BUCLE")
contador = 0
for i, text in enumerate(texto_split):
    print(i +1, text)
    if text == "fin":
        palabras_repetidas.append(text)
        
        
print(palabras_repetidas)
        