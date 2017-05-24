tone_values = {'LA3': 220, 'F3': 174, 'C4': 261, 'E4': 329, 'F4': 349, 'Ab3': 207, 'LA4': 440, 'Ab4': 415,
'G4': 392, 'Gb4': 370, 'Bb3': 233, 'Eb4': 311, 'D4': 293, 'Db4': 277, 'B3': 247}

from machine import Pin, PWM
from time import sleep

pin_piezo = Pin(13, Pin.OUT)

def beep(tone, time):
    for key in tone_values:
        if key == tone:
            value = tone_values[key]
    pwm = PWM(pin_piezo, freq=value, duty = 512)
    sleep(time)
    pwm.deinit()
    sleep(1/20)

beep('LA3', 1/2)
beep('LA3', 1/2)
beep('LA3', 1/2)
beep('F3', 1/3)
beep('C4', 1/6)
beep('LA3', 1/2)
beep('F3', 1/3)
beep('C4', 1/6)
beep('LA3', 1/2)
sleep(1/2)
beep('E4', 1/2)
beep('E4', 1/2)
beep('E4', 1/2)
beep('F4', 1/3)
beep('C4', 1/6)
beep('Ab3', 1/2)
beep('F3', 1/3)
beep('C4', 1/6)
beep('LA3', 1/2)
sleep(1/2)
beep('LA4', 1/2)
beep('LA3', 1/3)
beep('LA3', 1/6)
beep('LA4', 1/2)
beep('Ab4', 1/3)
beep('G4', 1/6)
beep('Gb4', 1/10)
beep('E4', 1/10)
beep('F4', 1/10)
sleep(1/2)
beep('Bb3', 1/6)
beep('Eb4', 1/2)
beep('D4', 1/3)
beep('Db4', 1/6)
beep('C4', 1/10)
beep('B3', 1/10)
beep('C4', 1/10)
