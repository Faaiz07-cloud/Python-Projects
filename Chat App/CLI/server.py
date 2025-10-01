# ---------- Chat App ----------

# Server-Side

# Modules
import socket
import threading

clients = []

def handle_clients(conn, addr):
      print(f"[NEW CONNECTION] {addr} connected.")
      while True:
          try:
             data = conn.recv(1024)
             if not data:
                 break
             print(f"{addr} - {data.decode()}")
             # Broadcast message to all other clients
             for connection in clients:
                 if connection != conn: # skip sender
                     connection.sendall(data)
          except (ConnectionResetError, ConnectionAbortedError, OSError):
                break

      # Remove client if disconnected
      print(f"[DISCONNECTED] {addr}")
      clients.remove(conn)
      conn.close()

def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind(('localhost', 47634))
    server_socket.listen(5)

    print("\n[SERVER STARTED] Waiting for connections...\n")

    while True:
        connection, client_address = server_socket.accept()
        clients.append(connection)
        threading.Thread(target=handle_clients, args=(connection, client_address)).start()

try:
   if __name__ == '__main__':
           start_server()
except KeyboardInterrupt:
           print("\n\nServer Closed...")