import pygame
import neat
from bird import Bird
from base import Base
from pipes import Pipe
import os
pygame.font.init()  # init font

# Window parameters
WIN_WIDTH = 600
WIN_HEIGHT = 800
FLOOR = 730

WIN = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
pygame.display.set_caption("Flappy Bird")

# loading imgs
pipe_img = pygame.transform.scale2x(pygame.image.load(os.path.join("img","pipe.png")).convert_alpha())
bg_img = pygame.transform.scale(pygame.image.load(os.path.join("img","bg.png")).convert_alpha(), (600, 900))
base_img = pygame.transform.scale2x(pygame.image.load(os.path.join("img", "base.png")).convert_alpha())

# set fonts
STAT_FONT = pygame.font.SysFont("comicsans", 50)
END_FONT = pygame.font.SysFont("comicsans", 70)

def draw_window(win, birds, base, pipes, score, level):
    # draw objects and labels on screen

    win.blit(bg_img, (0,0))

    base.draw(win)
    for bird in birds:
        bird.draw(win)
    for pipe in pipes:
        pipe.draw(win)

    # score
    score_label = STAT_FONT.render("Score: " + str(score), 1, (255, 255, 255))
    win.blit(score_label, (WIN_WIDTH - score_label.get_width() - 15, 10))

    # level
    level_label = STAT_FONT.render("Level: " + str(level), 1, (255, 255, 255))
    win.blit(level_label, (WIN_WIDTH - score_label.get_width() - 15, 50))

    pygame.display.update()

def main():
    # Main game loop

    global WIN

    win = WIN
    level = 1
    score = 0

    game_speed = 30
    initial_vel = 150/game_speed
    velocity = initial_vel

    birds = []

    birds.append(Bird(230, 350, game_speed))

    base = Base(730, base_img)

    pipes = []
    pipes.append(Pipe(700, level, pipe_img))

    clock = pygame.time.Clock()

    run = True
    while run and len(birds)>0:
        clock.tick(game_speed)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
                quit()
                break

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    for bird in birds:
                        bird.jump()


        pipe_ind = 0
        if len(birds)>0:
            if len(pipes) > 1 and birds[0].pos_x > pipes[0].x + pipes[0].PIPE_TOP.get_width():
                pipe_ind = 1


        for x, bird in enumerate(birds):
            bird.move()

        base.move(velocity)

        rem = []
        add_pipe = False
        for pipe in pipes:
            pipe.move(velocity)
            for bird in birds:
                if pipe.collide(bird):
                    birds.pop(birds.index(bird))

            if pipe.x + pipe.PIPE_TOP.get_width() < 0:
                rem.append(pipe)

            if not pipe.passed and pipe.x < bird.pos_x:
                pipe.passed = True
                add_pipe = True


        if add_pipe:
            score += 1
            pipes.append(Pipe(WIN_WIDTH,level,pipe_img))

        # defining level based on the game score
        if score <= 5:
            level = 1
        elif score <= 10:
            level = 2
        elif score <= 15:
            level = 3
        elif score <= 20:
            level = 4
        elif score <= 25:
            level = 5
        elif score <= 35:
            level = 6
        elif score <= 45:
            level = 7
        elif score <= 60:
            level = 8
        else:
            level = 9

        velocity = initial_vel + (level - 1) * (initial_vel / 10)
        for r in rem:
            pipes.remove(r)


        draw_window(win, birds, base, pipes, score, level)

        if score > 100:
            break



if __name__ == '__main__':
    main()

