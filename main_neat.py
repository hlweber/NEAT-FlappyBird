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

gen = 0

def draw_window(win, birds, base, pipes, score, level, gen):
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

    # generations
    gen_label = STAT_FONT.render("Gens: " + str(gen - 1), 1, (255, 255, 255))
    win.blit(gen_label, (10, 10))

    # alive
    alive_label = STAT_FONT.render("Alive: " + str(len(birds)), 1, (255, 255, 255))
    win.blit(alive_label, (10, 50))

    pygame.display.update()

def main(genomes, config):
    # Main game loop

    global WIN, gen

    win = WIN
    level = 1
    score = 0

    gen +=1

    game_speed = 30
    initial_vel = 150/game_speed
    velocity = initial_vel

    nets = []
    birds = []
    ge = []

    # create birds for each genome
    for genome_id, genome in genomes:
        genome.fitness = 0
        net = neat.nn.FeedForwardNetwork.create(genome, config)
        nets.append(net)
        birds.append(Bird(230, 350, game_speed))
        ge.append(genome)

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

        pipe_ind = 0
        if len(birds)>0:
            if len(pipes) > 1 and birds[0].pos_x > pipes[0].x + pipes[0].PIPE_TOP.get_width():
                pipe_ind = 1


        for x, bird in enumerate(birds):
            ge[x].fitness += 0.1
            bird.move()
            output = nets[birds.index(bird)].activate((bird.pos_y, abs(bird.pos_y - pipes[pipe_ind].height), abs(bird.pos_y - pipes[pipe_ind].bottom)))

            if output[0] > 0.5:  # we use a tanh activation function so result will be between -1 and 1. if over 0.5 jump
                bird.jump()

        base.move(velocity)

        rem = []
        add_pipe = False
        for pipe in pipes:
            pipe.move(velocity)
            for bird in birds:
                if pipe.collide(bird):
                    # if bird collides with pipe, we remove him and reduce its fitness
                    ge[birds.index(bird)].fitness -= 1
                    nets.pop(birds.index(bird))
                    ge.pop(birds.index(bird))
                    birds.pop(birds.index(bird))

            if pipe.x + pipe.PIPE_TOP.get_width() < 0:
                rem.append(pipe)

            if not pipe.passed and pipe.x < bird.pos_x:
                pipe.passed = True
                add_pipe = True


        if add_pipe:
            score += 1
            for genome in ge:
                # if bird has passe a pipe we increase his fitness
                genome.fitness += 5
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


        draw_window(win, birds, base, pipes, score, level, gen)

        if score > 100:
            break

def run(config_file):
    #runs the NEAT algorithm to train a neural network to play flappy bird.

    config = neat.config.Config(neat.DefaultGenome, neat.DefaultReproduction,
                         neat.DefaultSpeciesSet, neat.DefaultStagnation,
                         config_file)

    # Create the population, which is the top-level object for a NEAT run.
    p = neat.Population(config)

    # Add a stdout reporter to show progress in the terminal.
    p.add_reporter(neat.StdOutReporter(True))
    stats = neat.StatisticsReporter()
    p.add_reporter(stats)

    # Run for up to 50 generations.
    winner = p.run(main, 50)

    # show final stats
    print('\nBest genome:\n{!s}'.format(winner))


if __name__ == '__main__':
    # Determine path to configuration file.
    local_dir = os.path.dirname(__file__)
    config_path = os.path.join(local_dir, 'config-feedforward.txt')
    run(config_path)
