from tkinter import *

top = Tk()

top.geometry("1500x1000")
def fun():
    print("Hello")

b1 = Button(top, text="Red", bg="yellow", command=fun, activeforeground="red", activebackground="pink", pady=10)

b2 = Button(top, text="Blue", fg="red", activeforeground="blue", activebackground="pink", pady=10)

b1.pack(side = LEFT)
b2.pack(side = TOP, fill=X)

top.mainloop()