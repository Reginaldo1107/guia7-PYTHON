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


#2.5
#2.6
# 3 
#4.1
def listaDeEstudiantes () -> list :
    LaListaDeEstudiantes :list= []
    estudiantes  :str = input("Ingrese un estudiante si no lo desea escriba :listo ") 
    while(estudiantes != "listo"):
        LaListaDeEstudiantes.append(estudiantes)
        estudiantes = input("Ingrese otro estudiante si no lo desea escriba :listo ")

    return LaListaDeEstudiantes 
#4.2
def elMonedero ()-> list :
    listaDeMovimientosTuplas :list = []
    condicion : bool = True

    while(condicion == True):
        entrada : str = input("Para operarar, ingrese \n 'C' PARA CARGAR CREDITOS \n 'D' para extraer dinero \n 'X' para salir \n ")

        
        if(entrada == "C"):
            numero :int  = int(input("Ingrese el monto a cargar : "))
            tuplaDeMovimientos  = (entrada,numero)
            listaDeMovimientosTuplas.append(tuplaDeMovimientos)
        
        elif(entrada == "D"):
            numero :int  = int(input("Ingrese el monto a cargar : "))
            tuplaDeMovimientos  = (entrada,numero)
            listaDeMovimientosTuplas.append(tuplaDeMovimientos)
        elif(entrada == "X") :   
        
            print ("Usted acaba de terminar su lista gratsia")
            condicion =False
        else : 
            print ("ENTRADA INCORRECTA , VUELVA A INTENTARLO ")
    
    return listaDeMovimientosTuplas



print(elMonedero())



