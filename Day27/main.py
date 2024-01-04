import tkinter

window = tkinter.Tk()
window.title('First GUI Program')
window.minsize(width=500, height=300)

# Label
labool = tkinter.Label(text='I am a label', font=('Arial', 24, 'bold'))
labool.pack()


labool['text'] = 'new Text'
labool.config(text='labool')

# button


def button_clicked():
    labool.config(text=input_text.get())


button = tkinter.Button(text='Click Me', command=button_clicked)
button.pack()

# Entry
input_text = tkinter.StringVar()
input = tkinter.Entry(width=10, textvariable=input_text)
input.pack()


window.mainloop()
