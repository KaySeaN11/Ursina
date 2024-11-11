from ursina import * 
from ursina.prefabs.first_person_controller import FirstPersonController
import time



__ = False

app = Ursina()

class Player(FirstPersonController):
    def __init__(self):
        super().__init__(
            speed = 15,
            model = 'cube',
            collider = 'box',
            scale = 1,
            #texture = r'textures\axe.jpg'
        )
class Coin(Entity):
    def __init__(self, x, z):
        super().__init__(
            model='circle',
            color=color.yellow,
            scale=1,
            position=(x*5, 0, z*5),
            collider='box',
            double_sided=True
        )

    def update(self):
        # 회전 값을 간단하게 π (3.14159)로 설정
        self.rotation_y += 3  # 또는 math.pi를 써도 됩니다. 예: self.rotation_y += math.pi
        
        # 플레이어와의 충돌 확인
        if self.intersects(player):
            destroy(self)  # 충돌하면 동전 제거
          


class Warp(Entity):
    def __init__(self, i, j):
        super().__init__(
            model = 'cube',
            color = color.gray,
            scale = (5, 5, 5),
            position = (i*5, 0, j*5),
            collider = 'box'
        )
        self.player = player  # 전역 player 객체를 참조

    def update(self):
        if self.intersects(self.player):  # self.warp -> self
            self.player.position = (0, 5, 5)

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


EditorCamera()
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
    [11,__,__,__,__,11,__,11,11,11,__,11,11,11,__,11,11,11,__,11,11,11,__,11,11],
    [11,'w',11,11,__,11,__,11,11,11,__,11,11,11,__,__,__,__,__,__,__,__,__,11,11],
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
                player.position = (i*5,5,j*5)
                continue

            
            if MAP1[i][j] == 'e':
                exitdoor = Exit(i,j)
                continue
            
            if MAP1[i][j] == 'w':
                warp = Warp(i,j)
                continue

            wall = Entity(
                model = 'cube',
                #color = color.brown,
                scale = (5,10,5),
                position = (i*5,0,j*5),
                collider = 'box',
                texture = 'brick'
              ) 
        else:
            coin = Coin(i,j)           
           



ground = Entity(
    model = 'plane',
    #color = color.yellow,
    position = (0,-1,0),
    scale = (2000,1,2000),
    collider = 'mesh',
    texture = 'grass'

)

Sky(texture = 'sky_sunset')

app.run() 