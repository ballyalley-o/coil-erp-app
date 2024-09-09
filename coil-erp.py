import math
import tkinter as tk
from tkinter import messagebox, font

def compute_coil_outer_diameter(L, iD, T):
    outer_diameter = round((math.sqrt((L * T) / math.pi + (iD / 2) ** 2) * 2) * 100) / 100
    return outer_diameter

def compute_coil_length(oD, iD, T):
    length = round(((math.pi * (oD**2 - iD**2)) / (4 * T)) * 100) / 100
        if unit_var.get() == 'I':
            length = length / 12
        else :
            length = length / 1000
    return length

def convert_to_imperial(value, from_metric=True):
    """ Convert between metric (mm) and imperial (inches) """
    if from_metric:
        return value / 25.4
    else:
        return value * 25.4

def update_fields():
    if operation_var.get() == 'OD':
        length_entry.config(state="normal")
        outer_dia_entry.config(state="disabled")
    elif operation_var.get() == 'L':
        length_entry.config(state="disabled")
        outer_dia_entry.config(state="normal")

def calculate():
    try:
        L = float(length_entry.get()) if length_entry.get() else None
        oD = float(outer_dia_entry.get()) if outer_dia_entry.get() else None
        iD = float(inner_dia_entry.get())
        T = float(thickness_entry.get())

        if unit_var.get() == 'M':
            conversion_needed = True
            unit = "mm"
        else:
            conversion_needed = False
            unit = "inches"

        if operation_var.get() == 'OD':
            if not L:
                messagebox.showerror("Input Error", "Please enter coil length")
                return

            if conversion_needed:
                L = convert_to_imperial(L, from_metric=True)
                iD = convert_to_imperial(iD, from_metric=True)
                T = convert_to_imperial(T, from_metric=True)

            result = compute_coil_outer_diameter(L, iD, T)
            if conversion_needed:
                result = convert_to_imperial(result, from_metric=False)

            result_label.config(text=f"Outer Diameter: {result:.2f} {unit}", font=result_font)

        elif operation_var.get() == 'L':
            if not oD:
                messagebox.showerror("Input Error", "Please enter outer diameter")
                return

            if conversion_needed:
                oD = convert_to_imperial(oD, from_metric=True)
                iD = convert_to_imperial(iD, from_metric=True)
                T = convert_to_imperial(T, from_metric=True)

            result = compute_coil_length(oD, iD, T)
            if conversion_needed:
                result = convert_to_imperial(result, from_metric=False)

            result_label.config(text=f"Coil Length: {result:.2f} {unit}", font=result_font)

    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numeric values")

root = tk.Tk()
root.title("Coil Calculator")

result_font = font.Font(family="Helvetica", size=16, weight="bold")

unit_var = tk.StringVar(value="I")
root.geometry("500x500")
root.eval('tk::PlaceWindow . center')

tk.Label(root, text="Select Unit System").grid(row=0, column=0, columnspan=2)
tk.Radiobutton(root, text="Imperial (inches)", variable=unit_var, value="I").grid(row=1, column=0)
tk.Radiobutton(root, text="Metric (mm)", variable=unit_var, value="M").grid(row=1, column=1)

operation_var = tk.StringVar(value="OD")
tk.Label(root, text="Select Operation").grid(row=2, column=0, columnspan=2)
tk.Radiobutton(root, text="Calculate Outer Diameter", variable=operation_var, value="OD", command=update_fields).grid(row=3, column=0)
tk.Radiobutton(root, text="Calculate Coil Length", variable=operation_var, value="L", command=update_fields).grid(row=3, column=1)

tk.Label(root, text="Coil Length (L)").grid(row=4, column=0)
length_entry = tk.Entry(root)
length_entry.grid(row=4, column=1)

tk.Label(root, text="Outer Diameter (OD)").grid(row=5, column=0)
outer_dia_entry = tk.Entry(root)
outer_dia_entry.grid(row=5, column=1)

tk.Label(root, text="Inner Diameter (iD)").grid(row=6, column=0)
inner_dia_entry = tk.Entry(root)
inner_dia_entry.grid(row=6, column=1)

tk.Label(root, text="Thickness (T)").grid(row=7, column=0)
thickness_entry = tk.Entry(root)
thickness_entry.grid(row=7, column=1)

result_label = tk.Label(root, text="Result will be displayed here", fg="white", font=("Helvetica", 20, "bold"), padx=10, pady=10)
result_label.grid(row=8, column=0, columnspan=2)

calculate_button = tk.Button(root, text="Calculate", command=calculate)
calculate_button.grid(row=9, column=0, columnspan=2)

update_fields()

root.mainloop()