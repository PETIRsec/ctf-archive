def no():
    print('Wrong answer!', flush=True)
    exit()

print('This is my story: I have never had any malware installed on my host. I am curious and want to execute some malware I found in Windows Sandbox. It was actually fun, but I am more intrigued by Windows Sandbox itself. I captured its memory to analyze the structure, and it seems very different from an ordinary memory capture.\n', flush=True)

print('Answer the following question:', flush=True)

print('\n1. Tell me, where is the source of the malware I used to download? (just the main link, without the subdirectories)', flush=True)
print('>> ', end='', flush=True)
if input() != 'https://github.com/Da2dalus/The-MALWARE-Repo':
    no()

print('\n2. How many malwares have I downloaded?', flush=True)
print('>> ', end='', flush=True)
if input() != '9':
    no()

print('\n3. When did I run the last malware? (YYY-MM-DD HH:MM:SS)', flush=True)
print('>> ', end='', flush=True)
if input() != '2024-11-01 14:11:04':
    no()

print('\n4. I like the Windows Vista prank one. What is its PID?', flush=True)
print('>> ', end='', flush=True)
if input() != '6440':
    no()

print('\n5a. Out of all malware I downloaded, how many did I successfully execute?', flush=True)
print('>> ', end='', flush=True)
if input() != '4':
    no()

print('\n5b. Mention all malware I executed, separated by space (order does not matter)', flush=True)
print('>> ', end='', flush=True)
ans = input()
mal = ['Melting.exe', 'Curfun.exe', 'Vista.exe', 'CrazyNCS.exe']
ans = ans.split()
if len(ans) != 4:
    no()
for i in ans:
    if i not in mal:
        no()

import os
FLAG = os.getenv("FLAG", "[!] Something went wrong. Please contact the author.")
print(f'\nGreat job! Here is your flag: {FLAG}', flush=True)