#usr/bin/python3
from ADCDevice import *
import gpiozero
from gpiozero import Button
import mouse
import keyboard
button = Button('pin number') #when you find the pin number, replace 'pin number' with the actual pin number
button.when_pressed = mouse.click('left') # change it to button when you find the pin number
button2 = Button('other pin number') # type it in once, you find it.
button2.when_pressed = keyboard.press('r')
button3 = Button('pin number') # replace with real pin number oce you find it.
button3.when_pressed = keyboard.press('f')
# add joystick and other stuff later
from smbus2 import SMBus
import math

# Register
power_mgmt_1 = 0x6b
power_mgmt_2 = 0x6c

def read_byte(reg):
    return bus.read_byte_data(address, reg)

def read_word(reg):
    h = bus.read_byte_data(address, reg)
    l = bus.read_byte_data(address, reg+1)
    value = (h << 8) + l
    return value

def read_word_2c(reg):
    val = read_word(reg)
    if (val >= 0x8000):
        return -((65535 - val) + 1)
    else:
        return val

def dist(a,b):
    return math.sqrt((a*a)+(b*b))

def get_y_rotation(x,y,z):
    radians = math.atan2(x, dist(y,z))
    return -math.degrees(radians)

def get_x_rotation(x,y,z):
    radians = math.atan2(y, dist(x,z))
    return math.degrees(radians)

bus = smbus.SMBus(1) # bus = smbus.SMBus(0) fuer Revision 1
address = 0x68       # via i2cdetect

# Aktivieren, um das Modul ansprechen zu koennen
bus.write_byte_data(address, power_mgmt_1, 0)

gyroskop_xout = read_word_2c(0x43)
gyroskop_yout = read_word_2c(0x45)
gyroskop_zout = read_word_2c(0x47)
mouse.move(gryoskop_xout,gyroskkop_yout,gryoskop_zout)

def joystickfunction():
 while True:
  val_Z = gpiozero.input(12) # read digital value of axis Z 
val_Y = adc.analogRead(0) # read analog value of axis X and Y 
val_X = adc.analogRead(1)
mouse.move(vaal_x,val_y,val_z)
def safe_exit(signum, frame):
 from threading import Thread
from gpiozero import DistanceSensor

sensor = DistanceSensor(echo=20, trigger=21)

def safe_exit(signum, frame):
    exit(1)

def read_distance():
    while True:
        message = f"{sensor.value:1.2f} "
        return message
if message >= 1:
 def hi():
  if message >= 1:
   mouse.click('right')
  if  message is None:
   mouse.click('right')


read_distance()
main = '__main__'
if __name__ == '__main__':
 while true:
       main()

