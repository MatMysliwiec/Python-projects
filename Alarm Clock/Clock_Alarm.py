import time
import pygame


def play_alarm():
    pygame.init()
    pygame.mixer.music.load("alarm-clock.mp3")
    pygame.mixer.music.play()

    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)


def set_alarm(duration):
    time.sleep(duration)
    play_alarm()


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
