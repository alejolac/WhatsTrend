import re, sys
import pandas as pd

if len(sys.argv) < 2:
    print("Uso: python script.py nombre_del_archivo.txt")
    sys.exit(1)
    
nombre_archivo = sys.argv[1]

with open(nombre_archivo, "r", encoding="utf-8") as archivo:
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
print(countName)

# Ver cantidad de msj en total
print(df["nombre"].shape)

# Ver quien mando mas y la diferencia
diff = getDifferenceCount(countName)
print(diff)

        