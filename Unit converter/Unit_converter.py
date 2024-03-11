import tkinter as tk
from tkinter import ttk


class UnitConverter:
    def __init__(self, master):
        self.master = master
        self.master.title("Unit Converter")
        self.master.geometry("600x400")

        self.text_title = tk.Label(master, text="Unit Converter", fg="dark green", font="Verdana 30 bold")
        self.text_title.place(x=120, y=0)

        self.temp_button = tk.Button(master, text="Temp", font="Verdana 15", command=self.temperature_converter)
        self.temp_button.place(x=20, y=80)

        self.length_button = tk.Button(master, text="Length", font="Verdana 15", command=self.length_converter)
        self.length_button.place(x=120, y=80)

        self.area_button = tk.Button(master, text="Area", font="Verdana 15", command=self.area_converter)
        self.area_button.place(x=230, y=80)

        self.volume_button = tk.Button(master, text="Volume", font="Verdana 15", command=self.volume_converter)
        self.volume_button.place(x=320, y=80)

        self.weight_button = tk.Button(master, text="Weight", font="Verdana 15", command=self.mass_converter)
        self.weight_button.place(x=440, y=80)

        self.from_value_label = tk.Label(master, text="From:", font="Verdana 12")
        self.from_value_label.place(x=100, y=180)

        self.to_value_label = tk.Label(master, text="To:", font="Verdana 12")
        self.to_value_label.place(x=350, y=180)

        self.from_value_entry = tk.Entry(master, font="Verdana 12")
        self.from_value_entry.place(x=50, y=220)

        self.to_value_entry = tk.Entry(master, font="Verdana 12", state="readonly")
        self.to_value_entry.place(x=300, y=220)

        self.from_unit_listbox = ttk.Combobox(master, values="", font="Verdana 12", state="readonly")
        self.from_unit_listbox.place(x=50, y=270)

        self.to_unit_listbox = ttk.Combobox(master, values="", font="Verdana 12", state="readonly")
        self.to_unit_listbox.place(x=300, y=270)

        self.calc_button_volume = None
        self.calc_button_area = None
        self.calc_button_length = None
        self.calc_button_temp = None
        self.calc_button_weight = None

    def temperature_converter(self):

        values = ["Celsius", "Kelvin", "Fahrenheit"]
        self.from_unit_listbox.config(values=values)
        self.to_unit_listbox.config(values=values)
        self.temp_button.config(state="disabled")
        self.weight_button.config(state="active")
        self.length_button.config(state="active")
        self.area_button.config(state="active")
        self.volume_button.config(state="active")

        self.from_unit_listbox.set("")
        self.to_unit_listbox.set("")

        self.to_value_entry.config(state="normal")
        self.to_value_entry.delete(0, tk.END)
        self.from_value_entry.delete(0, tk.END)
        self.to_value_entry.config(state="readonly")

        def callback_temp():
            from_value = self.from_value_entry.get()
            from_unit = self.from_unit_listbox.get()
            to_unit = self.to_unit_listbox.get()

            if not from_value:
                return

            try:
                from_value = float(from_value)
            except ValueError:
                self.to_value_entry.config(state="normal")
                self.to_value_entry.delete(0, tk.END)
                self.to_value_entry.insert(0, 'Invalid input')
                self.to_value_entry.config(state="readonly")
                return

            if from_unit == "Celsius" and to_unit == "Fahrenheit":
                result = (from_value * 9 / 5) + 32
                self.to_value_entry.config(state="normal")
                self.to_value_entry.delete(0, tk.END)
                self.to_value_entry.insert(0, result)
                self.to_value_entry.config(state="readonly")
            elif from_unit == "Fahrenheit" and to_unit == "Celsius":
                result = (from_value - 32) * 5 / 9
                self.to_value_entry.config(state="normal")
                self.to_value_entry.delete(0, tk.END)
                self.to_value_entry.insert(0, result)
                self.to_value_entry.config(state="readonly")
            elif from_unit == "Fahrenheit" and to_unit == "Kelvin":
                result = (from_value - 32) * 5 / 9 + 273.15
                self.to_value_entry.config(state="normal")
                self.to_value_entry.delete(0, tk.END)
                self.to_value_entry.insert(0, result)
                self.to_value_entry.config(state="readonly")
            elif from_unit == "Kelvin" and to_unit == "Fahrenheit":
                result = (from_value - 273.15) * 9 / 5 + 32
                self.to_value_entry.config(state="normal")
                self.to_value_entry.delete(0, tk.END)
                self.to_value_entry.insert(0, result)
                self.to_value_entry.config(state="readonly")
            elif from_unit == "Celsius" and to_unit == "Kelvin":
                result = from_value + 273.15
                self.to_value_entry.config(state="normal")
                self.to_value_entry.delete(0, tk.END)
                self.to_value_entry.insert(0, result)
                self.to_value_entry.config(state="readonly")
            elif from_unit == "Kelvin" and to_unit == "Celsius":
                result = from_value - 273.15
                self.to_value_entry.config(state="normal")
                self.to_value_entry.delete(0, tk.END)
                self.to_value_entry.insert(0, result)
                self.to_value_entry.config(state="readonly")
            elif from_unit == to_unit:
                result = from_value
                self.to_value_entry.config(state="normal")
                self.to_value_entry.delete(0, tk.END)
                self.to_value_entry.insert(0, result)
                self.to_value_entry.config(state="readonly")

        if self.calc_button_length:
            self.calc_button_length.destroy()
        if self.calc_button_weight:
            self.calc_button_weight.destroy()
        if self.calc_button_area:
            self.calc_button_area.destroy()
        if self.calc_button_volume:
            self.calc_button_volume.destroy()

        self.calc_button_temp = tk.Button(self.master, text="Convert", command=callback_temp)
        self.calc_button_temp.place(x=300, y=320)

    def area_converter(self):
        factors = {'sqm': 1, 'sqkm': 1000000, 'sqr': 1011.7141056, 'sqcm': 0.0001, 'sqf': 0.09290304,
                   'sqi': 0.00064516, 'sqmi': 2589988.110336, 'sqmil': 0.000001, 'sqro': 25.29285264,
                   'sqy': 0.83612736, 'sqt': 93239571.9721, 'sqa': 4046.8564224, 'sqar': 100,
                   'sqb': 1e-28, 'sqh': 10000, 'sqho': 647497.027584}
        units = {'Square meter': 'sqm', 'Square km': 'sqkm', 'Square rood': 'sqr', 'Square cm': 'sqcm',
                 'Square foot': 'sqf', 'Square inch': 'sqi', 'Square mile': 'sqmi', 'Square milimeter': 'sqmil',
                 'Square rod': 'sqro', 'Square yard': 'sqy', 'Square township': 'sqt', 'Square acre': 'sqa',
                 'Square are': 'sqar', 'Square barn': 'sqb', 'Square hectare': 'sqh', 'Square homestead': 'sqho'}

        self.temp_button.config(state="active")
        self.weight_button.config(state="active")
        self.length_button.config(state="active")
        self.area_button.config(state="disabled")
        self.volume_button.config(state="active")

        self.from_unit_listbox.set("")
        self.to_unit_listbox.set("")

        self.to_value_entry.config(state="normal")
        self.to_value_entry.delete(0, tk.END)
        self.from_value_entry.delete(0, tk.END)
        self.to_value_entry.config(state="readonly")

        def convert_area(val, inp, to):
            if inp != 'sgm':
                val = val * factors[inp]
                return val / factors[to]
            else:
                return val / factors[to]

        def callback_area():
            try:
                val = float(self.from_value_entry.get())
            except ValueError:
                self.to_value_entry.config(state="normal")
                self.to_value_entry.delete(0, tk.END)
                self.to_value_entry.insert(0, 'Invalid input')
                self.to_value_entry.config(state="readonly")
                return None
            else:
                inp = units[self.from_unit_listbox.get()]
                to = units[self.to_unit_listbox.get()]
                self.to_value_entry.config(state="normal")
                self.to_value_entry.delete(0, tk.END)
                self.to_value_entry.insert(0, convert_area(val, inp, to))
                self.to_value_entry.config(state="readonly")

        self.from_unit_listbox.config(
            values=['Square meter', 'Square km', 'Square rood', 'Square cm', 'Square foot', 'Square inch',
                    'Square mile', 'Square milimeter', 'Square rod', 'Square yard', 'Square township', 'Square acre',
                    'Square are', 'Square barn', 'Square hectare', 'Square homestead'])
        self.to_unit_listbox.config(
            values=['Square meter', 'Square km', 'Square rood', 'Square cm', 'Square foot', 'Square inch',
                    'Square mile', 'Square milimeter', 'Square rod', 'Square yard', 'Square township', 'Square acre',
                    'Square are', 'Square barn', 'Square hectare', 'Square homestead'])

        if self.calc_button_temp:
            self.calc_button_temp.destroy()
        if self.calc_button_length:
            self.calc_button_length.destroy()
        if self.calc_button_weight:
            self.calc_button_weight.destroy()
        if self.calc_button_volume:
            self.calc_button_volume.destroy()

        self.calc_button_area = tk.Button(self.master, text="Convert", command=callback_area)
        self.calc_button_area.place(x=300, y=320)

    def volume_converter(self):
        factors = {'cm': 1, 'ckm': 1e-9, 'ccm': 1000000, 'cmil': 1000000000, 'lit': 1000, 'mlit': 1000000,
                   'gal': 264.17217686, 'qua': 1056.6887074, 'pin': 2113.3774149, "cup": 4226.7548297,
                   "flu": 33814.038638, "tab": 67628.077276, "tea": 202884.23183, "cmi": 2.399e-10,
                   "cya": 1.3079506193, "cft": 35.3146667, "cic": 61023.744}
        units = {"Cubic meter": 'cm', "Cubic kilometer": 'ckm', "Cubic centimeter": 'ccm', "Cubic milimeter": 'cmil',
                 "Liter": 'lit', "Milliliter": 'mlit', "Gallon": 'gal', "Quart": 'qua', "Pint": 'pin', "Cup": "cup",
                 "Fluid ounce": "flu", "Table spoon": "tab", "Tea spoon": "tea", "Cubic mile": "cmi",
                 "Cubic yard": "cya", "Cubic foot": "cft", "Cubic inch": "cic"}

        self.temp_button.config(state="active")
        self.weight_button.config(state="active")
        self.length_button.config(state="active")
        self.area_button.config(state="active")
        self.volume_button.config(state="disabled")

        self.from_unit_listbox.set("")
        self.to_unit_listbox.set("")

        self.to_value_entry.config(state="normal")
        self.to_value_entry.delete(0, tk.END)
        self.from_value_entry.delete(0, tk.END)
        self.to_value_entry.config(state="readonly")

        def convert_volume(val, inp, to):
            if inp != 'cm':
                val = val * factors[inp]
                return val / factors[to]
            else:
                return val / factors[to]

        def callback_volume():
            try:
                val = float(self.from_value_entry.get())
            except ValueError:
                self.to_value_entry.config(state="normal")
                self.to_value_entry.delete(0, tk.END)
                self.to_value_entry.insert(0, 'Invalid input')
                self.to_value_entry.config(state="readonly")
                return None
            else:
                inp = units[self.from_unit_listbox.get()]
                to = units[self.to_unit_listbox.get()]
                self.to_value_entry.config(state="normal")
                self.to_value_entry.delete(0, tk.END)
                self.to_value_entry.insert(0, convert_volume(val, inp, to))
                self.to_value_entry.config(state="readonly")

        self.from_unit_listbox.config(
            values=["Cubic meter", "Cubic kilometer", "Cubic centimeter", "Cubic milimeter", "Liter", "Milliliter",
                    "Gallon", "Quart", "Pint", "Cup", "Fluid ounce", "Table spoon", "Tea spoon", "Cubic mile",
                    "Cubic yard", "Cubic foot", "Cubic inch"])
        self.to_unit_listbox.config(
            values=["Cubic meter", "Cubic kilometer", "Cubic centimeter", "Cubic milimeter", "Liter", "Milliliter",
                    "Gallon", "Quart", "Pint", "Cup", "Fluid ounce", "Table spoon", "Tea spoon", "Cubic mile",
                    "Cubic yard", "Cubic foot", "Cubic inch"])

        if self.calc_button_temp:
            self.calc_button_temp.destroy()
        if self.calc_button_weight:
            self.calc_button_weight.destroy()
        if self.calc_button_area:
            self.calc_button_area.destroy()
        if self.calc_button_length:
            self.calc_button_length.destroy()

        self.calc_button_volume = tk.Button(self.master, text="Convert", command=callback_volume)
        self.calc_button_volume.place(x=300, y=320)

    def mass_converter(self):
        factors = {'kg': 1000, 'hg': 100, 'dg': 10, 'g': 1, 'deg': 0.1, 'cg': 0.01, 'mg': 0.001}
        units = {"Kilogram": 'kg', "Hectagram": 'hg', "Decagram": 'dg', "Decigram": 'deg',
                 "Gram": 'g', "Centigram": 'cg', "Milligram": 'mg'}

        self.temp_button.config(state="active")
        self.weight_button.config(state="disabled")
        self.length_button.config(state="active")
        self.area_button.config(state="active")
        self.volume_button.config(state="active")

        self.from_unit_listbox.set("")
        self.to_unit_listbox.set("")

        self.to_value_entry.config(state="normal")
        self.to_value_entry.delete(0, tk.END)
        self.from_value_entry.delete(0, tk.END)
        self.to_value_entry.config(state="readonly")

        def convert_weight(val, inp, to):
            if inp != 'g':
                val = val * factors[inp]
                return val / factors[to]
            else:
                return val / factors[to]

        def callback_weight():
            try:
                val = float(self.from_value_entry.get())
            except ValueError:
                self.to_value_entry.config(state="normal")
                self.to_value_entry.delete(0, tk.END)
                self.to_value_entry.insert(0, 'Invalid input')
                self.to_value_entry.config(state="readonly")
                return None
            else:
                inp = units[self.from_unit_listbox.get()]
                to = units[self.to_unit_listbox.get()]
                self.to_value_entry.config(state="normal")
                self.to_value_entry.delete(0, tk.END)
                self.to_value_entry.insert(0, convert_weight(val, inp, to))
                self.to_value_entry.config(state="readonly")

        self.from_unit_listbox.config(
            values=["Kilogram", "Hectagram", "Decagram", "Decigram", "Gram", "Centigram", "Milligram"])
        self.to_unit_listbox.config(
            values=["Kilogram", "Hectagram", "Decagram", "Decigram", "Gram", "Centigram", "Milligram"])

        if self.calc_button_temp:
            self.calc_button_temp.destroy()
        if self.calc_button_length:
            self.calc_button_length.destroy()
        if self.calc_button_area:
            self.calc_button_area.destroy()
        if self.calc_button_volume:
            self.calc_button_volume.destroy()

        self.calc_button_weight = tk.Button(self.master, text="Convert", command=callback_weight)
        self.calc_button_weight.place(x=300, y=320)

    def length_converter(self):
        factors = {'nmi': 1852, 'mi': 1609.34, 'yd': 0.9144, 'ft': 0.3048, 'inch': 0.0254, 'km': 1000, 'm': 1,
                   'cm': 0.01, 'mm': 0.001}
        units = {"Nautical Miles": 'nmi', "Miles": 'mi', "Yards": 'yd', "Feet": 'ft', "Inches": 'inch',
                 "Kilometers": 'km', "Meters": 'm', "Centimeters": 'cm', "Millileters": 'mm'}

        self.temp_button.config(state="active")
        self.weight_button.config(state="active")
        self.length_button.config(state="disabled")
        self.area_button.config(state="active")
        self.volume_button.config(state="active")

        self.from_unit_listbox.set("")
        self.to_unit_listbox.set("")

        self.to_value_entry.config(state="normal")
        self.to_value_entry.delete(0, tk.END)
        self.from_value_entry.delete(0, tk.END)
        self.to_value_entry.config(state="readonly")

        def convert_length(val, inp, to):
            if inp != 'm':
                val = val * factors[inp]
                return val / factors[to]
            else:
                return val / factors[to]

        def callback_length():
            try:
                val = float(self.from_value_entry.get())
            except ValueError:
                self.to_value_entry.config(state="normal")
                self.to_value_entry.delete(0, tk.END)
                self.to_value_entry.insert(0, 'Invalid input')
                self.to_value_entry.config(state="readonly")
                return None
            else:
                inp = units[self.from_unit_listbox.get()]
                to = units[self.to_unit_listbox.get()]
                self.to_value_entry.config(state="normal")
                self.to_value_entry.delete(0, tk.END)
                self.to_value_entry.insert(0, convert_length(val, inp, to))
                self.to_value_entry.config(state="readonly")

        self.from_unit_listbox.config(
            values=["Nautical Miles", "Miles", "Yards", "Feet", "Inches", "Kilometers", "Meters", "Centimeters",
                    "Millileters"])
        self.to_unit_listbox.config(
            values=["Nautical Miles", "Miles", "Yards", "Feet", "Inches", "Kilometers", "Meters", "Centimeters",
                    "Millileters"])

        if self.calc_button_temp:
            self.calc_button_temp.destroy()
        if self.calc_button_weight:
            self.calc_button_weight.destroy()
        if self.calc_button_area:
            self.calc_button_area.destroy()
        if self.calc_button_volume:
            self.calc_button_volume.destroy()

        self.calc_button_length = tk.Button(self.master, text="Convert", command=callback_length)
        self.calc_button_length.place(x=300, y=320)


if __name__ == "__main__":
    root = tk.Tk()
    app = UnitConverter(root)
    root.mainloop()
