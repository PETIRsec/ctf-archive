f = open("output2.txt", "r").readlines()
ks = []
cs = []
for i in range(2048):
    k,c = f[i].split()
    ks.append(int(k))
    cs.append(c.count('1'))

flag = 0
for i in range(max(ks).bit_length()):
    kk = [k >> i & 1 for k in ks]
    avg0 = sum([c for k,c in zip(ks,cs) if k >> i & 1 == 0]) / sum([1 for k in ks if k >> i & 1 == 0])
    avg1 = sum([c for k,c in zip(ks,cs) if k >> i & 1 == 1]) / sum([1 for k in ks if k >> i & 1 == 1])
    if avg0 < avg1:
        flag |= 0 << i
    else:
        flag |= 1 << i
print(flag.to_bytes((flag.bit_length() + 7) // 8, 'big'))
    