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
to_x = 0
to_y = 0


# event loop
running = True # is the game still running
while running:
    # checks for any event happening while running
    for event in pygame.event.get():
        if event.type == pygame.QUIT: # if window closed
            running = False # then game no long runs

        # checks if there's any key down
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                to_x -= 5
            elif event.key == pygame.K_RIGHT:
                to_x += 5
            elif event.key == pygame.K_DOWN:
                to_y +=5
            elif event.key == pygame.K_UP:
                to_y -= 5

        # checks if there a key up
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x = 0
            elif event.key == pygame.K_DOWN or event.key == pygame.K_UP:
                to_y = 0

    # this is done after the event check is done
    character_x_pos += to_x
    character_y_pos += to_y

    # ascertains that the character stays within the bound
    if character_x_pos  < 0:
        character_x_pos = 0
    elif character_x_pos > screen_width - character_width:
        character_x_pos = screen_width - character_width

    if character_y_pos < 0:
        character_y_pos = 0
    elif character_y_pos > screen_height - character_height:
        character_y_pos = screen_height - character_height

    screen.blit(background, (0,0))  # 배경 그리기

    screen.blit(character, (character_x_pos, character_y_pos)) # 캐릭터 그리기

    pygame.display.update() # 게임 화면을 다시 그리기!
                            # must be called every loop

# pygame 종료
pygame.quit()