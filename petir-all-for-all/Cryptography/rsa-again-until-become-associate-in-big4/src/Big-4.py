from Crypto.Util.number import *

FLAG = b'PETIR{if_you_understand_this_kind_of_inverse_and_cryptosystem_then_you_can_be_an_associate_:v}'

e = 65537

BITS = 1024
p = getPrime(BITS)
q = inverse(e,p)

while p%4 != 3 or q%4 != 3:
  p = getPrime(BITS)
  q = inverse(e,p)

m2 = bytes_to_long(FLAG)
n = p*q

c = pow(m2,BITS,n) % n

print(f'n = {n}')
print(f'e = {e}')
print(f'c = {c}')

