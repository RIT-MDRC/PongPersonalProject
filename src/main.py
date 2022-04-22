from machine import Pin
led = Pin(25, Pin.OUT)

led.high()

# Pin Init

#Setup output pins, initialize as zero
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
#setup input pins, no pullups needed
L4 = Pin(13, Pin.IN)
L3 = Pin(12, Pin.IN)
L2 = Pin(11, Pin.IN)
L1 = Pin(10, Pin.IN)

#End Pin Init

# Simulation Init

# All Sizes measured in steps
#Instruction every 7.5 Nanoseconds *Some resrictions apply, Results may vary, batteries not included

stepConvertConstant = (25.4)/(0.01*16) #Converts from inches (convert to mm) / (mm per step * 16 for no micro step mode)

fieldLength = (7.8 * stepConvertConstant)
fieldWidth = (5.5 * stepConvertConstant)

PadHeight = (2.5 * stepConvertConstant)

ballHeight = ((1 + (3/8)) * stepConvertConstant)
ballWidth = (1.5 * stepConvertConstant)

#End simmulation init


