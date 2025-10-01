# ----- Basic Client - Server Communication using UDP Protocol -----

# Server-Side

# Module
import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind(('localhost', 12346))

print('\nServer Listening....')

data , client_address = server_socket.recvfrom(1024)
print('\nServer Received:', data.decode())

server_socket.sendto(b'Hello Client!', client_address)

data2, client_address = server_socket.recvfrom(1024)
print('\nServer Received:', data2.decode())

server_socket.sendto(b'Yeah, Tell Me.', client_address)

server_socket.close()
