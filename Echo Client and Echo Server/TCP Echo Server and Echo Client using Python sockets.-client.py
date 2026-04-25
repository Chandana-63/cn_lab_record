import socket

def echo_client():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('127.0.0.1', 65432))

    message = input("Enter message: ")
    client_socket.sendall(message.encode())

    data = client_socket.recv(1024)
    print("Echo from server:", data.decode())

    client_socket.close()


if __name__ == '__main__':
    echo_client()