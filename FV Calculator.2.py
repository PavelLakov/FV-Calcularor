import tkinter as tk
from tkinter import messagebox
import matplotlib.pyplot as plt


def calculate_fv():
    try:
        principal = float(principal_entry.get())
        rate = float(rate_entry.get())
        years = int(years_entry.get())
    except ValueError:
        messagebox.showerror('Error', 'Please enter valid input')
        return

    future_values = []
    for year in range(1, years + 1):
        future_value = round(principal * (1 + rate / 100) ** year, 2)
        future_values.append(future_value)
        output_text.insert(tk.END, f'Year {year}: {future_value}\n')

    plt.plot(range(1, years + 1), future_values)
    plt.title('Future Value over Time')
    plt.xlabel('Years')
    plt.ylabel('Future Value')
    plt.show()


def exit_program():
    window.destroy()


window = tk.Tk()
window.title('FV Calculator')

principal_label = tk.Label(window, text='Principal:')
principal_label.grid(column=0, row=0)

principal_entry = tk.Entry(window)
principal_entry.grid(column=1, row=0)

rate_label = tk.Label(window, text='Interest Rate (%):')
rate_label.grid(column=0, row=1)

rate_entry = tk.Entry(window)
rate_entry.grid(column=1, row=1)

years_label = tk.Label(window, text='Years:')
years_label.grid(column=0, row=2)

years_entry = tk.Entry(window)
years_entry.grid(column=1, row=2)

calculate_button = tk.Button(window, text='Calculate FV', command=calculate_fv)
calculate_button.grid(column=0, row=3)

exit_button = tk.Button(window, text='Exit', command=exit_program)
exit_button.grid(column=1, row=3)

output_text = tk.Text(window)
output_text.grid(column=0, row=4, columnspan=2)

plt.rcParams["figure.figsize"] = (8, 6)
plt.rcParams.update({'font.size': 10})

window.mainloop()

