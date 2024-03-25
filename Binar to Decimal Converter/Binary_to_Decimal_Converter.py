import tkinter as tk
from tkinter import messagebox

class ConvertBINtoDEC:
    def __init__(self, master):
        self.master = master
        self.master.title("Binary to Decimal Converter")
        self.master.geometry("400x300")
        self.master.resizable(False, False)

        self.title_label = tk.Label(master, text="Bin to Dec(Dec to Bin) Converter", font=("Bold Helvetica", 18))
        self.title_label.pack(pady=10)

        self.bin_to_dec_button = tk.Button(master, text="Bin to Dec", font="Verdana 15", command=self.bin_to_dec)
        self.bin_to_dec_button.place(x=10, y=80)

        self.dec_to_bin_button = tk.Button(master, text="Dec to Bin", font="Verdana 15", command=self.dec_to_bin)
        self.dec_to_bin_button.place(x=200, y=80)

        self.from_label = tk.Label(master, text="From:", font=("Helvetica", 12))
        self.from_label.place(x=10, y=150)

        self.to_label = tk.Label(master, text="To:", font=("Helvetica", 12))
        self.to_label.place(x=200, y=150)

        self.from_entry = tk.Entry(master)
        self.from_entry.place(x=10, y=200)

        self.to_entry = tk.Entry(master, state="readonly")
        self.to_entry.place(x=200, y=200)

    def bin_to_dec(self):
        try:
            from_value = self.from_entry.get()
            result = int(from_value, 2)
            self.to_entry.config(state="normal")
            self.to_entry.delete(0, tk.END)
            self.to_entry.insert(0, result)
            self.to_entry.config(state="readonly")
        except ValueError:
            messagebox.showerror("Invalid input", "Please enter proper numeric value")

    def dec_to_bin(self):
        from_value = int(self.from_entry.get())
        result = bin(from_value).replace("0b", "")
        self.to_entry.config(state="normal")
        self.to_entry.delete(0, tk.END)
        self.to_entry.insert(0, result)
        self.to_entry.config(state="readonly")


if __name__ == "__main__":
    root = tk.Tk()
    app = ConvertBINtoDEC(root)
    root.mainloop()
