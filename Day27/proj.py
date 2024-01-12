import tkinter


def calc():
    initial_val = input.get()
    try:
        initial_val = float(initial_val)
        converted_val = initial_val * 1.60934
        res.config(text=str(converted_val))
    except ValueError:
        res.config(text='Invalid Input')


window = tkinter.Tk()
window.title('Miles to Km Converter')
window.minsize(width=200, height=100)
window.config(padx=100, pady=100)

lab = tkinter.Label(text='is equal to', font=('Arial', 12, 'normal'))
lab.grid(column=0, row=1)

input_num = tkinter.StringVar()
input = tkinter.Entry(width=10, textvariable=input_num)
# input.pack()
input.grid(column=2, row=0)
miles = tkinter.Label(text='Miles', font=('Arial', 12, 'normal'))
miles.grid(column=3, row=0)
km = tkinter.Label(text='Km', font=('Arial', 12, 'normal'))
km.grid(column=3, row=1)

res = tkinter.Label(text='', font=('Arial', 12, 'normal'))
res.grid(column=2, row=1)

button = tkinter.Button(text='Calculate', command=calc)
button.grid(column=2, row=2)


window.mainloop()
