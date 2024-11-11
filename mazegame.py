from ursina import * 
from ursina.prefabs.first_person_controller import FirstPersonController



__ = False

app = Ursina()

class Player(FirstPersonController):
    def __init__(self):
        super().__init__(
            speed = 15,
            model = 'axe.fbx',
            collider = 'mash',
            scale = 0.1,
            #texture = r'textures\axe.jpg'
        )

class Warp(Entity):
    def __init__(self,i,j):
        super().__init__(
            warp = Entity(
                model = 'cube',
                color = color.gray,
                scale = (5,5,5),
                position = (i*5,0,j*5),
                collider = 'box'
            )
        )
        self.a = player
        
    def update(self):
        self.abcd()

    def abcd(self):
        if self.warp.intersects(self.a):
            self.a.position = (0,10,0)

class Exit(Entity):
    def __init__(self,i,j):
        super().__init__(
            model = 'cube',
            color = color.black,
            scale = (5,5,5),
            position = ( i*5 ,0 ,j*5 ),
            collider = 'box'
        )
        self.player = player
        self.text = Text(
            text = 'you escaped!',
            scale = 2,
            origin = (0,0),
            visible = False
        )
    
    def update(self):
        self.clear()
    
    def clear(self):
        dis =  (self.player.position-self.position).length()
        print(dis) 
        if dis < 3.8:
            self.player.enabled = False  
            self.text.visible = True
 
def input(key):
    if key == 'escape':
        app.quit()


#EditorCamera()
player = Player()


axe = Entity(
                model = 'axe.fbx',
                color = color.blue,
                position = (5,0,5),
                scale = 0.1,
                #texture = r'textures\axe.jpg'
              ) 
        


MAP = [
    [11,'p',11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11],
    [11,__,__,__,__,__,__,__,__,__,__,__,__,__,__,__,__,11],
    [11,__,11,__,11,11,11,11,11,11,__,11,11,11,__,11,__,11],
    [11,__,11,__,__,11,__,__,__,11,__,__,__,11,__,11,__,11],
    [11,__,11,11,__,__,__,11,__,11,__,11,11,11,__,__,__,11],
    [11,__,11,__,__,11,__,11,__,11,__,11,__,__,__,11,__,11],
    [11,__,__,__,11,11,__,11,11,11,11,11,__,11,__,11,__,11],
    [11,__,11,__,11,__,__,__,__,__,11,11,__,11,__,__,__,11],
    [11,__,11,11,11,__,11,11,11,__,11,11,__,11,11,11,__,11],
    [11,__,__,__,11,11,11,11,__,__,11,__,__,__,__,11,__,11],
    [11,__,11,__,11,__,11,__,__,11,11,__,11,11,11,11,11,11],
    [11,__,11,__,__,__,11,11,__,__,11,__,__,__,__,__,__,11],
    [11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,'e',11], 
]


MAP1 = [
    [11,'p',11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11],
    [11,__,'w',__,__,11,__,11,11,11,__,11,11,11,__,11,11,11,__,11,11,11,__,11,11],
    [11,11,11,11,__,11,__,11,11,11,__,11,11,11,__,__,__,__,__,__,__,__,__,11,11],
    [11,11,11,__,__,11,__,11,11,11,__,11,11,11,__,11,11,11,11,11,11,11,__,11,11],
    [11,11,__,__,11,11,__,11,11,11,__,11,11,11,__,11,11,__,__,__,11,11,__,11,11],
    [11,__,__,11,11,11,__,11,11,11,__,11,11,11,__,11,__,__,11,__,__,__,__,11,11],
    [11,__,11,11,11,11,__,11,11,__,__,__,11,11,__,11,__,11,11,11,__,11,__,11,11],
    [11,__,__,__,__,__,__,11,11,__,11,__,11,11,__,11,__,__,11,__,__,__,__,11,11],
    [11,__,11,11,11,11,__,11,__,__,11,__,__,11,__,11,11,__,__,__,11,11,__,11,11],
    [11,__,11,11,11,11,__,11,__,11,11,11,__,11,__,11,11,11,__,11,11,11,__,11,11],
    [11,__,__,__,__,__,__,__,__,11,11,11,__,__,__,11,11,11,__,11,11,11,11,11,11],
    [11,11,11,11,11,11,11,__,11,11,11,11,11,__,11,11,11,11,__,11,11,11,11,11,11],
    [11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,__,__,__,__,__,__,11],
    [11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,'e',11],


]





for i in range(len(MAP1)):
    for j in range(len(MAP1[i])):
        if MAP1[i][j]:
            if MAP1[i][j] == 'p':
                player.position = (i*5,2,j*5)
                continue

            
            if MAP1[i][j] == 'e':
                exitdoor = Exit(i,j)
                continue
            
            if MAP1[i][j] == 'w':
                warp = Warp(i,j)
                continue

            wall = Entity(
                model = 'cube',
                color = color.gray,
                scale = (5,5,5),
                position = (i*5,0,j*5),
                collider = 'box',
                #texture = r'medieval_red_brick_4k.blend\textures\medieval_red_brick_diff_4k.jpg'
              ) 
            
           



ground = Entity(
    model = 'plane',
    color = color.yellow,
    position = (0,-1,0),
    scale = (2000,1,2000),
    collider = 'mesh',
    #texture = r'raw_plank_wall_4k.blend\textures\raw_plank_wall_diff_4k.jpg'

)


app.run() 