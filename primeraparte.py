#1)---------------------------------------------------
def pertenece1( LaLista : list ,  x:any) -> bool:
    pertence : bool = False 
    for i in range(len(LaLista)):
        if(LaLista[i] == x):
            pertence = True
    return pertence

def pertenece2( LaLista : list ,  x: int) -> bool:
    pertence : bool = False 
    i :int = 0
    while( i <len(LaLista) and pertence == False):
        if(LaLista[i] == x):
            pertence = True
        i+=1

    return pertence

#print(pertenece1( ['1','2','3','4','5'],  '5'))
#print(pertenece1( ['1','2','3','4','5'],  'A'))

#-------------------------------------------------------
#2)---------------------------------------------------
def divideATodos(LaLista :list , x :int ) -> bool :
    divideATodos : bool = True
    i :int = 0 
    while(i< len(LaLista) and divideATodos == True):
        if(LaLista[i] % x  != 0 ):
            divideATodos = False 

        i+=1
    return divideATodos

#print (divideATodos([2,4,6,8,9] , 1))
#print (divideATodos([2,4,6,8,9] , 2))
#print (divideATodos([2,4,6,8,2] , 2))

#-------------------------------------------------------
#3)-----------------------------------------------------
def sumaTotal(LaLista :list )->int :
    suma :int = 0
    for i in range (0, len(LaLista),1):
        suma += LaLista[i]

    return suma     
#print(sumaTotal([1,2,3,4,5]))
#print(sumaTotal([2,2,2,2,2]))
#print(sumaTotal([0,0,0,0,0]))
#print(sumaTotal([1,1,1,1,1]))
#-------------------------------------------------------
# 4.1)-----------------------------------------------------
def ordenados(LaLista : list) ->bool :
    i :int = 0
    creciente :bool = True 
    for i in range (0 , len(LaLista)-1 ,1):
        if(LaLista[i] >= LaLista[i+1]):
            creciente = False

    return creciente

# 5.1)-----------------------------------------------------
def mayorA7(LaLista :list ) ->bool :
    palabraMayorA7 :bool = False
    for i in LaLista :
        if(len(i) > 7 ):
            palabraMayorA7 = True

    return palabraMayorA7 
        
#----------------------------------------------------------
#6.1)----------------------------------------------------------
def palindromo (texto : str) ->bool :
    esPalindromo :bool = True
    i:int = 0 
    while (i < (len(texto))/2):
        if(texto[i] != texto [len(texto)-1-i]):
            esPalindromo = False
        
        i+=1    
    return esPalindromo



#----------------------------------------------------------
#7.1)----------------------------------------------------------
def longitudValidaVerde(texto:str )->bool: 
    return len(texto)> 8

def tiene1Minuscula(texto :str)-> bool :
    tieneLetraMinuscula : bool = False 
    for i in range (0 , len(texto),1):
        if (texto[i] >= 'a'  and texto[i] <= 'z'):
            tieneLetraMinuscula = True 
    return tieneLetraMinuscula


def tiene1Mayuscula(texto :str)-> bool :
    tieneLetraMayuscula : bool = False 
    for i in range (0 , len(texto),1):
        if (texto[i] >= 'A'  and texto[i] <= 'Z'):
            tieneLetraMayuscula = True 
    return tieneLetraMayuscula
    

def tieneDigitoNumerico(texto :str)-> bool :
    tieneDigitoNumerico : bool = False 
    for i in range (0 , len(texto),1):
        if (texto[i] >= '0'  and texto[i] <= '9'):
            tieneDigitoNumerico = True 
    return tieneDigitoNumerico
    
def lognitudValidaRoja(texto :str) ->bool:    
    return len(texto) < 5

def fortalecerContrasenia(contra:str) -> str :
    devolverContrasenia :str = "AMARRILLA"
    if(longitudValidaVerde(contra) and tiene1Minuscula(contra) and tiene1Mayuscula(contra) and tieneDigitoNumerico(contra) ):
        devolverContrasenia = "VERDE"
    elif(lognitudValidaRoja(contra)) :
        devolverContrasenia = "ROJA"   

    return devolverContrasenia
    
    
print(fortalecerContrasenia ("12345678fnvbnsd"))
print(fortalecerContrasenia ("12345678zZ"))
print(fortalecerContrasenia ("REGINAldosad"))
print(fortalecerContrasenia ("REG1"))














#4.2)-----------------------------------------------------
#def reemplazaVocales (LaLista :list )-> list :
   # if x not in "aeiou" :
#-------------------------------------------------------
