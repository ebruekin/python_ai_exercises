
import pygame
import random


#width height
WIDTH = 500
HEIGHT =500
FPS = 30

#RGB
RED =(255,0,0)
GREEN=(0,255,0)
BLUE =(0,0,255)
WHİTE =(255,255,255)
BLACK =(0,0,0)
DARKBLUE = (28, 15, 69)
YELLOW = (255, 255, 0)
VIOLET = (128,0,0)

# %% 
#player class
class Player(pygame.sprite.Sprite):
    # sprite for the player
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((30,30))
        self.image.fill(VIOLET)
        self.rect = self.image.get_rect()
        self.radius = 15
        pygame.draw.circle(self.image,VIOLET,self.rect.center,self.radius)
        self.rect.x = WIDTH /2
        self.rect.bottom = HEIGHT
        self.speedx = 0
        
    def update(self,action):
        self.speedx = 0
        #saga ve sola hareket
        keyState = pygame.key.get_pressed()
        
        if keyState[pygame.K_LEFT] or action == 0:
            self.speedx = -7
            
        elif keyState[pygame.K_RIGHT] or action == 1:
            self.speedx = 7
            
        else:
            self.speedx = 0
        
        self.rect.x += self.speedx
        
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
        if self.rect.left < 0:
            self.rect.left =0
            
    def getCoordinates(self):
        return (self.rect.x, self.rect.y)
        
# %% 
        
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((16,16))
        self.image.fill(DARKBLUE)
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(0,WIDTH -self.rect.width)
        self.radius = 8
        pygame.draw.circle(self.image,DARKBLUE,self.rect.center,self.radius)
        self.rect.y = random.randrange(2,155)
        self.speedx = 0
        self.speedy = 5
        
    def update(self):
        self.rect.x += self.speedx
        self.rect.y += (++self.speedy)      
        
       
        
        if self.rect.top > HEIGHT-16:           
            
            self.rect.x = random.randrange(0,WIDTH -self.rect.width)
            self.rect.y = random.randrange(2,15)
            self.speedy = 5       
                                
    def getCoordinates(self):
        return (self.rect.x, self.rect.y)                                         
        
# %%
class AStar:
    def __init__(self, enemies):
        
        self.enemies = enemies
        self.goals = self.find_goal()
        
    
    def isEnemyInside(self, f, t):
        for e in self.enemies:
            if(e >= f and e + 16 <= t):
                return True
        return False
    
    def isBetween(self,x, goal):
        if(x >= goal[0] and x + 30 <= goal[1]):
            return True
        return False
    
    def act(self,PlayerX):
        m = 500
        selectedCost = 0
        for i in range(len(self.goals)):
            value = self.heuristic(PlayerX,self.goals[i]) 
            if(self.isBetween(PlayerX, self.goals[i])):
                return 2
            elif(abs(value) < m):
                m = abs(value)
                selectedCost = value
        if(selectedCost > 0):
            return 1
        else:
            return 0
        
    def find_goal(self):
        fr = 0
        goals = list()
        m = 0
        for e in self.enemies:
            for o in self.enemies:
                print("From: {} - Enemy.X : {}".format(fr,o))
                if(o <= fr):
                    pass
                elif(not self.isEnemyInside(fr,o)):
                    if(o > m):
                        m = o
                    if(o - fr >= 30):
                        goals.append([fr, o])
                    fr = o + 16
                    break
                else:
                    pass
        if(500 - (m + 16) > 30):
            goals.append([(m+16),500])
        return goals
            
     

    def reset(self, enemies):
        self.enemies = enemies
        
        self.goals = self.find_goal()         
                    
    #Cost un bulunması
    def heuristic(self,PlayerX, goal):
        return goal[0] - PlayerX
        

            
# %%
        
class Env(pygame.sprite.Sprite):
    #init
    def __init__(self):
        
        pygame.sprite.Sprite.__init__(self)
        self.all_sprite = pygame.sprite.Group()
        self.enemy = pygame.sprite.Group()
        
        enemy_x = list()
        for e in self.enemy:
            #print(e.rect.x)
            enemy_x.append(e.rect.x)
            
        self.player = Player()
        self.m1 = Enemy()
        self.m2 = Enemy()
        self.m3 = Enemy()
        self.m4 = Enemy()
        
        self.enemy.add(self.m1)
        self.enemy.add(self.m2)
        self.enemy.add(self.m3)
        self.enemy.add(self.m4)
        
        self.all_sprite.add(self.m1)
        self.all_sprite.add(self.m2)
        self.all_sprite.add(self.m3)
        self.all_sprite.add(self.m4)
        
        self.all_sprite.add(self.player)   
        
        self.reward = 0
        self.total_reward = 0
        self.done = False
        self.agent = AStar(enemy_x)
        
        
        
    def findDistance(self,a,b):
        d = a-b
        return d
    #step
    def step(self,action):
        state_list = []
        
        enemy_x = list()
        for e in self.enemy:
            #print(e.rect.x)
            enemy_x.append(e.rect.x)
        
        self.player.update(action)
        self.enemy.update()
        self.agent.reset(enemy_x)

       
    #reset
    def initialState(self):
        #env classındaki init metodundaki agent hariç herşeyi resetliyoruz
        self.all_sprite = pygame.sprite.Group()
        self.enemy = pygame.sprite.Group()
        self.player = Player()
        self.m1 = Enemy()
        self.m2 = Enemy()
        self.m3 = Enemy()
        self.m4 = Enemy()

        self.enemy.add(self.m4)
        self.enemy.add(self.m1)
        self.enemy.add(self.m2)
        self.enemy.add(self.m3)
        self.all_sprite.add(self.m4)
        self.all_sprite.add(self.m1),
        self.all_sprite.add(self.m2)
        self.all_sprite.add(self.m3)
        self.all_sprite.add(self.player)   


    #run   
    def run(self):
        # game loop

        running = True
        #print(self.enemy)
        
    
        
        #self.agent.find_blocked()
        while running:
            self.reward = 2
            # keep loop running at the right speed
            clock.tick(FPS) 
            # process input
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False   
            # update
            action = self.agent.act(self.player.getCoordinates()[0])
            self.step(action)
 
                
            hits = pygame.sprite.spritecollide(self.player,self.enemy,False, pygame.sprite.collide_circle)   
            if hits:

                running = False
    
            

            # draw / render(show)
            screen.fill(YELLOW)
            self.all_sprite.draw(screen)
            # after drawing flip display
            pygame.display.flip()
    
        pygame.quit()  

if __name__ == "__main__":
    env = Env()
    liste = []
    t = 0
    while True:
        t += 1
        print("Episode: ",t)
        liste.append(env.total_reward)
                
        # initialize pygame and create window
        pygame.init()
        screen = pygame.display.set_mode((WIDTH,HEIGHT))
        pygame.display.set_caption("A* Game")
        clock = pygame.time.Clock()
        
        env.run()  
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
# %%    
    
# initialize pygame and create window
pygame.init()
screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("RL Game")
clock = pygame.time.Clock()

# sprite
#all_sprite = pygame.sprite.Group()
#enemy = pygame.sprite.Group()
#player = Player()
#m1 = Enemy()
#m2 = Enemy()
#m3 = Enemy()
#m4 = Enemy()
#enemy.add(m4)
#enemy.add(m1)
#enemy.add(m2)
#enemy.add(m3)
#all_sprite.add(m4)
#all_sprite.add(m1),
#all_sprite.add(m2)
#all_sprite.add(m3)
#all_sprite.add(player)
# %%
# game loop
#running = True
#while running:
#    # keep loop running at the right speed
#    clock.tick(FPS) 
#    
#    # process input
#    for event in pygame.event.get():
#        if event.type == pygame.QUIT:
#            running = False
#    
#    # update
#    all_sprite.update()
#    enemy.update()
#    hits = pygame.sprite.spritecollide(player,enemy,False,pygame.sprite.collide_circle)
#    if hits:
#        running = False
#        print("GAME OVER")
#    
#    # draw / render(show)
#    screen.fill(YELLOW)
#    all_sprite.draw(screen)
#    # after drawing flip display
#    pygame.display.flip()
#    
#pygame.quit()