from gpio import GPIO
import time
import math
import random

a=0
b=256
COMP=random.randint(0,255)
print (COMP)
j=int((a+b)/2)
while True:
    if COMP==j:
        print (j)
        break
    elif COMP>j:
        a=j
        j=int((a+b)/2)
        print("j =",j)
    elif COMP<j:
        b=j
        j=int((a+b)/2)
        print("j =",j)