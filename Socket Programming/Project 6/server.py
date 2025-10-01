# ----- Basic Client - Server Communication using TCP Protocol -----
# ----- Multi-clients with same server (use Threading) -----
# ----- Server sends different messages to each client -----

# Server-Side

# Module
import socket
import threading

def handle_clients(conn, addr):
     print('Connected by:', addr, flush=True)
     conn.sendall(b'Hello, client! How are you?')
     data = conn.recv(1024)
     print(f'Received from Client {addr}: {data.decode()}')
     conn.sendall(b'Do you need help?')
     client_name = data.decode()
     if "client 1" in client_name.lower():
         conn.sendall(b'Client 1')
     elif "client 2" in client_name.lower():
         conn.sendall(b'Client 2')
     elif "client 3" in client_name.lower():
         conn.sendall(b'Client 3')
     data2 = conn.recv(1024)
     print(f'Received from Client {addr}: {data2.decode()}')
     conn.close()

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind(('localhost', 13346))
server_socket.listen(3)

print("\nServer Listening! Waiting for connections....\n")

try:
   while True:
      connection, client_address = server_socket.accept()
      threading.Thread(target=handle_clients, args=(connection, client_address)).start()
except KeyboardInterrupt:
    print('\nClosing connections....')
finally:
     server_socket.close()







