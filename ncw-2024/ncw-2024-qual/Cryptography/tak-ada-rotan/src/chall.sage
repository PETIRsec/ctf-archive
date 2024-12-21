FLAG = open("flag.txt","rb").read().strip()
assert(len(FLAG) == 32)

coeffs = list(FLAG)
F.<x> = RealField(300)[]
f = sum([z * x**i for i, z in enumerate(coeffs)])
res = (f.roots()[0][0])

whole, dec = str(res).split('.')
coeffs2 = [int(dec[i:i+3]) for i in range(0, len(dec), 3)]
f2 = sum([z * x**i for i, z in enumerate(coeffs2)])
delim = len(dec)//3

print(whole)
print([f2(int(dec[i:i+delim])).integer_part() for i in range(0, len(dec), delim)])