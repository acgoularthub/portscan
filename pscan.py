import socket

ip = input("digite o ip/host: ")

ports = []
count = 0

while count <10:
    ports.append(int(input("Porta: ")))
    count +=1


for port in ports:
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.settimeout(0.05)
    code = client.connect_ex((ip, port))

    if code == 0:
        print(str(port), " => Porta Aberta")
    else:
        print(str(port), " => Porta Fechada")

