import socket
s = socket.socket()
portas = [80,443,1194,53,22,21]
for p in portas:
    if(s.connect_ex(("127.0.0.1",p)) == 0):
        print ("Porta "+str(p)+" aberta")
    else:
        print ("Porta "+str(p)+" fechada")
