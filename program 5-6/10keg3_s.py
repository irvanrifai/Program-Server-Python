import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("", 50003))
s.listen(5)
print "Server sudah siap"
perintah = ''
a = 0
while perintah != 'keluar':
    komm, addr = s.accept()
    while perintah != 'keluar':
        data = komm.recv(1024).lower().split("=")
        perintah = data[0]
        if perintah == 'keluar':
            s.close()
            break
        print 'Pesan:', perintah
        if perintah == a :
                L = int(a*a)
                respon = "oke"
                komm.send(respon)
        elif perintah == 'hitung':
            print ('Luas persegi dengan sisi',a,'adalah',L)
            komm.send(respon)
        else:
            komm.send('unknown command')
