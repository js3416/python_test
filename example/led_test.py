import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD) # set board mode to Broadcom

GPIO.setup(3, GPIO.OUT)
GPIO.setup(5, GPIO.OUT)
GPIO.setup(7, GPIO.OUT)

colors = {'red':(1,0,0), 'green':(0,1,0), 'blue':(0,0,1)}
try:
    while True:
        color = input("color=")
        if color in colors:
            GPIO.output(3, 0)
            GPIO.output(5, 0)
            GPIO.output(7, 0)

        if color == 'red':
            GPIO.output(3, colors[0][0])
        elif color == "green":
            GPIO.output(5, colors[1][1])
            
        
        #GPIO.output(3, i&0x4)
        #GPIO.output(5, i&0x2)
        #GPIO.output(7, i&0x1)
        
        time.sleep(0.5)
finally:
   GPIO.cleanup() 

""" 
for i in range(0,30):
    print(i)
    GPIO.output(3, 1)
    GPIO.output(5, 0)
    GPIO.output(7, 0)

    #GPIO.output(3, i&0x4)
    #GPIO.output(5, i&0x2)
    #GPIO.output(7, i&0x1)
    
    i += 1
    time.sleep(0.5)

GPIO.cleanup()
"""
