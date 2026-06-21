from direct.showbase.ShowBase import ShowBase
 
# class
class Game(ShowBase):
    def __init__(self):
        ShowBase.__init__(self)
        # load the model 
        # uncomment the lines one-by-one to see what the model looks like
        self.model = loader.loadModel('Blimp.egg')
        # self.model = loader.loadModel('Boeing707.egg')
        # self.model = loader.loadModel('Fighter.egg')
        # self.model = loader.loadModel('Sailboat.egg')
        # move model to render, change parent
        self.model.reparentTo(render)
        # try resizing the model
        self.model.setScale(0.1)
        # try moving the model along all the axes
        self.model.setPos(-2, 25, -3)
    
game = Game()
game.run()