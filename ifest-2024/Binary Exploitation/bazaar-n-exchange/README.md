# Bazaar n Exchange

Incorrect format specifier (%ld) leading to the overwrite of neighbouring variable. This allows the modification of how many values the read() function reads from the buffer, causing buffer overflow. Since the read() function doesn't write a null byte to the end of the buffer, the canary can be leaked. Call the barang\_tersembunyi() function. The parameter can be inserted to the rdi register by combining "pop rax; ret" gadget with "xchg rax, rdi; ret". Please refer to src/exploit.py for the full solve script. Hope you enjoy!
