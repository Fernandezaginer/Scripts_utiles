# Script de python para ejecutar un apagado automatico del ordenador
# Util para clases online

import os
import io
import time
import datetime
import pynput
import pyperclip as clipboard



# -----------------------------------------------------------
#                          CONFIG
# -----------------------------------------------------------


# Horas programadas de apagado
# Apagado (hora, min), grabacion, telnet, hora de grabación (hora, min)
APAGADOS = []
APAGADOS.insert(1,['M',19,40,0,0,19,0])
APAGADOS.insert(2,['V',19,5,0,0,19,0])
APAGADOS.insert(3,['L',19,5,0,0,19,0])

# Factor de alumnos para salida de la clase 
factor_alumnos = 0.6




# -----------------------------------------------------------
#                         FUNCIONES
# -----------------------------------------------------------


apagado = 0
numero = -1
n = 0

for i in range(len(APAGADOS)):
    DIAS = ['L','M','X','J','V','S','D']
    for j in range(len(DIAS)):
        if DIAS[j] == APAGADOS[i][0]:
            APAGADOS[i][0] = j+1
    
    

def hora():
    return list(time.localtime())[3]

def minutos():
    return list(time.localtime())[4]

def segundos():
    return list(time.localtime())[5]

def dia():
    fecha=datetime.date.today()
    return fecha.isoweekday()
    
def num_dia():
    return list(time.localtime())[2]

def mes():
    return list(time.localtime())[1]
    
def ano():
    return list(time.localtime())[0]


def numero_alumnos(aa):

    v = 1

    if aa == 0:
        v = 3
       
    # Posicion de 
    raton = pynput.mouse.Controller()
    raton.position = (1302,388)   # Mucho zoom
    #raton.position = (1339,325)  # con invitacion
    #raton.position = (1373,271)  # Poco Zoom
    #raton.position = (1339,284)  # Zoom normal
    #raton.position = (1362,210)  # Sin moderador
    time.sleep(0.3*v)
    
    # doble click
    raton.click(pynput.mouse.Button.left,2)
    time.sleep(0.3*v)
    
    # click derecho
    raton.click(pynput.mouse.Button.right,1)    
    time.sleep(0.6*v)
    
    # mover
    raton.move(21,18)
    time.sleep(0.15*v)    

    # copiar
    raton.click(pynput.mouse.Button.left,1)
    time.sleep(0.1*v)
    
    c = clipboard.paste()
    
    if type(c) == type('ab'):
        c = int(c)
    else:
        c = 0
    
    return c
    


def grabar():
    teclado = pynput.keyboard.Controller()
    mouse = pynput.mouse.Controller()
    
    mouse.position=(193,846)
    time.sleep(0.5)
    
    mouse.click(pynput.mouse.Button.left, 1)
    time.sleep(0.5)
    
    cad = "Xbox Game bar"
    for i in cad:
        teclado.press(i)
        time.sleep(0.07)

    mouse.position=(203,300)
    time.sleep(0.5)
    
    mouse.click(pynput.mouse.Button.left, 1)
    time.sleep(1.5)

    mouse.position=(230,111)
    time.sleep(0.5)

    mouse.click(pynput.mouse.Button.left, 1)
    time.sleep(1.5)

    mouse.position=(702,293)
    time.sleep(0.5)

    mouse.click(pynput.mouse.Button.left, 1)
    time.sleep(0.5)



def abandonar(): 

    '''
    time.sleep(0.25)
    raton = pynput.mouse.Controller()
    #raton.position = (1412,64)
    raton.position = (1480,50)
    time.sleep(0.25)
    raton.click(pynput.mouse.Button.left,1)
    '''
    
    registrar("Incio salida clase")
    
    t = pynput.keyboard.Controller()
    
    print("\a")
    t.press(pynput.keyboard.Key.ctrl)
    t.press(pynput.keyboard.Key.shift)
    t.press('b')    
    time.sleep(0.5)
    t.release('b')
    t.release(pynput.keyboard.Key.shift)
    t.release(pynput.keyboard.Key.ctrl)
    registrar("Fin salida clase")
    
    
def registrar(alm):
    os.chdir("C:\\Users\\mianf\\Z_PROGRAMACION")
    archivo = open("registro.txt", "a")
    cad = str(num_dia()) + "/" + str(mes()) + "/" + str(ano()) + "  "
    cad = cad + str(hora()) + ":" + str(minutos()) + ":" + str(segundos()) + "  "
    cad = cad + str(alm) + '\n'
    archivo.write(cad)
    archivo.close()
    
 
    
def apagar():
    os.chdir("C:\\Users\\mianf\\Z_PROGRAMACION")
    archivo = open( str(hora()) + "_" + str(minutos()) + "_" + str(segundos()) + '_' + str(n) + ".txt","w")
    time.sleep(2)
    archivo.close()
    print("\a")
    for i in range(11):
        os.system("cls")
        os.system("color 04")
        print("Apagado inminiente en",10-i,"segundos")
        print("Cierra esta ventana para cancelar")
        time.sleep(0.5)
        os.system("color 40")
        time.sleep(0.5)

    os.system("shutdown -f -s -t 10")
    registrar("Orden de apagado")

    


    
# -----------------------------------------------------------
#                           MAIN
# -----------------------------------------------------------


os.system("title Programa de apagado automatico")
os.system("color 0A")


for i in APAGADOS:
    fecha=datetime.date.today()
    
    if fecha.isoweekday() == i[0]:
        apagado = 1
        numero = APAGADOS.index(i)
        
    
if apagado == 0:
    print("¡¡NO hay apagado para hoy!!")
    time.sleep(10)


else:

    # Mostrar los carteles
    print("Hora de apagado: ", end="")
    s = str(APAGADOS[numero][1])
    s = s + ":"
    m = APAGADOS[numero][2] if (APAGADOS[numero][2] > 9) else ('0' + str(APAGADOS[numero][2]))
    s = s + str(m)
    s = s + " "
    print(s)

    if APAGADOS[numero][3] == 1:
        print("Inicio  REC:     ", end="")
        s = str(APAGADOS[numero][5])
        s = s + ":"
        m = APAGADOS[numero][6] if (APAGADOS[numero][6] > 9) else ('0' + str(APAGADOS[numero][6]))
        s = s + str(m)
        s = s + " "
        print(s)
    
    print("Grabacion:", 'ON' if APAGADOS[numero][3] == 1 else 'OFF' , " Telnet:",  'ON' if APAGADOS[numero][4] == 1 else 'OFF' )
    
    
    raton = pynput.mouse.Controller()
    while(raton.position[0] < 1214):
        time.sleep(0.1)
    time.sleep(2)
    
    no = numero_alumnos(0)
    n = no
    
    while (no*factor_alumnos < n):
        
        n = numero_alumnos(1)
        registrar(n)
        if n > no:
            no = n
        
        raton = pynput.mouse.Controller()
        i = 0
        
        while (not(raton.position[0] > 1214 and raton.position[1] > 234)):
            i = 1
        if i == 1:
            time.sleep(1)
        
        if (APAGADOS[numero][1] <= hora() and APAGADOS[numero][2] <= minutos()):
            print("Fallo de hora")
            time.sleep(1)
            break

    os.system("cls")
    os.system("color 40")
    print("APAGADO")
    print("Alumnos:", n)
    
    
    abandonar()
    apagar()
    