
# 1. Importing Modules
import pygame
import time
pygame.init()

# 2. Create Window
WIDTH, HEIGHT = 900, 700
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("L'Aventure de Cloé")

# 7. Create Player
PLAYER_WIDTH, PLAYER_HEIGHT = 50, 50
PLAYER_IMAGE = pygame.image.load("content/blondegirlasset1.png")
PLAYER_IMAGE = pygame.transform.scale(PLAYER_IMAGE, (PLAYER_WIDTH, PLAYER_HEIGHT))

# 5. Set Background
BG = pygame.image.load("content/redbackground.jpg")
BG = pygame.transform.scale(BG, (WIDTH, HEIGHT))

# 6. Draw Function
WIN.blit(BG, (0, 0))
WIN.blit(PLAYER_IMAGE, (WIDTH/2, HEIGHT/2))

pygame.display.update()

# 3. Main Game Loop
def main():
    run = True

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break
    pygame.quit

# 4. Guard Clause
if __name__ == "__main__":
    main()