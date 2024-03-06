import tkinter as tk
from tkinter import filedialog
import pygame
import os


class MP3Player:
    def __init__(self, master):
        self.master = master
        self.master.title("MP3 Player")
        self.master.geometry("400x200")

        self.playing = False
        self.playlist = []
        self.current_track = 0

        self.create_widgets()

    def create_widgets(self):
        self.play_button = tk.Button(self.master, text="Play", command=self.play)
        self.play_button.pack(pady=10)

        self.pause_button = tk.Button(self.master, text="Pause", command=self.pause)
        self.pause_button.pack(pady=5)

        self.stop_button = tk.Button(self.master, text="Stop", command=self.stop)
        self.stop_button.pack(pady=5)

        self.next_button = tk.Button(self.master, text="Next", command=self.next)
        self.next_button.pack(pady=5)

        self.prev_button = tk.Button(self.master, text="Prev", command=self.prev)
        self.prev_button.pack(pady=5)

        self.add_button = tk.Button(self.master, text="Add to Playlist", command=self.add)
        self.add_button.pack(pady=10)

        pygame.init()
        pygame.mixer.init()

    def add(self):
        folder_path = filedialog.askdirectory()
        for file in os.listdir(folder_path):
            if file.endswith((".mp3", ".mp4")):
                self.playlist.append(os.path.join(folder_path, file))

    def play(self):
        if not pygame.mixer.music.get_busy():
            pygame.mixer.music.load(self.playlist[self.current_track])
            pygame.mixer.music.play()
            self.playing = True

    def pause(self):
        if self.playing:
            pygame.mixer.music.pause()
            self.playing = False

    def stop(self):
        pygame.mixer.music.stop()
        self.playing = False

    def next(self):
        self.stop()
        self.current_track = (self.current_track + 1) % len(self.playlist)
        self.play()

    def prev(self):
        self.stop()
        self.current_track = (self.current_track - 1) % len(self.playlist)
        self.play()


if __name__ == "__main__":
    root = tk.Tk()
    player = MP3Player(root)
    root.mainloop()
