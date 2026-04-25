import socket

s = socket.socket()
s.bind(("127.0.0.1", 12345))
s.listen(1)

print("Server waiting...")

c, addr = s.accept()
print("Connected:", addr)

filename = c.recv(1024).decode()

with open("received_" + filename, "wb") as f:
    while True:
        data = c.recv(1024)
        if not data:
            break
        f.write(data)

print("File received!")
c.close()