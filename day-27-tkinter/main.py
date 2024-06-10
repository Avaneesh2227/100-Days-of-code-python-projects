from tkinter import *

window=Tk()
window.title("Miles to Km")
window.config(padx=20, pady=20)

def miles_to_km():
    km= float(miles_input.get()) * 1.609
    kilo_result.config(text=f"{km}")


miles_input=Entry(width=5)
miles_input.grid(column=1,row=0)
miles_label=Label(text="Miles")
miles_label.grid(column=2,row=0)
is_equal=Label(text="is equal to")
is_equal.grid(column=0,row=1)
kilo_result=Label(text="0")
kilo_result.grid(column=1,row=1)
kilometer=Label(text="Km")
kilometer.grid(column=2,row=1)
calculate=Button(text="Calculate", command=miles_to_km)
calculate.grid(column=1,row=2)






window.mainloop()

