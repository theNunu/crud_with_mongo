import time

def generar_hora_y_fecha()-> str:
    tiempo_local = time.localtime()

    print(f"tiempo local: {tiempo_local}")
    tiempo_formateado = time.strftime("%Y-%m-%d %H:%M:%S", tiempo_local)
    print(f"tiempo formateado: {tiempo_formateado}")
    return tiempo_formateado

    