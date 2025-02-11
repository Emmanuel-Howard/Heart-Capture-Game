
# 1. Importing Modules
import pygame
import time
import random   # For Heart position
pygame.init()

# 2. Create Window
WIDTH, HEIGHT = 600, 700
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("L'Aventure de Cloé")

# 7. Create Player
PLAYER_WIDTH, PLAYER_HEIGHT = 50, 50
PLAYER_IMAGE = pygame.image.load("content/blondegirlasset1.png")
PLAYER_IMAGE = pygame.transform.scale(PLAYER_IMAGE, (PLAYER_WIDTH, PLAYER_HEIGHT))
PLAYER_VEL = 8   # Speed at which the Player moves

# 11. Create Heart
HEART_WIDTH, HEART_HEIGHT = 50, 50
HEART_IMAGE = pygame.image.load("content/whiteheart.png")
HEART_IMAGE = pygame.transform.scale(HEART_IMAGE, (HEART_WIDTH, HEART_HEIGHT))
HEART_VEL = 5   # Speed at which the Heart moves

# 5. Set Background
BG = pygame.image.load("content/redbackground.jpg")
BG = pygame.transform.scale(BG, (WIDTH, HEIGHT))

# 6. Draw Function
def draw(player_x, hearts):
    WIN.blit(BG, (0, 0))
    WIN.blit(PLAYER_IMAGE, (player_x, HEIGHT - PLAYER_HEIGHT)) # Starts Player at the bottom

    for heart_x, heart_y in hearts:
        WIN.blit(HEART_IMAGE, (heart_x, heart_y))

    pygame.display.update()

# 3. Main Game Loop
def main():
    run = True

    player_x = WIDTH // 2 - PLAYER_WIDTH // 2   # Starts Player at bottom center

# 9. Establish Clock and Start Time
    clock = pygame.time.Clock()
    start_time = time.time()
    elapsed_time = 0

# 12. Establish heart list, count, and increment
    heart_add_increment = 1000   # Add a Heart every 1 second
    heart_count = 0
    hearts = []   # List of Hearts

    while run:

# 10. Lower Frame Rate
        heart_count += clock.tick(60)   # 60 frames per second
        elapsed_time = time.time() - start_time

# 13. Spawn Hearts 
        if heart_count >= heart_add_increment:
            for _ in range(1):   # Spawns 1 heart
                heart_x = random.randint(0, WIDTH - HEART_WIDTH)
                hearts.append((heart_x, 0))
                heart_count = 0

        # heart_add_increment = max(500, heart_add_increment -150)                  = Potential Add-On to speed up drop

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break

# 8. Player Movement
        keys = pygame.key.get_pressed()   # Left arrow key
        if keys[pygame.K_LEFT] and player_x -PLAYER_VEL >= 0:
            player_x -= PLAYER_VEL   # Move left by velocity
        if keys[pygame.K_RIGHT] and player_x + PLAYER_VEL + PLAYER_WIDTH <= WIDTH:   # Right arrow key
            player_x += PLAYER_VEL   # Move right by velocity

# 14. Heart Movement
        hearts = [(heart_x, heart_y + HEART_VEL) for heart_x, heart_y in hearts if heart_y < HEIGHT]

        draw(player_x, hearts)

    pygame.quit()


# 4. Guard Clause
if __name__ == "__main__":
    main()