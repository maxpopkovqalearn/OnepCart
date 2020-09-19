import socket

HOST, PORT = "localhost", 9999
data_to_send = str(input("Давайте отправим ссылку: "))

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
    sock.connect((HOST, PORT))
    sock.sendall(bytes(data_to_send + "\n", "utf-8"))

    received = str(sock.recv(1024), "utf-8")

print("Отправили адрес:     {}".format(data_to_send))
print("Получили заголовки : {}".format(received))
