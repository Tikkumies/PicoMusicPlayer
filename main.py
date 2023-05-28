from machine import Pin, PWM
from resources.notes import notes
from resources.songs import happy_birthday
from utils import play

button = Pin(27, Pin.IN, Pin.PULL_DOWN)

if __name__ == "__main__":
    while True:
        button_state = button.value()
        if button_state == True:
            for note_and_lenght in happy_birthday:
                note = notes[note_and_lenght[0]]
                play.play_note(note, note_and_lenght[1])


        


        
