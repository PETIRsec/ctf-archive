f = open('log.txt').readlines()

a = 0
b = 0
for line in f:
    time, req, data = line.split('  ')

    res = int(data.split('%20AND%20SLEEP(3)')[0].split('))=')[-1])
    if res == 0:
        print(chr(b), end='')

    col = int(data.split('%20LIMIT%20')[-1][0])
    if col != a:
        print()

    b = res
    a = col
