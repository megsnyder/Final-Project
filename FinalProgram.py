'''
Final Project:
A game where you try to hit a moving object, can control what angle you use
Sources: Noah, https://www.pythoncentral.io/how-to-generate-a-random-number-in-python/
'''
from ggame import App, Color, LineStyle, Sprite, RectangleAsset, CircleAsset, EllipseAsset, PolygonAsset, ImageAsset, Frame
from math import floor, sin, cos
import random
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 800

blue = Color(0x2EFEC8, 1.0)
black = Color(0x000000, 1.0)
pink = Color(0xFF00FF, 1.0)
red = Color(0xFF5733, 1.0)
white = Color(0xFFFFFF, 1.0)
red = Color(0xff0000, 1.0)
green = Color(0x00ff00, 1.0)
blue = Color(0x0000ff, 1.0)
black = Color(0x000000, 1.0)
white = Color(0xffffff, 1.0)
grey = Color(0xC0C0C0, 1.0)
teal = Color(0x9fffff, 1.0)
coral = Color(0xff9664, 1.0)
clear = Color(0x000000, 0.0)
bluegrey = Color(0x585d7c, 1.0)
blueblack = Color(0x37394c, 1.0)
winter = Color(0x1f1a68, 1.0)
maroon = Color(0x9f2d42, 1.0)
purple = Color(0x9f86c0, 1.0)

thinline = LineStyle(2, black)
blkline = LineStyle(1, black)
noline = LineStyle(0, white)
coolline = LineStyle(1, grey)
blueline = LineStyle(2, blue)
redline = LineStyle(1, red)
greenline = LineStyle(1, green)
gridline = LineStyle(1, grey)
clearline = LineStyle(1, clear)
tealline =  LineStyle(1, teal)
grid=RectangleAsset(30,30,gridline,white)

print("Hold down the mouse button to wind up your arm. Release and the snowball gets released as well.")

class Player(Sprite):
    """
    Create Player
    """
    asset=ImageAsset("images/Screenshot 2018-11-28 at 11.png")

    def __init__(self, position):
        super().__init__(Player.asset, position)
        
        self.vx = 0
        self.vy = 0

class Snow(Sprite):
    asset = RectangleAsset(2,2,noline,white)

    def __init__(self, position):
        super().__init__(Snow.asset, position)
        self.vx = 0
        self.vy = 5
class Arm(Sprite):
    asset = EllipseAsset(4,8, gridline, black)
    def __init__(self, position):
        super().__init__(Arm.asset, position)
        self.vx = 0
        self.vy = 0
        self.vr=0
        self.fxcenter=.5
        
class Snowball(Sprite):
    asset = CircleAsset(4, noline, white)
    def __init__(self, position):
        super().__init__(Snowball.asset, position)
        self.vx = 0
        self.vy = 0
        self.vr=0
        self.fxcenter=.5
        self.fycenter=-1.5
        self.m=0
class Game(App):
    """
    Tutorial4 space game example.
    """
    
    def __init__(self):
        super().__init__()
        # Backgroundw
        bg_asset = RectangleAsset(self.width, self.height, noline, winter)
        ground_asset = RectangleAsset(self.width, 300, noline, white)
        bg = Sprite(bg_asset, (0,0))
        ground = Sprite(ground_asset, (0,400))
        Player((54,343))
        self.asset = [0,0]
        Game.listenMouseEvent('mousedown', self.armspin)
        Game.listenMouseEvent('mouseup', self.armstop)
        Snowball((70,375))
        Arm((70,375))
        m=0
        
    def snowMaker():
        rand=random.randint(1,1001)
        rand2 = random.randint(1,1001)
        rand3 =random.randint(1,1001) 
        Snow((rand,0))
        Snow((rand2,0))
        Snow((rand3,0))
        for snow in Game.getSpritesbyClass(Snow):
            if snow.y>700:
                snow.destroy()
    def armspin(self,event):
        for arm in self.getSpritesbyClass(Arm):
            arm.vr=0.01
        for snowball in self.getSpritesbyClass(Snowball):
            snowball.vr=0.01
    def armstop(self, event):
        for arm in self.getSpritesbyClass(Arm):
            arm.vr=0
        for snowball in self.getSpritesbyClass(Snowball):
            snowball.vx0= (cos(snowball.rotation))*snowball.vr
            snowball.vy0=-(sin(snowball.rotation))*snowball.vr
            snowball.vr=0
            
    n=0
    time=0

    def step(self):
        for arm in self.getSpritesbyClass(Arm):
            if arm.vr>0:
                arm.vr = arm.vr+.01
            arm.rotation += arm.vr
            arm.x += arm.vx
            arm.y += arm.vy
        for snowball in self.getSpritesbyClass(Snowball):
            if snowball.vr>0:
                snowball.vr = snowball.vr+.01
                snowball.m+=1
            if snowball.vr==0 and snowball.m>0:
                #print("hi")
                snowball.vx=snowball.vx0*30
                snowball.vy=snowball.vy0*30 + .05*self.time
        
            snowball.rotation += snowball.vr
            snowball.x += snowball.vx
            snowball.y += snowball.vy 
        self.time+=1
        self.n+=1
        if self.n%5==0:
            Game.snowMaker()
        for snow in self.getSpritesbyClass(Snow):
            snow.vy = snow.vy+.25  

            snow.y += snow.vy
           
myapp = Game()
myapp.run()







