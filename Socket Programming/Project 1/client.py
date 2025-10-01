# ----- Basic Client - Server Communication using TCP Protocol -----

# Client-Side

# Module
import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('localhost', 12345))

client_socket.send(b"Hello Server! This is client. Waiting for connection.")

data = client_socket.recv(1024)
print(f"\nReceived from Server: {data.decode()}")

client_socket.close()



