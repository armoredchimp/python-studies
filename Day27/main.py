import tkinter


def button_clicked():
    # or could have input_text = input.get()
    labool.config(text=input_text.get())


window = tkinter.Tk()
window.title('First GUI Program')
window.minsize(width=500, height=300)
window.config(padx=100, pady=100)

# Label
labool = tkinter.Label(text='I am a label', font=('Arial', 24, 'bold'))
labool.pack()


labool['text'] = 'new Text'
labool.config(text='labool')
# labool.place(x=0,y=23)
# relative to other components, this is the same as 0, 0 since only grid item
labool.grid(column=0, row=0)
labool.config(padx=20, pady=20)

# button


button = tkinter.Button(text='Click Me', command=button_clicked)
# button.pack()
button.grid(column=1, row=1)

new_button = tkinter.Button(text='No')
new_button.grid(column=2, row=0)

# Entry
input_text = tkinter.StringVar()
input = tkinter.Entry(width=10, textvariable=input_text)
# input.pack()
input.grid(column=3, row=2)

window.mainloop()
