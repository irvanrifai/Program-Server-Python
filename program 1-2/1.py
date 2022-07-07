import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("", 50002))
s.listen(5)
print 'Program komunikasi tentang data diri'
data = ''
kamus = {'nama'     : 'Irvan Rifai',
         'NIM'      : 'L200180214',
         'angkatan' : '2018',
         }
while data.lower() !='q' :
    komm, addr = s.accept()
    while data.lower() != 'q':
        data = komm.recv(1024)
        if data.lower()== 'q':
            print('Siap !!!')
            s.close()
            break
        print 'perintah:' , data
        if kamus.has_key(data):
            komm.send(kamus[data])
        else:
                komm.send('maaf perintah tidak di mengerti')
