"""
Halo semuanya, sedikit backstory, filosofi dari series challenge saya ini adalah
melihat bahwa challenge yang kelihatan rumit, sebenarnya bisa sangat sederhana.
Dan challenge yang kelihatan sederhana, bisa memiliki approach yang tricky.

Nah awalnya saya siapin challenge yang isinya cuman 2 line berikut wkwkw:
"""
flag = int.from_bytes(open('flag.txt', 'rb').read())
print(pow(2, flag, 1154543773027194978300531105544404721440832315984713424625039))
"""
Tapi setelah dipikir-pikir, ini sebenarnya ngga terlalu menggambarkan filosofi yang saya mau.
Karena jatuhnya kayak crypto osint gitu. Jadi saya memutuskan untuk bikin chall yang baru.
"""


"""
Oleh karena itu, saya bikin challenge kedua, setelah bikin challenge ini,
Saya merasa sayang kalau challenge pertama ngga kepake, jadi saya tetap masukin wkwkkw
"""
import random
flag = int.from_bytes(open('flag.txt', 'rb').read())
for i in range(2048):
    k = random.getrandbits(flag.bit_length())
    c = bin(flag ^ k)[2:]
    random.shuffle(c)
    print(k, ''.join(c))
"""
Output dari program pertama (line 8-9) itu ada di output.txt, sementara yang kedua
(line 20-26) ada di output2.txt. Kalian bisa coba solve kedua challenge ini, flagnya sama kok,
jadi bisa pilih salah satu, tapi yang pertama jujur aja kayak crypto osint jadi kureng wkwkwk


Good luck, thanks for giving it a try!
P.S yang idiot admire complexity itu jauh lebih gampang jadi mungkin coba itu dulu wkwk
~ Wrth
"""