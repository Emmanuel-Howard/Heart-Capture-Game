# NEED TO: move yellow heart faster, export to .exe

# Bundling into .exe
import os
import sys

def resource_path(relative_path):
    """Get absolute path for bundled files in an .exe."""
    if getattr(sys, 'frozen', False): 
        base_path = sys._MEIPASS
    else:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)


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
PLAYER_IMAGE = pygame.image.load(resource_path("content/blondegirlasset1.png"))
PLAYER_IMAGE = pygame.transform.scale(PLAYER_IMAGE, (PLAYER_WIDTH, PLAYER_HEIGHT))
PLAYER_VEL = 12   # Speed at which the Player moves

# 11. Create Heart
HEART_WIDTH, HEART_HEIGHT = 60, 90
HEART_IMAGE = pygame.image.load("content/redpixelheart.png")
HEART_IMAGE = pygame.transform.scale(HEART_IMAGE, (HEART_WIDTH, HEART_HEIGHT))
HEART_VEL = 5   # Speed at which the Heart moves

# 11 (B). Create Golden Star
GOLDEN_HEART_IMAGE = pygame.image.load("content/goldenstar.png")
GOLDEN_HEART_IMAGE = pygame.transform.scale(GOLDEN_HEART_IMAGE, (HEART_WIDTH, HEART_HEIGHT))

# 11 (C). Create broken Heart
BROKEN_HEART_IMAGE = pygame.image.load("content/brokenpixelheart.png")
BROKEN_HEART_IMAGE = pygame.transform.scale(BROKEN_HEART_IMAGE, (HEART_WIDTH, HEART_HEIGHT))

# 11 (D). Create Black Heart
BLACK_HEART_IMAGE = pygame.image.load("content/blackheart.png")
BLACK_HEART_IMAGE = pygame.transform.scale(BLACK_HEART_IMAGE, (HEART_WIDTH, HEART_HEIGHT))

# 11 (E). Create Special Heart
SPECIAL_HEART_IMAGE = pygame.image.load("content/specialheart.png")
SPECIAL_HEART_IMAGE = pygame.transform.scale(SPECIAL_HEART_IMAGE, (50, 65))

# 5. Set Backgrounds
BG_1 = pygame.image.load("content/snowbackground.png")
BG_1 = pygame.transform.scale(BG_1, (WIDTH, HEIGHT))

BG_2 = pygame.image.load("content/Snow game cover (3).png")
BG_2 = pygame.transform.scale(BG_2, (WIDTH, HEIGHT))

BG_3 = pygame.image.load("content/Snow game cover (4).png")
BG_3 = pygame.transform.scale(BG_3, (WIDTH, HEIGHT))

BG_4 = pygame.image.load("content/Snow game cover (5).png")
BG_4 = pygame.transform.scale(BG_4, (WIDTH, HEIGHT))

# 16. Set Font
FONT = pygame.font.SysFont("lobster", 50)

# 19. Set Sound
# I'd usually put the main music here but need it in the main() since I'm not creating a game loop
hit_sound = pygame.mixer.Sound("sound/hit sound.MP3")
hit_sound.set_volume(1.0) 

receive_sound = pygame.mixer.Sound("sound/retro-coin-3-236679.mp3")
receive_sound.set_volume(0.1)

# 21. Create Menu
def menu():
    menu_bg = pygame.image.load("content/Snow game cover (2).png")
    menu_bg = pygame.transform.scale(menu_bg, (WIDTH, HEIGHT))

    run = True
    while run:
        WIN.fill((0, 0, 0))
        WIN.blit(menu_bg, (0, 0))

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    run = False
                if event.key == pygame.K_q:
                    pygame.quit()
                    exit()

# 23: End Game Screen
def end_game_screen():
    end_game_screen = pygame.image.load("content/gameover.png")
    end_game_screen = pygame.transform.scale(end_game_screen, (WIDTH, HEIGHT))

    run = True
    while run:
        WIN.fill((0, 0, 0))
        WIN.blit(end_game_screen, (0, 0))

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    run = False
                    main()
                if event.key == pygame.K_q:
                    pygame.quit()
                    exit()

# 24: Win Game Screen
def win_game_screen():
    win_game_screen = pygame.image.load("content/wincover.png")
    win_game_screen = pygame.transform.scale(win_game_screen, (WIDTH, HEIGHT))

    run = True
    while run:
        WIN.fill((0, 0, 0))
        WIN.blit(win_game_screen, (0, 0))

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    run = False
                    main()
                if event.key == pygame.K_q:
                    pygame.quit()
                    exit()
                                                                                 # NOTE: I used AI for the FADE-IN EFECT
# 22. New Backgrounds
def fade_in_background(old_bg, new_bg, alpha, speed=5):
    # Create a surface for blending the old and new backgrounds
    blended_bg = pygame.Surface((WIDTH, HEIGHT))
    blended_bg.blit(old_bg, (0, 0))
    blended_bg.set_alpha(alpha)  # Set the alpha (transparency)
    
    WIN.blit(blended_bg, (0, 0))  # Draw the old background with transparency
    WIN.blit(new_bg, (0, 0))  # Draw the new background over it
    
    # Gradually increase the alpha value to create the fade effect
    alpha = min(255, alpha + speed)
    return new_bg, alpha

# 6. Draw Function
def draw(player_x, hearts, score, current_bg, last_bg_switch_time, bg_switch_interval, alpha):

    global BG_1, BG_2, BG_3, BG_4

    # Get the current time
    current_time = pygame.time.get_ticks()  # in milliseconds

    # Check if enough time has passed to switch the background
    if current_time - last_bg_switch_time >= bg_switch_interval:
        # Update the last background switch time
        last_bg_switch_time = current_time

        # Switch background based on time
        if current_time // bg_switch_interval % 4 == 0:
            new_bg = BG_1
        elif current_time // bg_switch_interval % 4 == 1:
            new_bg = BG_2
        elif current_time // bg_switch_interval % 4 == 2:
            new_bg = BG_3
        else:
            new_bg = BG_4

        current_bg, alpha = fade_in_background(current_bg, new_bg, alpha)

    else:
        WIN.fill((0, 0, 0))  # Clear screen
        WIN.blit(current_bg, (0, 0))  # Draw the selected background

    WIN.blit(PLAYER_IMAGE, (player_x, HEIGHT - PLAYER_HEIGHT)) # Starts Player at the bottom

    for heart_x, heart_y, heart_type in hearts:
        if heart_type == "normal":
            WIN.blit(HEART_IMAGE, (heart_x, heart_y))
        elif heart_type == "golden":
            WIN.blit(GOLDEN_HEART_IMAGE, (heart_x, heart_y))
        elif heart_type == "broken":
            WIN.blit(BROKEN_HEART_IMAGE, (heart_x, heart_y))
        elif heart_type == "black":
            WIN.blit(BLACK_HEART_IMAGE, (heart_x, heart_y))
        elif heart_type == "special":
            WIN.blit(SPECIAL_HEART_IMAGE, (heart_x, heart_y))

    score_text = FONT.render(f"Amour de Manu: {score}", 1, "red")   
    WIN.blit(score_text, (10,10))

    pygame.display.update()

    return last_bg_switch_time, current_bg, alpha

# 3. Main Game Loop
def main():
    run = True

    player_x = WIDTH // 2 - PLAYER_WIDTH // 2   # Starts Player at bottom center

# 9. Establish Clock and Start Time
    clock = pygame.time.Clock()
    start_time = time.time()
    elapsed_time = 0

# 12. Establish heart list, count, and increment
    heart_add_increment = 450   # Add a Heart every 0.5 seconds
    heart_count = 0
    hearts = []   # List of Hearts

    last_bg_switch_time = 0  # Time of last background switch
    bg_switch_interval = 15000  # Background switches every 10 seconds
    alpha = 0

# 17. Establish Score, current background, and special heart appearance
    score = 5
    current_bg = BG_1
    special_heart_appeared = False

# Sound for loop
    pygame.mixer.music.load("sound/ifollowrivers.mp3")
    pygame.mixer.music.set_volume(0.4)
    pygame.mixer.music.play(-1)  # -1 plays the music on loop

    while run:

# 10. Lower Frame Rate
        heart_count += clock.tick(60)   # 60 frames per second
        elapsed_time = time.time() - start_time

# 13. Spawn Hearts 
        if heart_count >= heart_add_increment:
            for _ in range(1):   # Spawns 1 heart
                heart_x = random.randint(0, WIDTH - HEART_WIDTH)

                heart_type = random.choice(["normal", "golden", "broken", "black",])   # Randomly selects a heart type

                hearts.append((heart_x, 0, heart_type))
                heart_count = 0

# 13 (B). Check for Special Heart
        if score % 20 == 0 and score != 0 and not special_heart_appeared:  # Special heart appears when score reaches 20
            special_heart_appeared = True
            heart_x = random.randint(0, WIDTH - HEART_WIDTH)
            heart_y = 0
            hearts.append((heart_x, heart_y, "special"))

# Reset special heart appearance for the next cycle of 20 points
        if score % 20 == 0 and score != 0 and not special_heart_appeared:
            special_heart_appeared = True
            heart_x = random.randint(0, WIDTH - HEART_WIDTH)
            heart_y = 0
            hearts.append((heart_x, heart_y, "special"))
            special_heart_appeared = False

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

            if heart_type == "special":
                new_y = heart_y + HEART_VEL + 2
            else:
                new_y = heart_y + HEART_VEL

            hearts[i] = (heart_x, new_y, heart_type)  # Update "Y" position of heart
        
# 15. Heart Collision
        new_hearts = []   # New Heart list
        for heart in hearts:
            heart_x, heart_y, heart_type = heart   # Heart Details: x, y, type
            if player_x < heart_x < player_x + PLAYER_WIDTH and HEIGHT - PLAYER_HEIGHT < heart_y < HEIGHT:  
                if heart_type == "normal":
                    receive_sound.play()
                    score += 1
                elif heart_type == "golden":
                    receive_sound.play()
                    score += 2  
                elif heart_type == "broken":
                    hit_sound.play()  
                    score -= 3
                elif heart_type == "black":
                    score -= 100000
                elif heart_type == "special":
                    score += 100000


                continue
            new_hearts.append(heart)  # Keep heart if not collected

        hearts = new_hearts  # Update the heart list

# 18. Decrease Score by Heart Missed
        missed_hearts = [heart for heart in hearts if heart[1] >= HEIGHT]   # Check hearts that are missed (out of bounds)
        for heart in missed_hearts:
            heart_x, heart_y, heart_type = heart
            if heart_type == "normal" or heart_type == "golden":  # Only penalize for non-broken/black hearts
                score -= 2

        hearts = [heart for heart in hearts if heart[1] < HEIGHT]   # Remove hearts that went out of bounds
        score = max(0, score) 

# 20. If score reaches 0 (Game Over)
        if score == 0:
            pygame.mixer.music.stop()
            pygame.mixer.music.load("sound/game-over-arcade-6435.mp3")
            pygame.mixer.music.play(1)

            end_game_screen()

            while pygame.mixer.music.get_busy():
                pygame.time.Clock().tick(10)

            pygame.mixer.music.load("sound/stvalentin game end.mp3")
            pygame.mixer.music.play(1)

            end_game_screen()

        if score >= 100000:
            pygame.mixer.music.stop()
            pygame.mixer.music.load("sound/windoot-96335.mp3")
            pygame.mixer.music.play(1)

            win_game_screen()

            while pygame.mixer.music.get_busy():
                pygame.time.Clock().tick(10)

            pygame.mixer.music.load("sound/wingamemessage.mp3")
            pygame.mixer.music.play(1)




        last_bg_switch_time, current_bg, alpha = draw(player_x, hearts, score, current_bg, last_bg_switch_time, bg_switch_interval, alpha)

    pygame.quit()


# 4. Guard Clause
if __name__ == "__main__":
    menu()
    main()