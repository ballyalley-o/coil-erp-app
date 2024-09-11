import math
import tkinter as tk
from tkinter import messagebox, font, ttk

def compute_coil_outer_diameter(L, iD, T):
    outer_diameter = round((math.sqrt((L * T) / math.pi + (iD / 2) ** 2) * 2) * 100) / 100
    return outer_diameter

def compute_coil_length(oD, iD, T):
    length = round(((math.pi * (oD**2 - iD**2)) / (4 * T)) * 100) / 100
    return length

def compute_outer_dia_by_weight(weight, width, density, iD):
    outer_dia = 2 * math.sqrt(weight / (width * density * math.pi)) + (iD / 2) ** 2
    return round(outer_dia * 100) / 100

def convert_to_imperial(value, from_metric=True):
    """ Convert between metric (mm) and imperial (inches) """
    if from_metric:
        return value / 25.4  # mm to inches
    else:
        return value * 25.4  # inches to mm

def update_fields():
    if operation_var.get() == 'OD':
        length_entry.config(state="normal")
        outer_dia_entry.config(state="disabled")
        weight_entry.config(state="disabled")
        width_entry.config(state="disabled")
    elif operation_var.get() == 'L':
        length_entry.config(state="disabled")
        outer_dia_entry.config(state="normal")
        weight_entry.config(state="disabled")
        width_entry.config(state="disabled")
    elif operation_var.get() == 'WOD':
        length_entry.config(state="disabled")
        outer_dia_entry.config(state="disabled")
        weight_entry.config(state="normal")
        width_entry.config(state="normal")

def calculate():
    try:
        L = float(length_entry.get()) if length_entry.get() else None
        oD = float(outer_dia_entry.get()) if outer_dia_entry.get() else None
        iD = float(inner_dia_entry.get())
        T = float(thickness_entry.get())
        weight = float(weight_entry.get()) if weight_entry.get() else None
        width = float(width_entry.get()) if width_entry.get() else None

        if unit_var.get() == 'M':
            conversion_needed = True
            unit = "mm"
            density = float(density_var.get())
        else:
            conversion_needed = False
            unit = "inches"
            density = 0.2833  # 2833 kg/m³ = 2833 g/cm³ = 0.2833 g/mm³

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

        elif operation_var.get() == 'WOD':
            if not weight or not width:
                messagebox.showerror("Input Error", "Please enter weight and width")
                return

            if conversion_needed:
                iD = convert_to_imperial(iD, from_metric=True)
                width = convert_to_imperial(width, from_metric=True)

            result = compute_outer_dia_by_weight(weight, width, density, iD)
            if conversion_needed:
                result = convert_to_imperial(result, from_metric=False)

            result_label.config(text=f"Outer Diameter by Weight: {result:.2f} {unit}", font=result_font)

    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numeric values")

root = tk.Tk()
root.title("Coil Calculator")

result_font = font.Font(family="Helvetica", size=16, weight="bold")

unit_var = tk.StringVar(value="I")
tk.Label(root, text="Select Unit System").grid(row=0, column=0, columnspan=2)
tk.Radiobutton(root, text="Imperial (inches)", variable=unit_var, value="I").grid(row=1, column=0)
tk.Radiobutton(root, text="Metric (mm)", variable=unit_var, value="M").grid(row=1, column=1)

density_var = tk.StringVar(value="2850")
density_label = tk.Label(root, text="Density (kg/m³) [Metric Only]")
density_label.grid(row=2, column=0)
density_dropdown = ttk.Combobox(root, textvariable=density_var, state="readonly")
density_dropdown['values'] = ["2850", "2860", "2870", "2880", "2890"]
density_dropdown.grid(row=2, column=1)

operation_var = tk.StringVar(value="OD")
tk.Label(root, text="Select Operation").grid(row=3, column=0, columnspan=2)
tk.Radiobutton(root, text="Calculate Outer Diameter", variable=operation_var, value="OD", command=update_fields).grid(row=4, column=0)
tk.Radiobutton(root, text="Calculate Coil Length", variable=operation_var, value="L", command=update_fields).grid(row=4, column=1)
tk.Radiobutton(root, text="Calculate Outer Diameter by Weight", variable=operation_var, value="WOD", command=update_fields).grid(row=5, column=0, columnspan=2)

tk.Label(root, text="Coil Length (L)").grid(row=6, column=0)
length_entry = tk.Entry(root)
length_entry.grid(row=6, column=1)

tk.Label(root, text="Outer Diameter (OD)").grid(row=7, column=0)
outer_dia_entry = tk.Entry(root)
outer_dia_entry.grid(row=7, column=1)

tk.Label(root, text="Inner Diameter (iD)").grid(row=8, column=0)
inner_dia_entry = tk.Entry(root)
inner_dia_entry.grid(row=8, column=1)

tk.Label(root, text="Thickness (T)").grid(row=9, column=0)
thickness_entry = tk.Entry(root)
thickness_entry.grid(row=9, column=1)

tk.Label(root, text="Weight (W)").grid(row=10, column=0)
weight_entry = tk.Entry(root)
weight_entry.grid(row=10, column=1)

tk.Label(root, text="Width (W)").grid(row=11, column=0)
width_entry = tk.Entry(root)
width_entry.grid(row=11, column=1)

result_label = tk.Label(root, text="Result will be displayed here", fg="blue", font=result_font)
result_label.grid(row=12, column=0, columnspan=2)

calculate_button = tk.Button(root, text="Calculate", command=calculate)
calculate_button.grid(row=13, column=0, columnspan=2)

update_fields()

root.mainloop()