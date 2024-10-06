import socket
# socket.AddressInfo()
def start_client():
    # Koneksi ke server
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('22.22.22.97', 9999))  # Ganti dengan IP server jika tidak lokal

    print("Terhubung ke server. Menunggu permainan dimulai...")
    pesan = client_socket.recv(1024).decode()
    nama = input('Nama kamu : ')
    client_socket.send(nama.encode())
    listpemain = client_socket.recv(1024).decode()
    print('#'*30)
    print(listpemain)
    while True:
        print('#'*30)
        print('\tATURAN MAIN')
        print(' 1 = gunting\n 2 = batu\n 3 = kertas')
        gbk = ['gunting', 'batu', 'kertas']
        pilih = int(input('Pilih (1 / 2 / 3) lalu enter : ').strip())
        client_socket.send(gbk[pilih-1].encode())
        print('')
        p = client_socket.recv(1024).decode()
        print(p)
        if 'HASIL SERI' in p:
            continue
        client_socket.send(b'')
        hasil = client_socket.recv(1024).decode()
        if not 'Kamu lolos' in hasil:
            break
        
        print(hasil)
        client_socket.send(b'')

if __name__ == "__main__":
    start_client()
