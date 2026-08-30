import socket

ip = input("Enter target ip address : ")
port = int(input("Enter maximum port number to scan : "))

for i in range(1,port+1):
    sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    sock.settimeout(1)
    result = sock.connect_ex((ip,i))
    if result == 0:
        with open("result.txt" , "a") as f:
            f.write(f"Port {i} is OPEN\n")
    else:
        pass
    sock.close()

with open("result.txt" , "r") as f:
    print(f.read())