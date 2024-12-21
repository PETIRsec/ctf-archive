from sdp import SdpStruct
import socket

s = socket.socket()
host = '127.0.0.1'
port = 8888

s.connect((host, port))

data = SdpStruct.unpack(s.recv(4096))

d = data.get(0, -1)

if d == -1:
    print('Oh no! `d` is not a valid private key!')
    exit()

n = data.get(1, -1)
if n == -1:
    print('Oh no! `n` is not a valid modulus!')
    exit()

name = input('Gimme ur name: ')
sign = int(input('Sign ur name please: '))

s.send(SdpStruct.pack(SdpStruct({
    0: name,
    1: sign
})))

data = SdpStruct.unpack(s.recv(4096))
print(data)