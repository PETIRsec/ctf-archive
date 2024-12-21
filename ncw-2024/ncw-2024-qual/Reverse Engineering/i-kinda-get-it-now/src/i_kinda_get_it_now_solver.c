#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define KEY_LENGTH 16
#define ROUNDS 10

unsigned char substitution_table[256];
unsigned char inverse_substitution_table[256];

void mod_scramble_reverse(unsigned char *buffer, size_t length, unsigned char mod_value) {
    for (size_t i = 0; i < length; i++) {
        buffer[i] = (buffer[i] + mod_value - i) % mod_value;
    }
}

void rotate_bits_reverse(unsigned char *buffer, size_t length, unsigned char rotate_by) {
    for (size_t i = 0; i < length; i++) {
        buffer[i] = (buffer[i] >> rotate_by) | (buffer[i] << (8 - rotate_by));
    }
}

int mod_inverse(int a, int m) {
    a = a % m;
    for (int x = 1; x < m; x++) {
        if ((a * x) % m == 1) {
            return x;
        }
    }
    return -1;
}

void affine_transform_reverse(unsigned char *buffer, size_t length, int a, int b) {
    int inv_a = mod_inverse(a, 256);
    if (inv_a == -1) {
        return;
    }

    for (size_t i = 0; i < length; i++) {
        buffer[i] = (inv_a * ((buffer[i] + 256 - b) % 256)) % 256;
    }
}


void byte_substitute_reverse(unsigned char *buffer, size_t length) {
    for (size_t i = 0; i < length; i++) {
        buffer[i] = inverse_substitution_table[buffer[i]];
    }
}

void circular_shift_reverse(unsigned char *buffer, size_t length, int shift) {
    shift = shift % length;  
    if (shift < 0) {
        shift += length;
    }

    unsigned char temp[length];
    for (size_t i = 0; i < length; i++) {
        temp[i] = buffer[(i + shift) % length];
    }
    memcpy(buffer, temp, length);
}

void init_substitution_tables() {
    unsigned int seed = 12345;
    for (int i = 0; i < 256; i++) {
        substitution_table[i] = i;
    }
    for (int i = 255; i > 0; i--) {
        seed = (1103515245 * seed + 12345) % 2147483647;
        int j = seed % (i + 1);
        unsigned char temp = substitution_table[i];
        substitution_table[i] = substitution_table[j];
        substitution_table[j] = temp;
    }

    for (int i = 0; i < 256; i++) {
        inverse_substitution_table[substitution_table[i]] = i;
    }
}

void decryption(unsigned char *ciphertext, size_t length, unsigned char *plaintext) {
    memcpy(plaintext, ciphertext, length);

    for (int round = 0; round < ROUNDS; round++) {
        circular_shift_reverse(plaintext, length, 2);
        byte_substitute_reverse(plaintext, length);
        affine_transform_reverse(plaintext, length, 5, 8);
        rotate_bits_reverse(plaintext, length, 3);
        mod_scramble_reverse(plaintext, length, 255);
    }
}

int main() {
    init_substitution_tables();

    unsigned char ciphertext[] = {107, 207, 161, 72, 67, 246, 216, 243, 182, 94, 113, 117, 163, 2, 159};
    size_t length = sizeof(ciphertext) / sizeof(ciphertext[0]);
    unsigned char plaintext[length + 1];

    decryption(ciphertext, length, plaintext);

    plaintext[length] = '\0';

    printf("Decrypted Plaintext: %s\n", plaintext);

    return 0;
}
