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

        self.master.after(self.transition_duration, self.face_out)

    def fade_out(self):
        for alpha in range(255, -1, -10):
            self.canvas.delete("all")
            current_image = self.photo_images[self.current_image_index]
            current_image.putalpha(alpha)
            self.canvas.create_image(0, 0, archor=tk.NW, image=current_image)
            self.master.update()
            time.sleep(0.03)

        self.master.after(10, self.next_image)

    def next_image(self):
        self.current_image_index = (self.current_image_index + 1) % len(self.image_paths)
        self.load_images()
        self.show_image()


if __name__ == "__main__":
    root = tk.Tk()
    root.title("Slideshow App")
    root.geometry("800x600")

    image_paths = ["image1.jpg", "image2.jpg"]
    duration = 2000

    app = SlideshowApp(root, image_paths, duration)

    root.mainloop()
