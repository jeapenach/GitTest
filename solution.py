#NO ELIMINAR LAS SIGUIENTES IMPORTACIONES, sirven para el funcionamiento de las librería csv y json respectivamente
import csv, json
"""NOTAS: 
    - PARA ESTE RETO PUEDES PROBAR TU PROGRAMA, DANDO CLICK EN LA NAVE ESPACIAL
    - LA CONSOLA TE DIRÁ SI TU SOLUCIÓN ES CORRECTA O NO
    - NO olvidar evaluar tu solución
"""


"""Inicio espacio para programar funciones propias"""
#En este espacio podrás programar las funciones que deseas usar en la función solución (ES OPCIONAL)



"""Fin espacio para programar funciones propias"""

def solucion():
    #ESTA ES LA FUNCIÓN A LA QUE LE DEBES GARANTIZAR LOS RETORNOS REQUERIDOS EN EL ENUNCIADO.

    encabezado = []
    registros = []
    
    with open("GLOBANT.csv", "r") as archivo_globant:
        archivo = csv.reader(archivo_globant)
        encabezado = next(archivo)
                
        for fila in archivo:
            registros.append(fila)
             
    with open("analisis_archivo.csv", "w", newline="") as archivo_analisis:
        header = ["Fecha","Comportamiento de la accion","Punto medio HIGH-LOW"]
        analisis = csv.writer(archivo_analisis, delimiter="\t", )
        analisis.writerow(header)
        linea=[]
        contador_sube = 0
        contador_baja = 0
        contador_estable = 0
        
        for registro in registros:
            fecha = registro[0]
            if float(registro[4]) - float(registro[1]) > 0:
                comportamiento = "SUBE"
                contador_sube += 1
            elif float(registro[4]) - float(registro[1]) < 0:
                comportamiento = "BAJA"
                contador_baja += 1
            else:
                comportamiento = "ESTABLE"
                contador_estable += 1
                
            highlow = (float(registro[2])-float(registro[3]))/2

            linea = [fecha,comportamiento,highlow]

            analisis.writerow(linea)
   
    precio_bajo = float(registros[0][3])
    fecha_precio_bajo = registros[0][0]
    
    for fila in range(1,len(registros)):
        
        if float(registros[fila][3]) < precio_bajo:
            precio_bajo = float(registros[fila][3])
            fecha_precio_bajo = registros[fila][0]

    precio_alto = float(registros[0][2])
    fecha_precio_alto = registros[0][0]
    
    for fila in range(1,len(registros)):
    
        if float(registros[fila][2]) > precio_alto:
            precio_alto = float(registros[fila][2])
            fecha_precio_alto = registros[fila][0]
            
            
    print(precio_bajo," ",fecha_precio_bajo)
    
    print(precio_alto," ",fecha_precio_alto)
        
    print(contador_sube,contador_baja,contador_estable)
    
    diccionario_detalles = {"date_lowest_price" : fecha_precio_bajo, "lowest_price" : precio_bajo, "date_highest_price" : fecha_precio_alto, "highest_price": precio_alto, "cantidad_veces_sube": contador_sube, "cantidad_veces_baja" : contador_baja, "cantidad_veces_estable": contador_estable}
    
    with open("detalles.json", "w",newline="") as archivo_detalle:
                
        json.dump(diccionario_detalles, archivo_detalle)
        
solucion() 
    

    
        
    
    
    
    