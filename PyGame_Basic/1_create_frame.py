import pygame

pygame.init() # 반드시 필요

# 화면 크기 설정
screen_width = 480
screen_height = 640
screen = pygame.display.set_mode((screen_width, screen_height))

#화면 타이틀 설정
pygame.display.set_caption("Sam's game") # name of the game

# event loop
running = True # is the game still running
while running:
    # checks for any event happening while running
    for event in pygame.event.get():
        if event.type == pygame.QUIT: # if window closed
            running = False # then game no long runs

# pygame 종료
pygame.quit()