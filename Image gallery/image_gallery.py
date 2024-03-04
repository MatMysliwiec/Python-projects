from abc import ABC, abstractmethod
from PIL import Image, ImageTk
from tkinter import ttk
import tkinter as tk


class ImageBase(ABC):
    @abstractmethod
    def load(self, file_path):
        pass

    @abstractmethod
    def display(self, canvas):
        pass


class JPEGImage(ImageBase):
    def __init__(self):
        self.image = None

    def load(self, file_path):
        self.image = Image.open(file_path)

    def display(self, canvas):
        tk_image = ImageTk.PhotoImage(self.image)
        canvas.create_image(0, 0, archor=tk.NW, image=tk_image)
        canvas.tk_image = tk_image


class ImageGalleryApp:
    def __init__(self, root, image_paths):
        self.root = root
        self.root.title("Image Gallery")

        self.images = []
        self.load_images(image_paths)

        self.create_gallery()

    def load_images(self, image_paths):
        for path in image_paths:
            if path.lower().endswith(".jpg") or path.lower().endswith(".jpeg") or path.lower().endswith(".png"):
                image = JPEGImage()
            else:
                raise ValueError(f"Unsupported image type for file: {path}")

    def create_gallery(self):
        gallery_frame = ttk.Frame(self.root)
        gallery_frame.pack(fill=tk.BOTH, expand=True)

        for i, image in enumerate(self.images):
            canvas = tk.Canvas(gallery_frame, width=300, height=200)
            canvas.grid(row=i // 3, column=1 % 3, padx=10, pady=10)
            image.display(canvas)


if __name__ == "__main":
    root = tk.Tk()
    image_paths = []
    app = ImageGalleryApp(root, image_paths)
    root.mainloop()
