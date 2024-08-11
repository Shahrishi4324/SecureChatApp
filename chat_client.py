import socket
import threading
from cryptography.fernet import Fernet

def receive_messages(client_socket, cipher):
    while True:
        try:
            message = client_socket.recv(1024)
            if message:
                decrypted_message = cipher.decrypt(message).decode('utf-8')
                print(f"\nServer: {decrypted_message}")
            else:
                break
        except:
            break

def start_client():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('localhost', 9999))
    
    key = client_socket.recv(1024)
    cipher = Fernet(key)
    
    receive_thread = threading.Thread(target=receive_messages, args=(client_socket, cipher))
    receive_thread.start()
    
    while True:
        message = input("You: ")
        if message.lower() == 'exit':
            break
        encrypted_message = cipher.encrypt(message.encode('utf-8'))
        client_socket.send(encrypted_message)
    
    client_socket.close()

if __name__ == "__main__":
    start_client()