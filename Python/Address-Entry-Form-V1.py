import tkinter as tk

window = tk.Tk()

f_name = tk.Label(text="First Name:")
l_name = tk.Label(text="Last Name:")
adr = tk.Label(text="Address:")
city = tk.Label(text="City:")
prov = tk.Label(text="Province:")
ps_code = tk.Label(text="Postal Code:")
country = tk.Label(text="Country:")

f_name.grid(row=0, column=0)
l_name.grid(row=1, column=0)
adr.grid(row=2, column=0)
city.grid(row=3, column=0)
prov.grid(row=4, column=0)
ps_code.grid(row=5, column=0)
country.grid(row=6, column=0)

ety1 = tk.Entry(width=50)
ety2 = tk.Entry(width=50)
ety3 = tk.Entry(width=50)
ety4 = tk.Entry(width=50)
ety5 = tk.Entry(width=50)
ety6 = tk.Entry(width=50)
ety7 = tk.Entry(width=50)

ety1.grid(row=0, column=1)
ety2.grid(row=1, column=1)
ety3.grid(row=2, column=1)
ety4.grid(row=3, column=1)
ety5.grid(row=4, column=1)
ety6.grid(row=5, column=1)
ety7.grid(row=6, column=1)

btn1 = tk.Button(text="Clear")
btn2 = tk.Button(text="Submit")

btn1.grid(row=7, column=1)
btn2.place(x=300, y=150)

window.mainloop()
