import tkinter as tk
import winsound
import threading

def play_sound(filename):
    def _play():
        winsound.PlaySound(filename, winsound.SND_FILENAME)
    threading.Thread(target=_play).start()

def cal(event=None):
    b1.config(relief=tk.SUNKEN)
    play_sound('nota-do.wav')
    b1.after(30, lambda: b1.config(relief=tk.RAISED))

def re(event=None):
    b2.config(relief=tk.SUNKEN)
    play_sound('nota-re.wav')
    b2.after(30, lambda: b2.config(relief=tk.RAISED))

def mi(event=None):
    b3.config(relief=tk.SUNKEN)
    play_sound('nota-mi.wav')
    b3.after(30, lambda: b3.config(relief=tk.RAISED))

def fa(event=None):
    b4.config(relief=tk.SUNKEN)
    play_sound('nota-fa.wav')
    b4.after(30, lambda: b4.config(relief=tk.RAISED))

def sol(event=None):
    b5.config(relief=tk.SUNKEN)
    play_sound('nota-sol.wav')
    b5.after(30, lambda: b5.config(relief=tk.RAISED))

def la(event=None):
    b6.config(relief=tk.SUNKEN)
    play_sound('nota-lya.wav')
    b6.after(30, lambda: b6.config(relief=tk.RAISED))

def si(event=None):
    b7.config(relief=tk.SUNKEN)
    play_sound('nota-si.wav')
    b7.after(30, lambda: b7.config(relief=tk.RAISED))

def otomatik():
    pass

pencere = tk.Tk()
pencere.title('Piyano')
pencere.geometry('520x400')

b1 = tk.Button(pencere, text='Do', font='Verdana 14 bold', bg='white', fg='black', height=10, width=3, command=cal)
b1.place(x=50, y=20)

b2 = tk.Button(pencere, text='Re', font='Verdana 14 bold', bg='white', fg='black', height=10, width=3, command=re)
b2.place(x=110, y=20)

b3 = tk.Button(pencere, text='Mi', font='Verdana 14 bold', bg='white', fg='black', height=10, width=3, command=mi)
b3.place(x=170, y=20)

b4 = tk.Button(pencere, text='Fa', font='Verdana 14 bold', bg='white', fg='black', height=10, width=3, command=fa)
b4.place(x=230, y=20)

b5 = tk.Button(pencere, text='Sol', font='Verdana 14 bold', bg='white', fg='black', height=10, width=3, command=sol)
b5.place(x=290, y=20)

b6 = tk.Button(pencere, text='Lâ', font='Verdana 14 bold', bg='white', fg='black', height=10, width=3, command=la)
b6.place(x=350, y=20)

b7 = tk.Button(pencere, text='Si', font='Verdana 14 bold', bg='white', fg='black', height=10, width=3, command=si)
b7.place(x=410, y=20)

b8 = tk.Button(pencere, text='Otomatik', font='Verdana 14 bold', bg='white', fg='black', height=1, width=10, command=otomatik)
b8.place(x=175, y=300)

pencere.bind('<a>', cal)
pencere.bind('<s>', re)
pencere.bind('<d>', mi)
pencere.bind('<f>', fa)
pencere.bind('<g>', sol)
pencere.bind('<h>', la)
pencere.bind('<j>', si)

pencere.mainloop()
