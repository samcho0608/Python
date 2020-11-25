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

#캐릭터(스프라이트) 불러오기
character = pygame.image.load("D:\\Python\\PyGame_Basic\\character.png")
character_size = character.get_rect().size # 이미지의 크기를 구해옴
character_width = character_size[0]
character_height = character_size[1]
character_x_pos = screen_width / 2 - character_width / 2
character_y_pos = screen_height - character_height

# event loop
running = True # is the game still running
while running:
    # checks for any event happening while running
    for event in pygame.event.get():
        if event.type == pygame.QUIT: # if window closed
            running = False # then game no long runs

    screen.blit(background, (0,0))  # 배경 그리기

    screen.blit(character, (character_x_pos, character_y_pos)) # 캐릭터 그리기

    pygame.display.update() # 게임 화면을 다시 그리기!
                            # must be called every loop

# pygame 종료
pygame.quit()