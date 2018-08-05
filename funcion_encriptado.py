claveacceso="klmnEowxCDFGHsgrabcdefijB789[W0,.;:{}XYZ15+*!#$%6hIJRSTKLUpqyzA]&/(tuvVMNOPQ234)=?" ##El mensaje solo podra ser descifrado por quien tenga la "claveacceso"

n=0
while n<7:
      claveacceso=claveacceso+claveacceso
      n+=1

dic=claveacceso

clave=4
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

while True:
      texto=raw_input(">: ")
      print encriptar(texto,clave)
