import tkinter as tk
from tkinter import scrolledtext
from suitescript_converter import convert_suitescript

# GUI Setup
def create_gui():
    def on_convert():
        input_code = input_text.get("1.0", tk.END)
        output_code = convert_suitescript(input_code)
        output_text.delete("1.0", tk.END)
        output_text.insert(tk.END, output_code)

    window = tk.Tk()
    window.title("SuiteScript 1.0 to 2.1 Converter")

    tk.Label(window, text="SuiteScript 1.0").grid(row=0, column=0)
    tk.Label(window, text="SuiteScript 2.1").grid(row=0, column=1)

    input_text = scrolledtext.ScrolledText(window, width=40, height=20)
    input_text.grid(row=1, column=0, padx=10, pady=10)

    output_text = scrolledtext.ScrolledText(window, width=40, height=20)
    output_text.grid(row=1, column=1, padx=10, pady=10)

    convert_button = tk.Button(window, text="Convert", command=on_convert)
    convert_button.grid(row=2, column=0, columnspan=2, pady=10)

    window.mainloop()

create_gui()
