from gl import Renderer, color, V3, V2
from shaders import flat

width = 960
height = 540

rend = Renderer(width, height)

rend.active_shader = flat

rend.glLoadModel("model.obj",
                 translate = V3(width/2, height/2, 250),
                 rotate = V3(0, 180, 0), 
                 scale = V3(200,200,200))


rend.glFinish("output.bmp")

