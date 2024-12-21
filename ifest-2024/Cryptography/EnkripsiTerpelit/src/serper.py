from Crypto.Util.number import *
import string
import random
import time

def generate_random_string(length):
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for _ in range(length))

def encrypt(plain):
    p, q = getPrime(2048), getPrime(2048)
    n = p * q
    m  = bytes_to_long(plain)
    a, b = random.randint((n-1) // 2, n-1), random.randint((n-1) // 2, n-1)
    c = ((13082024*pow(m,2)*a*b) * (13092024*pow(m,3)*a*b)) % n
    return c, n, a, b

menu = """
Pilihlah menu dibawah ini, Waktu anda hanya 35 detik!
1. Lihat Enkripsi Rahasia
2. Tebak Rahasia
3. Exit
"""
count = 0

rahasia = generate_random_string(100).encode()

init = time.time()
while 1:
    print(menu)
    choose = input("Pilih: ")
    if time.time() - init > 35:
        print(f"kelamaan, waktu anda {time.time() - init}")
        exit()
    if choose == "1":
        if count < 2:
            c, n, a, b = encrypt(rahasia)
            print(f'c = {c}')
            print(f'n = {n}')
            print(f'a = {a}')
            print(f'b = {b}')
            count += 1
        else:
            print("Sayang sekali sudah gabisa liat lagi nih :(")
    elif choose == "2":
        tebak = input(">> ").encode()
        if time.time() - init > 35:
            print(f"kelamaan, waktu anda {time.time() - init}")
            exit()
        if tebak == rahasia:
            with open("flag.txt", "rb") as f:
                flag = f.read().strip()
            print(flag)
            exit()
        else:
            print("Nope")
            exit()
    elif choose == "3":
        exit()
    else:
        print("paan we...")
        exit()

    


    


