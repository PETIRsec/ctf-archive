from PIL import Image
from random import randint

def to_bytes(i, len):
    return i.to_bytes(len, byteorder='big')

def boo(f, pix, x, y, len):
    try:
        r,g,b,a = pix[x,y]
    except:
        r,g,b = pix[x,y]
    if len == 2:
        r,g,b = (r*2)^0x11, (g*2)^0x12, (b*2)^0x13
    f.write(to_bytes(r ^ randint(50,100), len))
    f.write(to_bytes(g ^ randint(50,100), len))
    f.write(to_bytes(b ^ randint(50,100), len))

def enhance(w, h, pix):
    for y in range(h):
        for x in range(w):
            ran = randint(1,20)
            len = 2 if (y+1) % ran == 0 else 1
            if len == 2:
                f.write(b'DOPE')
            boo(f, pix, x, y, len)

print('++  PerfectNG, your perfect PNG enhancer')
print('++  "Not Portable, but Perfect!"')
name = input('++  Please input the image file name: ')

try:
    img = Image.open(name)
    pix = img.load()
    w,h = img.size
    img.close()
except:
    print('++  Invalid image file')
    exit()

sign = b'PerfectNG' + to_bytes(w,2) + to_bytes(h,2)
f = open(name, 'wb')
f.write(sign)
f.write(b'DAMN')

enhance(w, h, pix)

f.write(b'DONE')
f.close()

print('++  Done! Your image has been enhanced!')
