import pygame, sys

def drawtext(text, color, size, surface, x, y, font=None, alignment="topleft"):
    font = pygame.font.SysFont(font, size)
    obj = font.render(text, 1, color)
    rect = obj.get_rect()

    # Tops
    if alignment == "topleft":
        rect.topleft = (x, y)
    elif alignment == "topright":
        rect.topright = (x, y)
    # Bottoms
    elif alignment == "bottomleft":
        rect.bottomleft = (x, y)
    elif alignment == "bottomright":
        rect.bottomright = (x, y)
    # Mids
    elif alignment == "midtop":
        rect.midtop = (x, y)
    elif alignment == "midleft":
        rect.midleft = (x, y)
    elif alignment == "midright":
        rect.midright = (x, y)
    elif alignment == "midbottom":
        rect.midbottom = (x, y)
    # Center
    elif alignment == "center":
        rect.center = (x, y)

    surface.blit(obj, rect)

# Save Game Data
def save(fpath, data_in):
    with open(fpath, "w") as file_in:
        file_in.write(data_in)

class Button():
    def __init__(self, x, y, scale, image, hover=any):
        if hover == any:
            hover = image

        width = image.get_width()
        heigth = image.get_height()

        self.image = pygame.transform.scale(image, (int(width * scale), int(heigth * scale)))
        self.hover = pygame.transform.scale(hover, (int(width * scale), int(heigth * scale)))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.clicked = False
        
    def draw(self, surface):

        # Get mouse position
        mousePos = pygame.mouse.get_pos()

        # Check clicked conditions
        if self.rect.collidepoint(mousePos):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True   
        
        if pygame.mouse.get_pressed()[0] == 0:
                self.clicked = False  

        # Draw button on surface (could have a hover image too)
        if self.rect.collidepoint(mousePos):
            surface.blit(self.hover, (self.rect.x, self.rect.y))              
        else:
            surface.blit(self.image, (self.rect.x, self.rect.y))

        
