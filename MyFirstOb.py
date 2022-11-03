from PyGine import GameObject
from PyGine import DrawCircleComponent
from PyGine import Vector3
from PyGine.Debug import PrintDebug
from MyFirstScript import MyFirstScript

class MyFirstOb(GameObject) :

    def start(self):


        PrintDebug("my first object is starting !")
        # modifying the start x scale of the object in the scene
        self.transform.scale.x = 10

        # modifying the start position of the object in the scene
        self.transform.position = Vector3(100,100,0)

        # attach a drawCircle component, from the standard lib of PyGine, to this gameobject
        self.addComponent(DrawCircleComponent(self,(255,0,0,0),self.transform.scale.x))

        # attach a custom component, called a script, to this gameobject
        self.addComponent(MyFirstScript(self))

        #attach the camera to this object
        self.AttachCamera(True)