from pyexpat import model
import sys
from turtle import position
from ursina import *
from ursina.shaders import lit_with_shadows_shader

Entity.default_shader = lit_with_shadows_shader
app = Ursina()

exit = Button(text='hello world!', color=color.red, scale=.1, text_origin=(0,0), position=(20, 200, 0))
exit.on_click = application.quit

enableFB = False
sphereTexture = FileBrowser(file_types=('.*'), enabled=enableFB)
userModel = "sphere"

ground = Entity(
    model = "cube",
    collider = "ground",
    scale = (25, 1, 25),
    texture='grass',
    position = (0, -1, 0),
)

defaultCube = Entity(
    model = userModel,
    collider = "sphere",
    texture = sphereTexture
)


window.color=color.light_gray.tint(.1)
camera.orthographic = False
camera.fov = 8

sun = DirectionalLight()

sun.look_at(Vec3(1,-1,-1))
Sky()

EditorCamera()

app.run()