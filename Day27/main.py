import tkinter

window = tkinter.Tk()
window.title('First GUI Program')
window.minsize(width=500, height=300)

# Label
labool = tkinter.Label(text='I am a label', font=('Arial', 24, 'bold'))
labool.pack(side="left")


window.mainloop()
