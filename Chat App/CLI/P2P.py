# ---------- Chat App  ----------

# P2P

# Modules
import socket
import threading

def receive_messages(sock):
    while True:
       try:
           data = sock.recv(1024)
           print(f"\rClient>>>: {data.decode()}\nYou>>> ", end="", flush=True)
       except (ConnectionResetError, ConnectionAbortedError, OSError):
           print(f"\n\n[Client Disconnected]")
           sock.close()
           break

def start_as_client():
     client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
     try:
        client_socket.connect(('localhost', 54356))
        print('\nClient connected\n')
        return client_socket
     except (ConnectionResetError, ConnectionAbortedError, OSError):
         return None

def start_as_server():
     server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
     server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
     server_socket.bind(('localhost', 54356))

     server_socket.listen(2)
     print('\n[ONLINE]\n')

     conn, addr = server_socket.accept()
     print('Client connected\n')
     return conn

def main():
    sock = start_as_client()
    if not sock:
       sock = start_as_server()

    thread = threading.Thread(target=receive_messages, args=(sock,), daemon=True)
    thread.start()

    while True:
        msg =input("You>>> ")
        sock.send(msg.encode())

if __name__ == '__main__':
    print("\n---------- Chat App ---------- ")
    main()