from PIL import Image
import numpy as np
from random import seed

def unscramble_image(input_file, output_file, secret_seed):
    try:
        img = Image.open(input_file)
        width, height = img.size
        pixels = np.array(img)
    except:
        print("err")
        return

    seed(secret_seed)
    np.random.seed(secret_seed)

    pixel_order = np.arange(width * height)
    np.random.shuffle(pixel_order)

    random_matrix = np.random.randint(1, 256, size=(height, width), dtype=np.uint8)

    has_alpha = pixels.shape[2] == 4

    unscrambled = np.zeros_like(pixels)
    for i, idx in enumerate(pixel_order):
        dest_y, dest_x = divmod(idx, width)
        y, x = divmod(i, width)
        
        if has_alpha:
            r, g, b, a = pixels[y, x]
        else:
            r, g, b = pixels[y, x]
        
        rand_val = random_matrix[y, x]
        
        orig_r = r ^ rand_val
        orig_g = g ^ rand_val
        orig_b = b ^ rand_val

        if has_alpha:
            unscrambled[dest_y, dest_x] = [orig_r, orig_g, orig_b, a]
        else:
            unscrambled[dest_y, dest_x] = [orig_r, orig_g, orig_b]

    unscrambled_img = Image.fromarray(unscrambled.astype(np.uint8))
    unscrambled_img.save(output_file)

    print(f"Unscrambled image saved as {output_file}")

if __name__ == "__main__":
    input_file = input("Enter the name of your scrambled image file: ")
    output_file = "unscrambled_" + input_file
    secret_seed = int(input("Enter the seed for unscrambling: "))
    unscramble_image(input_file, output_file, secret_seed)
