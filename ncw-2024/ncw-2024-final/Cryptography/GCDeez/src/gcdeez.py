import random
from Crypto.Util.number import getStrongPrime, isPrime, bytes_to_long

FLAG = open("flag.txt", "rb").read().strip()

p = getStrongPrime(1024)
q = getStrongPrime(1024)
N = [p * q]
for _ in range(3):
    while True:
        x = random.getrandbits(192)
        if isPrime(p+x) and isPrime(q-x):
            N.append((p+x)*(q-x))
            break

div = len(FLAG) // 4
block = [FLAG[i:i+div] for i in range(0, len(FLAG), div)]
M = [bytes_to_long(b) for b in block]
e = 0x10001
C = []
for i, (m, n) in enumerate(zip(M, N)):
    assert m < n
    C.append(pow(m, e, n))

print(N)
print(C)