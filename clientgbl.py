import socket

# Inisialisasi client
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('22.22.22.135', 9999))  # Ganti '127.0.0.1' dengan IP server jika berada di komputer berbeda

# Terima pesan dari server
pesan = client_socket.recv(1024).decode()
print(pesan)

# Kirim pilihan ke server
pilihan = input("Masukkan pilihan (1 = gunting, 2 = batu, 3 = kertas): ")
client_socket.send(pilihan.encode())

# Terima hasil dari server
hasil = client_socket.recv(1024).decode()
print(hasil)

# Tutup koneksi
client_socket.close()
