import tkinter as tk
from PIL import Image, ImageTk
import time


class SlideshowApp:
    def __init__(self, master, image_paths, transition_duration=1000):
        self.master = master
        self.image_paths = image_paths
        self.transition_duration = transition_duration
        self.current_image_index = 0

        self.canvas = tk.Canvas(master)
        self.canvas.pack(fill=tk.BOTH, expand=True)

        self.load_images()
        self.show_image()

    def load_images(self):
        self.images = [Image.open(path) for path in self.image_paths]
        self.photo_images = [ImageTk.PhotoImage(image) for image in self.images]

    def show_image(self):
        current_image = self.photo_images[self.current_image_index]
        self.canvas.create_image(0, 0, anchor=tk.NW, image=current_image)

        self.master.after(self.transition_duration, self.fade_out)

    def fade_out(self, alpha=255):
        if alpha >= 0:
            self.canvas.delete("all")
            current_image = self.photo_images[self.current_image_index].copy()
            current_image.putalpha(alpha)
            self.canvas.create_image(0, 0, anchor=tk.NW, image=current_image)
            self.master.update()
            self.master.after(10, self.fade_out, alpha - 1)
        else:
            self.master.after(10, self.next_image)

        self.master.after(10, self.next_image)

    def next_image(self):
        self.current_image_index = (self.current_image_index + 1) % len(self.image_paths)
        self.load_images()
        self.show_image()


if __name__ == "__main__":
    root = tk.Tk()
    root.title("Slideshow App")
    root.geometry("800x600")

    image_paths = [
        r"C:\Users\User\OneDrive - Politechnika Krakowska im. Tadeusza Kościuszki\Pulpit\Projekty_python\Slide show\Image files\img1.jpg",
        r"C:\Users\User\OneDrive - Politechnika Krakowska im. Tadeusza Kościuszki\Pulpit\Projekty_python\Slide show\Image files\img2.jpg",
        r"C:\Users\User\OneDrive - Politechnika Krakowska im. Tadeusza Kościuszki\Pulpit\Projekty_python\Slide show\Image files\img3.jpg"
    ]
    duration = 2000

    app = SlideshowApp(root, image_paths, duration)

    root.mainloop()
