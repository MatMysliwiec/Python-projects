import time
import pygame
import tkinter as tk
from tkinter import ttk


def pomodoro_timer(work_duration, break_duration, cycles):
    for cycle in range(cycles):
        print(f"Pomodoro cycle: {cycle + 1}")
        set_alarm(work_duration * 60)
        print("Take a break!")
        set_alarm(break_duration*60)
    print("Pomodoro Timer completed.")

def play_alarm():
    pygame.init()
    pygame.mixer.music.load("alarm-clock.mp3")
    pygame.mixer.music.play()

    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(8)


def set_alarm(duration):
    time.sleep(duration)
    play_alarm()

'''
choice = input("Set by time(T) or duration(D)")

if choice.lower().startswith("t"):
    alarm_time = input("Enter the alarm time in HH:MM format: ")
    current_time = time.strftime("%H:%M")

    while current_time != alarm_time:
        current_time = time.strftime("%H:%M")
        time.sleep(1)
    print("ALARM!")
    play_alarm()

elif choice.lower().startswith("d"):
    alarm_duration = int(input("Enter the alarm duration in minutes: "))
    set_alarm(alarm_duration * 60)

else:
    print("Invalid choice")
'''


if __name__ == "__main__":
    work_time = int(input("Enter time of work: "))
    break_time = int(input("Enter break time: "))
    cycles = int(input("Enter number of cycles: "))
    pomodoro_timer(work_time, break_time, cycles)