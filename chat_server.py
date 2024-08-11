import socket
import threading

def handle_client(client_socket, client_address):
    print(f"Client {client_address} connected.")
    client_socket.send("Welcome to the chat!".encode('utf-8'))
    while True:
        message = client_socket.recv(1024).decode('utf-8')
        if message:
            print(f"Client {client_address}: {message}")
        else:
            break
    client_socket.close()

def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('localhost', 9999))
    server_socket.listen(5)
    print("Server started and listening for connections...")

    while True:
        client_socket, client_address = server_socket.accept()
        client_thread = threading.Thread(target=handle_client, args=(client_socket, client_address))
        client_thread.start()

if __name__ == "__main__":
    start_server()