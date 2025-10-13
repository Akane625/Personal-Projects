import tkinter as tk

window = tk.Tk()
window.title("Address Entry Form")

frame = tk.Frame(master=window, relief=tk.SUNKEN, borderwidth=3)
frame.grid(row=0, column=0)

f_name = tk.Label(master=frame, text="First Name:")
l_name = tk.Label(master=frame, text="Last Name:")
adr = tk.Label(master=frame, text="Address:")
city = tk.Label(master=frame, text="City:")
prov = tk.Label(master=frame, text="Province:")
ps_code = tk.Label(master=frame, text="Postal Code:")
country = tk.Label(master=frame, text="Country:")

row1 = 0
for i in [f_name, l_name, adr, city, prov, ps_code, country]:
    i.grid(row=row1, column=0, sticky="e")
    row1 += 1

ety1 = tk.Entry(master=frame, width=50)
ety2 = tk.Entry(master=frame, width=50)
ety3 = tk.Entry(master=frame, width=50)
ety4 = tk.Entry(master=frame, width=50)
ety5 = tk.Entry(master=frame, width=50)
ety6 = tk.Entry(master=frame, width=50)
ety7 = tk.Entry(master=frame, width=50)

row2 = 0
for i in [ety1, ety2, ety3, ety4, ety5, ety6, ety7]:
    i.grid(row=row2, column=1, sticky="e")
    row2 += 1


frame_button = tk.Frame()
frame_button.grid(row=1, column=0, ipadx=5, ipady=5)

btn1 = tk.Button(master=frame_button, text="Submit")
btn2 = tk.Button(master=frame_button, text="Clear")

btn1.grid(row=0, column=1, padx=5, ipadx=5)
btn2.grid(row=0, column=0, ipadx=5)

window.mainloop()
