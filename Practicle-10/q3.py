from tkinter import *
from tkinter import font

# Create window
root = Tk()
root.title("Font Menu")
root.geometry("500x300")

# Available options
font_list = ["Times", "Verdana", "Arial", "Courier"]
style_list = ["normal", "italic", "bold", "bold italic"]
size_list = list(range(8, 31))

# Functions
def apply_font():
    f = listbox_font.get(ACTIVE)
    s = listbox_style.get(ACTIVE)
    sz = listbox_size.get(ACTIVE)

    weight = "normal"
    slant = "roman"

    if "bold" in s:
        weight = "bold"
    if "italic" in s:
        slant = "italic"

    my_font = font.Font(family=f, size=sz, weight=weight, slant=slant)
    label_sample.config(font=my_font)

# Labels
Label(root, text="Font").grid(row=0, column=0)
Label(root, text="Font Style").grid(row=0, column=1)
Label(root, text="Font Size").grid(row=0, column=2)

# Listboxes
listbox_font = Listbox(root, height=6)
for item in font_list:
    listbox_font.insert(END, item)
listbox_font.grid(row=1, column=0)

listbox_style = Listbox(root, height=6)
for item in style_list:
    listbox_style.insert(END, item)
listbox_style.grid(row=1, column=1)

listbox_size = Listbox(root, height=6)
for item in size_list:
    listbox_size.insert(END, item)
listbox_size.grid(row=1, column=2)

# Button
Button(root, text="Apply Font", command=apply_font).grid(row=2, column=1, pady=10)

# Sample Text
label_sample = Label(root, text="Sample", font=("Arial", 12))
label_sample.grid(row=3, column=1)

# Run GUI
root.mainloop()