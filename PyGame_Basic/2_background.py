import pygame

pygame.init() # 반드시 필요

# 화면 크기 설정
screen_width = 480
screen_height = 640
screen = pygame.display.set_mode((screen_width, screen_height))

#화면 타이틀 설정
pygame.display.set_caption("Sam's game") # name of the game

#배경 이미지 불러오기
background = pygame.image.load("D:\\Python\\PyGame_Basic\\background.png")

# event loop
running = True # is the game still running
while running:
    # checks for any event happening while running
    for event in pygame.event.get():
        if event.type == pygame.QUIT: # if window closed
            running = False # then game no long runs

    # (0,0) is the top left corner
    # screen.fill((200,40,200)) # do this to simply fill with color
    screen.blit(background, (0,0))  # 배경 그리기
    # this coordinate is where the top left corner of the background image will be placed

    pygame.display.update() # 게임 화면을 다시 그리기!
                            # must be called every loop

# pygame 종료
pygame.quit()