import pygame,sys
from game import Game
from block import Block
from colors import Colors


pygame.init()

title_font=pygame.font.Font(None,40)
score_surface=title_font.render("Score",True,Colors.white)

next_surface=title_font.render("Next Tile",True,Colors.white)

game_over_surface=title_font.render("GAME OVER",True,Colors.white)

score_rect=pygame.Rect(320,55,170,60)

next_rect=pygame.Rect(320,215,170,180)
screen=pygame.display.set_mode((500,620))
pygame.display.set_caption("Python Tetris")

clock=pygame.time.Clock()

game=Game()

GAME_UPDATE=pygame.USEREVENT
pygame.time.set_timer(GAME_UPDATE,200)

while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type==pygame.KEYDOWN:
            if game.game_over==True:
                game.game_over=False
                game.reset()
            if event.key==pygame.K_LEFT and game.game_over==False:
                game.move_left()
            if event.key==pygame.K_RIGHT and game.game_over==False:
                game.move_right()
            if event.key==pygame.K_DOWN and game.game_over==False:
                game.move_down()
                game.update_score(0,1)
            if event.key==pygame.K_UP and game.game_over==False:
                game.rotate()
        if event.type==GAME_UPDATE and game.game_over==False:
            game.move_down()

    
    score_number=title_font.render(str(game.score),True,Colors.black)

    screen.fill(Colors.light_blue)

    screen.blit(score_surface,(365,20))
    screen.blit(next_surface,(345,180))
    
    
    
    if game.game_over==True:
        screen.blit(game_over_surface,(320,450))
    pygame.draw.rect(screen,Colors.light_grey,score_rect)
    screen.blit(score_number,score_number.get_rect(centerx=score_rect.centerx,centery=score_rect.centery))
    pygame.draw.rect(screen,Colors.light_grey,next_rect)
    game.draw(screen)
    pygame.display.update()
    clock.tick(60)

