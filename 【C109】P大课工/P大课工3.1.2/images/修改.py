from PIL import Image
from typing import Sized
import colorsys
pic = Image.open("start.png")
w,h = pic.size
pic.thumbnail((w//2,h//2))
pic.save("start.png","PNG")