import os
import pygame
#############################################################################
#           Essentials and Steps
#############################################################################
pygame.init() # 반드시 필요

# 화면 크기 설정
screen_width = 640
screen_height = 480
screen = pygame.display.set_mode((screen_width, screen_height))

#화면 타이틀 설정
pygame.display.set_caption("게임 이름") # name of the game

#FPS
clock = pygame.time.Clock()
#############################################################################

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
        elif direction == "U":
            self.y -= self.speed * dt
        elif direction == "D":
            self.y += self.speed * dt
        elif direction == "N":
            self.x += 0

    def set_coordinate(self, x = None, y = None):
        if x != None:
            self.x = x
        if y != None:
            self.y = y

# 1. Initialize Game contents(Background, Game image, coordinate, speed, font, etc.)
current_path = os.path.dirname(__file__)    # returns the current address of the file
image_path = os.path.join(current_path, "images")   # returns the address of images folder

# Game Elements
background = pygame.image.load(os.path.join(image_path, "background.png"))
stage = pygame.image.load(os.path.join(image_path, "stage.png"))

# main character
main_character = Character(pygame.image.load(os.path.join(image_path, "character.png")))
main_character.set_coordinate(screen_width / 2 - main_character.width / 2, screen_height - stage.get_size()[1] - main_character.height)

# list of weapons
weapons = []
weapon_sprite = pygame.image.load(os.path.join(image_path, "weapon.png"))



# Game title
pygame.display.set_caption("Sam's Pang Game")




# event loop
running = True # is the game still running
direction = "N" # neutral direction
R_UP = L_UP = True # left and right arrow keys are both up
while running:
    dt = clock.tick(60) # 게임 화면의 초당 프레임 수 설정

    # 2. 이벤트 처리
    for event in pygame.event.get():
        if event.type == pygame.QUIT: # if window closed
            running = False # then game no long runs
        
        # when key is pressed down
        if event.type == pygame.KEYDOWN:
            # move left
            if event.key == pygame.K_LEFT:
                direction = "L"
                L_UP = False
            # move right
            elif event.key == pygame.K_RIGHT:
                direction = "R"
                R_UP = False
            # shoot weapon
            elif event.key == pygame.K_SPACE:
                weapons.append(Character(weapon_sprite))
                weapons[len(weapons) - 1].set_coordinate(main_character.x + main_character.width/2\
                    - weapons[len(weapons) - 1].width / 2, main_character.y)
                weapons[len(weapons) - 1].speed = 0.6



        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT or event.key == pygame.K_LEFT:
                direction = "N"
                if event.key == pygame.K_RIGHT:
                    R_UP = True
                    if not L_UP:
                        direction = "L"
                else:
                    L_UP = True
                    if not R_UP:
                        direction = "R"

    main_character.move(direction, dt)
    for weapon in weapons:
        weapon.move("U", dt)

    # 3. 게임 캐릭터 위치 정의

    # 4. 충돌 처리

    # 5. 화면에 그리기

    screen.blit(background, (0,0))
    for weapon in weapons:
        screen.blit(weapon.sprite, (weapon.x, weapon.y))
    screen.blit(stage, (0, screen_height - stage.get_size()[1]))
    screen.blit(main_character.sprite, (main_character.x, main_character.y))

    pygame.display.update() # 게임 화면을 다시 그리기!
                            # must be called every loop

# pygame 종료
pygame.quit()