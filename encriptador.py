import socket
import sys
import threading

claveacceso="klmnEowxCDFGHsgrabcdefijB789[W0,.;:{}XYZ15+*!#$%6hIJRSTKLUpqyzA]&/(tuvVMNOPQ234)=?" ##El mensaje solo podra ser descifrado por quien tenga la "claveacceso", la que corresponde a todo el conjunto de caracteres, pero desordenados. Lo importante es que sea la misma en ambos usuarios.

n=0
while n<7:
      claveacceso=claveacceso+claveacceso
      n+=1

dic=claveacceso

def enviar(ip,puertodestino,msg):                                        #Funcion para enviar data a travez de UDP
    sock = socket.socket(socket.AF_INET, # Internet
                         socket.SOCK_DGRAM) # UDP
    sock.sendto(msg, (ip, puertodestino))



def recibir():                                                          #Funcion para recibir data a travez de UDP.
    sock = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM) # UDP
    sock.bind(("", puertoorigen))
    usuariodestinatario=""
    while True:
          data, addr = sock.recvfrom(1024) # buffer size is 1024 bytes
          f=str(data)
          tx=desencriptar(f,clave)
          print ip,":",tx



def encriptar(texto,clave):               ##Funcion de encriptado, para encriptar el texto antes de enviarlo.
    l=list(texto)
    n=0
    j=1
    while n<len(l):
          k=dic.find(l[n])
          if l[n]==" ":
             l[n]=" "
          if l[n]!=" ":
             l[n]=dic[k+int(clave+j)]
          j+=clave
          n+=1
    f="".join(l)
    return f

def desencriptar(texto,clave):            ##Funcion desencriptado, proceso inverso del encriptado (notese que la funcion es casi la misma)
    l=list(texto)
    n=0
    j=1
    while n<len(l):
          k=dic.find(l[n])
          if l[n]==" ":
             l[n]=" "
          if l[n]!=" ":
             l[n]=dic[k-int(clave+j)]
          j+=clave
          n+=1
    f="".join(l)
    return f

print "==========Proyecto redes de computadores==========="
print "=====================Elo322========================"
print "Datos de destinatario: ip_destino puerto_origen puerto_destino"  
accion=raw_input(">>> ")   #Aqui el usuario ingresa los valores solicitados, separados por un espacio.
datass=accion.split()
ip=datass[0]
puertoorigen=int(datass[1])
puertodestino=int(datass[2])
clave=len(str(puertoorigen))


threading.Thread(target=recibir).start()    #Permite enviar mensajes, al mismo tiempo que se escucha el socket asociado al perto indicado, para recibir.
while True:
      msg=raw_input("")  
      msg=encriptar(msg,clave)
      enviar(ip,puertodestino,msg)
