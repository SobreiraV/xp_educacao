import socket # permite fazer conexões de ip e porta
import os # interagir com o sistema operacional
import ipaddress # permite manipular informações de rede como host, endereço



net_input = input("\nInforme a rede. (Exemplo: 192.168.200.0/24): ") # Armazena o ip que o usuário passar
net = ipaddress.ip_network(net_input) # Usa o ip do alvo na função ip_network e armazena o resultado em net
hosts = [str(ip) for ip in net.hosts()] # Captura os possiveis hosts na rede amarazenada na variavel net

print("\nHosts possiveis: {}".format(len(hosts))) # {} estão associadas a estrutura .format(...)

ports = [80, 443, 1194, 53, 22, 21, 8080] # portas alvos
live_hosts = [] # hosts que forem encontrados ativos

try:
    for h in hosts: # Para cada host dentro de hosts
        response = os.system("ping -c 1 -w 1 "+h+">/dev/null") # -c = 1 ping -W = 1 segundo | >/dev/null apaga dados desnecessários
        if response == 0:
            print("Host {} => up!".format(h))
            live_hosts.append(h)
        else:
            print("Host {} => down!".format(h))
    
    print ("\nHosts verificados: {}".format(len(live_hosts)))
    print ("\nIniciando Scanner...")
    print(hosts)
    
    for ip in live_hosts:
        print("\nScanner do Host: "+ip)
        for p in ports:
            s = socket.socket()
            result = s.connect_ex((ip,p)) # alvo IP e porta a ser testada P
            s.close() # fecha o socket
            if result == 0:
                print("Porta {} => Aberta".format(p))
            else:
                print("Host {} => Fechada".format(p))

except KeyboardInterrupt:
    print("\n\nInterrompido pelo usuário")
