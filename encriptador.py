import socket
import sys
import threading


claveacceso="klmnEowxCDFGHsgrabcdefijB789[W0,.;:{}XYZ15+*!#$%6hIJRSTKLUpqyzA]&/(tuvVMNOPQ234)=?klmnEowxCDFGHsgrabcdefijB789[W0,.;:{}XYZ15+*!#$%6hIJRSTKLUpqyzA]&/(tuvVMNOPQ234)=?klmnEowxCDFGHsgrabcdefijB789[W0,.;:{}XYZ15+*!#$%6hIJRSTKLUpqyzA]&/(tuvVMNOPQ234)=?klmnEowxCDFGHsgrabcdefijB789[W0,.;:{}XYZ15+*!#$%6hIJRSTKLUpqyzA]&/(tuvVMNOPQ234)=?klmnEowxCDFGHsgrabcdefijB789[W0,.;:{}XYZ15+*!#$%6hIJRSTKLUpqyzA]&/(tuvVMNOPQ234)=?klmnEowxCDFGHsgrabcdefijB789[W0,.;:{}XYZ15+*!#$%6hIJRSTKLUpqyzA]&/(tuvVMNOPQ234)=?klmnEowxCDFGHsgrabcdefijB789[W0,.;:{}XYZ15+*!#$%6hIJRSTKLUpqyzA]&/(tuvVMNOPQ234)=?klmnEowxCDFGHsgrabcdefijB789[W0,.;:{}XYZ15+*!#$%6hIJRSTKLUpqyzA]&/(tuvVMNOPQ234)=?klmnEowxCDFGHsgrabcdefijB789[W0,.;:{}XYZ15+*!#$%6hIJRSTKLUpqyzA]&/(tuvVMNOPQ234)=?klmnEowxCDFGHsgrabcdefijB789[W0,.;:{}XYZ15+*!#$%6hIJRSTKLUpqyzA]&/(tuvVMNOPQ234)=?klmnEowxCDFGHsgrabcdefijB789[W0,.;:{}XYZ15+*!#$%6hIJRSTKLUpqyzA]&/(tuvVMNOPQ234)=?klmnEowxCDFGHsgrabcdefijB789[W0,.;:{}XYZ15+*!#$%6hIJRSTKLUpqyzA]&/(tuvVMNOPQ234)=?klmnEowxCDFGHsgrabcdefijB789[W0,.;:{}XYZ15+*!#$%6hIJRSTKLUpqyzA]&/(tuvVMNOPQ234)=?klmnEowxCDFGHsgrabcdefijB789[W0,.;:{}XYZ15+*!#$%6hIJRSTKLUpqyzA]&/(tuvVMNOPQ234)=?klmnEowxCDFGHsgrabcdefijB789[W0,.;:{}XYZ15+*!#$%6hIJRSTKLUpqyzA]&/(tuvVMNOPQ234)=?klmnEowxCDFGHsgrabcdefijB789[W0,.;:{}XYZ15+*!#$%6hIJRSTKLUpqyzA]&/(tuvVMNOPQ234)=?klmnEowxCDFGHsgrabcdefijB789[W0,.;:{}XYZ15+*!#$%6hIJRSTKLUpqyzA]&/(tuvVMNOPQ234)=?klmnEowxCDFGHsgrabcdefijB789[W0,.;:{}XYZ15+*!#$%6hIJRSTKLUpqyzA]&/(tuvVMNOPQ234)=?klmnEowxCDFGHsgrabcdefijB789[W0,.;:{}XYZ15+*!#$%6hIJRSTKLUpqyzA]&/(tuvVMNOPQ234)=?klmnEowxCDFGHsgrabcdefijB789[W0,.;:{}XYZ15+*!#$%6hIJRSTKLUpqyzA]&/(tuvVMNOPQ234)=?klmnEowxCDFGHsgrabcdefijB789[W0,.;:{}XYZ15+*!#$%6hIJRSTKLUpqyzA]&/(tuvVMNOPQ234)=?klmnEowxCDFGHsgrabcdefijB789[W0,.;:{}XYZ15+*!#$%6hIJRSTKLUpqyzA]&/(tuvVMNOPQ234)=?klmnEowxCDFGHsgrabcdefijB789[W0,.;:{}XYZ15+*!#$%6hIJRSTKLUpqyzA]&/(tuvVMNOPQ234)=?klmnEowxCDFGHsgrabcdefijB789[W0,.;:{}XYZ15+*!#$%6hIJRSTKLUpqyzA]&/(tuvVMNOPQ234)=?" ##El mensaje solo podra ser descifrado por quien tenga la "claveacceso"


dic=claveacceso

def enviar(ip,puertodestino,msg):
    sock = socket.socket(socket.AF_INET, # Internet
                         socket.SOCK_DGRAM) # UDP
    sock.sendto(msg, (ip, puertodestino))



def recibir():
    sock = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM) # UDP
    sock.bind(("", puertoorigen))

    while True:
          data, addr = sock.recvfrom(1024) # buffer size is 1024 bytes
          f=str(data)
          print "                             ",desencriptar(f,clave)



def encriptar(texto,clave):
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

def desencriptar(texto,clave):
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

ip=raw_input("ip: ")
#ip="127.0.0.1"
puertoorigen=int(raw_input("puerto de origen: "))
puertodestino=int(raw_input("puerto de destino: "))
cons=len(puertoorigen)
clave=cons



#msg=raw_input("inicio: ")
#msg=encriptar(msg,clave)
#enviar(ip,puertodestino,msg)

threading.Thread(target=recibir).start()

while True:
      msg=raw_input("> ")  
      msg=encriptar(msg,clave)
      enviar(ip,puertodestino,msg)

