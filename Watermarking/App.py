from PIL import Image, ImageDraw, ImageFont
import os
import threading

class WatermarkThread(threading.Thread):
    def __init__(self, input_path, output_path, watermark_text):
        threading.Thread.__init__(self)
        self.input_path = input_path
        self.output_path = output_path
        self.watermark_text = watermark_text

    def run(self):
        self.add_watermark()

    def add_watermark(self):
        image = Image.open(self.input_path)
        width, height = image.size

        # Adding watermark text
        draw = ImageDraw.Draw(image)
        font = ImageFont.load_default()
        text_width, text_height = draw.textsize(self.watermark_text, font)

        # Position the watermark in the bottom-right corner
        x = width - text_width - 10
        y = height - text_height - 10

        # Set watermark transparency (optional)
        watermark_opacity = 100
        watermark_color = (255, 255, 255, watermark_opacity)
        draw.text((x, y), self.watermark_text, font=font, fill=watermark_color)

        # Save the watermarked image
        image.save(self.output_path)

def watermark_images(input_folder, output_folder, watermark_text):
    # Create output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Get a list of all image files in the input folder
    image_files = [f for f in os.listdir(input_folder) if f.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp'))]

    # Create and start threads for watermarking
    threads = []
    for image_file in image_files:
        input_path = os.path.join(input_folder, image_file)
        output_path = os.path.join(output_folder, image_file)
        thread = WatermarkThread(input_path, output_path, watermark_text)
        threads.append(thread)
        thread.start()

    # Wait for all threads to finish
    for thread in threads:
        thread.join()

if __name__ == "__main__":
    input_folder = "input_images"
    output_folder = "output_images"
    watermark_text = "YourWatermark"

    watermark_images(input_folder, output_folder, watermark_text)