#!/usr/bin/env python3

import sys
import collections
import statistics
from collections import deque
from math import ceil
from operator import itemgetter

def freqEN(i):
    letterFrequency =  {'E': 12.70, 'T': 9.06, 'A': 8.17, 'O': 7.51, 'I': 6.97, 'N': 6.75, 'S': 6.33, 'H': 6.09, 'R': 5.99, 'D': 4.25, 'L': 4.03, 'C': 2.78, 'U': 2.76, 'M': 2.41, 'W': 2.36, 'F': 2.23, 'G': 2.02, 'Y': 1.97, 'P': 1.93, 'B': 1.29, 'V': 0.98, 'K': 0.77, 'J': 0.15, 'X': 0.15, 'Q': 0.10, 'Z': 0.07}
    return letterFrequency[i]


#calculate MIC
def MIC(Q):
    return sum(((freqEN(chr(i+65)) * freq(i,Q)))/len(Q) for i in range(26))

def freq(i,Q):
    A = deque([])
    for a in range(26):
        A.append(0)
    for j in range(len(Q)):
        if Q[j] != -1:
            A[Q[j]] += 1
    return A[i]

def num_of_letters(L):
    c = 0
    for i in range(26):
      val =  L.count(i)
      if val!=0:
          c+=1
      return c

def ic(L):
  num = 0.0
  den = 0.0
  c = 0
  for i in range(26):
    val =  L.count(i)
    num += val * (val - 1)
    den += val
  if (den == 0.0):
    return 0.0

  else:
    return num / ( den * (den - 1))

file = sys.argv[1]
f = open(file, "r")
text = ""
C = deque([])
K = deque([])
M = deque([])

for i in f.read():
    text += i
    if i.isalpha():
        C.append(ord(i)-65)


c_length = len(C)
IC_x = deque([])

#if key length is 1 the problem responds to a Caesar cipher problem
key_length = 1
min = 100
shift0 = 0
icx0 = -1
for i in range(26):
    for m in C:
        M.append((m - i) % 26)

    icx = ic(M)
    icx_dif = abs(icx - 0.065)
    if (icx_dif < min):
        min = icx_dif
        shift0 = i
        icx0 = icx

IC_x.append(icx0)

for key_length in range(2,11):
    icx = deque([])
    IC_x.append(0)
    cols,rows = (key_length, ceil(c_length/key_length))
    A = [[0 for i in range(cols)] for j in range(rows)]

    for i in range(rows):
        for j in range(cols):

            if ((i*key_length) + j < c_length):
                A[i][j] = C[(i*key_length)+ j]
            else:
                A[i][j] = -1

    for j in range(cols):
        icx.append(ic(A[:][j]))


    IC_x[key_length-1] = statistics.median(icx)

ic_arr = deque([])
length_of_key = 2

ic_arr.append([IC_x[0],min, 1])
for x in IC_x:
    ic_arr.append([abs(x - 0.065),x, length_of_key])
    length_of_key += 1

ic_arr = sorted(ic_arr, key=itemgetter(0))
#for x,y,z in ic_arr:
#    print( "IC = ",y , " for key length ",  z  , end = "\n")



for tries in range(10):
    print("Try ", tries+1)
    k_len = ic_arr[tries][2]
    final_ic = deque([])
    shifts = [-1 for i in range(k_len)]
    for j in range(k_len):
        if k_len == 1:
            shifts[j] = shift0
        else:
            L = deque([])
            for i in range(ceil(c_length/k_len)):
                if (i*k_len)+j < c_length:
                    L.append(C[(i*k_len)+j])

            max = 0
            for shift in range(26):
                shifted_L = [ (x - shift) % 26 for x in L]
                micx = MIC(shifted_L)
                if micx > max :
                    shifts[j] = shift
                    max = micx


    possible_key = [0 for i in range(k_len)]

    print("A possible key is: ")

    for j in shifts:
        print(chr(j+65),end = "")
    print("\n")


    print("The decrypted text is: ")

    X = deque([])
    counter = 0
    while counter < c_length:
        for t in text:
            if t.isalpha():
                x_i = (C[counter] - shifts[counter % k_len])% 26
                X.append(x_i)
                if t.isupper():
                    print(chr(x_i+65),end = "")
                elif t.islower():
                    print(chr(x_i+65).lower(),end = "")
                counter +=1
            else:
                print(t,end = "")

    print("\n")
    print("Index Of Coincidence : ", ic(X))
    print("\n")
