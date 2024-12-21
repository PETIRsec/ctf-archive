from Crypto.Util.number import *
from pwn import *

# to run: NO_COLOR=1 sage solv.sage

#ser = process(['python3', 'crypto16.py'])
ser = remote('157.230.38.61',1043)

ser.sendline(b'1')
ser.recvuntil(b'c = ')
c1 = int(ser.recvline().strip().decode())
ser.recvuntil(b'n = ')
n1 = int(ser.recvline().strip().decode())
ser.recvuntil(b'a = ')
a1 = int(ser.recvline().strip().decode())
ser.recvuntil(b'b = ')
b1 = int(ser.recvline().strip().decode())

ser.sendline(b'1')
ser.recvuntil(b'c = ')
c2 = int(ser.recvline().strip().decode())
ser.recvuntil(b'n = ')
n2 = int(ser.recvline().strip().decode())
ser.recvuntil(b'a = ')
a2 = int(ser.recvline().strip().decode())
ser.recvuntil(b'b = ')
b2 = int(ser.recvline().strip().decode())

N = n1 * n2
PR.<x> = PolynomialRing(Zmod(N))

k1 = crt([1, 0], [n1, n2])
k2 = crt([0, 1], [n1, n2])

f1 = (13082024*x^2*a1*b1)*(13092024*x^3*a1*b1) - c1
f2 = (13082024*x^2*a2*b2)*(13092024*x^3*a2*b2) - c2

f = k1*f1 + k2*f2
f = f.monic()

d = f.degree()
beta = 1
epsilon = 0.05
X = ceil(0.5 * N^RR(beta^2 / d - epsilon))
res = int(f.small_roots(X=X, beta=beta, epsilon=epsilon)[0])

rahasia = long_to_bytes(res)
print(rahasia)

ser.sendline(b'2')
ser.sendline(rahasia)
ser.interactive()
