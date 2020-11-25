import pygame

pygame.init() # 반드시 필요

# 화면 크기 설정
screen_width = 480
screen_height = 640
screen = pygame.display.set_mode((screen_width, screen_height))

#화면 타이틀 설정
pygame.display.set_caption("Sam's game") # name of the game

#FPS
clock = pygame.time.Clock()


#배경 이미지 불러오기
background = pygame.image.load("PyGame_Basic\\background.png")

#캐릭터(스프라이트) 불러오기
character = pygame.image.load("PyGame_Basic\\character.png")
character_size = character.get_rect().size # 이미지의 크기를 구해옴
character_width = character_size[0]
character_height = character_size[1]
character_x_pos = screen_width / 2 - character_width / 2
character_y_pos = screen_height - character_height
to_x = 0
to_y = 0
character_speed = 0.6 # character gotta move 10 pixels/s

#적(스프라이트) 불러오기
enemy = pygame.image.load("PyGame_Basic\\enemy.png")
enemy_size = enemy.get_rect().size # 이미지의 크기를 구해옴
enemy_width = enemy_size[0]
enemy_height = enemy_size[1]
enemy_x_pos = screen_width / 2 - enemy_width / 2
enemy_y_pos = screen_height / 2 - enemy_height / 2
to_x = 0
to_y = 0
enemy_speed = 0.3 # character gotta move 10 pixels/s

# 폰트 정의
game_font = pygame.font.Font(None, 40)

# 총 시간
total_time = 10

# 시작 시간
start_ticks = pygame.time.get_ticks() # 시작 tick을 받아옴

# event loop
running = True # is the game still running
while running:
    dt = clock.tick(60) # 게임 화면의 초당 프레임 수 설정

    # print("fps : " + str(clock.get_fps()) + " dt: {0}".format(dt)) # to check the fpsh and stuff

    # 캐릭터가 1초 동안에 100만큼 이동을 해야함
    # 10 fps: 1초 동안에 10번 update -> 1번에 10만큼 -> 10 * 10 = 100
    # 20 fps: 1초 동안에 20번 update -> 1번에 5만큼 -> 5 * 20 = 100

    # checks for any event happening while running
    for event in pygame.event.get():
        if event.type == pygame.QUIT: # if window closed
            running = False # then game no long runs

        # checks if there's any key down
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                to_x -= character_speed
            elif event.key == pygame.K_RIGHT:
                to_x += character_speed
            elif event.key == pygame.K_DOWN:
                to_y += character_speed
            elif event.key == pygame.K_UP:
                to_y -= character_speed

        # checks if there a key up
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x = 0
            elif event.key == pygame.K_DOWN or event.key == pygame.K_UP:
                to_y = 0

    # multipy dt to to_x or to_y to account for the change in fps
    character_x_pos += to_x * dt
    character_y_pos += to_y * dt

    # ascertains that the character stays within the bound
    if character_x_pos  < 0:
        character_x_pos = 0
    elif character_x_pos > screen_width - character_width:
        character_x_pos = screen_width - character_width

    if character_y_pos < 0:
        character_y_pos = 0
    elif character_y_pos > screen_height - character_height:
        character_y_pos = screen_height - character_height

    # 충돌 처리
    character_rect = character.get_rect()
    character_rect.left = character_x_pos
    character_rect.top = character_y_pos

    enemy_rect = enemy.get_rect()
    enemy_rect.left = enemy_x_pos
    enemy_rect.top = enemy_y_pos

    if character_rect.colliderect(enemy_rect):
        print("충돌했어요")
        running = False

    screen.blit(background, (0,0))  # 배경 그리기
    screen.blit(character, (character_x_pos, character_y_pos)) # 캐릭터 그리기
    screen.blit(enemy, (enemy_x_pos, enemy_y_pos))  # 적 그리기

    # 타이머 집어넣기
    # 경과 시간 계산
    elapsed_time = ((pygame.time.get_ticks()) - start_ticks) / 1000 # divided by 1000 bc originally in miliseconds

    #출력할 글자
    timer = game_font.render(str(int(total_time - elapsed_time)), True, (255,255,255))
    
    screen.blit(timer, (10,10))

    if total_time - elapsed_time <= 0:
        print("타임 아웃")
        running = False

    pygame.display.update() # 게임 화면을 다시 그리기!
                            # must be called every loop

pygame.time.delay(2000)

# pygame 종료
pygame.quit()