#2.1
def borrarPares(listaNum : list) -> None :
    for i in range (0 , len(listaNum),1):
        if (i % 2 == 0):
            listaNum[i] = 0 
        print(listaNum[i]) 


# 2.2

def borraParesConCopia(listaNum : list) -> list:
    listaAuxiliar : list = listaNum.copy()
    for i in range (0 , len(listaAuxiliar),1):
        if (i % 2 == 0):
            listaAuxiliar[i] = 0 
        
    return listaAuxiliar



#2.3

def borrarVocales (cadenaChar : [str]) -> [str] :
    cadenaAuxiliar :str = [] # o salida : str = ""
    
    for i in range (0,len(cadenaChar),1):
        if( not cadenaChar[i]  in "aeiouAEIOU"):
            cadenaAuxiliar.append(cadenaChar[i])
            

    return cadenaAuxiliar
# otra forma de hacerlo es cadenaAuxiliar :str = ""
# y luego ir sumando con lo que no son vocales 
#    salida:str=""
#   for i in range(0,len(palabra)):
#        if (not(es_vocal(palabra[i]))):
#            salida+=palabra[i]
#    return salida


#2.4

def reemplazaVocales(listaChar :list) -> list :
    listaAuxiliar :list = []
    for i in range (0,len(listaChar),1):
        if(listaChar[i] in "aeiouAEIOU"):
            listaAuxiliar+=" "
        else :
            listaAuxiliar+=listaChar[i]
              
    return listaAuxiliar    
        
