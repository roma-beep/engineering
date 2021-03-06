import RPi.GPIO as GPIO
#from gpio import GPIO
import time
import math
#import string
GPIO.setmode(GPIO.BCM)
GPIO.setup(26, GPIO.OUT)
GPIO.setup(19, GPIO.OUT)
GPIO.setup(13, GPIO.OUT)
GPIO.setup(6, GPIO.OUT)
GPIO.setup(5, GPIO.OUT)
GPIO.setup(11, GPIO.OUT)
GPIO.setup(9, GPIO.OUT)
GPIO.setup(10, GPIO.OUT)
GPIO.setup(17, GPIO.OUT)
GPIO.setup(4, GPIO.IN)


D=[26,19,13,6,5,11,9,10]
GPIO.output(21, 1)
def Let_it_light():
    for k in range (8):
        GPIO.output(D[k], 1) 

def Let_it_dark():
    for k in range (8):
        GPIO.output(D[k], 0)
     
def decToBinList(number):
    c=bin(number)[2:] 
    c=c[::-1] 
    s=[0, 0, 0, 0, 0, 0, 0, 0 ] 
    for k in range (len(c)):
        s[k]=int(c[k])        
    s.reverse()
    return s

def lightNumber(List_of_number):
    Let_it_dark()
    for i in range (7,-1,-1): 
        if List_of_number[i]==1:
            GPIO.output(D[i], List_of_number[i]) 
GPIO.output(17,1)
while True:
    c=0
    b=255
    j=int((c+b)/2)
    #Let_it_light1()
    #Let_it_dark1()
    while j:
        a=decToBinList(j)
        lightNumber(a)
        time.sleep(0.01)
        if b-c==2 :
            Voltage=int(((j*3.3)/256)*100)/100
            print("Digital value: ", j , ", Analog Value: ", Voltage, "V")
            break
        elif GPIO.input(4)==1:
            c=j
            j=int((c+b)/2)  
            #print(j)     
        elif GPIO.input(4)==0:
            b=j
            j=int((c+b)/2) 
            #print(j)    

    



