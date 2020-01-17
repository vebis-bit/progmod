from pygame import *

pygame.init()
overflate = pygame.display.set_mode((500,250))
pygame.display.set_caption("simulering")

BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
WHITE = (255, 255, 255)
black = (0, 0, 0)

overflate.fill(GREEN)
pygame.draw.rect(overflate, BLUE, (100, 100,150, 30),0)
pygame.display.update()

while True:
    for e in pygame.event.get():
        if e.type ==pygame.QUIT:
            pygame.quit()
    pygame.display.update()
