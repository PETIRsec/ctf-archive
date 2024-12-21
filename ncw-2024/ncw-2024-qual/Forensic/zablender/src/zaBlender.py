from PIL import Image
import numpy as np
from random import randint, seed

def scramble_pixels(pixels, width, height):
    flat_pixels = pixels.reshape(-1, pixels.shape[-1])
    pixel_order = list(range(width * height))
    np.random.shuffle(pixel_order)
    scrambled = np.zeros_like(flat_pixels)
    for i, idx in enumerate(pixel_order):
        scrambled[i] = flat_pixels[idx]
    return scrambled.reshape(pixels.shape)

def xor_pixels(pixels, random_matrix):
    return pixels ^ random_matrix[:, :, np.newaxis]

def enhance_image():
    print("Welcome to za ImageBlender")
    print("za ImageBlender will blend your image to a Special Image")
    print("make sure your image is in the same folder as za ImageBlender")
    input_file = input("Enter the name of your image file to blend: ")
    output_file = "blended_" + input_file

    try:
        img = Image.open(input_file)
        width, height = img.size
        pixels = np.array(img)
    except:
        print("Oops! Couldn't put the image in za blender. Did you spell it right?")
        return

    secret_seed = (width * height) % 10000
    seed(secret_seed)
    np.random.seed(secret_seed)

    scrambled_pixels = scramble_pixels(pixels, width, height)

    random_matrix = np.random.randint(1, 256, size=(height, width), dtype=np.uint8)
    xored_pixels = xor_pixels(scrambled_pixels, random_matrix)

    scrambled_img = Image.fromarray(xored_pixels)
    scrambled_img.save(output_file)

    print(f"Blendered image is saved as {output_file}")
    print(f"Don't forget this special ingredient: {secret_seed}")

if __name__ == "__main__":
    enhance_image()
