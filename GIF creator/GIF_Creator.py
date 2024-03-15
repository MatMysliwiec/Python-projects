from PIL import Image
from moviepy.editor import VideoFileClip
import os


def create_from_image(image_folder, gif_path, duration=0.2):
    images = []

    image_files = [f for f in os.listdir(image_folder) if f.endswith(('.png', '.jpg', '.jpeg', '.tif', '.tiff'))]
    image_files.sort()

    for image_file in image_files:
        image_path = os.path.join(image_folder, image_file)
        img = Image.open(image_path)
        images.append(img)

    images[0].save(gif_path, save_all=True, append_images=images[1:], duration=duration, loop=0)
    print("Convert images to gif completed.")

def convert_video_to_gif(video_path, gif_path, duration=0.1):
    try:
        clip = VideoFileClip(video_path)
        clip.write_videofile(gif_path, fps=1/duration, codec='gif')
    except Exception as e:
        print("Error: ", e)
    print("Convert video to gif completed.")


if __name__ == "__main__":
    image_path = r"C:\Users\User\OneDrive - Politechnika Krakowska im. Tadeusza Kościuszki\Pulpit\Projekty_python\GIF creator\Image file"
    gif_path = r"C:\Users\User\OneDrive - Politechnika Krakowska im. Tadeusza Kościuszki\Pulpit\Projekty_python\GIF creator\Gif file\output_video.gif"
    video_path = r"C:\Users\User\OneDrive - Politechnika Krakowska im. Tadeusza Kościuszki\Pulpit\Projekty_python\GIF creator\Video file\vidoe.mp4"

    convert_video_to_gif(video_path,gif_path)
    #create_from_image(image_path, gif_path)

