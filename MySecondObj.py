from PyGine import GameObject, SpriteComponent, BoxColliderComponent
from PyGine import DrawRectComponent
from PyGine import Vector3
from MySecondScript import MySecondScript

class MySecondObj(GameObject) :
    def start(self):
        self.transform.scale.x = 10
        self.transform.position = Vector3(100,100,0)
        self.addComponent(DrawRectComponent(self,(0,255,255)))
        self.addComponent(MySecondScript(self))
