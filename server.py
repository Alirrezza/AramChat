import socket
import threading


server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

server.bind(('localhost',9898))
server.listen()

clients=[]
names=[]

def broadcast(message,cli):
    if cli:
        message=names[clients.index(cli)]+':'+message
    for client in clients:
            if client!=cli:
                client.send(message.encode())


def handle(cl):
    try:
        while True:
            message=cl.recv(1024)
            #print(message)
            broadcast(message.decode(),cl)
    except:
            cl.close()
            index=clients.index(cl)
            del clients[index]
            message=names[index]+" "+"left the chatrrom"
            print(message)
            broadcast(message,0)
            del names[index]
            


# def write2file():
#     with open("online_users.txt",'w+') as f:
#         for name in names:
#             f.write(name+'\n')


def receive():

    while True:
        
        client,addr=server.accept()
        clients.append(client)
        client.send(b"OK")
        name=client.recv(1024).decode()
        names.append(name)
        print(f"connednt to {addr} name={name}")
        t1=threading.Thread(target=handle,args=(client,))
        t1.start()
        # t2=threading.Thread(target=write2file) 
        # t2.start()
       


receive()


