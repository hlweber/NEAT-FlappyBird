import pygame
import random

class Pipe():
    # Travel speed of pipe on x-axis
    VEL = 5

    def __init__(self, x, level, pipe_img):
        self.level = level

        # GAP BASED ON LEVEL
        if self.level == 1:
            self.gap = random.randint(220,250)
        elif self.level == 2:
            self.gap = random.randint(200, 250)
        elif self.level == 3:
            self.gap = random.randint(200, 220)
        elif self.level == 4:
            self.gap = random.randint(180, 220)
        elif self.level == 5:
            self.gap = random.randint(180, 200)
        elif self.level == 6:
            self.gap = random.randint(150, 200)
        elif self.level == 7:
            self.gap = random.randint(150, 180)
        elif self.level == 8:
            self.gap = random.randint(130, 180)
        else:
            self.gap = random.randint(130,150)

        self.x = x
        self.height = 0

        # where the top and bottom of the pipe is
        self.top = 0
        self.bottom = 0

        self.PIPE_TOP = pygame.transform.flip(pipe_img, False, True)
        self.PIPE_BOTTOM = pipe_img

        self.passed = False

        self.set_height()

    def set_height(self):
        # height of pipe
        self.height = random.randrange(50, 450)
        self.top = self.height - self.PIPE_TOP.get_height()
        self.bottom = self.height + self.gap

    def move(self, vel):
        # moving pipe
        self.x -= vel

    def draw(self, win):
        # draw top pipe
        win.blit(self.PIPE_TOP, (self.x, self.top))
        # draw bottom pipe
        win.blit(self.PIPE_BOTTOM, (self.x, self.bottom))


    def collide(self, bird):
        # check if pipe is colliding with bird
        bird_mask = bird.get_mask()
        top_mask = pygame.mask.from_surface(self.PIPE_TOP)
        bottom_mask = pygame.mask.from_surface(self.PIPE_BOTTOM)
        top_offset = (self.x - bird.pos_x, self.top - round(bird.pos_y))
        bottom_offset = (self.x - bird.pos_x, self.bottom - round(bird.pos_y))

        b_point = bird_mask.overlap(bottom_mask, bottom_offset)
        t_point = bird_mask.overlap(top_mask,top_offset)

        if b_point or t_point:
            return True

        return False
