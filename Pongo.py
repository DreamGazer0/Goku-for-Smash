import pygame

pygame.init()

width = 400; height = 400
screen = pygame.display.set_mode((width, height))

white = (255, 255, 255)
black = (0, 0, 0)

clock = pygame.time.Clock()
FPS = 180

blockX = 30
blockY = 130

block2X = 360
block2Y = 30
blockW = block2W = 10
blockH = block2H = 100
#Grapes
moveUp = True
moveDown = False

while True:

    clock.tick(FPS)

    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit(); sys.exist()
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w] and blockY > 0:
        blockY -= 10
    if keys[pygame.K_s] and blockY < 400 - blockH:
        blockY += 10
    if keys[pygame.K_o] and block2Y > 0:
        block2Y -= 10
    if keys[pygame.K_l] and block2Y < 400 - block2H:
        block2Y += 10
        '''            
        if blockY >= 0 and moveUp:
            blockY -= 2
            if blockY < 0:
                moveUp = False
                moveDown = True
        elif (blockY + 100) < 400 and moveDown:
            blockY += 2
        else:
            moveUp = True
            moveDown = False
        '''

                
    screen.fill(black)
    #pygalme.draw.circle(screen, (255, 0, 0), (int(posX), int(posY)), 10)
    pygame.draw.rect(screen, (white), (block2X, block2Y, block2W, block2H), 0)
    pygame.draw.rect(screen, (white), (blockX, blockY, blockW, blockH), 0)

    pygame.display.update()
