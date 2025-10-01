# ----- Basic Client - Server Communication using TCP Protocol -----
# ----- Sockets in non-blocking Mode -----

# Server-Side

# Module
import socket
import time

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.setblocking(False) # Now non-blocking mode is ON
server_socket.bind(('localhost', 57535))

server_socket.listen(1)
print("\nServer Listening......")

try:
    while True:
        try:
            conn, addr = server_socket.accept()
            print(f"\nConnected by: {addr}")
            # break # if you want only one client-connection
        except BlockingIOError:
            print("\nNo new connections yet...")
        time.sleep(3)
except KeyboardInterrupt:
    print("Closing server...")
finally:
    server_socket.close()

