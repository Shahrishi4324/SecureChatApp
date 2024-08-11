import socket

def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('localhost', 9999))
    server_socket.listen(5)
    print("Server started and listening for connections...")

    while True:
        client_socket, client_address = server_socket.accept()
        print(f"Client {client_address} connected.")
        client_socket.send("Welcome to the chat!".encode('utf-8'))
        while True:
            message = client_socket.recv(1024).decode('utf-8')
            if message:
                print(f"Client {client_address}: {message}")
            else:
                break
        client_socket.close()

if __name__ == "__main__":
    start_server()