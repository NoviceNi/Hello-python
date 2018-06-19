#! /usr/bin/env python
# -*- coding:utf-8 -*-
from PIL import Image, ImageFilter, ImageDraw, ImageFont
import os
import sys
import random

def rndChar():
    return chr(random.randint(65, 90))

def rndColor():
    return (random.randint(64, 255), random.randint(64, 255), random.randint(64, 255))

def rndColor2():
    return (random.randint(32, 127), random.randint(32, 127), random.randint(32, 127))

w = 60 * 4
h = 60
img = Image.new("RGB", (w, h), (255, 255, 255))
draw = ImageDraw.Draw(img)

font = ImageFont.truetype("C:\Windows\Fonts\Arial.ttf", 36)
for x in range(w):
    for y in range(h):
        draw.point((x, y),fill=rndColor())

for i in range(4):
    draw.text((60*i + 10, 10), rndChar(), fill=rndColor2(), font=font)

image = img.filter(ImageFilter.BLUR)
image.show()
