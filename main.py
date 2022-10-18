import sys
import pygame


class Player():
    x = 50
    y = 50

    playerIMG = pygame.image.load("resources/img.png")

    def __init__(self):
        pass

    def draw(self,surface):
        rect = pygame.Rect(self.x,self.y,50,50)
        pygame.draw.rect(surface,"#3d6973",rect)
        surface.blit(self.playerIMG,(self.x,self.y))

class Projectile():
    
    pass


def drawAll(surface):
    global p

    surface.fill((0,0,0)) #Fills the screen between each draw

    p.draw(surface) #draws the player

    pygame.display.update()

def move():
    global run
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        Player.x -= 10
        
    if keys[pygame.K_RIGHT]:
        Player.x += 10

    if keys[pygame.K_UP]:
        Player.y -= 10

    if keys[pygame.K_DOWN]:
        Player.y += 10

def main():
    global run
    global p
    surface = pygame.display.set_mode((1600,900))
    p = Player()

    clock = pygame.time.Clock()
    run = True

    while run:

        pygame.time.delay(20)

        move()

        drawAll(surface)

        clock.tick()

main()