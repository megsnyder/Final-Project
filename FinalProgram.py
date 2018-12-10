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
print(" ")

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
        self.reverse=False
        self.spin=False
    '''    
    def step(self):
    
        if self.vr>0:
            self.vr = self.vr+.01
        self.rotation += self.vr
        self.x += self.vx
        self.y += self.vy
    '''
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
        self.time=0
        self.score=0
        self.holding=True
        self.reverse=False
        self.spin=False
    
    def step(self):
        if self.reverse==False:
            if self.spin==True and self.holding==True:
                self.vr = self.vr+.01
                self.m+=1
            if self.spin==False and self.m>0 and self.holding==False:
                #print("hi")
                self.vx=self.vx0*35
                self.vy=self.vy0*35 + .1*self.time
        if self.reverse==True:
            if self.spin==True and self.holding==True:
                self.vr = self.vr-.01
                self.m+=1
            if self.spin==False and self.m>0 and self.holding==False:
                #print("hi")
                self.vx=-self.vx0*35
                self.vy=self.vy0*35 + .1*self.time
        self.rotation += self.vr
        self.x += self.vx
        self.y += self.vy 
        self.time+=1
        '''
        for snowman in Game.getSpritesbyClass(Snowman):
                if self.collidingWith(snowman):
                    snowman.destroy()
                    self.score=self.score+1
                    print(self.score)
         for snowman in Game.getSpritesbyClass(Snowman):            
            for player in Game.getSpritesbyClass(Player):
                for arm in Game.getSpritesbyClass(Arm):
                    if snowman.collidingWith(player):
                        player.destroy()
                        arm.destroy()
                        self.destroy()
                        print("Your score is: " + str(self.score))
        '''
        
class Snowman(Sprite):
    asset=ImageAsset("images/Screenshot 2018-11-28 at 12.png")

    def __init__(self, position):
        super().__init__(Snowman.asset, position)
        
        self.vx = 0
        self.vy = 0
class Core(Sprite):
    asset=RectangleAsset(30,150,noline, teal)

    def __init__(self, position):
        super().__init__(Core.asset, position)
        self.visible=False
        self.vx = 0
        self.vy = 0

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
        Player((484,343))
        self.asset = [0,0]
        Game.listenMouseEvent('mousedown', self.armspin)
        Game.listenMouseEvent('mouseup', self.armstop)
        Game.listenKeyEvent("keydown", "right arrow", self.right)
        #Game.listenKeyEvent("keyup", "right arrow", self.right2)
        Game.listenKeyEvent("keydown", "left arrow", self.left)
        #Game.listenKeyEvent("keyup", "left arrow", self.left2)
        Snowball((500,375))
        Arm((500,375))
        #Snowman((400,195))
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
            arm.spin=True
        for snowball in self.getSpritesbyClass(Snowball):
            if snowball.holding==True:
                snowball.spin=True

    def armstop(self, event):
        for arm in self.getSpritesbyClass(Arm):
            arm.vr=0
            arm.spin=False
            arm.destroy()
        for snowball in self.getSpritesbyClass(Snowball):
            if snowball.holding==True:
                snowball.vx0= (cos(snowball.rotation))*snowball.vr
                snowball.vy0=-(sin(snowball.rotation))*snowball.vr
                snowball.vr=0
                snowball.spin=False
                snowball.holding=False
            if snowball.y>700:
                snowball.destroy()
        for player in self.getSpritesbyClass(Player):        
            Snowball((500,375))
            Arm((500,375))
    def right(self,event):
        for player in self.getSpritesbyClass(Player):
            #player.vx = 2
            player.width=42
            player.x=484
        for arm in self.getSpritesbyClass(Arm):
            #arm.vx = 2
            arm.reverse=False
        for snowball in self.getSpritesbyClass(Snowball):
            snowball.reverse=False
            #if snowball.holding==True:
                #snowball.vx = 2
    '''
    def right2(self,event):
        for player in self.getSpritesbyClass(Player):
            player.vx=0 

        for arm in self.getSpritesbyClass(Arm):
            arm.vx = 0
        for snowball in self.getSpritesbyClass(Snowball):
            if snowball.holding==True:
                snowball.vx = 0
    '''
    def left(self,event):
        for player in self.getSpritesbyClass(Player):
            #player.vx = -2
            
            player.width=-42
            player.x=player.x+30
        for arm in self.getSpritesbyClass(Arm):
            #arm.vx = -2
            arm.reverse=True
        for snowball in self.getSpritesbyClass(Snowball):
            snowball.reverse=True
            #if snowball.holding==True:
                #snowball.vx = -2
    '''
    def left2(self,event):
        for player in self.getSpritesbyClass(Player):
            player.vx=0 
            player.width=player.width
            #player.x=player.x-30
        for arm in self.getSpritesbyClass(Arm):
            arm.vx = 0
        for snowball in self.getSpritesbyClass(Snowball):
            if snowball.holding==True:
                snowball.vx = 0
    '''
    
    def snowmenMaker():
        Snowman((1100,195))
        Core((1170,250))
        for snowman in Game.getSpritesbyClass(Snowman):
            if snowman.x<0:
                snowman.destroy()
        for core in Game.getSpritesbyClass(Core):
            if core.x<0:
                core.destroy()
            
    n=0
    time=0
    o=0
    score=0
    def step(self):
        #for arm in self.getSpritesbyClass(Arm):
            #arm.step()
        for snowball in self.getSpritesbyClass(Snowball):
            snowball.step()
        for player in self.getSpritesbyClass(Player):
 
            player.x += player.vx
            player.y += player.vy
        
        for arm in self.getSpritesbyClass(Arm):
            if arm.reverse==False:
                if arm.spin==True:
                    arm.vr = arm.vr+.01
            if arm.reverse==True:
                if arm.spin==True:
                    arm.vr = arm.vr-.01
            arm.rotation += arm.vr
            arm.x += arm.vx
            arm.y += arm.vy
        '''
        for snowball in self.getSpritesbyClass(Snowball):
            if snowball.vr>0:
                snowball.vr = snowball.vr+.01
                snowball.m+=1
            if snowball.vr==0 and snowball.m>0:
                #print("hi")
                snowball.vx=snowball.vx0*35
                snowball.vy=snowball.vy0*35 + .1*self.time
                
            snowball.rotation += snowball.vr
            snowball.x += snowball.vx
            snowball.y += snowball.vy 
        '''
        
    
        if self.n%5==0:
            Game.snowMaker()
        for snow in self.getSpritesbyClass(Snow):
            snow.vy = snow.vy+.25  

            snow.y += snow.vy
        if self.o%130==0:
            Game.snowmenMaker()
        if self.time>0:
            for core in self.getSpritesbyClass(Core):
                core.vx = -7

                core.x += core.vx
            for snowman in self.getSpritesbyClass(Snowman):
                snowman.vx = -7  

                snowman.x += snowman.vx
        if self.time>750:
            for core in self.getSpritesbyClass(Core):
                core.vx = -11

                core.x += core.vx
            for snowman in self.getSpritesbyClass(Snowman):
                snowman.vx = -11  

                snowman.x += snowman.vx
        if self.time>1250:
            for core in self.getSpritesbyClass(Core):
                core.vx = -15

                core.x += core.vx
            for snowman in self.getSpritesbyClass(Snowman):
                snowman.vx = -15  

                snowman.x += snowman.vx
        
        for snowman in self.getSpritesbyClass(Snowman):
            for snowball in self.getSpritesbyClass(Snowball):
                for core in self.getSpritesbyClass(Core):
                    if snowball.collidingWith(core):
                        snowman.destroy()
                        core.destroy()
                        self.score=self.score+1
                        #print(self.score)
        '''
        for core in self.getSpritesbyClass(Core):
            for snowman in self.getSpritesbyClass(Snowman):
                for snowball in self.getSpritesbyClass(Snowball):
                    for player in self.getSpritesbyClass(Player):
                        for arm in self.getSpritesbyClass(Arm):
                            if core.collidingWith(player):
                                player.destroy()
                                arm.destroy()
                                snowball.destroy()
                                print("Your score is: " + str(self.score))
        '''               
            
        self.time+=1
        self.n+=1
        self.o+=1
        
myapp = Game()
myapp.run()







