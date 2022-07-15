from gl import Renderer, color, V2
import random

width = 1920
height = 1080

rend = Renderer(width, height)

steps = 100

dy = height / steps
dx = width / steps

x = 0
y = height
for i in range(steps):
    rend.glLine(V2(x,0), V2(0, y))
    rend.glLine(V2(x,0), V2(width, height - y))
    rend.glLine(V2(width - x,height), V2(0, y))
    rend.glLine(V2(width - x,height), V2(width, height - y))
    x += dx
    y -= dy




rend.glFinish("output.bmp")

