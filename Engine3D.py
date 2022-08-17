from gl import Renderer, color, V3, V2
from texture import Texture
from shaders import flat, gourad, toon2, negative

width = 960
height = 540

rend = Renderer(width, height)

rend.active_shader = negative
rend.active_texture = Texture("models/bullTexture.bmp")

rend.dirLight = V3(0.5, 0, -0.5)
rend.glLoadModel("models/bull.obj",
                 translate = V3(0, -1, -8),
                 scale = V3(0.2,0.2,0.2),
                 rotate = V3(35,0,0))

rend.glFinish("Outputs/output1.bmp")

#high angle
''' rend.active_shader = gourad
rend.active_texture = Texture("bullTexture.bmp")

rend.dirLight = V3(0.5, 0, -0.5)
rend.glLoadModel("bull.obj",
                 translate = V3(0, -1.7, -8),
                 scale = V3(0.2,0.2,0.2),
                 rotate = V3(-35,0,0))

rend.glFinish("output.bmp") '''


#Low angle
''' rend.active_shader = gourad
rend.active_texture = Texture("bullTexture.bmp")

rend.dirLight = V3(0, -1, 0)
rend.glLoadModel("bull.obj",
                 translate = V3(0, -1.5, -7),
                 scale = V3(0.3,0.3,0.3),
                 rotate = V3(-30,0,0))

rend.glFinish("output.bmp")
 '''
