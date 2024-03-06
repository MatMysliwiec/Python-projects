import tkinter as tk


class UnitConverterGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Unit Converter")
        self.master.geometry("800x600")

        self.label = tk.Label(master, text="Select the type of converter:")
        self.label.pack(pady=10)

        self.choices = [
            "Temperature Converter",
            "Currency Converter",
            "Volume Converter",
            "Mass Converter",
            "Length Converter"
        ]

        self.selected_converter = tk.StringVar(master)
        self.selected_converter.set(self.choices[0])

        self.converter_menu = tk.OptionMenu(master, self.selected_converter, *self.choices)
        self.converter_menu.pack(pady=10)

        self.convert_button = tk.Button(master, text="Convert", command=self.convert)
        self.convert_button.pack(pady=10)

    def convert(self):
        selected_option = self.selected_converter.get()

        if selected_option == "Temperature Converter":
            self.temperature_converter()
        elif selected_option == "Currency Converter":
            self.currency_converter()
        elif selected_option == "Volume Converter":
            self.volume_converter()
        elif selected_option == "Mass Converter":
            self.mass_converter()
        elif selected_option == "Length Converter":
            self.length_converter()

    def temperature_converter(self):
        pass

    def currency_converter(self):
        pass

    def volume_converter(self):
        pass

    def mass_converter(self):
        pass

    def length_converter(self):
        pass


if __name__ == "__main__":
    root = tk.Tk()
    app = UnitConverterGUI(root)
    root.mainloop()
