# algoritma tebak angka
# loop (while), if-else, perbandingan lebihdari ">" dan kurangdari "<"
import random
def tebakAngka():

    angkaAcak = random.randrange(1,100)

    while True:
        tebak = int(input('angka : '))
        if tebak > angkaAcak:
            print('angka benar lebih kecil dari angka tebakan')
        elif tebak < angkaAcak:
            print('angka benar lebih besar dari angka tebakan')
        else:
            print(f'anka acak adalah {tebak}')
            break



# algoritma gunting batu kertas 
# try-except, if-else, and, perbandingan sama dengan "="
def GBK():
    try:
        print('Gunting Batu Kertas\n 1 = gunting\n 2 = batu\n 3 = kertas')
        listGBK     = ['gunting','batu','kertas']
        komputer    = random.randrange(0,3)
        user        = int(input('pilih : ')) - 1

        komputer    = listGBK[komputer]
        user        = listGBK[user]
        if (komputer==listGBK[0]) and (user==listGBK[1]):
            print(f'kamu menang, komputer memegang {komputer}')
        elif (komputer==listGBK[1]) and (user==listGBK[2]):
            print(f'kamu menang, komputer memegang {komputer}')
        elif (komputer==listGBK[2]) and (user==listGBK[0]):
            print(f'kamu menang, komputer memegang {komputer}')
        elif (komputer==listGBK[1]) and (user==listGBK[0]):
            print(f'kamu kalah, komputer memegang {komputer}')
        elif (komputer==listGBK[2]) and (user==listGBK[1]):
            print(f'kamu kalah, komputer memegang {komputer}')
        elif (komputer==listGBK[0]) and (user==listGBK[2]):
            print(f'kamu kalah, komputer memegang {komputer}')
        else:
            print(f'seri, komputer memegang {komputer}')
    except (ValueError,IndexError) :
        print('hanya masukan angka 1, 2, 3')
        GBK()
# algoritma kalkulator sederhana
# loop (while), eval, if-else, operasi matematika, 
def kalkulator():
    print(' * = kali\n / = bagi\n + = tambah\n - = kurang\n = = samadengan')
    all = ''
    while True:
        number1 = input('number     : ')
        if number1.isdecimal() or number1.isdigit():
            all += number1
        else:
            print('hanya masukan number')
            continue
        operasi = input('operasi    : ')
        if operasi=='=':
            print(f'hasil akhir adalah {all} = {eval(all)}')
            break
        elif operasi in ['-','*','/','+']:
            all += operasi
        else:
            print(f'operator salah, hasil akhir adalah {all} = {eval(all)}')
            break
    
    

kalkulator()