# ----- Basic Client - Server Communication using TCP Protocol -----
# ----- Multi-clients with same server (use Threading) -----
# ----- Server sends different messages to each client -----

# Client-Side

# Module
import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('localhost', 13346))

data = client_socket.recv(1024)
print(f"\nReceived from Server: {data.decode()}")

client_socket.sendall(b"This is Client 2. Very Well.")

data2 = client_socket.recv(1024)
print(f"\nReceived from Server: {data2.decode()}")

data3 = client_socket.recv(1024)
print(f"\nReceived from Server: {data3.decode()}")

client_socket.sendall(b"Yes I'm Client 2.")

client_socket.close()
