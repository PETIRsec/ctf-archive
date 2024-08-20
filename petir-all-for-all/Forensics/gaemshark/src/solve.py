from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
import os

def decrypt_file(password: str, file_path: str):
    # Read the salt from the .salt file
    with open(f"{file_path}.salt", "rb") as salt_file:
        salt = salt_file.read(8)
    
    # Read the IV from the .iv file
    with open(f"{file_path}.iv", "rb") as iv_file:
        iv = iv_file.read(16)
    
    # Derive the key using PBKDF2
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA1(),
        length=32,  # 256 bits for AES
        salt=salt,
        iterations=65536,  # Number of iterations
        backend=default_backend()
    )
    key = kdf.derive(password.encode())
    
    # Initialize the cipher for decryption
    cipher = Cipher(
        algorithms.AES(key),
        modes.CBC(iv),
        backend=default_backend()
    )
    decryptor = cipher.decryptor()
    
    # Read the encrypted file and decrypt it
    with open(file_path, "rb") as enc_file, open(file_path.replace(".enc", ""), "wb") as dec_file:
        chunk_size = 64
        while True:
            chunk = enc_file.read(chunk_size)
            if not chunk:
                break
            decrypted_chunk = decryptor.update(chunk)
            dec_file.write(decrypted_chunk)
        dec_file.write(decryptor.finalize())
    
 

# Example usage
decrypt_file("Password", "Encrypted_file")
