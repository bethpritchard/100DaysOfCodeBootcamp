from tkinter import *
FONT = ("Arial",16, "normal")


window = Tk()
window.title("Distance converter")
window.minsize(width=300, height= 200)
window.config(padx = 10, pady=50)

# Text on screen

miles_label = Label(text = "miles", font = FONT)
miles_label.grid(column = 3, row = 1)
# miles_label.config(padx=50, pady=50)

equals_label = Label(text = "is equal to", font = FONT)
equals_label.grid(column = 1, row = 2)
# equals_label.config(padx=50, pady=50)

km_label = Label(text = "km", font = FONT)
km_label.grid(column = 3, row = 2)

km_converted = Label(text="0", font = FONT)
km_converted.grid(column = 2, row = 2)


# Miles input button

miles_enter = Entry(width=10, font = FONT)
# Add some text to begin with
miles_enter.insert(END, string="0")
# Gets text in entry

miles_enter.grid(column = 2, row = 1)


# Calculate button

def m_convert_km():
    miles = int(miles_enter.get())
    km_converted["text"] = str(int(miles*8/5))


calculate_button = Button(text = "Calculate", font = FONT, command = m_convert_km)
calculate_button.grid(column = 2, row = 3)













window.mainloop()
