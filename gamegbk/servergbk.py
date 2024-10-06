import socket

def tentukan_pemenang(pemain):
    # {'muhsin':'batu','idris':'kertas','muhajir':'batu'}
    # Aturan permainan
    aturan = {
        'gunting': 'kertas',
        'kertas': 'batu',
        'batu': 'gunting'
    }
    
    # Mencari nilai unik dari pilihan pemain
    pilihan_unik = set(pemain.values())
    
    # mengecek apakah hasil seri
    if (len(pilihan_unik) == 1) or (len(pilihan_unik) > 2):
        return False,False
    
    # Menentukan pilihan yang menang
    menang = None
    for pilihan in pilihan_unik:
        lawan = [p for p in pilihan_unik if p != pilihan][0]
        # print(lawan)
        if aturan[pilihan] == lawan:
            menang = pilihan
            break
    
    # Menentukan pemenang berdasarkan pilihan yang menang
    pemenang = [nama for nama, pilihan in pemain.items() if pilihan == menang]
    return pemenang,menang

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('0.0.0.0', 9999))
server_socket.listen(30)
server_socket.settimeout(20)
pemain = []
while True:
    try:
        print('fas')
        conn, addr = server_socket.accept()
        pemain.append((conn,addr))
        print(f"Pemain 1 terhubung dari {addr}")
        print(len(pemain))
    except:
        break
print("permainan sudah di mulai, menuggun balasan pemain")
for conn,_ in pemain:
    conn.send(b'nama')
listpemain = {}
print(listpemain)
for conn,_ in pemain:
    nama = conn.recv(1024).decode()
    listpemain.update({nama:conn})
for conn,_ in pemain:
    conn.send(b'\tList Player\n * '+b'\n * '.join( x.encode() for x in listpemain.keys()))
full = listpemain
while True:
    GbkUser = {}
    print(GbkUser)
    for nama,conn in listpemain.items():
        gbk = conn.recv(1024).decode()
        GbkUser.update({nama:gbk})
    print(GbkUser)
    hasil,menang = tentukan_pemenang(GbkUser)
    if not hasil:
        for nama,conn in listpemain.items():
            conn.send(b'HASIL SERI, LANJUTKAN BERMAIN')
        continue
    if len(hasil)==1:
        for nama,conn in full.items():
            conn.send(b'SELAMAT '+hasil[0].encode()+b' MEMENANGAN PERMAINAN')
        conn.close()
        break
    for nama,conn in listpemain.items():
        conn.send(b'LIST PEMAIN LOLOS ('+menang.encode()+b')\n * '+b'\n * '.join(x.encode() for x in hasil))
    lis = {}
    
    if hasil and len(hasil)>=2:
        for x in hasil:
            lis.update({x:listpemain[x]})
            listpemain[x].send(b'Kamu lolos ke babak selanjutnya!!!')
    elif len(hasil)==2:
        for x in hasil:
            lis.update({x:listpemain[x]})
            listpemain[x].send(b'kamu lolos ke babak final!!!')

    listpemain = lis



        



# print(tentukan_pemenang({'muhsin':'batu','idris':'gunting','muhajir':'batu'}))