from tqdm import tqdm
import numpy as np

np.random.seed(0x2019)

# highly reccomended use google colab

# using the challenge script in cell above
s = [[i.detach().numpy().tolist() for i in sigma(convert("PETIR{000000000000000000000000000000000}"))[0]]]
print(s)

for i in range(33):
    test = 'PETIR{' + ''.join('1'if j == i else '0'for j in range(33)) + '}'
    s.append([k.detach().numpy().tolist() for k in sigma(convert(test))[0]])

open('dump.txt', 'w').write(repr(s))

print(s)
target = list(map(float,"22847.716796875 -21964.810546875 -14513.71875 -3790.312744140625 -8359.19921875 -950.1218872070312 -25765.904296875 33915.84765625 25927.662109375 2029.1702880859375 20599.05859375 -22778.146484375 23582.5546875 -33654.6640625 -10178.52734375 10646.5927734375 18819.64453125 -8857.6650390625 2287.3623046875 22975.994140625 8632.626953125 1591.319580078125 -3773.903564453125 6465.8408203125 -14653.0146484375 7569.791015625 -5770.65673828125 -34205.97265625 -16681.216796875 -3415.234375 5391.5654296875 -12609.5859375 4626.630859375".split()))
data = eval(open('dump.txt').read())
# print(data)
print("noice") if s == data else next()

a = np.array(target)
dt = np.array(data)
v = np.array(data[0])

b = []
for i in range(33):
    b.append(dt[i + 1] - dt[0])
    v -= b[-1] * 48

b = np.array(b)
# print(b)
assert(len(b) == len(a-v))
# flag*b+v=a
r = np.matmul(a - v, np.linalg.inv(b))
# print(r)
# print(np.matmul(r.reshape((1, 24)), b) + v)
flag = bytes(r.round().astype(np.uint8))
print(flag)