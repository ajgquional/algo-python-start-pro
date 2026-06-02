from pygame import *

# fix if the game assets cannot be found even if it is in the same folder as the script
# this happens when the terminal does not point specifically to the folder where the script is located, but to a parent folder
from pathlib import Path
script_dir = Path(__file__).resolve().parent

# parent class for sprites
class GameSprite(sprite.Sprite):
   #class constructor
   def __init__(self, player_image, player_x, player_y, player_speed):
       super().__init__()
       # each sprite must store an image property
       self.image = transform.scale(image.load(script_dir / player_image), (55, 55))
       # use image.load(player_image), (55, 55)) if terminal points to the folder where the script is located
       self.speed = player_speed
       # each sprite must store the rect property it is inscribed in
       self.rect = self.image.get_rect()
       self.rect.x = player_x
       self.rect.y = player_y

   def reset(self):
       window.blit(self.image, (self.rect.x, self.rect.y))


# child class for the player sprite (controlled by arrows)
class Player(GameSprite):
   def update(self):
       keys = key.get_pressed()
       if keys[K_LEFT] and self.rect.x > 5:
           self.rect.x -= self.speed
       if keys[K_RIGHT] and self.rect.x < win_width - 80:
           self.rect.x += self.speed
       if keys[K_UP] and self.rect.y > 5:
           self.rect.y -= self.speed
       if keys[K_DOWN] and self.rect.y < win_height - 80:
           self.rect.y += self.speed


# child class for the enemy sprite (moves itself)
class Enemy(GameSprite):
   def update(self):
       if self.rect.x <= 470:
           self.side = "right"
       if self.rect.x >= win_width - 85:
           self.side = "left"
       if self.side == "left":
           self.rect.x -= self.speed
       else:
           self.rect.x += self.speed


# class for obstacle sprites
class Wall(sprite.Sprite):
   def __init__(self, color_1, color_2, color_3, wall_x, wall_y, wall_width, wall_height):
       super().__init__()
       self.color_1 = color_1
       self.color_2 = color_2
       self.color_3 = color_3
       self.width = wall_width
       self.height = wall_height
       # picture of the wall — a rectangle of the desired size and color
       self.image = Surface((self.width, self.height))
       self.image.fill((color_1, color_2, color_3))
       # each sprite must store a rect property
       self.rect = self.image.get_rect()
       self.rect.x = wall_x
       self.rect.y = wall_y
   
   def draw_wall(self):
       window.blit(self.image, (self.rect.x, self.rect.y))
       # draw.rect(window, (self.color_1, self.color_2, self.color_3), (self.rect.x, self.rect.y, self.width, self.height))


# game scene:
win_width = 700
win_height = 500
window = display.set_mode((win_width, win_height))
display.set_caption("Maze")
background = transform.scale(image.load(script_dir / "background.jpg"), (win_width, win_height))
# use image.load("background.jpg"), (win_width, win_height)) if terminal points to the folder where the script is located

# game characters:
player = Player(script_dir / 'hero.png', 5, win_height - 80, 4)
monster = Enemy(script_dir / 'cyborg.png', win_width - 80, 280, 2)
final = GameSprite(script_dir / 'treasure.png', win_width - 120, win_height - 80, 0)

# creating the walls of the maze
# wall parameters: color_1, color_2, color_3, wall_x, wall_y, wall_width, wall_height

color_1 = 154
color_2 = 205
color_3 = 50

walls = [
    # original walls
    Wall(color_1, color_2, color_3, 100, 20 , 600, 10), # w1 # original wall_width = 450
    Wall(color_1, color_2, color_3, 100, 480, 350, 10), # w2
    Wall(color_1, color_2, color_3, 100, 20 , 10, 380), # w3

    # expansion
    Wall(color_1, color_2, color_3, 200, 100 , 400, 10),
    Wall(color_1, color_2, color_3, 200, 100 , 10, 380),
    Wall(color_1, color_2, color_3, 600, 100 , 10, 150),
    Wall(color_1, color_2, color_3, 600, 350 , 10, 50),
]

game = True
finish = False
clock = time.Clock()
FPS = 60

font.init()
font = font.Font(None, 70)
win = font.render('YOU WIN!', True, (255, 215, 0))
lose = font.render('YOU LOSE!', True, (180, 0, 0))

# music
mixer.init()
mixer.music.load(script_dir / 'jungles.ogg')
# use mixer.music.load("jungles.ogg") if terminal points to the folder where the script is located
mixer.music.play()

# sound effects
money = mixer.Sound(script_dir / 'money.ogg')
# use mixer.Sound("money.ogg") if terminal points to the folder where the script is located
kick = mixer.Sound(script_dir / 'kick.ogg')
# use mixer.Sound("kick.ogg") if terminal points to the folder where the script is located

# game loop
while game:
   for e in event.get():
       if e.type == QUIT:
           game = False
  
   if finish != True:
       window.blit(background,(0, 0))
       player.update()
       monster.update()
      
       player.reset()
       monster.reset()
       final.reset()

       for wall in walls:
           wall.draw_wall()

       # "Losing" situation
       if sprite.collide_rect(player, monster) or any(sprite.collide_rect(player, wall) for wall in walls):
           finish = True
           window.blit(lose, (200, 200))
           kick.play()

       # "Winning" situation
       if sprite.collide_rect(player, final):
           finish = True
           window.blit(win, (200, 200))
           money.play()

   display.update()
   clock.tick(FPS)
