
# 1. Importing Modules
import pygame
import time
import random  
pygame.init()
pygame.font.init()
pygame.mixer.init()

# 2. Create Window
WIDTH, HEIGHT = 600, 700
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("L'Aventure de Cloé")

# 7. Create Player
PLAYER_WIDTH, PLAYER_HEIGHT = 70, 70
PLAYER_IMAGE = pygame.image.load("content/blondegirlasset1.png")
PLAYER_IMAGE = pygame.transform.scale(PLAYER_IMAGE, (PLAYER_WIDTH, PLAYER_HEIGHT))
PLAYER_VEL = 10   # Speed at which the Player moves

# 11. Create Heart
HEART_WIDTH, HEART_HEIGHT = 50, 80
HEART_IMAGE = pygame.image.load("content/redpixelheart.png")
HEART_IMAGE = pygame.transform.scale(HEART_IMAGE, (HEART_WIDTH, HEART_HEIGHT))
HEART_VEL = 5   # Speed at which the Heart moves

# 11 (B). Create Golden Heart
GOLDEN_HEART_IMAGE = pygame.image.load("content/goldenstar.png")
GOLDEN_HEART_IMAGE = pygame.transform.scale(GOLDEN_HEART_IMAGE, (HEART_WIDTH, HEART_HEIGHT))

# 11 (C). Create Golden Heart
BROKEN_HEART_IMAGE = pygame.image.load("content/brokenpixelheart.png")
BROKEN_HEART_IMAGE = pygame.transform.scale(BROKEN_HEART_IMAGE, (HEART_WIDTH, HEART_HEIGHT))


# 5. Set Background
BG = pygame.image.load("content/snowbackground.png")
BG = pygame.transform.scale(BG, (WIDTH, HEIGHT))

# 16. Set Font
FONT = pygame.font.SysFont("lobster", 50)

# 19. Set Sound
pygame.mixer.music.load("sound/ifollowrivers.mp3")
pygame.mixer.music.play(-1)  # -1 plays the music on loop

# 6. Draw Function
def draw(player_x, hearts, score):
    WIN.blit(BG, (0, 0))
    WIN.blit(PLAYER_IMAGE, (player_x, HEIGHT - PLAYER_HEIGHT)) # Starts Player at the bottom

    for heart_x, heart_y, heart_type in hearts:
        if heart_type == "normal":
            WIN.blit(HEART_IMAGE, (heart_x, heart_y))
        elif heart_type == "golden":
            WIN.blit(GOLDEN_HEART_IMAGE, (heart_x, heart_y))
        elif heart_type == "broken":
            WIN.blit(BROKEN_HEART_IMAGE, (heart_x, heart_y))

    score_text = FONT.render(f"Amour de Manu: {score}", 1, (255, 255, 255))   
    WIN.blit(score_text, (10,10))

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
    heart_add_increment = 500   # Add a Heart every 1 second
    heart_count = 0
    hearts = []   # List of Hearts

# 17. Establish Score
    score = 5

    while run:

# 10. Lower Frame Rate
        heart_count += clock.tick(60)   # 60 frames per second
        elapsed_time = time.time() - start_time

# 13. Spawn Hearts 
        if heart_count >= heart_add_increment:
            for _ in range(1):   # Spawns 1 heart
                heart_x = random.randint(0, WIDTH - HEART_WIDTH)

                heart_type = random.choice(["normal", "golden", "broken"])   # Randomly selects a heart type

                hearts.append((heart_x, 0, heart_type))
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
        for i, heart in enumerate(hearts): 
            heart_x, heart_y, heart_type = heart
            hearts[i] = (heart_x, heart_y + HEART_VEL, heart_type)  # Update "Y" position of heart
        
# 15. Heart Collision
        new_hearts = []   # New Heart list
        for heart in hearts:
            heart_x, heart_y, heart_type = heart   # Heart Details: x, y, type
            if player_x < heart_x < player_x + PLAYER_WIDTH and HEIGHT - PLAYER_HEIGHT < heart_y < HEIGHT:  
                if heart_type == "normal":
                    score += 1
                elif heart_type == "golden":
                    score += 2  
                elif heart_type == "broken":
                    score -= 3  
            else:
                new_hearts.append(heart)  # Keep heart if not collected

        hearts = new_hearts  # Update the heart list

# 18. Decrease Score by Heart Missed
        missed_hearts = [heart for heart in hearts if heart[1] >= HEIGHT]   # Check hearts that are missed (out of bounds)
        for heart in missed_hearts:
            heart_x, heart_y, heart_type = heart
            if heart_type == "normal" or heart_type == "golden":  # Only penalize for non-broken hearts
                score -= 3

        hearts = [heart for heart in hearts if heart[1] < HEIGHT]   # Remove hearts that went out of bounds
        score = max(0, score) 

# 20. If score reaches 0 (Game Over)
        if score == 0:
            pygame.mixer.music.stop()

            lost_text = FONT.render("GAME OVER!", 1, "black")
            WIN.blit(lost_text, (WIDTH/2 - lost_text.get_width()/2, HEIGHT/2 - lost_text.get_height()/2))
            pygame.display.update()
            pygame.time.delay(6000)
            break


        draw(player_x, hearts, score)

    pygame.quit()


# 4. Guard Clause
if __name__ == "__main__":
    main()