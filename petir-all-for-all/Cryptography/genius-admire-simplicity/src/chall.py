# flag = int.from_bytes(open('flag.txt', 'rb').read())
# print(pow(2, flag, 1154543773027194978300531105544404721440832315984713424625039))

import random
flag = int.from_bytes(open('flag.txt', 'rb').read())
for i in range(2048):
    k = random.getrandbits(flag.bit_length())
    c = bin(flag ^ k)[2:]
    random.shuffle(list(c))
    print(k, ''.join(c))