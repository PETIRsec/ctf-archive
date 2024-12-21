FLAG = open("flag.txt", "rb").read().strip()
flagbit = [int(x) for x in bin(int(FLAG.hex(), 16))[2:]]

p = 196602566043829842353828575048265134713308607440986277882677957131182678360677315691770139798172153327996603619
F = GF(p)
E = EllipticCurve(F,[1,0]) 
n = E.order()

output = []
for i in range(len(flagbit)):
    P = E.random_point()
    x,y = randint(0,n), randint(0,n)

    z = 0
    if flagbit[i]:
        z = x*y
    else: 
        z = randint(0,n)

    output.append([P.xy(),(P*x).xy(),(P*y).xy(),(P*z).xy()])
print(output)