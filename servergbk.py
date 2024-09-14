import socket

# Fungsi untuk menentukan pemenang
def tentukan_pemenang(player1, player2):
    if player1 == player2:
        return "Seri!"
    elif (player1 == 'gunting' and player2 == 'kertas') or \
         (player1 == 'batu' and player2 == 'gunting') or \
         (player1 == 'kertas' and player2 == 'batu'):
        return "Player 1 menang!"
    else:
        return "Player 2 menang!"

# Inisialisasi server
print(socket.AF_INET,socket.SOCK_STREAM)
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print(server_socket)
server_socket.bind(('0.0.0.0', 9999))
server_socket.listen(2)  # Server menunggu dua pemain

print("Menunggu dua pemain terhubung...")

# Menerima koneksi dari dua pemain
conn1, addr1 = server_socket.accept()
print(f"Pemain 1 terhubung dari {addr1}")

conn2, addr2 = server_socket.accept()
print(f"Pemain 2 terhubung dari {addr2}")

# Mengirim pesan bahwa game siap dimulai
conn1.send(b"Siap bermain! Pilih: 1 = gunting, 2 = batu, 3 = kertas")
conn2.send(b"Siap bermain! Pilih: 1 = gunting, 2 = batu, 3 = kertas")

# Menerima pilihan dari kedua pemain
pilihan1 = int(conn1.recv(1024).decode().strip()) - 1
pilihan2 = int(conn2.recv(1024).decode().strip()) - 1

# Daftar pilihan GBK
listGBK = ['gunting', 'batu', 'kertas']

# Mengambil pilihan pemain
player1_choice = listGBK[pilihan1]
player2_choice = listGBK[pilihan2]

# Tentukan pemenang
hasil = tentukan_pemenang(player1_choice, player2_choice)

# Kirim hasil ke kedua pemain
conn1.send(f"Hasil: Player 1 memilih {player1_choice}, Player 2 memilih {player2_choice}. {hasil}".encode())
conn2.send(f"Hasil: Player 1 memilih {player1_choice}, Player 2 memilih {player2_choice}. {hasil}".encode())

# Tutup koneksi
conn1.close()
conn2.close()
server_socket.close()
