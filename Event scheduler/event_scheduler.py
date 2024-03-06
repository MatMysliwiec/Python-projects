import tkinter as tk
from tkinter import messagebox, simpledialog
from datetime import datetime


class Event:
    def __init__(self, date, time, notes):
        self.date = date
        self.time = time
        self.notes = notes

    def __str__(self):
        return f"{self.date} {self.time}: {self.notes}"

class EventSchedulerApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Event Scheduler")

        self.events = []

        self.date_label = tk.Label(master, text="Date (YYYY-MM-DD): ")
        self.date_label.grid(row=0, column=0)
        self.date_entry = tk.Entry(master)
        self.date_entry.grid(row=0, column=1)

        self.time_label = tk.Label(master, text="Time (HH:MM): ")
        self.time_label.grid(row=1, column=0)
        self.time_entry = tk.Entry(master)
        self.time_entry.grid(row=1, column=1)

        self.notes_label = tk.Label(master, text="Event notes")
        self.notes_label.grid(row=2, column=0)
        self.notes_entry = tk.Entry(master)
        self.notes_entry.grid(row=2, column=1)

        self.add_button = tk.Button(master, text="Add Event", command=self.add_event)
        self.add_button.grid(row=4, column=0, columnspan=2)

        self.calendar_button = tk.Button(master, text="View Calendar", command=self.display_calendar)
        self.calendar_button.grid(row=5, column=0, columnspan=2)

        self.search_button = tk.Button(master, text="Search Calendar", command=self.search_cal)
        self.search_button.grid(row=6, column=0, columnspan=2)

    def add_event(self):
        date_str = self.date_entry.get()
        time_str = self.time_entry.get()
        notes = self.notes_entry.get()

        try:
            date = datetime.strptime(date_str, "%Y-%m-%d")
            time = datetime.strptime(time_str, "%H:%M").time()
        except ValueError:
            messagebox.showerror("Error", "Invalid date or time format")
            return

        event = Event(date, time, notes)
        self.events.append(event)
        messagebox.showinfo("Success", "Event added successfully")

        self.date_entry.delete(0, tk.END)
        self.time_entry.delete(0, tk.END)
        self.notes_entry.delete(0, tk.END)

    def display_calendar(self):
        if not self.events:
            tk.messagebox.showinfo("Calendar", "No events to display")
            return

        calendar_window = tk.Toplevel(self.master)
        calendar_window.title("Calendar")
        calendar_window.geometry("400x300")

        listbox = tk.Listbox(calendar_window)
        listbox.pack(expand=True, fill='both')

        for event in self.events:
            listbox.insert(tk.END, str(event))

    def search_cal(self):
        keyword = tk.simpledialog.askstring("Search", "Enter to search")
        if keyword is None:
            return

        matching_events = [event for event in self.events if keyword.lower() in event.notes.lower()]

        if not matching_events:
            tk.messagebox.showinfo("Search Results", "No matching events found")
            return

        search_results_window = tk.Toplevel(self.master)
        search_results_window.title("Search Results")

        listbox = tk.Listbox(search_results_window)
        listbox.pack(expand=True, fill='both')

        for event in matching_events:
            listbox.insert(tk.END, str(event))


if __name__ == "__main__":
    root = tk.Tk()
    app = EventSchedulerApp(root)
    root.mainloop()
