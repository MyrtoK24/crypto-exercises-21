import math
from random import *
import sys

def fastermod(factor,power,modulus):

    result = 1;
    while(power > 0):
        if (power % 2 == 1):
            result = (result*factor) % modulus
            power -=1

        power = power//2
        factor = (factor*factor)%modulus

    return result


def isPrime(inputNum,s,numTrials):


    # step counter
    s += 1;

    # run through numTrials
    for trial in range(numTrials):
        # increment step counter
        s += 6;

        # generate a between 1 and inputNum - 1
        randTest = randint(1,inputNum-1)
        
        # check if common factor exists
        # fermat test
        if (fastermod(randTest,inputNum-1,inputNum)!=1):
       # must be composite
           return False
    # end for loop

    return True



num = [67280421310721,170141183460469231731687303715884105721,2**2281 - 1,2**9941 - 1,2**19939 - 1]
trials = 20
steps = 1

for i in num:
    print(isPrime(i,steps,trials))
