from gl import Renderer, color
import random

width = 100
height = 100

rend = Renderer(width, height)

rend.glViewport(int(width / 4),
                int(height / 4),
                int(width / 4),
                int(height / 4))

rend.glClearColor(0,0.5,0)
rend.glClear()
rend.glClearViewport(color(0.5,0,0))


rend.glPoint_vp(0,0)


rend.glFinish("output.bmp")



# Static
#for x in range(width):
#    for y in range(height):
#        if random.random() > 0.5:
#            rend.glPoint(x, y, color(1,1,1))

#Color static
#for x in range(width):
#    for y in range(height):
#        pixelColor = color(random.random(), random.random(),random.random())
#        rend.glPoint(x, y, pixelColor)

#for x in range(width):
#    # y = mx + b
#    slope = 3
#    y = int(slope * x)
#    rend.glPoint(x, y)

# Starfield
#for x in range(width):
#    for y in range(height):
#        if random.random() > 0.995:
#            size = random.randrange(0, 3)

#            brightness = random.random() / 2 + 0.5

#            starColor = color(brightness, brightness, brightness)

#            if size == 0:
#                rend.glPoint(x,y,starColor)

#            elif size == 1:
#                rend.glPoint(x,y,starColor)
#                rend.glPoint(x+1,y,starColor)
#                rend.glPoint(x+1,y+1,starColor)
#                rend.glPoint(x,y+1,starColor)

#            elif size == 2:
#                rend.glPoint(x,y,starColor)
#                rend.glPoint(x,y+1,starColor)
#                rend.glPoint(x,y-1,starColor)
#                rend.glPoint(x+1,y,starColor)
#                rend.glPoint(x-1,y,starColor)


