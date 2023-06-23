import socket

host = '10.9.64.161'  
port = 8877

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, port))

while True:
    command = input("Enter command (or 'quit' to exit): ")
    s.sendall(command.encode())
    
    if command == "quit":
        break

    response = s.recv(4096).decode()
    print("Output from server:")
    print(response)

s.close()
