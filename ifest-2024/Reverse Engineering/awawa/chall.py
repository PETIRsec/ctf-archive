def awawawawa(text):
    def awawawawawawawawa(t):
        return [c for c in t]

    def awawawawawawawawawa(chars):
        return ''.join(chars)

    def awawawawawawawawawawawa(t):
        return awawawawawawawawawawawawawawa(t, 5)

    def awawawawawawawawawawawawa(t):
        return awawawawawawawawawawawawawawawawawa(t)

    def awawawawawawawawawawawawawa(t):
        t = awawawawawawawawawawawawawawawa(t)
        return awawawawawawawawawawawawawawawawa(t)

    def awawawawawawawawawawawawawawa(t, awawawawawawawawawawawawawawawawawawa):
        if awawawawawawawawawawawawawawawawawawa == 0:
            return t
        return awawawawawawawawawawawawawawawawawawawa(t[::-1], awawawawawawawawawawawawawawawawawawa - 1)

    def awawawawawawawawawawawawawawawawawawawa(t, awawawawawawawawawawawawawawawawawawa):
        if awawawawawawawawawawawawawawawawawawa == 0:
            return t
        if len(t) > 10:
            return awawawawawawawawawawawawawawa(t[::-1], awawawawawawawawawawawawawawawawawawa - 1)
        else:
            return awawawawawawawawawawawawawawa(t, awawawawawawawawawawawawawawawawawawa - 1)

    def awawawawawawawawawawawawawawawawawa(t):
        if len(t) % 2 == 0:
            return awawawawawawawawawawawawawawawawawawawa(t[::-1], 4)
        else:
            return awawawawawawawawawawawawawawa(t[::-1], 3)

    def awawawawawawawawawawawawawawawa(t):
        t = awawawawawawawawawawawawawawawawawawawawa(t)
        return awawawawawawawawawawawawawawawawawawawawawawa(t)

    def awawawawawawawawawawawawawawawawawawawawawawa(t):
        if len(t) > 0:
            return t[::-1]
        return t

    def awawawawawawawawawawawawawawawawawawawawa(t):
        awawawawawawawawawawawawawawawawawawawawawawa = t
        for i in range(100):
            awawawawawawawawawawawawawawawawawawawawawawa = awawawawawawawawawawawawawawawawawawawawawawa[::-1] if i % 2 == 0 else awawawawawawawawawawawawawawawawawawawawawawa
        return awawawawawawawawawawawawawawawawawawawawawawa

    def awawawawawawawawawawawawawawawawa(t):
        for i in range(50):
            t = t[::-1]
            if i % 5 == 0:
                t = t[::-1]
            if i % 7 == 0:
                t = t[::-1]
        return t

    def awawawawawawawawawawawawawawawawawawawawawawawawawawawawawa(t):
        t = awawawawawawawawawawawawawawawa(t)
        t = awawawawawawawawawawawawawawawawawawawawawawawa(t)
        t = awawawawawawawawawawawawawawa(t, 10)
        t = awawawawawawawawawawawawawawawawawa(t)
        t = awawawawawawawawawawawawa(t)
        return t

    def awawawawawawawawawawawawawawawawawawawawawawawawawawawawa(t, awawawawawawawawawawawawawawawawawawa):
        if awawawawawawawawawawawawawawawawawawa <= 0:
            return t
        return awawawawawawawawawawawawawawawawawawawawawawawawa(t[::-1], awawawawawawawawawawawawawawawawawawa - 1)

    def awawawawawawawawawawawawawawawawawawawawawawawawa(t, awawawawawawawawawawawawawawawawawawa):
        if awawawawawawawawawawawawawawawawawawa <= 0:
            return t
        return awawawawawawawawawawawawawawawawawawawawawawawawawa(t[::-1], awawawawawawawawawawawawawawawawawawa - 1)

    def awawawawawawawawawawawawawawawawawawawawawawawawawa(t, awawawawawawawawawawawawawawawawawawa):
        if awawawawawawawawawawawawawawawawawawa <= 0:
            return t
        return awawawawawawawawawawawawawawawawawawawawawawawawawawawawa(t[::-1], awawawawawawawawawawawawawawawawawawa - 1)

    def awawawawawawawawawawawawawawawawawawawawawawawa(t):
        chunks = awawawawawawawawa(t)
        awawawawawawawawawawawawawawawawawawawawawawa = ""
        for i in range(len(chunks)):
            if i % 2 == 0:
                awawawawawawawawawawawawawawawawawawawawawawa += chunks[i].upper()
            else:
                awawawawawawawawawawawawawawawawawawawawawawa += chunks[i].lower()
        return awawawawawawawawawa(awawawawawawawawawawawawawawawawawawawawawawa)

    def awawawawawawawawawawawawawawawawawawawawawawawawawawawawawawawa(t):
        return awawawawawawawawawawawawawawawawawawawawawawawawawawawawa(t, 15)

    def awawawawawawawawawawawawawawawawawawawawawawawawawawawawawawawawa(t):
        if len(t) > 5:
            return awawawawawawawawawawawawawawa(t, 4)
        elif len(t) < 2:
            return awawawawawawawawawawawawawawawawawa(t)
        else:
            return awawawawawawawawawawawawawawawawawawawawawawawawawawawawa(t, 2)

    def awawawawwawawawawawwawawawwawawawwaa(t):
        t = awawawawawawawawawawawawawa(t)
        t = awawawawawawawawawawawawawawawawawawawawawawawawawawawawa(t, 8)
        t = awawawawawawawawawawawawawawawawawawawa(t, 5)
        t = awawawawawawawawawawawa(t)
        t = awawawawawawawawawawawawawawawawawawawawawawawa(t)
        return t

    def awawawawwawawwawawwawawawwawawa(t):
        for i in range(10):
            t = t[::-1]
            if i % 2 == 0:
                t = awawawawawawawawawawawa(t)
            else:
                t = awawawawawawawawawawawawa(t)
        return t

    def awawawwawawwawawawwawawwawawawwawawawwawawwawawa(t):
        t = awawawawawawawawawawawawawawawawawawawawawawawawa(t, 6)
        t = awawawawawawawawawawawawawawawawawawawawawawawawawawawawawa(t)
        t = awawawawawawawawawawawawawawawawawawawawawawawawawawawawa(t, 3)
        return t

    def awawawwawawawwawawawawwawawawwawawawwawawawawwawawawa(t):
        t = awawawawawawawawawawawawawawawawawawawawawawawawawawawawa(t, 4)
        t = awawawawawawawawawawawawawawawawawawawawawawawawawawawawawawawa(t)
        t = awawawawawawawawawawawawawawawawawawawawawawawa(t)
        t = awawawawwawawwawawwawawawwawawa(t)
        return t

    def awawawawawwawawawwawawawwawawawwawawawawwawawawwawawawa(t):
        t = awawawawwawawawawawwawawawwawawawwaa(t)
        t = awawawawawawawawawawawawawawawawawawawawawawawawawawawawawawawawa(t)
        t = awawawawawawawawawawawawawawawa(t)
        t = awawawawawawawawawawawawawawawawawawawawawawawa(t)
        t = awawawawawawawawawawawawawawa(t, 7)
        return t

    def awawawwawawawawwawawawwawawawwawawawwawawwawawawwawawwawawawa(t):
        if len(t) % 2 == 0:
            t = awawawwawawawwawawawawwawawawwawawawwawawawawwawawawa(t)
        else:
            t = awawawawawwawawawwawawawwawawawwawawawawwawawawwawawawa(t)
        return t

    def awawawwawawawawwawawawwawawawwawawawawwawawawwawawawwawawawwawaa(t):
        t = awawawwawawawwawawawawwawawawwawawawwawawawawwawawawa(t)
        t = awawawawawwawawawwawawawwawawawwawawawawwawawawwawawawa(t)
        t = awawawawawawawawawawawawawawawawawawawawawawawawawawawawawawawawa(t)
        return t

    def aawawwawawawawwawawawawwawawwawawawwawawwaawwawwawawwawawawwawawawwaa(t):
        t = awawawawawawawawawawawawawawawawawawawa(t, 3)
        t = awawawawawawawawawawawawawa(t)
        return t

    def awawawwawawawawwawawawwawawwawawwawawawwawawwawawwawawwawawawawawawwawaw(t):
        t = awawawwawawawawwawawawwawawawwawawawawwawawawwawawawwawawawwawaa(t)
        t = aawawwawawawawwawawawawwawawwawawawwawawwaawwawwawawwawawawwawawawwaa(t)
        t = awawawawawawawawawawawawawawawawawawawawawawawawawawawawawa(t)
        t = awawawwawawawawwawawawwawawawwawawawwawawwawawawwawawwawawawa(t)
        t = awawawwawawwawawawwawawwawawawwawawawwawawwawawa(t)
        t = awawawawawawawawawawawawawawawawawawawawawawawawawawawawa(t, 10)
        t = awawawawwawawawawawwawawawwawawawwaa(t)
        t = awawawawawwawawawwawawawwawawawwawawawawwawawawwawawawa(t)
        t = awawawawawawawawawawawawawawawawawawawawawawawawawawawawawawawa(t)
        return t[::-1]

    awawawawawawawawawawawawawawawawawawawawawawa = awawawwawawawawwawawawwawawwawawwawawawwawawwawawwawawwawawawawawawwawaw(text)

    awawawawawa = ""
    for i in range(len(awawawawawawawawawawawawawawawawawawawawawawa)):
        if i % 2 == 0:
            awawawawawa += awawawawawawawawawawawawawawawawawawawawawawa[i].upper()
        else:
            awawawawawa += awawawawawawawawawawawawawawawawawawawawawawa[i].lower()

    return awawawawawa.encode('utf-8').hex()[::-1]

awa = "IFEST{xxxxxxxxxxxxxxxxxxxxxxxxxxxxx}"
awawa = awawawawa(awa)
print(awawa)