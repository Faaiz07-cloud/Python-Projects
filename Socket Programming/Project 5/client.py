# ----- Basic Client - Server Communication using TCP Protocol -----
# ----- Sockets in non-blocking Mode -----

# Client-Side

# Module
import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('localhost', 57535))