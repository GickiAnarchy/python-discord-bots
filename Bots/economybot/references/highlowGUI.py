import cards
import time
from PIL import Image, ImageTk
import tkinter as tk

deck = Deck()

window = tk.Tk()

mainframe = tk.Frame(master=window)

mainframe.pack(expand = True)

for i in range(3):
    for j in range(5):
        
        frame = tk.Frame(master=mainframe, relief=tk.RAISED, borderwidth=5)
        frame.grid(row=i, column=j)
        lbl = tk.Label(master = frame)
        lbl.pack()
 
window.mainloop()