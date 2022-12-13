from tkinter import *
colors = {
    'red': '#ff0000',
    'orange': '#FFA500',
}
root = Tk()
root.geometry('200x100')
label = Label(text='color')
entry = Entry(width=10)
button_frame = Frame()
button_red = Button(button_frame, bg='red')
button_orange = Button(button_frame, bg='orange')
button_yellow = Button(button_frame, bg='yellow')
button_green = Button(button_frame, bg='green')
button_lightblue = Button(button_frame, bg='lightblue')
button_blue = Button(button_frame, bg='blue')
button_magenta = Button(button_frame, bg='magenta')
label.pack()
entry.pack(fill=X)
button_frame.pack()
button_red.pack(side=LEFT)
button_orange.pack(side=LEFT)
button_yellow.pack(side=LEFT)
button_green.pack(side=LEFT)
button_lightblue.pack(side=LEFT)
button_blue.pack(side=LEFT)
button_magenta.pack(side=LEFT)
root.mainloop()
