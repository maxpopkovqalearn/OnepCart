import socketserver
import json
import requests


class MyTCPHandler(socketserver.BaseRequestHandler):
    # Описываем "стандартный" сервер для получения http запроса
    def handle(self):
        self.data = self.request.recv(1024).strip()
        print("{} wrote:".format(self.client_address[0]))
        print(self.data)
    # Получаем заголовки и переводим формат
        header = dict(requests.get(self.data).headers)
        data = json.dumps(dict(header))
        self.request.sendall(data.encode("utf-8"))

if __name__ == "__main__":
    #Запуск сервера
    HOST, PORT = "localhost", 9999
    server = socketserver.TCPServer((HOST, PORT), MyTCPHandler)
    server.serve_forever()