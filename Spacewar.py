import pygame
import button
import random

clock = pygame.time.Clock()

pygame.init()

#create game window
SCREEN_WIDTH = 626
SCREEN_HEIGHT = 417

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
resume_button = button.Button(220, 100, resume_img, 1)
quit_button = button.Button(250, 250, quit_img, 1)

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
    screen.blit(background, (0, 0))


    my_spaseship = pygame.image.load("images/Spaceship_me.png")
    screen.blit(my_spaseship, (270, 170))


    enemy_spaceship = pygame.image.load("images/Spaceship_enemy.png")
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