

import socket
import threading



host='127.0.0.1'
port=12345
server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind((host,port))
server.listen()
clients=[]
names=[]

def broadcast(message):
    for client in clients:
        client.send(message)

def handle_client(client):
    while True:
        try:
            message=client.recv(1024)
            broadcast(message)
        except:
            index=clients.index(client)
            clients.remove(index)
            client.close()
            name=names[index]
            broadcast(f"{name} has left chat".encode('utf-8'))
            names.remove(name)
            break
def recive():
    while True:
        print("server has started")
        client,address=server.accept()
        print(f'connected address= {str(address)}')
        client.send('alias'.encode('utf-8'))
        alias=client.recv(1024)
        names.append(alias)
        clients.append(client)
        print(f'{alias} has joined the chat')
        broadcast(f'{alias} has joined the chat'.encode('utf-8'))
        client.send('you have joined'.encode('utf-8'))
        thread=threading.Thread(target=handle_client,args=(client,))
        thread.start()

if __name__=='__main__':
    recive()
