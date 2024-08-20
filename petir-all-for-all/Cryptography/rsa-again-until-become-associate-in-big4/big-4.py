from Crypto.Util.number import *

FLAG = b'PETIR{REDACTED}'

e = 65537

BITS = 1024
p = getPrime(BITS)
q = inverse(e,p)

assert p%4 == 3 and q%4 == 3

m2 = bytes_to_long(FLAG)
n = p*q

c = pow(m2,BITS,n) % n

print(f'n = {n}')
print(f'e = {e}')
print(f'c = {c}')

