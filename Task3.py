import tkinter as tk

def convert_temperature():
    try:
        temperature = float(entry.get())
        if var.get() == 1:
            result = (temperature - 32) * 5/9
            label_result.config(text=f"Celsius: {result:.2f}°C")
        else:
            result = (temperature * 9/5) + 32
            label_result.config(text=f"Fahrenheit: {result:.2f}°F")
    except ValueError:
        label_result.config(text="Invalid input!")


root = tk.Tk()
root.title("Temperature Converter")


entry = tk.Entry(root, width=20)
entry.pack()


var = tk.IntVar()
radio_fahrenheit = tk.Radiobutton(root, text="Fahrenheit to Celsius", variable=var, value=1)
radio_celsius = tk.Radiobutton(root, text="Celsius to Fahrenheit", variable=var, value=2)
radio_fahrenheit.pack()
radio_celsius.pack()


convert_button = tk.Button(root, text="Convert", command=convert_temperature)
convert_button.pack()

label_result = tk.Label(root, text="")
label_result.pack()


root.mainloop()
