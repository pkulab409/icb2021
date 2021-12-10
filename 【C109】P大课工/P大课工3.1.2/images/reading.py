from PIL import Image
from typing import Sized
import colorsys
pic1 = Image.open("北京大学还是你最卷啊.jpg")
pic2 = Image.open("background2.jpg")
x,y = pic2.size
w,h = pic1.size
print(w,h)
print(x,y)