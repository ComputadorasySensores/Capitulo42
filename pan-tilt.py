from machine import Pin, PWM
import time

servo_pan = PWM(Pin(0))
servo_pan.freq(50)

servo_tilt = PWM(Pin(1))
servo_tilt.freq(50)

pan_mas = machine.Pin(16, machine.Pin.IN, machine.Pin.PULL_DOWN)
pan_menos = machine.Pin(17, machine.Pin.IN, machine.Pin.PULL_DOWN)

tilt_mas = machine.Pin(18, machine.Pin.IN, machine.Pin.PULL_DOWN)
tilt_menos = machine.Pin(19, machine.Pin.IN, machine.Pin.PULL_DOWN)

valor_pan = 4586  # valor inicial
valor_tilt = 4586 # valor inicial

incremento = 364  # 10 grados

servo_pan.duty_u16(valor_pan)
servo_tilt.duty_u16(valor_tilt)

while True:
    if pan_mas.value() == 1:
        valor_pan = valor_pan + incremento
        if valor_pan > 7862:  # limite 180 grados
            valor_pan = 7862
        servo_pan.duty_u16(valor_pan)
        time.sleep(0.5)
    if pan_menos.value() == 1:
        valor_pan = valor_pan - incremento
        if valor_pan < 1311:  # limite 0 grados
            valor_pan = 1311
        servo_pan.duty_u16(valor_pan)
        time.sleep(0.5)
        
    if tilt_mas.value() == 1:
        valor_tilt = valor_tilt + incremento
        if valor_tilt > 6406:  # limite 50 grados
            valor_tilt = 6406
        servo_tilt.duty_u16(valor_tilt)
        time.sleep(0.5)
    if tilt_menos.value() == 1:
        valor_tilt = valor_tilt - incremento
        if valor_tilt < 3130:  # limite 130 grados
            valor_tilt = 3130
        servo_tilt.duty_u16(valor_tilt)
        time.sleep(0.5)
    
