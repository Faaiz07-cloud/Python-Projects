# ----- Basic Client - Server Communication using TCP Protocol -----

# Server-Side

# Module
import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
# SO_REUSEADDR allows immediate reuse of a recently used port (in TIME_WAIT) to avoid
# bind errors during rapid server restarts.
server_socket.bind(("localhost", 12345))

server_socket.listen()

print("\nServer Listening. Waiting for a connection...")

client_socket, client_address = server_socket.accept()
print("\nClient Connected: ", client_address)

data = client_socket.recv(1024)
print(f"\nReceived from Client: {data.decode()}")

client_socket.send(b"Hello! You are now successfully connected to the server.")

server_socket.close()

