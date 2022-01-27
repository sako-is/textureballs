from pyexpat import model
from string import whitespace
import sys
from turtle import position
from ursina import *
from ursina.shaders import lit_with_shadows_shader
from ursina.prefabs.first_person_controller import FirstPersonController

Entity.default_shader = lit_with_shadows_shader
app = Ursina()

# exit = Button(text='quit', color=color.red, scale=.1, text_origin=(0,0), position=(20, 200, 0))
# exit.on_click = application.quit


enableFB = False
# enableFButton = Button(text='enable', color=color.white, scale = 0.1)

sphereTexture = FileBrowser(file_types=('.*'), enabled=enableFB)
userModel = "sphere"

ground = Entity(
    model = "cube",
    collider = "ground",
    scale = (25, 1, 25),
    texture='grass',
    position = (0, -1, 0),
)

class UserObject(Button):
    def __init__(self, position = (0, 0, 0)):
        super().__init__(
            parent = scene,
            model = userModel,
            collider = "sphere",
            texture = "brick", 
            position = position,
            color = color.white,
            opacity = 1
        )

    def input(self, key):
        if self.hovered:
            if key == 'left mouse down':
                self.y += 1


window.color=color.light_gray.tint(.1)
camera.orthographic = False
camera.fov = 8

sun = DirectionalLight()

sun.look_at(Vec3(1,-1,-1))
Sky()
defaultObj = UserObject()

player = FirstPersonController()
EditorCamera()

def update():
    if held_keys['W']: player.x += 1
    if held_keys['A']: player.y -= 1
    if held_keys['S']: player.x -= 1
    if held_keys['D']: player.y += 1
    if held_keys['Space']: player.z += 1
    if held_keys['E']: player.z += 1
    if held_keys['Q']: player.z -= 1

app.run()
