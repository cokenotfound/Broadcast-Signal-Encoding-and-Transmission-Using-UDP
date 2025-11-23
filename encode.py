def chain_encode(c1,c2,c3,d1,d2,d3):
    s1 = [0] * (len(c1) * len(d1))
    s2 = [0] * (len(c2) * len(d2))
    s3 = [0] * (len(c3) * len(d3))

    s1=XORing(c1,d1,s1)
    s2=XORing(c2,d2,s2)
    s3=XORing(c3,d3,s3)
    
    s1=convertBitToSignal(s1)
    s2=convertBitToSignal(s2)
    s3=convertBitToSignal(s3)
    
    Signal=[]
    for i in range(len(s1)):
        Signal.append(s1[i]+s2[i]+s3[i])
    
    return Signal

def XORing(c, d, s):
    k=0
    for i in range(len(d)):
        for j in range(len(c)):
            s[k] = d[i] ^ c[j]
            k+=1   
    return s  
    
def convertBitToSignal(arr):
    for i in range(len(arr)):
        if arr[i] == 0:
            arr[i] = 1
        else:
            arr[i] = -1
    return arr

import socket

c1 = list(map(int, input("Enter Chain Code 1: ").split()))
c2 = list(map(int, input("Enter Chain Code 2: ").split()))
c3 = list(map(int, input("Enter Chain Code 3: ").split()))
d1 = list(map(int, input("Enter Data Bit 1: ").split()))
d2 = list(map(int, input("Enter Data Bit 2: ").split()))
d3 = list(map(int, input("Enter Data Bit 3: ").split()))

print(chain_encode(c1,c2,c3,d1,d2,d3))

udp=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
udp.bind(('Localhost',12345))

print("Transmitting Signal...")

while True:
    data, addr = udp.recvfrom(1024)
    print(f"{data.decode()} from {addr}")
    Signal = chain_encode(c1,c2,c3,d1,d2,d3)
    data = str(Signal).encode()
    udp.sendto(data, addr)
