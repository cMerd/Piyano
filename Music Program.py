import tkinter as tk
import pygame
import threading

# @WARNING: Constants, do not edit or reassign
DEFAULT_FONT = "Verdana 14 bold"
DEFAULT_TITLE = "Piyano"
DEFAULT_WIDTH = 520
DEFAULT_HEIGHT = 400
DEFAULT_DIMENSIONS = str(DEFAULT_WIDTH) + 'x' + str(DEFAULT_HEIGHT)
BG_COL = "white"
FG_COL = "black"

KEY_HEIGHT = 10
KEY_WIDTH = 3


def play_sound(filename):
    def _play():
        pygame.mixer.Sound(filename).play()
    threading.Thread(target=_play).start()


def play_note(note, btn):
    # @param: note - string; name of note to be played (eg. 'do', 're', 'mi')
    # @param: btn - tkinter button: button to play animation on
    # @return: no return
    btn.config(relief=tk.SUNKEN)
    play_sound("./notes/nota-" + note + ".wav")
    btn.after(30, lambda: btn.config(relief=tk.RAISED))


def otomatik():
    # @TODO: Implement automation
    pass


if __name__ == "__main__":
    pygame.mixer.init()
    pencere = tk.Tk()
    pencere.title(DEFAULT_TITLE)
    pencere.geometry(DEFAULT_DIMENSIONS)

    b1 = tk.Button(pencere, text='Do', font=DEFAULT_FONT,
                   bg=BG_COL, fg=FG_COL, height=KEY_HEIGHT, width=KEY_WIDTH,
                   command=lambda: play_note('do', b1))
    b1.place(x=50, y=20)

    b2 = tk.Button(pencere, text='Re', font=DEFAULT_FONT,
                   bg=BG_COL, fg=FG_COL, height=KEY_HEIGHT, width=KEY_WIDTH,
                   command=lambda: play_note('re', b2))
    b2.place(x=110, y=20)

    b3 = tk.Button(pencere, text='Mi', font=DEFAULT_FONT,
                   bg=BG_COL, fg=FG_COL, height=KEY_HEIGHT, width=KEY_WIDTH,
                   command=lambda: play_note('mi', b3))
    b3.place(x=170, y=20)

    b4 = tk.Button(pencere, text='Fa', font=DEFAULT_FONT,
                   bg=BG_COL, fg=FG_COL, height=KEY_HEIGHT, width=KEY_WIDTH,
                   command=lambda: play_note('fa', b4))
    b4.place(x=230, y=20)

    b5 = tk.Button(pencere, text='Sol', font=DEFAULT_FONT,
                   bg=BG_COL, fg=FG_COL, height=KEY_HEIGHT, width=KEY_WIDTH,
                   command=lambda: play_note('sol', b5))
    b5.place(x=290, y=20)

    b6 = tk.Button(pencere, text='Lâ', font=DEFAULT_FONT,
                   bg=BG_COL, fg=FG_COL, height=KEY_HEIGHT, width=KEY_WIDTH,
                   command=lambda: play_note('lya', b6))
    b6.place(x=350, y=20)

    b7 = tk.Button(pencere, text='Si', font=DEFAULT_FONT,
                   bg=BG_COL, fg=FG_COL, height=KEY_HEIGHT, width=KEY_WIDTH,
                   command=lambda: play_note('si', b7))
    b7.place(x=410, y=20)

    b8 = tk.Button(pencere, text='Otomatik', font=DEFAULT_FONT,
                   bg=BG_COL, fg=FG_COL, height=1, width=10, command=otomatik)
    b8.place(x=175, y=300)

    pencere.bind('<a>', lambda event: play_note('do', b1))
    pencere.bind('<s>', lambda event: play_note('re', b2))
    pencere.bind('<d>', lambda event: play_note('mi', b3))
    pencere.bind('<f>', lambda event: play_note('fa', b4))
    pencere.bind('<g>', lambda event: play_note('sol', b5))
    pencere.bind('<h>', lambda event: play_note('lya', b6))
    pencere.bind('<j>', lambda event: play_note('si', b7))

    pencere.mainloop()
