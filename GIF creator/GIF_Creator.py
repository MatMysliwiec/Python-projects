from PIL import Image
import imageio
from moviepy.editor import VideoFileClip
import os


def create_from_image(image_folder, gif_path, duration=0.2):
    images = []

    image_files = [f for f in os.listdir(image_folder) if f.endswith(('png', 'jpg', 'jpeg', 'tif', 'tiff'))]
    image_files.sort()

    for image_file in image_files:
        image_path = os.path.join(image_folder, image_file)
        img = Image.open(image_path)
        images.append(img)

    images[0].save(gif_path, save_all=True, append_images=images[1:], duration=duration, loop=0)


def convert_video_to_gif(video_path, gif_path, duration=0.2):
    clip = VideoFileClip(video_path)
    clip.write_gif(gif_path, fps=1/duration, program='imageio_ffmpeg')
