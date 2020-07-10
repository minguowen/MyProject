from socket import *  
  
HOST = '127.0.0.10'  
PORT = 21546  
BUFSIZE = 1024

ADDR = (HOST, PORT)  

tcpCliSock = socket(AF_INET, SOCK_DGRAM)  
 
while True:   
    data = input('> ')
    
    if not data:  
        break
    
    tcpCliSock.sendto(('%s\r\n' % data).encode(), ADDR)  
    data,addr = tcpCliSock.recvfrom(BUFSIZE)
    
    if not data:  
        break
    
    print(data.decode().strip())
    
tcpCliSock.close() 
