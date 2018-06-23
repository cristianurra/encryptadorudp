import socket
dic="abcdefghijklmnopqrstuvwxyz1234567890,.;:{}[]+*!#$%&/()=?abcdefghijklmnopqrstuvwxyz1234567890,.;:{}[]+*!#$%&/()=?abcdefghijklmnopqrstuvwxyz1234567890,.;:{}[]+*!#$%&/()=?"

def enviar(ip,puerto,msg):
    sock = socket.socket(socket.AF_INET, # Internet
                         socket.SOCK_DGRAM) # UDP
    sock.sendto(msg, (ip, puerto))



def recibir(ip,puerto):
    sock = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM) # UDP
    sock.bind((ip, puerto))


    data, addr = sock.recvfrom(1024) # buffer size is 1024 bytes
    f=str(data)
    print encriptar(f,-clave)



def encriptar(texto,clave):
    l=list(texto)
    n=0
    while n<len(l):
          k=dic.find(l[n])
          if l[n]==" ":
             l[n]=" "
          if l[n]!=" ":
             l[n]=dic[k+int(clave)]
          n+=1
    f="".join(l)
    return f

ip=raw_input("ip: ")
ip="127.0.0.1"
puertoorigen=int(raw_input("puerto de origen: "))
puertodestino=int(raw_input("puerto de destino: "))
clave=int(raw_input("Clave: "))



msg=raw_input("inicio: ")
msg=encriptar(msg,clave)
enviar(ip,puertodestino,msg)


while True:
      recibir(ip,puertoorigen)

      msg=raw_input("Texto: ")
      msg=encriptar(msg,clave)
      enviar(ip,puertodestino,msg)

