from data.notes import notes
from data.songs import happy_birthday
from utils import play
from io.io_definitions import button

if __name__ == "__main__":
    while True:
        button_state = button.value()
        if button_state == True:
            for note_and_lenght in happy_birthday:
                note = notes[note_and_lenght[0]]
                play.play_note(note, note_and_lenght[1])
