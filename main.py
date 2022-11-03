from PyGine import PyGineGame
from Scene1 import maPremeiereScene
class myGame(PyGineGame) :
    def __init__(self):
        super().__init__(1000,600,self)
        self.addScene(maPremeiereScene())
        self.setScene(0)

    def update(self):
        self.setCaption(f"My awesome game ! dt : {self.dt} ms")


myGame().run()
