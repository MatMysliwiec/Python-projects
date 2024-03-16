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
        self.master.resizable(False, False)

        self.default_work_duration = 0
        self.default_break_duration = 0
        self.default_cycles = 0

        self.work_duration = tk.IntVar(value=self.default_work_duration)
        self.break_duration = tk.IntVar(value=self.default_break_duration)
        self.cycles = tk.IntVar(value=self.default_cycles)

        self.current_cycle = 0
        self.is_work_time = True
        self.pause = False

        self.info_label = ttk.Label(self.master, text="", font=("Helvetica", 12))
        self.info_label.pack(pady=10)

        self.timer_label = ttk.Label(self.master, text="", font=("Helvetica", 24))
        self.timer_label.pack(pady=10)

        self.start_button = ttk.Button(self.master, text="Pause", command=self.toggle_timer)
        self.start_button.pack(side=tk.LEFT, padx=10, pady=10)

        self.reset_button = ttk.Button(self.master, text="Reset", command=self.reset_timer)
        self.reset_button.pack(side=tk.LEFT, padx=10, pady=10)

        self.start_button.config(state="disabled")
        self.reset_button.config(state="disabled")

        self.show_settings_dialog()

    def show_settings_dialog(self):

        settings_dialog = tk.Toplevel(self.master)
        settings_dialog.title("Timer Settings")
        settings_dialog.resizable(False, False)

        def update_total_time_label():
            # noinspection PyBroadException
            try:
                work_value = self.work_duration.get() * 60 if self.work_duration.get() else 0
                break_value = self.break_duration.get() * 60 if self.break_duration.get() else 0
                cycles_value = self.cycles.get() if self.cycles.get() else 0
                total_time = (work_value + break_value) * cycles_value
                total_time_str = time.strftime("%H:%M:%S", time.gmtime(total_time))
                total_time_value.config(text=total_time_str)
            except Exception:
                pass

        work_label = ttk.Label(settings_dialog, text="Work Duration (min)")
        work_label.grid(row=0, column=0, padx=10, pady=5)
        work_entry = ttk.Entry(settings_dialog, textvariable=self.work_duration)
        work_entry.grid(row=0, column=1, padx=10, pady=5)
        self.work_duration.trace_add("write",
                                     lambda name, index, mode, var=self.work_duration: update_total_time_label())

        break_label = ttk.Label(settings_dialog, text="Break Duration (min)")
        break_label.grid(row=1, column=0, padx=10, pady=5)
        break_entry = ttk.Entry(settings_dialog, textvariable=self.break_duration)
        break_entry.grid(row=1, column=1, padx=10, pady=5)
        self.break_duration.trace_add("write", lambda name, index, mode, var=self.break_duration: update_total_time_label())

        cycles_label = ttk.Label(settings_dialog, text="Number of Cycles:")
        cycles_label.grid(row=2, column=0, padx=10, pady=5)
        cycles_entry = ttk.Entry(settings_dialog, textvariable=self.cycles)
        cycles_entry.grid(row=2, column=1, padx=10, pady=5)
        self.cycles.trace_add("write", lambda name, index, mode, var=self.cycles: update_total_time_label())

        total_time_label = ttk.Label(settings_dialog, text="Total time:")
        total_time_label.grid(row=3, column=0, padx=10, pady=5)
        total_time_value = ttk.Label(settings_dialog)
        total_time_value.grid(row=3, column=1, padx=10, pady=5)

        update_total_time_label()

        confirm_button = ttk.Button(settings_dialog, text="Confirm",
                                    command=lambda: self.apply_settings(settings_dialog))
        confirm_button.grid(row=4, column=0, columnspan=2, pady=10)

    def apply_settings(self, settings_dialog):
        try:
            self.default_work_duration = self.work_duration.get()
            self.default_break_duration = self.break_duration.get()
            self.default_cycles = self.cycles.get()

            self.work_duration = self.default_work_duration * 60
            self.break_duration = self.default_break_duration * 60
            self.cycles = self.default_cycles

            settings_dialog.destroy()
            self.start_button.config(state="active")
            self.reset_button.config(state="active")

            self.start_pomodoro_timer()
        except Exception:
            messagebox.showerror("Invalid Input", "Please enter valid numerical values")

    def start_pomodoro_timer(self):
        if self.current_cycle < self.cycles:
            self.timer_label.after(0, self.update_timer)
            self.timer_label.config(font=("Helvetica", 24))

    def toggle_timer(self):
        if not self.pause:
            self.pause = True
            self.start_button.config(text="Resume")
        else:
            self.pause = False
            self.start_button.config(text="Pause")
            self.start_pomodoro_timer()

    def update_timer(self):
        if not self.pause:
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
                    self.work_duration = self.default_work_duration * 60
                    self.break_duration = self.default_break_duration * 60
                else:
                    self.timer_label.config(text="Pomodoro Timer completed.", font=("Helvetica", 12))
                    self.start_button.config(state="disabled")
                    self.current_cycle = 0
                    return

            self.timer_label.after(1000, self.update_timer)

    def reset_timer(self):
        self.is_work_time = True
        self.pause = False
        self.start_button.config(text="Pause")
        self.work_duration = tk.IntVar(value=self.default_work_duration)
        self.break_duration = tk.IntVar(value=self.default_break_duration)
        self.cycles = tk.IntVar(value=self.default_cycles)
        self.current_cycle = 0
        self.timer_label.after_cancel(self.update_timer)
        self.info_label.config(text="")
        self.timer_label.config(text="")
        self.start_button.config(state="disabled")
        self.reset_button.config(state="disabled")
        self.show_settings_dialog()

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
