from tkinter import *


def add_label():
    label_1 = Label(my_window,
                    text='Hello World')
    label_1.pack()


my_window = Tk()

my_window.geometry('200x100')

# 25. INTRODUCTION TO PYTHON TKINTER BUTTON
button_1 = Button(my_window,
                  text='Click Me',
                  command=add_label)

button_1.pack()

my_window.mainloop()
