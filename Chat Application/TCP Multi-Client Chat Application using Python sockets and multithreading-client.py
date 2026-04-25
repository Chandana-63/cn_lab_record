import socket, threading

def receive(c):
    while True:
        try:
            msg = c.recv(1024)
            if not msg:
                break
            print(msg.decode())
        except:
            break

c = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
c.connect(("127.0.0.1", 55555))

threading.Thread(target=receive, args=(c,), daemon=True).start()

while True:
    msg = input()
    c.sendall(msg.encode())