# ----- Basic Client - Server Communication using TCP Protocol -----
# ----- Multi-clients with same server (use Threading) -----
# ----- Server sends the same message to all clients -----

# Client-Side

# Module
import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('localhost', 13351))

data = client_socket.recv(1024)
print(f"\nReceived from Server: {data.decode()}")

client_socket.sendall(b"This is Client 3. I'm Good.")

data2 = client_socket.recv(1024)
print(f"\nReceived from Server: {data2.decode()}")

client_socket.close()
