from machine import Pin, PWM
from utime import sleep
piezo = PWM(Pin(28))

def play_note(note, note_length):
    if note_length == "half":
        length = 1
    elif note_length == "quarter":
        length = 0.5
    elif note_length == "sixteenth":
        length = 0.125
    elif note_length == "eight_dotted":
        length = 0.375
    else:
        length = 1
        
    piezo.duty_u16(65000)
    piezo.freq(note)
    sleep(length)
    piezo.duty_u16(0)
    sleep(0.01)