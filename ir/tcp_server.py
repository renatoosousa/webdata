import socket
import json
from ir import IR

# Processamneto aqui


HOST = '127.0.0.1'
PORT = 8484
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(2)

score = IR()
conn1, addr1 = s.accept()
print 'Connected by', addr1

while 1:
    try:
        data = conn1.recv(1024)
    except socket.error:
        print ''
    if data:
    	obj = data.decode('utf-8')
    	obj_json = json.loads(obj)
        print obj_json['cidade']

        #Rankeamento aqui
        score.setRequest(data)
        score.ranking()
        data = score.getInfo() #pode passar como parametro o numero de docs retornados

        conn1.send('data')