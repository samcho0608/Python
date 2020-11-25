import pygame
#############################################################################
#           Essentials and Steps
#############################################################################
pygame.init() # 반드시 필요

# 화면 크기 설정
screen_width = 480
screen_height = 640
screen = pygame.display.set_mode((screen_width, screen_height))

#화면 타이틀 설정
pygame.display.set_caption("게임 이름") # name of the game

#FPS
clock = pygame.time.Clock()
#############################################################################

# 1. Initialize Game contents(Background, Game image, coordinate, speed, font, etc.)

# event loop
running = True # is the game still running
while running:
    dt = clock.tick(60) # 게임 화면의 초당 프레임 수 설정

    # 2. 이벤트 처리
    for event in pygame.event.get():
        if event.type == pygame.QUIT: # if window closed
            running = False # then game no long runs

    # 3. 게임 캐릭터 위치 정의

    # 4. 충돌 처리

    # 5. 화면에 그리기

    pygame.display.update() # 게임 화면을 다시 그리기!
                            # must be called every loop

# pygame 종료
pygame.quit()