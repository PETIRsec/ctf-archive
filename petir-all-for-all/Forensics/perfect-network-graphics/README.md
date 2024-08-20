# Perfect Network Graphics

A custom encoder gets each pixel's RGB values by XORing them with a random number between 50 and 100. But if the y-coordinate of the pixel modulo the random number equals zero, then a junk 'DOPE' will present, doubles the original RGB value (expanding it to 2 bytes), and XORs it once again with the given value.

The solution is to track the 'DOPE' values. Since the original random number used for the first XOR cannot be retrieved, use the average of 50 and 100 (which is 75) for XORing.