from tkinter import *

# Create window
root = Tk()
root.title("Calculator")
root.geometry("350x250")

# Variables
num1 = StringVar()
num2 = StringVar()
result = StringVar()

# Functions
def add():
    result.set(float(num1.get()) + float(num2.get()))

def sub():
    result.set(float(num1.get()) - float(num2.get()))

def mul():
    result.set(float(num1.get()) * float(num2.get()))

def div():
    if float(num2.get()) != 0:
        result.set(float(num1.get()) / float(num2.get()))
    else:
        result.set("Error")

# Labels and Entry fields
Label(root, text="Enter Number1:").grid(row=0, column=0, padx=10, pady=10)
Entry(root, textvariable=num1).grid(row=0, column=1)

Label(root, text="Enter Number2:").grid(row=1, column=0, padx=10, pady=10)
Entry(root, textvariable=num2).grid(row=1, column=1)

# Buttons
Button(root, text="+", width=5, command=add).grid(row=2, column=0, pady=10)
Button(root, text="-", width=5, command=sub).grid(row=2, column=1)

Button(root, text="*", width=5, command=mul).grid(row=3, column=0)
Button(root, text="/", width=5, command=div).grid(row=3, column=1)

# Result
Label(root, text="Answer is").grid(row=4, column=0, pady=10)
Entry(root, textvariable=result).grid(row=4, column=1)

# Run GUI
root.mainloop()