#!/usr/bin/env python3

import sys
import collections
from collections import deque

file = sys.argv[1]
f = open(file, "r")
text = ""
C = deque([])
K = deque([])

def freqEN(i):
    letterFrequency =  {'E': 12.70, 'T': 9.06, 'A': 8.17, 'O': 7.51, 'I': 6.97, 'N': 6.75, 'S': 6.33, 'H': 6.09, 'R': 5.99, 'D': 4.25, 'L': 4.03, 'C': 2.78, 'U': 2.76, 'M': 2.41, 'W': 2.36, 'F': 2.23, 'G': 2.02, 'Y': 1.97, 'P': 1.93, 'B': 1.29, 'V': 0.98, 'K': 0.77, 'J': 0.15, 'X': 0.15, 'Q': 0.10, 'Z': 0.07}
    return letterFrequency[i]

def freq(i,Q):
    A = deque([])
    for a in range(26):
        A.append(0)
    for j in range(len(Q)):
        A[Q[j]] += 1
    return A[i]

#calculate MIC
def MIC(Q,k):
    return sum((freqEN(chr(i+65)) * freq(i,Q))/(len(Q)) for i in range(26))


for i in f.read():
    text += str(i)
    if i.isalpha():
        C.append((ord(i.upper())-65))

key = "CRYPTOGRAPHY"
key_length = len(key)
c_length = len(C)
key_to_number = [ord(k)-65 for k in key]

for j in range (0,key_length):
    K.append(ord(key[j])-65)

max = 0
max_j = -1
for j in range(1,26):
    M = deque([])
    #try all possible keys
    for i in range(0,c_length):
        key_j = (K[i % key_length]- j) % 26
        x_i =  (C[i] - key_j ) % 26
        M.append(x_i)
    #find max MIC
    #print(MIC(M,j))
    if(MIC(M,j)>max):
        max = MIC(M,j)
        max_j = j

print("KEY IS:")
for i in K:
    print(chr(((i-max_j)%26) + 65),end = "")
print("\n")

print("DECRYPTED TEXT : ")
counter = 0
while counter < c_length:
    for t in text:
        if t.isalpha():
            key_j = (K[counter % key_length]- max_j) % 26
            x_i =  (C[counter] - key_j ) % 26
            if t.isupper():
                print(chr(x_i+65),end = "")
            elif t.islower():
                print(chr(x_i+65).lower(),end = "")
            counter +=1
        else:
            print(t,end = "")
print("")
