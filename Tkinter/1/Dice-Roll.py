import tkinter as tk
import random

window = tk.Tk()


def roll():
    num = random.randint(1, 6)
    lbl_value["text"] = num


window.rowconfigure([0, 1], minsize=50, weight=1)
window.columnconfigure(0, minsize=50, weight=2)

btn_roll = tk.Button(master=window, text="roll", command=roll)
btn_roll.grid(row=0, column=0, sticky="nsew")

lbl_value = tk.Label(master=window, text="0")
lbl_value.grid(row=1, column=0)

window.mainloop()
