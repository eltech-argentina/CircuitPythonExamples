import time # librería delay
import board # librería de placas
from digitalio import DigitalInOut, Direction, Pull  # importar función entrada y salida y pull-ups

led = DigitalInOut(board.D13) # definir pin de LED
led.direction = Direction.OUTPUT # definir salida

switch = DigitalInOut(board.D5)  # definir pin boton
switch.direction = Direction.INPUT # definir entrada
switch.pull = Pull.UP # definir pull up

while True: # loop
    if switch.value:
        led.value = False
    else:
        led.value = True

    time.sleep(0.01)  # delay anti rebote