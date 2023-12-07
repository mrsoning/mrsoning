import pygame
import button
import random

clock = pygame.time.Clock()


pygame.init()


x_1 = 200
y_1 = 300

x_2 = 600
y_2 = 300

bullet_1 = pygame.image.load('images/laser.png')
bullet_1 = pygame.transform.scale(bullet_1, (8, 8))
bullets_1 = []

bullet_2 = pygame.image.load('images/laser.png')
bullet_2 = pygame.transform.scale(bullet_2, (8, 8))
bullets_2 = []

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
      #draw pause screen buttonsw
      if resume_button.draw(screen):
        game_paused = True
      if quit_button.draw(screen):
        run = False
  else:
    # game
    fps = clock.tick(30)

    background = pygame.image.load("images/background.jpg")
    background = pygame.transform.scale(background, (800, 600))
    screen.blit(background, (0, 0))



    player_speed = 5
    # move my spaceship
    my_spaseship = pygame.image.load("images/Spaceship.png")
    my_spaseship = pygame.transform.scale(my_spaseship, (32, 32))
    screen.blit(my_spaseship, (x_1, y_1))

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w] and y_1 > 10:
      y_1 -= player_speed
    if keys[pygame.K_s] and y_1 < 560:
      y_1 += player_speed
    if keys[pygame.K_a] and x_1 > 10:
      x_1 -= player_speed
    if keys[pygame.K_d] and x_1 < 300:
      x_1 += player_speed


    if keys[pygame.K_LCTRL]:
      bullets_1.append(bullet_1.get_rect(topleft=(x_1 +30, y_1 + 10)))
    pygame.display.update()

    if bullets_1:
      for (i, el) in enumerate(bullets_1):
        screen.blit(bullet_1, (el.x, el.y))
        el.x += 6

        if el.x > 820:
          bullets_1.pop(i)


    enemy_spaceship = pygame.image.load("images/Spaceship_2.png")
    enemy_spaceship = pygame.transform.scale(enemy_spaceship, (32, 32))
    screen.blit(enemy_spaceship, (x_2, y_2))

    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP] and y_2 > 10:
      y_2 -= player_speed
    if keys[pygame.K_DOWN] and y_2 < 560:
      y_2 += player_speed
    if keys[pygame.K_LEFT] and x_2 > 450:
      x_2 -= player_speed
    if keys[pygame.K_RIGHT] and x_2 < 760:
      x_2 += player_speed

    if keys[pygame.K_RCTRL]:
      bullets_2.append(bullet_2.get_rect(topleft=(x_2 -30, y_2 +10)))
    if bullets_2:
      for (g, el) in enumerate(bullets_2):
        screen.blit(bullet_2, (el.x, el.y))
        el.x -= 6

        if el.x < -10:
           bullets_2.pop(g)

    pygame.display.update()

  #event handler
  for event in pygame.event.get():
    if event.type == pygame.KEYDOWN:
      if event.key == pygame.K_ESCAPE:
        game_paused = False
    if event.type == pygame.QUIT:
      run = False

  pygame.display.update()

pygame.quit()

