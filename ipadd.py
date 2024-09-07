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
    string_biner = ''
    for _ in range(panjang_prefix):
        string_biner += '1'
    string_biner = string_biner.ljust(32, '0')
    
    bagian_biner = []
    for i in range(0, len(string_biner), 8):
        bagian_biner.append(string_biner[i:i+8])
    bagian_biner = '.'.join(bagian_biner)
    print('Binear\t\t: ' + bagian_biner)
    
    bagian_biner_tanpa_nol = bagian_biner.replace('0', '').split('.')
    bagian_biner_tanpa_nol = list(filter(None, bagian_biner_tanpa_nol))
    
    nilai_oktet = []
    for _ in range(4):
        nilai = 0
        nilai_bit = [128, 64, 32, 16, 8, 4, 2, 1]
        try:
            for bit in bagian_biner_tanpa_nol[_]:
                nilai += nilai_bit.pop(0)
        except IndexError:
            pass
        nilai_oktet.append(nilai)
    
    def bukan_nol(angka):
        return angka != 0
    
    netmask = 256 - list(filter(bukan_nol, nilai_oktet))[-1]
    print('Netmask\t\t: ' + '.'.join([str(x) for x in nilai_oktet]))
    print('Jumlah Subnet\t: ' + str(2 * len(bagian_biner_tanpa_nol[-1])))
    print('Block Subnet\t: ' + str(netmask))
    
    nexthop = [0]
    for _ in range(100):
        nexthop.append(nexthop[-1] + netmask)
    print('Nexthop\t\t: ' + ','.join(str(x) for x in nexthop))
    
    if panjang_prefix in range(1, 8):
        pass
    elif panjang_prefix in range(8, 16):
        pass
    elif panjang_prefix in range(16, 24):
        pass
    elif panjang_prefix in range(24, 33):
        bagian_terakhir_ip = bagian_ip[3]
        try:
            ip_sebelum = [x for x in nexthop if x <= int(bagian_terakhir_ip)][-1]
            ip_selanjutnya = [x for x in nexthop if x > int(bagian_terakhir_ip)][0]
        except IndexError:
            ip_sebelum = 0
            ip_selanjutnya = 256
        
        ip_network = bagian_ip[0:3]
        ip_network.append(str(ip_sebelum))
        
        ip_broadcast = bagian_ip[0:3]
        ip_broadcast.append(str(ip_selanjutnya - 1))
        
        print('Network\t\t: ' + '.'.join(ip_network))
        print('Broadcast\t: ' + '.'.join(ip_broadcast))

hitung_ip('12.23.43.123', 24)
