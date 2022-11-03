from PyGine import GameObject
from PyGine import SpriteComponent
from PyGine import Vector3
from PyGine.Debug import PrintDebug
from MyFirstScript import MyFirstScript

class MyFirstOb(GameObject) :

    def start(self):


        PrintDebug("my first object is starting !")
        # modifying the start x scale of the object in the scene
        self.transform.scale= Vector3(100,100,0)
        # modifying the start position of the object in the scene
        self.transform.position = Vector3(100,100,0)

        # attach a drawCircle component, from the standard lib of PyGine, to this gameobject
        self.addComponent(SpriteComponent(self,"FirstSprite.png"))

        # attach a custom component, called a script, to this gameobject
        self.addComponent(MyFirstScript(self))

        #attach the camera to this object
        self.AttachCamera(True)