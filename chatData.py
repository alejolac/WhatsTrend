import re
import pandas as pd

with open("primerosMensaje.txt", "r", encoding="utf-8") as archivo:
    archivo = archivo.readlines()
mensajes = []

patron = r'\[(\d{1,2}/\d{1,2}/\d{2,4}), ([^\]]+)\] ([^:]+): (.*)'

for linea in archivo:
    match = re.match(patron, linea)
    if match:
        fecha, hora, nombre, mensaje = match.groups()
        mensajes.append({
            "fecha": fecha.strip(),
            "hora": hora.strip(),
            "nombre": nombre.strip(),
            "mensaje": mensaje.strip()

        })
        
df = pd.DataFrame(mensajes)
        
print(df)