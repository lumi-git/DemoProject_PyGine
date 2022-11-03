from PyGine import PyGineGame
from Scene1 import maPremeiereScene
class myGame(PyGineGame) :
    def __init__(self):
        super().__init__(1000,600,self)
        self.addScene(maPremeiereScene())
        self.setScene(0)
        self.fps = 60
    def update(self):
        self.setCaption(f"My awesome game ! fps : {round(1000/self.dt)} fps")


myGame().run()










