import tkinter as tk
import re


class RegexQueryTool:
    def __init__(self, master):
        self.master = master
        self.master.title("Regex Query Tool")

        self.text_label = tk.Label(master, text="Enter Text:")
        self.text_label.pack()
        self.text_entry = tk.Entry(master, width=50)
        self.text_entry.pack()

        self.regex_label = tk.Label(master, text="Enter Regex Pattern")
        self.regex_label.pack()
        self.regex_entry = tk.Entry(master, width=50)
        self.regex_entry.pack()

        self.result_label = tk.Label(master, text="Result")
        self.result_label.pack()
        self.result_text = tk.Text(master, height=10, width=50, state=tk.DISABLED)
        self.result_text.pack()

        self.run_button = tk.Button(master, text="Run Regex", command=self.run_regex)
        self.run_button.pack()

    def run_regex(self):
        self.result_text.config(state=tk.NORMAL)
        self.result_text.delete(0.0, tk.END)

        text = self.text_entry.get()
        regen_pattern = self.regex_entry.get()

        try:
            regex = re.compile(regen_pattern)
            matches = regex.finditer(text)
            match_counter = 0

            for match in matches:
                match_counter += 1
                self.result_text.insert(tk.END, f"Match {match_counter} at index {match.start()}-{match.end()}\n")
        except re.error as e:
            self.result_text.insert(tk.END, f"Regex error: {str(e)}\n")

        self.result_text.config(state=tk.DISABLED)


if __name__ == "__main__":
    root = tk.Tk()
    app = RegexQueryTool(root)
    root.mainloop()
