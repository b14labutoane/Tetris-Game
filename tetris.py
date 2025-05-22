import pygame, sys
from game import Game
from colors import Colors

pygame.init()

screen = pygame.display.set_mode((300, 600))
pygame.display.set_caption("Python Tetris")

clock = pygame.time.Clock()

game = Game()

#GAME_UPDATE = pygame.USEREVENT
#pygame.time.set_timer(GAME_UPDATE, 200)

i=0

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if game.game_over:
                game.game_over = False
                game.reset()
            if event.key == pygame.K_LEFT and not game.game_over:
                game.move_left()
            if event.key == pygame.K_RIGHT and not game.game_over:
                game.move_right()
            if event.key == pygame.K_DOWN and not game.game_over:
                game.move_down()
                game.update_score(0, 1)
            if event.key == pygame.K_UP and not game.game_over:
                game.rotate()
                
        #if event.type == GAME_UPDATE and not game.game_over:
        # game.move_down()
        
        
    if i == 12:
             game.move_down()
             i = 0
    i+=1    
    screen.fill(Colors.dark_blue)

    game.draw(screen)

    pygame.display.update()
    clock.tick(60)
