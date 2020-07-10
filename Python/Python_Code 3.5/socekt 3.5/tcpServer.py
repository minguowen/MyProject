# Echo server program  
from socket import *  
from time import ctime  
  
HOST = '127.0.0.1'                 # Symbolic name meaning all available interfaces  
PORT = 50007              # Arbitrary non-privileged port  
BUFSIZE = 1000  
ADDR = (HOST, PORT)  
  
tcpSerSock = socket(AF_INET, SOCK_STREAM) 
'''
socket.AF_INET表示创建一个IP套接字；socket.SOCK_STREAM 表示流式socket , for TCP
sock_DGRAM表示数据报式socket , for UDP
''' 

tcpSerSock.bind(ADDR)  
'''
服务器必须用socket包中的两个方法来建立网络连接，
第一个是socket.socket，它会创建一个空的套接字；
第二个是bind会绑定（监听这个IP地址和端口的所有数据）到这个套接字上
'''

tcpSerSock.listen(5)  
'''
表示最多可以和5个客户端连接，超过5个就会拒绝
'''
  
while True:  
    print('waiting for connection...')  
	
    tcpCliSock, addr = tcpSerSock.accept() 
	'''
	调 用accept方法时，socket会时入“waiting”状态。客户请求连接时，方法建立连接并返回服务器。
	accept方法返回一个含有两个元素的 元组(connection,address)。
	第一个元素connection是新的socket对象，服务器必须通过它与客户通信；
	第二个元素 address是客户的Internet地址
	'''
    print('...connected from:', addr)  
  
    while True:  
        data = tcpCliSock.recv(BUFSIZE).decode() 
		'''
		指定最大可以接受消息长度为1000字节
		'''
		
        if not data:  
            break  
        tcpCliSock.sendall(('[%s] %s' % (ctime(), data)).encode())  
  
    tcpCliSock.close()  
tcpSerSock.close()  
