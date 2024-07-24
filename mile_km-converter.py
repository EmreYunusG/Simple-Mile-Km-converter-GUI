from tkinter import *

def converter():
    inp = input.get()
    mile = 1.609344
    if radio_state.get() == 1:
        km = float(inp) * mile
        km = round(km, 2)
        result_label.config(text=km)
        from_label.config(text="Miles")
        to_label.config(text="Km")
    elif radio_state.get() == 2:
        mil = float(inp) / mile
        mil = round(mil, 2)
        result_label.config(text=mil)
        from_label.config(text="Km")
        to_label.config(text="Miles")

# window
window = Tk()
window.title("Converter")
window.minsize(width=300, height=150)
window.config(padx=20, pady=20)

# Labels
is_equal_to_label = Label(text="is equal to", font=("Arial", 10))
is_equal_to_label.grid(row=1, column=1)

result_label = Label(width=15, text="0")
result_label.grid(row=1, column=2)

to_label = Label(text="Km", font=("Arial", 10))
to_label.grid(row=1, column=3)

input = Entry(width=15)
input.grid(row=0, column=2)

from_label = Label(text="Miles", font=("Arial", 10))
from_label.grid(row=0, column=3)

# Button
button = Button(text="Convert", command=converter)
button.grid(row=2, column=2)

# Radiobuttons
radio_state = IntVar()
radio_state.set(1)

miles_to_km_option = Radiobutton(text="Miles to Km", value=1, variable=radio_state, command=converter)
miles_to_km_option.grid(row=3, column=2)

km_to_miles_option = Radiobutton(text="Km to Miles", value=2, variable=radio_state, command=converter)
km_to_miles_option.grid(row=4, column=2)

window.mainloop()


