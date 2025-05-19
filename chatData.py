import re, sys
import pandas as pd

import matplotlib.pyplot as plt

if len(sys.argv) < 2:
    print("Uso: python script.py nombre_del_archivo.txt")
    sys.exit(1)
    
nombre_archivo = sys.argv[1]

with open(nombre_archivo, "r", encoding="utf-8") as archivo:
    archivo = archivo.readlines()
mensajes = []


## Patro de Expresion Regular
## Captura 
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
        
def getCountName (list):
    resultado = {}
    for name in list:
        mensajes_usuario = df[df["nombre"] == name]
        resultado[name] = mensajes_usuario.shape[0]
    return resultado

def getDifferenceCount (dic):
    diferencia = {}
    users = list(dic.keys())
    if len(users) != 2:
        return {"error": "Debe haber exactamente dos usuarios"}
    
    val1 = dic[users[0]] 
    val2 = dic[users[1]]
    diff = val1 - val2 
    
    if diff == 0:
        diferencia["same"] = 0
    elif diff > 0:
        diferencia[users[0]] = diff
    else:
        diferencia[users[1]] = abs(diff)
        
    return diferencia

# Constantes
dfNombres = df["nombre"].unique()

# Ver nombres y mensajes
countName = getCountName(dfNombres)
#print(countName)

# Ver cantidad de msj en total
#print(df["nombre"].shape[0])

# Ver quien mando mas y la diferencia
diff = getDifferenceCount(countName)
#print(diff)


## Chats por Dia
#print(df["fecha"].head())
df["fecha"] = pd.to_datetime(df["fecha"], format="%d/%m/%y", errors='coerce')
mensajes_por_dia = df["fecha"].value_counts().sort_index()

dia_max_mensajes = mensajes_por_dia.idxmax()
cantidad_max = mensajes_por_dia.max()



#print(f"El día con más mensajes fue {dia_max_mensajes.date()} con {cantidad_max} mensajes.")
text_to_save = df[df["fecha"] == dia_max_mensajes]


# Codigo Para guardar texto de dia con mas mensajes en un archivo

"""
Crear contenido a guardar
contenido = "\nPrimeros 50 mensajes de ese día:\n\n"
for index, row in text_to_save.iterrows():
    contenido += f"[{row['fecha'].date()} {row['hora']}] {row['nombre']}: {row['mensaje']}\n"

# Guardar en archivo
with open("reporte_dia_mas_activo.txt", "w", encoding="utf-8") as archivo_salida:
    archivo_salida.write(contenido)
""" 


"""
usuario = df["nombre"].unique()[1]  # Elegís el primer nombre
mensajes_usuario = df[df["nombre"] == usuario] 
test = mensajes_usuario["fecha"].value_counts().sort_index().plot(kind='line')

plt.title(f"Actividad diaria de {usuario}")
plt.xlabel("Fecha")
plt.ylabel("Cantidad de mensajes")
plt.grid(True)
plt.show()
"""

print(df[df["fecha"] == "2022-07-01"])