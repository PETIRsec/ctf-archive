# LineCryptor
TL;DR
1. The files was python compiled to exe, we need to get the exe back to python using pyinstxtractor or any other tools.
2. Read the pyc code using pycdc or any other tools.
3. Beautify the code and learn the algorithm.
4. The code was reading all the files in the same directory and encrypt with aes.
5. The IV is get from the link in line 965374.
6. The key are using the filename but the filename are change to 16 char of real_filename ^ with the line 965374 or the IV and convert it to base64
7. So to get the key decode the base 64 and xor with the IV.
8. Decrypt the file with script or do it manualy on cyber chef.
