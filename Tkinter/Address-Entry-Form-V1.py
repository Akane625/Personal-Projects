import tkinter as tk

window = tk.Tk()
window.title("Address Entry Form")

f_name = tk.Label(text="First Name:")
l_name = tk.Label(text="Last Name:")
adr = tk.Label(text="Address:")
city = tk.Label(text="City:")
prov = tk.Label(text="Province:")
ps_code = tk.Label(text="Postal Code:")
country = tk.Label(text="Country:")

ety1 = tk.Entry(width=50)
ety2 = tk.Entry(width=50)
ety3 = tk.Entry(width=50)
ety4 = tk.Entry(width=50)
ety5 = tk.Entry(width=50)
ety6 = tk.Entry(width=50)
ety7 = tk.Entry(width=50)

row1 = 0
for i in [f_name, l_name, adr, city, prov, ps_code, country]:
    i.grid(row=row1, column=0)
    row1 += 1

row2 = 0
for i in [ety1, ety2, ety3, ety4, ety5, ety6, ety7]:
    i.grid(row=row2, column=1)
    row2 += 1

btn1 = tk.Button(text="Clear")
btn2 = tk.Button(text="Submit")

btn1.grid(row=7, column=1)
btn2.place(x=300, y=150)

window.mainloop()
