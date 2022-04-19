# Programa en el que el computador selecciona un número al azar y luego hay que adivinarlo
import random
import os
import time as t
from datetime import datetime

# Función para limpiar y dar un delay de tiempo entre mensajes en la consola
# {param} segundos int
def limpiarPantalla(segundos):
    t.sleep(segundos)
    os.system('cls')

# Función que valida el formato de números dependiendo la operación realizada 
# {param} valor int
# {param} operacion int
# {return} boolean
def validarNumero(valor, operacion):
    valida = False

    # Diccionario de datos simulando sentencia SWITCH
    op_switch = {
        1 : 'rango',
        2 : 'adivinar',
    }

    msg_error = {
        1 : 'ERROR : El rango debe ser mayor a 0',
    }


    opcion = op_switch.get(operacion)

    try:
        valor = int(valor)

        if(opcion == 'rango'):
            if(valor > 0): return True
            print(msg_error.get(1))
            limpiarPantalla(2)
        elif(opcion == 'adivinar'): return True

    except:
        print('Valor inválido!')
        limpiarPantalla(2)
        print('El valor debe ser Númerico')
        limpiarPantalla(2)

    return valida

    
# Función que retorna un número random
# {return} int
def generarRandom():
    valor = input('¿ Hasta que número puedo elegir ? ')
    valida = validarNumero(valor,1)
    while valida == False:
        valor = input('¿ Hasta que número puedo elegir ? ')
        valida = validarNumero(valor,1)
    return random.randrange(int(valor))


# Función que compara el número generado random con el Input del usuario
# {param} elegido int
# {param} pensado int
def adivinarNumero(elegido,pensado):
    # Creo un archivo
    archivo = crearArchivo()
    while elegido != pensado: #inicio el ciclo de comparación
        elegido = input("Adivine que número elegí :  ")
        if(validarNumero(elegido,2)):
            elegido = int(elegido)
            limpiarPantalla(1)
            if(archivo != None):
                if pensado > elegido:
                    print ("el número que pensé es mayor ")
                    limpiarPantalla(1)
                if pensado < elegido:
                    print ("el número que pensé es menor ")
                    limpiarPantalla(1)
                # Guardamos en un archivo txt el número elegido
                guardarIntento(elegido,archivo)
        else:
            elegido = -2
    mensajeGanar(elegido)

# Función que guarda en un archivo el registro de intentos
# {param} numero int
def guardarIntento(numero,nombre):
    archivo = open(nombre,'a') # Abro el archivo para escritura
    archivo.write(str(numero) + '\n') #\ interpretalo pero no lo leas #\n salto de linea 
    archivo.close() # Cierra el archivo

# Función que valida si existe el archivo ingresado y si no existe lo crea
# {param} nombre string
# {return} boolean
def validarArchivo(nombre):
    try:
        open(nombre,'x') 
        return True
    except:
        return False

# Función que crea un archivo y retorna el nombre del mismo
# {return} string or Null
def crearArchivo():
    fechaActual = datetime.now()
    nombre = './registro/juego-' + datetime.strftime(fechaActual, '%d-%m-%Y-%H-%M-%S') + '.txt'
    if(validarArchivo(nombre)):
        return nombre
    else:
        return None


# Función que muestra un mensaje al usuario cuando gana
# {param} pensado int
def mensajeGanar(pensado):
    print ("Acertó!!! el número que pensé es : ", pensado)
    print ("Ganó, felicitaciones!!!")

# Función principal para ejecutar el Juego
def jugar():
    adivinarNumero(int(-2), generarRandom())

jugar()