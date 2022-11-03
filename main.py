from PyGine import PyGineGame
from Scene1 import maPremeiereScene
class myGame(PyGineGame) :
    def __init__(self):
        super().__init__(1000,600,self)

        self.addScene(maPremeiereScene())

        self.setScene(0)
        self.setCaption("mon super premier jeu")


myGame().run()
