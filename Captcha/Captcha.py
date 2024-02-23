from captcha.image import ImageCaptcha
import random
import string
from PIL import Image, ImageDraw, ImageFont
from captcha_solver import CaptchaSolver


def generate_captcha():
    captcha_text = "".join(random.choices(string.ascii_uppercase + string.ascii_lowercase + string.digits, k=6))
    captcha = ImageCaptcha()
    image_data = captcha.generate(captcha_text)
    captcha_image_path = f"captcha_{captcha_text}.png"
    captcha.write(captcha_text, captcha_image_path)

    return captcha_text, captcha_image_path


captcha_text, captcha_image_path = generate_captcha()
print(f"Captcha Text: {captcha_text}")
print(f"Captcha Image saved at: {captcha_image_path}")


def generate_PIL():
    captcha_text = "".join(random.choices(string.ascii_uppercase + string.ascii_lowercase + string.digits, k=6))
    image = Image.new("RGB", (150, 50), color="white")
    draw = ImageDraw.Draw(image)

    font = ImageFont.load_default(24)

    draw.text((10.0, 10.0), captcha_text, fill="black", font=font)

    captcha_image_path = f"captcha_{captcha_text}.png"
    image.save(captcha_image_path)

    return captcha_text, captcha_image_path


captcha_text2, captcha_image_path2 = generate_PIL()
print(f"Captcha Text: {captcha_text2}")
print(f"Captcha Image saved at: {captcha_image_path2}")


def generate_captcha_solver():
    captcha_text = ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))

    solver = CaptchaSolver('browser')

    captcha_image = solver
    captcha_image_path = f'captcha_{captcha_text}.png'
    captcha_image.save(captcha_image_path)

    return captcha_text, captcha_image_path


captcha_text3, captcha_image_path3 = generate_captcha_solver()
print(f"Captcha Text: {captcha_text3}")
print(f"Captcha Image saved at: {captcha_image_path3}")