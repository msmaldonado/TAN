# -*- coding: utf-8 -*-
"""
Editor de Spyder
Miguel Sánchez Maldonado

Teoría de Números y Criptografía
"""

"""
Ejercicios Practica0
"""

"""
Ejercicio 1
"""
#Funcion que nos devuelve el valor de una letra en una posición
def elemento(hexstring,i):
    lista_hexadecimal={}
    #Almaceno las letras usadas por los hexadecimales
    lista_hexadecimal["a"]=10
    lista_hexadecimal["b"]=11
    lista_hexadecimal["c"]=12
    lista_hexadecimal["d"]=13
    lista_hexadecimal["e"]=14
    lista_hexadecimal["f"]=15
    #compruebo si la letra corresponde a alguna de la lista hexadecimal
    if hexstring[i] in lista_hexadecimal:
        return lista_hexadecimal[hexstring[i]]
    else :#sino en esa posición hay un numero, lo devuelvo.
        return hexstring[i]
    #else:
     #   print "El numero no es hexadecimal"

"""
Ejercicio 2
"""
#Funcion que nos devuelve el valor decimal de un numero hexadecimal
def hextodec_it(hexastring):
    lista_hexadecimal={}
    #Almaceno las letras usadas por los hexadecimales
    lista_hexadecimal["a"]=10
    lista_hexadecimal["b"]=11
    lista_hexadecimal["c"]=12
    lista_hexadecimal["d"]=13
    lista_hexadecimal["e"]=14
    lista_hexadecimal["f"]=15
    resultado=0

    for i in range(len(hexastring)):#Recorro todas las posiciones
        if hexastring[i] in lista_hexadecimal:#Miro si en la posición hay una letra de los hexadecimales
            resultado+=(16**(len(hexastring)-1-i))*lista_hexadecimal[hexastring[i]]#actualizo resultado
        else:#Si en la posición no hay una letra, será un numero
            resultado+=(16**(len(hexastring)-1-i))*int(hexastring[i])#actualizo resultado
    return resultado

"""
Ejercicio 3
"""
#Funcion que nos devuelve el valor decimal de un numero hexadecimal de forma recursiva
def hextodec_rec(hexastring):
    lista_hexadecimal={}
     #Almaceno las letras usadas por los hexadecimales
    lista_hexadecimal["a"]=10
    lista_hexadecimal["b"]=11
    lista_hexadecimal["c"]=12
    lista_hexadecimal["d"]=13
    lista_hexadecimal["e"]=14
    lista_hexadecimal["f"]=15

    if len(hexastring) == 1:#si es de una cifra
        if str(hexastring) in lista_hexadecimal:#Si es una letra devuelve su correspondiente numero
            return lista_hexadecimal[str(hexastring)]
        else:#Sino es numero, devuelve el entero
            return int(hexastring)
    else:#si el numero tiene varias cifras, voy "quitando una a una" para hacer llamadas recursivas con una cifra menos
        hexastring.replace(hexastring[len(hexastring)-1],"")
        auxiliar = list(hexastring)
        del(auxiliar[len(auxiliar)-1])
        auxiliar="".join(auxiliar)

        return 16*hextodec_rec(auxiliar)+hextodec_rec(hexastring[len(hexastring)-1])

"""
Ejercicio 4
"""
#Funcion ayuda que nos convierte un digito a su valor en hexadecimal
def con_dig_a_hex(dig):
    #vemos el valor del digito y lo asociamos a su valor en hexadecimal
    if dig<10:
        return str(dig)
    elif (dig == 10):
        return 'A';
    elif (dig == 11):
        return 'B'
    elif (dig == 12):
        return 'C'
    elif (dig == 13):
        return 'D'
    elif (dig == 14):
        return 'E'
    elif (dig == 15):
        return 'F'

#Funcion que asocia a un entero su expresión en hexadecimal
def dectohex_rec(entero):
    #Aplicamos recursivamente la función al cociente y con el resto llamamos a la funcion de ayuda
    cociente = entero / 16
    resto = entero % 16

    if cociente == 0:#si no hay cociente devuelva el valor del resto
        return con_dig_a_hex(resto)
    else:#Sino llamada recursiva al cociente y el resto lo convierte a su hexadecimal
        return dectohex_rec(cociente) + con_dig_a_hex(resto)

"""
Ejercicios Practica1
"""

"""
Ejercicio 1
"""
#Funcion que separa un mensaje un palabras para almacenarla en una lista
def lista_palabras(mensaje) :
    lista_palabras = []
    palabra = ""
    for i in lista_palabras:#Recorremos el mensaje char a char
        if i is not "":#Si no es espacio estamos en la misma palabra
            palabra += i#Vamos completando la palabra
        else :#Si habiamos encontrado un espacio ya habiamos recorrido una palabra
            lista_palabras.append(palabra)#Introducimos la nueva palabra
            palabra = ""#Actualizamos palabra a vacio porque vamos a buscar una nueva
    if(palabra is not ""):#Si el mensaje no acaba en espacio, paara no perder la ultima palabra
        lista_palabras.append(palabra)

    return lista_palabras

        #return mensaje.split()
        #la funcion split ya nos separa las palabras del mensaje
"""
Ejercicio 2
"""

#Funcion que convierte las palabras de un mensaje en una lista en hexadecimal.
def str_to_hexalist(mensaje):
    palabras_codificadas = []
    palabras = lista_palabras(mensaje)#Obtengo la lista de palabras
    for i in palabras:#Recorro la lista y a cada palabra le asocio su hexadecimal
        palabras_codificadas.append(i.encode('hex'))
    return palabras_codificadas

"""
Ejercicio 3
"""

#Funcion que convierte una lista en hexadecimal en un mensaje.
def  hexalist_to_str(lista):
    mensaje =[]
    for i in lista:#Recorremos la lista de hexadecimal y a cada uno le asociamos la palabra
        mensaje.append(i.decode('hex'))
    mensaje =  ' '.join(mensaje)  #Coloco espacios entre palabras
    return mensaje

"""
Ejercicios Practica2
"""

"""
Ejercicio 1
"""
#Función de parametros mensaje,a,b,n que nos codificará un mensaje
def cod_afin(mensaje,a,b,n):
    if gcd(a,n)==1:#mcd(a,n) es 1
        lista_hexadecimal=str_to_hexalist(mensaje)#mensaje a hexadecimal
        lista_codificada=[]
        for i in lista_hexadecimal:
            decimal = hextodec_it(i)#hexadecimal a decimal
            lista_codificada.append((a*int(decimal)+b)%n)#el decimal transformado por la aplicación afin
        return lista_codificada
    else:
        print "mcd(a,n) no es 1. "
"""
Ejercicio 2
"""
#Funcion que recibe una lista codificada,a,b,n y nos devuelve el mensaje original
def deco_afin(lista,a,b,n):
    lista_hexadecimal = []
    for i in lista:
        decimal = ((int(i) - b)/a)%n #aplicacion afin inversa para obtener el decimal
        lista_hexadecimal.append(dectohex_rec(int(decimal)))#pasamos el decimal a hexadecimal y se guarda en una lista
    mensaje = hexalist_to_str(lista_hexadecimal)# obtenemos el mensaje
    return mensaje


"""
Ejercicios Practica3
"""
#Funcion que calculará los dos primos cuyo producto es n
def calcula_primos(n):
    p1=nextprime(pow(10,90))#El primer primo es el siguiente a 10^90
    p2= n/p1 #sabemos que n= p1 * p2
    return (p1 , p2)

#Funcion de Euler
def funcion_Euler(primo1,primo2): #Recibe dos primos como parámetros y delvuelve el producto de p-1
    return (primo1-1)*(primo2-1)

#Generación de clave publica e
def calcular_e(euler):
    for i in range(12334, 12345):#Recorro los valores en el rango de valores delimitado anteriormente
        if gcd(euler,i) == 1:#Compruebo el MCD
            print i

#Calculamos la privada en función de la publica
posibles_e=[12335,12337,12341,12343]
def clave_d_privada():
    lista_d=[]
    for i in posibles_e:#Saco la d para cada e
        lista_d.append(gcdex(i,phi)[0]%phi)
    return lista_d

#Funcion para sacar los posibles mensajes para nuestra lista de d
def posibles_mensajes():
    mensaje=[]
    for i in d:#Recorro todas las d candidatas
        for j in mensaje_codificar:#Para cada d recorro la web
            mensaje.append(pow(j,long(i),n))#Veo todos los posibles mensajes y los voy almacenando
    return mensaje

#Funcion que nos convertira el mensaje a hexadecimal pero solo aquellos que tienen longitud par
def dec_to_hex_list(mens):
    listahexadecimal=[]
    for i in mens:#Recorro el mensaje
        hexadecimal = dectohex_rec(i)#Convierto cada i en hexadecimal
        if len(hexadecimal)%2==0:#Compruebo si el tamaño del hexadecimal es par
            listahexadecimal.append(hexadecimal)#Si es par lo añado a la lista de hexadecimales
    return listahexadecimal

#Funcion que nos crea la tabla de Vigenere y nos genera la codificacion
def tablavigenere(pos_inicial,clave, m):
    tablavigenere=[]
    row=[]#FilaAuxiliar
    solucion=""#Iniciamos a palabra vacia
    m=m.upper()#Trabajamos con mayusculas
    clave= clave.upper()#Trabajamos con mayusculas
    for i in range(len(abecedario)): #Recorremos tantas letras como tenga el abecedarios que serán las columnas
        for k in range(pos_inicial+i,len(abecedario)+pos_inicial+i): #Recorro las filas
            row.append(abecedario[k%len(abecedario)])#Voy completando cada fila
        tablavigenere.append(row)#Meto la fila entera
        row = []#La inicializamos a vacio de nuevo la fila
    for j in range(len(m)):#Ahora recorremos el tamaño del mensaje
        for k in tablavigenere:#Recorremos toda la tabla y vemos la comprobación de la palabra y lo metemos en solucion
            if k[0] == clave[j%len(m)]:
                aux=k.index(m[j])
        solucion=solucion+tablavigenere[0][aux]#Vamos añadiendo
    return solucion

"""
Ejercicios Practica4
"""
#Funcion psp(n) con salida (b,true) o (b,false)
def psp(n):
    b=random.randint(1,n-1)#Tomamos una base positiva al alzar y que sea menor que n, ya que n no nos interesa sabemos que si es divisor
    if gcd(b,n)!=1:#Vemos si la base es divisor de n, con el mcd
        print "El MCD("+str(b)+","+str(n)+")="+str(sp.gcd(n,b))
        return (b,False)
    else:#Si MCD= 1 hacemos la otra comprobación
        if pow(b,n-1,n)!=1:#Comprobamos el b^(n-1) =1 %n
            return (b,False)
        else:
            return (b,True)

#Funcion pspKveces recursiva de psp
def pspKVeces(n,k):
    b=0
    for i in range(0,k):#Llamamos a la funcion psp k veces
        recursivo = psp(n)
        b=recursivo[0]#almacenamos la base
        #print str(b) # Si queremos comprobar que hace las k bases
        if not recursivo[1]:# Comprobamos el valor de booleano, si es false lo deolvemos
            return recursivo
    print "Es posible que " +str(n) + " sea primo"
    return (b,True)

#Funcion epsp que le pasamos nuestro n y devuelve una base y booleano
def epsp(n):
    if(n%2==0):#Comprobamos si el numero es par
        print str(n)+" es par"
        return (2,False)
    b=random.randint(2,n-1)#Base al alzar
    if gcd(b,n)!=1:#Si el MCD no es 1
        print str(gcd(n,b)) + " es divisor de " + str(n)
        return (b,False)
    else:#Si MCD es 1 hacemos las comprobaciones
        if pow(b,(n-1)/2,n) == jacobi_symbol(b,n)%n :#Comprobamos la igualdad
            return (b,True)
        else:
            return (b,False)

#Funcion epspKVeces que realiza epsp k veces
def epspKVeces(n,k):
    b= 0
    for i in range(1,k):#Llamamos a la funcion spsp k veces de forma recursiva
        recursivoEuler=epsp(n)
        b= recursivoEuler[0]#Saco la base
        #print str(b)#Comprobar que hace las k bases
        if not recursivoEuler[1]:#Compruebo el valor del booleano, si es falso lo devolvemos
            return recursivoEuler
    print "Es posible que "+str(n)+ " sea primo"
    return (b,True)

#Funcion mpot que nos devuelve la mayor potencia p que divide a m
def mpot(p,m):
    potencia=p#Almacenamos el valor de nuestra potencia
    n_potencias = 0 #Almacenamos el numero de veces que esta la potencia
    while m%potencia == 0:
        n_potencias = n_potencias +1#Aumento el contador
        potencia= potencia*p#Actualizo a la potencia
    return n_potencias

def fpsp(n):
    if n%2==0:#Comprobamos si el numero es par y acabamos
        print str(n)+" es par"
        return(2,False)
    else:#Si el numero es impar
        s=mpot(2,n-1)#Calculamos la mayor potencia ya que el otro numero es impar
        t=(n-1)/pow(2,s)#dividimos n-1 entre la potencia anterior
        base = random.randint(1,n-1) #tomamos la base aleatoria
        if gcd(base,n)!=1:
            print str(gcd(base,n))+" es divisor de "+ str(n)
            return (base,False)
        else:
            if pow(base,t,n)==1 or pow(base,t,n)==(-1%n):#Si es cierto Base^t %n =1
                return(base,True)
            else:
                for i in range(1,s):#Comprobar si para algun i se rerifica la ecuacion
                    if pow(base,t*pow(2,i),n)==(-1%n):
                        #return (i,base,True)
                        return (base,True)
            return(base,False)

def fpspKVeces(n,k):
    bases = []#Almacenamos todas lsa bases que usamos
    for i in range (0,k):#Realizamos las iteraciones
        pseudoprimo = fpsp(n)#Llamamos a la función anterior del ejercicio6
        bases.append(pseudoprimo[0])#Almaceno el valor de la base
        if not pseudoprimo [1]:#Vemos el valor del booleano
            return pseudoprimo
    print " es posible que " + str(n)+" sea primo"
    return(bases, True)
