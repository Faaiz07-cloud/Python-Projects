# ---------- Chat App ----------

# Client-Side

# Modules
import socket
import threading

def receive_messages(sock):
    while True:
               try:
                   data = sock.recv(1024)
                   if data:
                       print(data.decode())
               except (ConnectionResetError, ConnectionAbortedError, OSError):
                   print("Disconnected from server.")
                   sock.close()
                   break

def start_client():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('localhost', 47634))

    print("\nConnected to chat server. Type messages and press Enter to send.")

    thread = threading.Thread(target=receive_messages, args=(client_socket,), daemon=True)
    thread.start()

    while True:
          msg = input()
          if msg.lower() == 'quit':
              client_socket.close()
              break
          else:
              client_socket.sendall(msg.encode())

try:
    if __name__ == "__main__":
        start_client()
except KeyboardInterrupt:
    print("\n\nClient Exit...")