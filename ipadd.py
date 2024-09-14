# def hitung_ip(ip_address, prefix_length):
#     ip_parts = ip_address.split('.')
#     binary_string = ''
#     for _ in range(prefix_length):
#         binary_string += '1'
#     binary_string = binary_string.ljust(32, '0')
    
#     binary_parts = []
#     for i in range(0, len(binary_string), 8):
#         binary_parts.append(binary_string[i:i+8])
#     binary_parts = '.'.join(binary_parts)
#     print('Binear\t\t: ' + binary_parts)
    
#     non_zero_binary_parts = binary_parts.replace('0', '').split('.')
#     non_zero_binary_parts = list(filter(None, non_zero_binary_parts))
    
#     octet_values = []
#     for _ in range(4):
#         value = 0
#         bit_values = [128, 64, 32, 16, 8, 4, 2, 1]
#         try:
#             for bit in non_zero_binary_parts[_]:
#                 value += bit_values.pop(0)
#         except IndexError:
#             pass
#         octet_values.append(value)
    
#     def is_non_zero(number):
#         return number != 0
    
#     subnet_mask = 256 - list(filter(is_non_zero, octet_values))[-1]
#     print('Netmask\t\t: ' + '.'.join([str(x) for x in octet_values]))
#     print('Jumlah Subnet\t: ' + str(2 * len(non_zero_binary_parts[-1])))
#     print('Block Subnet\t: ' + str(subnet_mask))
    
#     next_hops = [0]
#     for _ in range(100):
#         next_hops.append(next_hops[-1] + subnet_mask)
#     print('Nexthop\t\t: ' + ','.join(str(x) for x in next_hops))
    
#     if prefix_length in range(1, 8):
#         pass
#     elif prefix_length in range(8, 16):
#         pass
#     elif prefix_length in range(16, 24):
#         pass
#     elif prefix_length in range(24, 33):
#         last_ip_part = ip_parts[3]
#         try:
#             previous_ip = [x for x in next_hops if x <= int(last_ip_part)][-1]
#             next_ip = [x for x in next_hops if x > int(last_ip_part)][0]
#         except IndexError:
#             previous_ip = 0
#             next_ip = 256
        
#         network_ip = ip_parts[0:3]
#         network_ip.append(str(previous_ip))
        
#         broadcast_ip = ip_parts[0:3]
#         broadcast_ip.append(str(next_ip - 1))
        
#         print('Network\t\t: ' + '.'.join(network_ip))
#         print('Broadcast\t: ' + '.'.join(broadcast_ip))
# hitung_ip('12.23.43.123', 24)

def hitung_ip(alamat_ip, panjang_prefix):
    bagian_ip = alamat_ip.split('.')
    # membuat angka 1 sebanyak panjang prefik dan sisanya di ganti dengan 0 sampai panjang biner nya
    string_biner = ('1'*panjang_prefix) + '0' * (32-panjang_prefix)
    # setiap 8 byte di pisahkan oleh titik (.)
    bagian_biner = []
    for i in range(0, 32, 8):
        bagian_biner.append(string_biner[i:i+8])
    bagian_biner = '.'.join(bagian_biner)
    # cetak biner yang sudah di pisahkan oleh titik
    print('Binear\t\t: ' + bagian_biner)
    # hapus byte 0 lalu ubah menjadi list dengan cara di bagi oleh titik, jika ada index yang isinya kosong maka akan di hapus menggunakan fungsi filter
    bagian_biner_tanpa_nol = bagian_biner.replace('0', '').split('.')
    bagian_biner_tanpa_nol = list(filter(None, bagian_biner_tanpa_nol))
    # jumlahkan byte yang sudah menjadi list masing masing 8 byte(mengubah byte ke desimal)
    netmask = []
    for _ in range(4):
        nilai = 0
        # nilai byte dari kanan ke kiri
        nilai_bit = [128, 64, 32, 16, 8, 4, 2, 1]
        try:
            for bit in bagian_biner_tanpa_nol[_]:
                # tambah terus sebanyak jumlah byte 1
                nilai += nilai_bit.pop(0)
        except IndexError:
            pass
        # tambahkan oktet ke list netmask
        netmask.append(nilai)
    
    def bukan_nol(angka):
        return angka != 0
    # rumus block subnet = 256 - ujung dari netmask
    block_subnet = 256 - list(filter(bukan_nol, netmask))[-1]
    print('Netmask\t\t: ' + '.'.join([str(x) for x in netmask]))
    # rumus jumlah subnet = 2 ^ panjang byte 1 paling akhir
    print('Jumlah Subnet\t: ' + str(2 ** len(bagian_biner_tanpa_nol[-1])))
    print('Block Subnet\t: ' + str(block_subnet))
    # kumpulkan nexthop sebanyak 100
    nexthop = [0]
    for _ in range(100):
        nexthop.append(nexthop[-1] + block_subnet)
    # cetak nexthop
    print('Nexthop\t\t: ' + ','.join(str(x) for x in nexthop))
    # tentukan bagian ip yang akan berubah sesuai kelas frefik
    if panjang_prefix in range(1, 8):
        bagian_terakhir_ip = bagian_ip[0]
    elif panjang_prefix in range(8, 16):
        bagian_terakhir_ip = bagian_ip[1]
    elif panjang_prefix in range(16, 24):
        bagian_terakhir_ip = bagian_ip[2]
    elif panjang_prefix in range(24, 33):
        bagian_terakhir_ip = bagian_ip[3]
    
    # mencari nexthop yang lebih dari dan kurang dari bagian akhir ip(yang akan berubah sesuai kelas) jika terjadi error maka di atur 0 dan 255(untuk /16,/24,/33)
    try:
        ip_sebelum = [x for x in nexthop if x <= int(bagian_terakhir_ip)][-1]
        ip_selanjutnya = [x for x in nexthop if x > int(bagian_terakhir_ip)][0]
    except IndexError:
        ip_sebelum = 0
        ip_selanjutnya = 256

    """
        mulai hitung ip
        rumus 
        kelas a 
        network = 123.123.0.0
                        oktet 2 di isi dengan nexthop sebelumnya dan sisa nya di ganti dengan 0
        netmask = 123.123.255.255
                        oktet 2 di isi dengan nexthop setelahnya - 1 dan sisa nya di ganti dengan 0
        kelas b dan c sama seperti kelas a hanya saja kelas b oktet 3 yang berubah dan kelas c oktet 4 yang berubah
    """
    if panjang_prefix in range(1, 8):
        ip_network = bagian_ip[0:0]
        ip_network.append(str(ip_sebelum))
        ip_broadcast = bagian_ip[0:0]
        ip_broadcast.append(str(ip_selanjutnya - 1))
        ip_broadcast+=['255','255','255']
        ip_network+=['0','0','0']
    elif panjang_prefix in range(8, 16):
        ip_network = bagian_ip[0:1]
        ip_network.append(str(ip_sebelum))
        ip_broadcast = bagian_ip[0:1]
        ip_broadcast.append(str(ip_selanjutnya - 1))
        ip_broadcast+=['255','255']
        ip_network+=['0','0']
    elif panjang_prefix in range(16, 24):
        ip_network = bagian_ip[0:2]
        ip_network.append(str(ip_sebelum))
        ip_broadcast = bagian_ip[0:2]
        ip_broadcast.append(str(ip_selanjutnya - 1))
        ip_broadcast+=['255']
        ip_network+=['0']
    elif panjang_prefix in range(24, 33):
        ip_network = bagian_ip[0:3]
        ip_network.append(str(ip_sebelum))
        ip_broadcast = bagian_ip[0:3]
        ip_broadcast.append(str(ip_selanjutnya - 1))
    else:
        print('invalid ip address')
        exit()
    print('Network\t\t: ' + '.'.join(ip_network))
    print('Broadcast\t: ' + '.'.join(ip_broadcast))

hitung_ip('12.23.43.123', 33)
