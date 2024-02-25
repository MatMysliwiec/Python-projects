import time
import pygame
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox


def play_alarm():
    pygame.init()
    pygame.mixer.music.load("alarm-clock.mp3")
    pygame.mixer.music.play()


def set_alarm(duration):
    time.sleep(duration)
    play_alarm()


class PomodoroTimer:

    def __init__(self, master):
        self.master = master
        self.master.title("Pomodoro Timer")
        self.master.geometry("300x150")

        self.default_work_duration = 30 * 60
        self.default_break_duration = 10 * 60
        self.default_cycles = 5

        self.work_duration = self.default_work_duration
        self.break_duration = self.default_break_duration
        self.cycles = self.default_cycles
        self.current_cycle = 0
        self.is_work_time = True

        self.info_label = ttk.Label(self.master, text="", font=("Helvetica", 12))
        self.info_label.pack(pady=10)

        self.timer_label = ttk.Label(self.master, text="", font=("Helvetica", 24))
        self.timer_label.pack(pady=10)

        self.start_button = ttk.Button(self.master, text="Start", command=self.show_settings_dialog)
        self.start_button.pack(pady=10)

    def show_settings_dialog(self):
        settings_dialog = tk.Toplevel(self.master)
        settings_dialog.title("Timer Settings")

        work_label = ttk.Label(settings_dialog, text="Work Duration (min)")
        work_label.grid(row=0, column=0, padx=10, pady=5)
        work_var = tk.StringVar()
        work_entry = ttk.Entry(settings_dialog, textvariable=work_var)
        work_entry.grid(row=0, column=1, padx=10, pady=5)

        break_label = ttk.Label(settings_dialog, text="Break Duration (min)")
        break_label.grid(row=1, column=0, padx=10, pady=5)
        break_var = tk.StringVar()
        break_entry = ttk.Entry(settings_dialog, textvariable=break_var)
        break_entry.grid(row=1, column=1, padx=10, pady=5)

        cycles_label = ttk.Label(settings_dialog, text="Number of Cycles:")
        cycles_label.grid(row=2, column=0, padx=10, pady=5)
        cycles_var = tk.StringVar()
        cycles_entry = ttk.Entry(settings_dialog, textvariable=cycles_var)
        cycles_entry.grid(row=2, column=1, padx=10, pady=5)

        confirm_button = ttk.Button(settings_dialog, text="Confirm",
                                    command=lambda: self.apply_settings(work_var, break_var, cycles_var,
                                                                        settings_dialog))
        confirm_button.grid(row=3, column=0, columnspan=2, pady=10)

    def apply_settings(self, work_var, break_var, cycles_var, settings_dialog):
        try:
            self.default_work_duration = int(work_var.get()) * 60
            self.default_break_duration = int(break_var.get()) * 60
            self.default_cycles = int(cycles_var.get())

            self.work_duration = self.default_work_duration
            self.break_duration = self.default_break_duration
            self.cycles = self.default_cycles

            settings_dialog.destroy()

            self.start_pomodoro_timer()
        except ValueError:
            messagebox.showerror("Invalid Input", "Please enter valid numerical values")

    def start_pomodoro_timer(self):
        if self.current_cycle < self.cycles:
            self.timer_label.after(0, self.update_timer)
            self.timer_label.config(font=("Helvetica", 24))
            self.start_button.config(state="disabled")

    def update_timer(self):
        if self.work_duration > 0:
            self.display_time(self.work_duration)
            self.work_duration -= 1
            self.display_info()
            if self.work_duration == 0:
                play_alarm()
                self.is_work_time = False
        elif self.break_duration > 0:
            self.display_time(self.break_duration)
            self.break_duration -= 1
            self.display_info()
            if self.break_duration == 0 and self.current_cycle < self.cycles:
                play_alarm()
                self.current_cycle += 1
                self.is_work_time = True
        else:
            if self.current_cycle < self.cycles:
                self.work_duration = self.default_work_duration
                self.break_duration = self.default_break_duration
            else:
                self.timer_label.config(text="Pomodoro Timer completed.", font=("Helvetica", 12))
                self.start_button.config(state="normal")
                self.current_cycle = 0
                return

        self.timer_label.after(1000, self.update_timer)

    def display_time(self, duration):
        minuts, secods = divmod(duration, 60)
        time_str = f"{minuts:02d}:{secods:02d}"
        self.timer_label.config(text=time_str)

    def display_info(self):
        if self.is_work_time:
            info_str = f"Work Time - Cycle {self.current_cycle + 1}"
        else:
            info_str = f"Break Time - Cycle {self.current_cycle + 1}"
        self.info_label.config(text=info_str)


if __name__ == "__main__":
    root = tk.Tk()
    app = PomodoroTimer(root)
    root.mainloop()
