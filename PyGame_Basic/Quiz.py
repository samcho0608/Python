# 똥 피하기 게임 만들기

# [게임 조건]
# 1. 캐릭터는 화면 가장 아래에 위치, 좌우로만 이동 가능
# 2. 똥은 화면 가장 위에서 떨어짐. x 좌표는 매번 랜덤으로 설정
# 3. 캐릭터가 똥을 피하면 다음 똥이 다시 떨어짐
# 4. 캐릭터가 똥과 충돌하면 게임 종료
# 5. FPS는 30으로 고정

# MAKE THE MOVEMENT SMOOTHER

import pygame
from random import randint

pygame.init()

# Class definition
class Character:
    def __init__(self, sprite, x = 0, y = 0):
        self.x = x
        self.y = y
        self.sprite = sprite
        self.speed = 0.3
        size = sprite.get_rect().size
        self.width = size[0]
        self.height = size[1]
    
    def move(self, direction, dt):
        if direction == "L":
            self.x -= self.speed * dt
        elif direction == "R":
            self.x += self.speed * dt
        elif direction == "D":
            self.y += self.speed * dt
        elif direction == "N":
            self.x += 0

    def set_coordinate(self, x = None, y = None):
        if x != None:
            self.x = x
        if y != None:
            self.y = y

# Screen setup
screen_width = 480
screen_height = 640
screen = pygame.display.set_mode((screen_width, screen_height))

background = pygame.image.load("PyGame_Basic\\background.png")

# Title
pygame.display.set_caption("똥 피하기")

# FPS
clock = pygame.time.Clock()

main_character = Character(pygame.image.load("PyGame_Basic\\character.png"))

main_character.set_coordinate((screen_width / 2 - main_character.width / 2), (screen_height - main_character.height))

poop = Character(pygame.image.load("PyGame_Basic\\enemy.png"))
poop.set_coordinate(randint(0, screen_width - poop.width), 0 - poop.height)

# direction declaration has to be done outside of the loop
# otherwise, when key held down, it will reassign the initial value 
# and thus stop the wanted continuous mvt
direction = "N"
running = True

L_UP = R_UP = True
while(running): 
    dt = clock.tick(30)     # FPS set to 30

    for event in pygame.event.get():
        # if closed, game should stop
        if event.type == pygame.QUIT:
            running = False

        # if key down for character's movement
        # this only checks the very instant event happens aka doesn't account for when key held down
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                direction = "L"
                L_UP = False
            elif event.key == pygame.K_RIGHT:
                direction = "R"
                R_UP = False

        # if key up to stop character's movement
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                direction = "N"
                L_UP = True
                # if R key still pressed
                if not R_UP:
                    direction = "R"
            elif event.key == pygame.K_RIGHT:
                direction = "N"
                R_UP = True
                # if L key still pressed
                if not L_UP:
                    direction = "L"

    # move the characters
    main_character.move(direction, dt)
    poop.move("D", dt)

    # movement control
    if main_character.x < 0:
        main_character.set_coordinate(0)
    elif main_character.x > screen_width - main_character.width:
        main_character.set_coordinate(screen_width - main_character.width)

    if main_character.y < 0:
        main_character.set_coordinate(y = 0)
    elif main_character.y > screen_height - main_character.height:
        main_character.set_coordinate(y = screen_height - main_character.height)

    if poop.y > screen_height:
        poop.set_coordinate(randint(0, screen_width - poop.width), 0 - poop.height)
    
    # Collision Control
    main_character_rect = main_character.sprite.get_rect()
    main_character_rect.left = main_character.x
    main_character_rect.top = main_character.y

    poop_rect = poop.sprite.get_rect()
    poop_rect.left = poop.x
    poop_rect.top = poop.y

    if main_character_rect.colliderect(poop_rect):
        print("떨어지는 똥 맞음")
        running = False

    # Draw the elements in
    screen.blit(background, (0,0))
    screen.blit(main_character.sprite, (main_character.x, main_character.y))
    screen.blit(poop.sprite, (poop.x, poop.y))

    pygame.display.update()

pygame.quit()