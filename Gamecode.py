from tkinter import *
root =Tk()

button = Button(None,text="1",fg="yellow",bg="yellow")
button.pack(fill=X)


button = Button(None,text="4",fg="green",bg="green")
button.pack(side=BOTTOM,fill=X)

button = Button(None,text="2",fg="blue",bg="blue")
button.pack(side = RIGHT,fill=Y)

button = Button(None,text="3",fg="red",bg="red")
button.pack(side=LEFT,fill=Y)



root.mainloop()
