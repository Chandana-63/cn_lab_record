import socket

c = socket.socket()
c.connect(("127.0.0.1", 12345))

filename = input("Enter file name: ")

c.send(filename.encode())

with open(filename, "rb") as f:
    while True:
        data = f.read(1024)
        if not data:
            break
        c.sendall(data)

print("File sent!")
c.close()