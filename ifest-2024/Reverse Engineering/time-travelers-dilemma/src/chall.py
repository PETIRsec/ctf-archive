from pycrunch_trace.client.api import trace
import random

@trace    
def run(n):
    rand_gen(n)

# LCG taken from https://github.com/rossilor95/lcg-python/blob/main/lcg.py
def linear_congruential_generator(m: int, a: int, c: int, seed: int):
    x = seed
    while True:
        yield x
        x = (a * x + c) % m

def rand_gen(n_samples: int, seed: int = 123_456_789):
    m: int = 2_147_483_648
    a: int = 594_156_893
    c: int = 0
    gen = linear_congruential_generator(m, a, c, seed)

    for i in range(0, n_samples):
        rand = next(gen) + random.randint(0, 1333333777777)
        print(rand)
        
run(4)