import os
import re
import json

class Reader_for_logs:

    def __init__(self, file_name):
        self.file_name = file_name
        self.logs = []
        self.conversion_ip = {}
        self.number_of_get = 0
        self.number_of_post = 0
        self.all_req = 0

    def read_file(self):
        # Чтение и подготовка данных
        regex = '([(\d\.)]+) - - \[(.*?)\] "(.*?)" (\d+)'
        with open(self.file_name, 'r', encoding='UTF-8') as file_log:
            for lines in file_log:
                self.all_req += 1
                access_list = re.match(regex, lines).groups()
                if 'GET' in access_list[2]:
                    self.number_of_get += 1
                elif 'POST' in access_list[2]:
                    self.number_of_post += 1
                self.logs.append(access_list)
                self.conversion_ip[access_list[0]] = 0

            print("Всего запросов:", self.all_req, "\nВсего запросов GET:", self.number_of_get,
                  "\nВсего запросов POST:", self.number_of_post)

    def run(self):
        # Запуск парсинга
        self.read_file()

    def parser_ip(self):
        # пасирнг по IP
        for key in self.conversion_ip:
            for key_log in self.logs:
                if key in key_log:
                    self.conversion_ip[key] += 1
        print(self.conversion_ip)

    def write_json(self):
        to_json = {'POST': self.number_of_post, 'GET': self.number_of_get, 'ALL': self.all_req, 'IP': self.conversion_ip}
        with open('request.json', 'w') as f:
            json.dump(to_json, f, sort_keys=False, indent=2)

def find(name_file, path):
    for root, dirs, files in os.walk(path):
        if name_file in files:
            return os.path.join(root, name_file)

path = 'C:\\logs'
file_name = 'access.txt'
file=find(name_file=file_name, path=path)
#Специально заменил чтобы "отлаживать", но работает и с указанием по путу
log = Reader_for_logs(file_name='access.txt')
log.run()
log.parser_ip()
log.write_json()