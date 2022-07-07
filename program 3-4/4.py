import socket
import platform
hostname = 'localhost'
pesan =''
s= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((hostname,50015))
print 'Program komunikasi tentang server'
while pesan.lower() !='q' :
    pesan = raw_input('Command: ')
    s.send(pesan)
    if pesan.lower()=='quit':
            s.close()
            break
    elif pesan.lower() !='q':
        response =s.recv(1024)
        print 'command:' , response
s.close()
