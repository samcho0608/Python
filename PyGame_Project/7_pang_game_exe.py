import os, random, pygame
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
    def __init__(self, sprite, x = 0, y = 0, speed = 0):
        self.x = x
        self.y = y
        self.sprite = sprite
        self.speed_x = self.speed_y = speed
        size = sprite.get_rect().size
        self.width = size[0]
        self.height = size[1]
    
    def move(self, direction, dt):
        if direction == "L":
            self.x -= self.speed_x * dt
        elif direction == "R":
            self.x += self.speed_x * dt
        elif direction == "U":
            self.y -= self.speed_y * dt
        elif direction == "D":
            self.y += self.speed_y * dt
        elif direction == "N":
            self.x += 0

    def set_coordinate(self, x = None, y = None):
        if x != None:
            self.x = x
        if y != None:
            self.y = y

class Ball(Character):
    def __init__(self, x = 0, y = 0, size_index = 0, dir = "R"):
        Character.__init__(self, balloon_sprites[size_index], x, y, 0.2)
        self.speed_y = -0.3
        self.size_index = size_index
        self.dir = dir

    def move(self, dt):
        if self.dir == "R":
            self.x += self.speed_x * dt
        else:
            self.x += -1 * self.speed_x * dt
        self.y += self.speed_y * dt

# 1. Initialize Game contents(Background, Game image, coordinate, speed, font, etc.)
current_path = os.path.dirname(__file__)    # returns the current address of the file
image_path = os.path.join(current_path, "images")   # returns the address of images folder

# Game Elements
background = pygame.image.load(os.path.join(image_path, "background.png"))
stage = pygame.image.load(os.path.join(image_path, "stage.png"))
stage_width = stage.get_size()[0]
stage_height = stage.get_size()[1]

# main character
main_character = Character(pygame.image.load(os.path.join(image_path, "character.png")), speed = 0.3)
main_character.set_coordinate(screen_width / 2 - main_character.width / 2, screen_height - stage_height - main_character.height)

# list of weapons
weapons = []
weapon_sprite = pygame.image.load(os.path.join(image_path, "weapon.png"))

# balloon images
balloon_sprites = [
    pygame.image.load(os.path.join(image_path, "balloon1.png")),
    pygame.image.load(os.path.join(image_path, "balloon2.png")),
    pygame.image.load(os.path.join(image_path, "balloon3.png")),
    pygame.image.load(os.path.join(image_path, "balloon4.png"))
]


balloons = [Ball(0, 0, size_index=0)]


# Game title
pygame.display.set_caption("Sam's Pang Game")

# Game Font
game_font = pygame.font.Font(None, 40)



# Extra variables for control

total_time = 100
start_tick = pygame.time.get_ticks()
pause = False # not paused
running = True # is the game still running
direction = "N" # neutral direction
R_UP = L_UP = True # left and right arrow keys are both up
regeneration_check = 0
ball_to_remove = -1
weapon_to_remove = -1
ball_count = 6
game_over = "Mission Accomplished"

# event loop
while running:
    dt = clock.tick(60) # 게임 화면의 초당 프레임 수 설정
                        # returns how many ms have passed since the last call

    # 2. 이벤트 처리
    for event in pygame.event.get():
        if event.type == pygame.QUIT: # if window closed
            game_over = "QUIT"
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
                weapons.append(Character(weapon_sprite, speed = 0.9))
                weapons[len(weapons) - 1].set_coordinate(main_character.x + main_character.width/2\
                    - weapons[len(weapons) - 1].width / 2, main_character.y)
            elif event.key == pygame.K_ESCAPE:
                pause = not pause

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

    if pause:
        continue

    main_character.move(direction, dt)
    for weapon in weapons:
        weapon.move("U", dt)
    
    for ball in balloons:
        ball.move(dt)

    elapsed_time = (pygame.time.get_ticks() - start_tick) / 1000
    timer = game_font.render("Time : {}".format(int(total_time - elapsed_time)), True, (255,255,255))
    if elapsed_time - regeneration_check >= 10 and ball_count > 0:
        regeneration_check = elapsed_time
        balloons.append(Ball(random.randint(0, 255), 0, dir = "L" if random.randint(0,1) == 0 else "R"))
        ball_count -= 1

    # 3. 게임 캐릭터 위치 정의

    # main_character
    if main_character.x < 0:
        main_character.x = 0
    elif main_character.x > screen_width - main_character.width:
        main_character.x = screen_width - main_character.width

    # weapon
    for weaponInd, weapon in enumerate(weapons):
        if weapon.y < 0 - weapon.height:
            weapon_to_remove = weaponInd

    if weapon_to_remove != -1:
        del weapons[weapon_to_remove]
        weapon_to_remove = -1

    # ball
    for ball in balloons:
        # x-axis
        if ball.x <= 0 or ball.x >= screen_width - ball.width:
            ball.speed_x *= -1  # if hit wall, reverse the movement direction
            if ball.x <= 0:
                ball.x = 0
            else:
                ball.x = screen_width - ball.width
        # y-axis
        if ball.y >= screen_height - stage_height - ball.height:
            ball.y = screen_height - stage_height - ball.height
            ball.speed_y *= -1
            ball.speed_y += 0.02 # represesnts energy loss aka lower bounces
        else:
            ball.speed_y += 0.02

    # 4. 충돌 처리

    main_character_rect = main_character.sprite.get_rect()
    main_character_rect.left = main_character.x
    main_character_rect.top = main_character.y

    # ball collision
    for ballInd, ball in enumerate(balloons):
        ball_rect = ball.sprite.get_rect()
        ball_rect.left = ball.x
        ball_rect.top = ball.y

        if main_character_rect.colliderect(ball_rect):
            game_over = "Game Over"
            running = False
            break

        for weaponInd, weapon in enumerate(weapons):
            weapon_rect = weapon.sprite.get_rect()
            weapon_rect.left = weapon.x
            weapon_rect.top = weapon.y

            if weapon_rect.colliderect(ball_rect):
                ball_to_remove = ballInd
                weapon_to_remove = weaponInd
                break

    if ball_to_remove > -1:
        ball = balloons[ball_to_remove]
        if ball.size_index < 3:
            new_x = ball.x + ball.width / 2 - balloon_sprites[ball.size_index + 1].get_width() / 2
            new_y = ball.y + ball.height / 2 -  balloon_sprites[ball.size_index + 1].get_height() / 2
            balloons.append(Ball(new_x, new_y, ball.size_index + 1, "L"))
            balloons.append(Ball(new_x, new_y, ball.size_index + 1, "R"))
        del balloons[ball_to_remove]
        ball_to_remove = -1
    if weapon_to_remove > -1:
        del weapons[weapon_to_remove]
        weapon_to_remove = -1


    # 5. 화면에 그리기
    screen.blit(background, (0,0))
    for weapon in weapons:
        screen.blit(weapon.sprite, (weapon.x, weapon.y))
    for ball in balloons:
        screen.blit(ball.sprite, (ball.x, ball.y))
    screen.blit(stage, (0, screen_height - stage_height))
    screen.blit(main_character.sprite, (main_character.x, main_character.y))
    screen.blit(timer, (10, 10))

    if total_time - elapsed_time == 0:
        game_over = "Time Over"
        running = False

    if ball_count == 0 and len(balloons) == 0:
        running = False

    pygame.display.update() # 게임 화면을 다시 그리기!
                            # must be called every loop

msg = game_font.render(game_over, True, (255,255,0))
msg_rect = msg.get_rect(center = (int(screen_width / 2), int(screen_height / 2)))
screen.blit(msg, msg_rect)
pygame.display.update()


pygame.time.delay(2000)

# pygame 종료
pygame.quit()