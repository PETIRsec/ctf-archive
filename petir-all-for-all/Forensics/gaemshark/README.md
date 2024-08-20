# GaemShark

TL;DR

- Analyzing logcat
- Encrypted local files with crydroid ransomware
- Decrypting whatsapp backup with stored keys


Crydroid ransomware could be analyzed from logcat, it will encrypt all of the files on /sdcard with several extensions. 

This ransomware could be decrypted straightforwardly if we got direct access to Android device because of the encrypted password is located on logcat and shared_preferences file.

In this challenge, participant only provided with exported /sdcard files and logcat files. Participant must analyze the logcat to answer several questions and decrypting the encrypted files, then decrypting WhatsApp backup chat (.crypt15) with known end-to-end keys.


### CryDroid

#### Encrypt / Decrypt Algorithm:
- AES/CBC
- Key Generation for AES: calculating password & salt from logcat for every encrypted files with PBKDFwithSHA1 (65536 Iterations)
- IV is provided differently from every file.

