from PIL import Image

name = 'kanade.png'
f = open(name, 'rb')
sign = f.read(9)
# print(sign)

w = int.from_bytes(f.read(2), byteorder='big')
h = int.from_bytes(f.read(2), byteorder='big')
# print(w, h)

img = Image.new('RGB', (w,h))
pix = img.load()

for y in range(h):
    for x in range(w):
        red = int.from_bytes(f.read(1))
        green = int.from_bytes(f.read(1))
        blue = int.from_bytes(f.read(1))
        if f'{chr(red)}{chr(green)}{chr(blue)}' == 'DOP':
            f.read(1)
            # print('DOPE')
            red, green, blue = red ^ 0x75, green ^ 0x75, blue ^ 0x75
            red = (int.from_bytes(f.read(2), byteorder='big') ^ 0x11) // 2
            green = (int.from_bytes(f.read(2), byteorder='big') ^ 0x12) // 2
            blue = (int.from_bytes(f.read(2), byteorder='big') ^ 0x13) // 2
            pix[x,y] = (red, green, blue)
        else:
            red, green, blue = red ^ 0x75, green ^ 0x75, blue ^ 0x75
            pix[x,y] = (red, green, blue)

img.save('flag.png')
