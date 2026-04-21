from tkinter import *

# Create window
root = Tk()
root.title("Weight Converter")
root.geometry("400x200")

# Function to convert weight
def convert():
    kg = float(entry_kg.get())
    
    gram = kg * 1000
    pound = kg * 2.20462
    ounce = kg * 35.274
    
    text_gram.delete("1.0", END)
    text_gram.insert(END, gram)
    
    text_pound.delete("1.0", END)
    text_pound.insert(END, pound)
    
    text_ounce.delete("1.0", END)
    text_ounce.insert(END, ounce)

# Input
Label(root, text="Enter the weight in Kg").grid(row=0, column=0, padx=10, pady=10)
entry_kg = Entry(root)
entry_kg.grid(row=0, column=1)

# Button
Button(root, text="Convert", command=convert).grid(row=0, column=2, padx=10)

# Output Labels
Label(root, text="Gram").grid(row=1, column=0)
Label(root, text="Pounds").grid(row=1, column=1)
Label(root, text="Ounce").grid(row=1, column=2)

# Output Textboxes
text_gram = Text(root, height=1, width=10)
text_gram.grid(row=2, column=0)

text_pound = Text(root, height=1, width=10)
text_pound.grid(row=2, column=1)

text_ounce = Text(root, height=1, width=10)
text_ounce.grid(row=2, column=2)

# Run GUI
root.mainloop()