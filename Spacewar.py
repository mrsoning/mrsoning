import pygame
import button
import random

clock = pygame.time.Clock()

pygame.init()

player_x = 400
player_y = 280


#create game window
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600


screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Spasewar")
icon = pygame.image.load('images/icon.png')
pygame.display.set_icon(icon)


# background sound
bg_sound = pygame.mixer.Sound("sounds/Space_bg.mp3")
bg_sound.play(-1)

#game variables
game_paused = False
menu_state = "main"

#define fonts
font = pygame.font.SysFont("arialblack", 40)

#define colours
TEXT_COL = (255, 255, 255)

#load button images
resume_img = pygame.image.load("images/button_resume.png").convert_alpha()
quit_img = pygame.image.load("images/button_quit.png").convert_alpha()

#create button instances
resume_button = button.Button(230, 250, resume_img, 1)
quit_button = button.Button(430, 250, quit_img, 1)

def draw_text(text, font, text_col, x, y):
  img = font.render(text, True, text_col)
  screen.blit(img, (x, y))

#game loop
run = True
while run:

  screen.fill((52, 78, 91))

  #check if game is paused
  if game_paused == False:
    #check menu state
    if menu_state == "main":
      #draw pause screen buttons
      if resume_button.draw(screen):
        game_paused = True
      if quit_button.draw(screen):
        run = False
  else:
    # game
    background = pygame.image.load("images/background.jpg")
    background = pygame.transform.scale(background, (800, 600))
    screen.blit(background, (0, 0))



    player_speed = 3

    # move my spaceship
    my_spaseship = pygame.image.load("images/Spaceship_me.png")
    my_spaseship = pygame.transform.scale(my_spaseship, (32, 32))
    screen.blit(my_spaseship, (player_x, player_y))

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
      print("w")
      player_y -= player_speed
    if keys[pygame.K_s]:
      print("s")
      player_y += player_speed
    if keys[pygame.K_a]:
      print("a")
      player_x -= player_speed
    if keys[pygame.K_d]:
      print("d")
      player_x += player_speed
    print(player_y, player_x)

    pygame.display.update()

    enemy_spaceship = pygame.image.load("images/Spaceship_enemy.png")
    enemy_spaceship = pygame.transform.scale(enemy_spaceship, (32, 32))
    screen.blit(enemy_spaceship, (10, 10))



  #event handler
  for event in pygame.event.get():
    if event.type == pygame.KEYDOWN:
      if event.key == pygame.K_ESCAPE:
        game_paused = False
    if event.type == pygame.QUIT:
      run = False

  pygame.display.update()

pygame.quit()
clock.tick(15)
