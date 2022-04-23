from time import sleep
from machine import Pin

led = Pin(25, Pin.OUT)  # Light indicates program running
led.high()

# Pin Init

# Setup output pins, initialize as zero
D1 = Pin(14, Pin.OUT)
D1.value(0)
S1 = Pin(15, Pin.OUT)
S1.value(0)
S4 = Pin(16, Pin.OUT)
S4.value(0)
D4 = Pin(17, Pin.OUT)
D4.value(0)
S3 = Pin(18, Pin.OUT)
S3.value(0)
D3 = Pin(19, Pin.OUT)
D3.value(0)
S2 = Pin(20, Pin.OUT)
S2.value(0)
D2 = Pin(21, Pin.OUT)
D2.value(0)
# setup input pins, no pullups needed
L4 = Pin(13, Pin.IN)
L3 = Pin(12, Pin.IN)
L2 = Pin(11, Pin.IN)
L1 = Pin(10, Pin.IN)

# End Pin Init

# Simulation Init

# All Sizes measured in steps
# Instruction every 7.5 Nanoseconds *Some resrictions apply, Results may vary, batteries not included

stepConvertConstant = (25.4) / (
            0.01 * 16)  # Converts from inches (convert to mm) / (mm per step * 16 for no micro step mode)

fieldWidth = int(7.8 * stepConvertConstant)
fieldHeight = int(5.5 * stepConvertConstant)

padHeight = int(2.5 * stepConvertConstant)
leftPadBottomPos = 0
rightPadBottomPos = 0

ballHeight = int((1 + (3 / 8)) * stepConvertConstant)
ballWidth = int(1.5 * stepConvertConstant)

# End simulation init

ballX = int(fieldWidth / 2)
ballY = int(fieldHeight / 2)
ballIncrementX = 1
ballIncrementY = 1

while True:
    if (ballY >= fieldHeight):
        ballIncrementY *= -1
    if (ballY <= 0):
        ballIncrementY *= -1
    if (ballX >= fieldWidth):
        if (ballY >= rightPadBottomPos and ballY <= (rightPadBottomPos + padHeight)):
            ballIncrementX *= -1
        else:
            print("Left Score")
            # Score Fail state
    if (ballX <= 0):
        if (ballY >= leftPadBottomPos and ballY <= (leftPadBottomPos + padHeight)):
            ballIncrementX *= -1
        else:
            print("Right Score")
            # Score Fail state


def motor_Drive(mtr, steps, direction):
    match (mtr):
        case 1:
            # set direction
            if (direction == 'L' or direction == 'l'):
                D1.value(1)
            elif (direction == 'R' or direction == 'r'):
                D1.value(0)

            # Increment to steps from zero
            for x in range(0, steps):
                S1.value(1)
                sleep(0.001)
                S1.value(0)
                sleep(0.001)
            # Return pins to original state pins
            D1.value(0)
            S1.value(0)
        case 2:
            # set direction
            if (direction == 'L' or direction == 'l'):
                D2.value(1)
            elif (direction == 'R' or direction == 'r'):
                D2.value(0)

            # Increment to steps from zero
            for x in range(0, steps):
                S2.value(1)
                sleep(0.001)
                S2.value(0)
                sleep(0.001)
            # Return pins to original state pins
            D2.value(0)
            S2.value(0)
        case 3:
            # set direction
            if (direction == 'L' or direction == 'l'):
                D3.value(1)
            elif (direction == 'R' or direction == 'r'):
                D3.value(0)

            # Increment to steps from zero
            for x in range(0, steps):
                S3.value(1)
                sleep(0.001)
                S3.value(0)
                sleep(0.001)
            # Return pins to original state pins
            D3.value(0)
            S3.value(0)
        case 4:
            # set direction
            if (direction == 'L' or direction == 'l'):
                D4.value(1)
            elif (direction == 'R' or direction == 'r'):
                D4.value(0)

            # Increment to steps from zero
            for x in range(0, steps):
                S4.value(1)
                sleep(0.001)
                S4.value(0)
                sleep(0.001)
            # Return pins to original state pins
            D4.value(0)
            S4.value(0)
 def Homing():
    #Zero on Motor 1
    while L1 != 1:
        motor_Drive(1, 1, 'L')
    motor_Drive(1, 2, 'R') 
    
    #Zero on Motor 2
    while L2 != 1:
        motor_Drive(2, 1, 'L')
    motor_Drive(2, 2, 'R')  
    
    #Zero on Motor 3
    while L3 != 1:
        motor_Drive(3, 1, 'R')
    motor_Drive(3, 2, 'L')  
    
    #Zero on Motor 4
    while L4 != 1:
        motor_Drive(4, 1, 'R')
    motor_Drive(4, 2, 'L')
            
 def set_Point(x, y):
     if(x > ballX):
        while(x > ballX):
            motor_Drive(2, 1, 'L')
     elif(x < ballX):
        while(x < ballX):
            motor_Drive(2, 1, 'R')
            
     if(y > ballY):
        while(y > ballY):
            motor_Drive(3, 1, 'R')
     elif(y < ballY):
        while(y < ballY):
            motor_Drive(3, 1, 'L')
led.low()
