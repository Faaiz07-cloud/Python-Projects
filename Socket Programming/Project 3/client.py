# ----- Basic Client - Server Communication using UDP Protocol -----

# Client-Side

# Module
import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

client_socket.sendto(b'Hello Server, This is Client.', ('localhost', 12346))

data, server_address = client_socket.recvfrom(1024)
print("\nClient Received:", data.decode())

client_socket.sendto(b'Hey Server, can you have some time.', server_address)

data2, server_address = client_socket.recvfrom(1024)
print("\nClient Received:", data2.decode())

client_socket.close()