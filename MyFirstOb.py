from PyGine import GameObject
from PyGine import DrawCircleComponent
from PyGine import Vector3
from PyGine.Debug import PrintDebug
from MyFirstScript import MyFirstScript

class MyFirstOb(GameObject) :
    def start(self):
        PrintDebug("my first object is starting !")
        self.transform.scale.x = 10
        self.transform.position = Vector3(100,100,0)
        self.addComponent(DrawCircleComponent(self,(255,0,0,0),self.transform.scale.x))
        self.addComponent(MyFirstScript(self))