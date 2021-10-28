import pygame

pygame.init()

WIDTH = 1280
HEIGHT = 720
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))

pygame.display.set_caption('My Game')

#Player Variables
posX = 200
posY = 200
vel = 5
cubeWidth = HEIGHT//10
cubeHeight = HEIGHT//10
cubeColor = (255, 0, 0)

#Main Loop
is_running = True
while is_running:
    pygame.time.delay(10)
    keys = pygame.key.get_pressed()
    for event in pygame.event.get(): 
        if (event.type == pygame.QUIT): 
            run = False
        #Cube and mouse collition
        if (event.type == pygame.MOUSEBUTTONDOWN): 
            mouse_position = pygame.mouse.get_pos() 
            if (cube.collidepoint( mouse_position)):
                print("hit")
            else:
                print("click-outside!")

    #Player Sprite
    cube = pygame.Rect(posX, posY, cubeWidth, cubeHeight)

    #Player Movement 
    if (keys[pygame.K_LEFT] or keys[pygame.K_a]) and posX>0: 
        posX -= vel 
    if (keys[pygame.K_RIGHT] or keys[pygame.K_d]) and posX<WIDTH-cubeWidth: 
        posX += vel 
    if (keys[pygame.K_UP] or keys[pygame.K_w]) and posY>0: 
        posY -= vel 
    if (keys[pygame.K_DOWN] or keys[pygame.K_s]) and posY<HEIGHT-cubeHeight: 
        posY += vel 

    #Render Block
    SCREEN.fill((0, 0, 0)) 
    pygame.draw.rect( SCREEN, cubeColor, cube)  # Draw Our Rectangle
    pygame.display.update()  

pygame.quit()