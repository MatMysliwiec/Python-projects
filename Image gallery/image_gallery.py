from abc import ABC, abstractmethod
from PIL import Image, ImageTk
from tkinter import ttk
import tkinter as tk
import cv2

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
        self.image = cv2.imread(file_path)
        if self.image is None:
            raise FileNotFoundError(f"Image file not found or cannot be opened: {file_path}")


    def display(self, canvas):
        if self.image is None:
            raise ValueError("Image is not loaded.")
        height = 300
        ratio = height / self.image.shape[0]
        width = int(self.image.shape[1] * ratio)
        resized_image = cv2.resize(self.image,(width,height), interpolation=cv2.INTER_LINEAR)
        tk_image = ImageTk.PhotoImage(resized_image)
        canvas.create_image(0, 0, anchor=tk.NW, image=tk_image)
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
            if path.lower().endswith((".jpg", ".jpeg", ".png")):
                image = JPEGImage()
                image.load(path)
                self.images.append(image)
            else:
                raise ValueError(f"Unsupported image type for file: {path}")

    def create_gallery(self):
        gallery_frame = ttk.Frame(self.root)
        gallery_frame.pack(fill=tk.BOTH, expand=True)

        for i, image in enumerate(self.images):
            canvas = tk.Canvas(gallery_frame, width=400, height=300)
            canvas.grid(row=i // 3, column=i % 3, padx=10, pady=10)
            image.display(canvas)


if __name__ == "__main__":
    root = tk.Tk()
    image_paths = [
        r"C:\Users\User\OneDrive - Politechnika Krakowska im. Tadeusza Kościuszki\Pulpit\Projekty_python\Image gallery\Image file\img1.jpg",
        r"C:\Users\User\OneDrive - Politechnika Krakowska im. Tadeusza Kościuszki\Pulpit\Projekty_python\Image gallery\Image file\img2.jpg",
        r"C:\Users\User\OneDrive - Politechnika Krakowska im. Tadeusza Kościuszki\Pulpit\Projekty_python\Image gallery\Image file\img3.jpg"
    ]
    app = ImageGalleryApp(root, image_paths)
    root.mainloop()
