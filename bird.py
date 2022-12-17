import pygame
import os


class Bird:
    MAX_ROT = 25
    MIN_ROT = -60
    IMGS = [pygame.transform.scale2x(pygame.image.load(os.path.join("img", "bird" + str(x) + ".png"))) for x in
            range(1, 4)]
    ANIMATION_INTERVAL = 5

    def __init__(self, pos_x, pos_y, game_velocity):
        self.pos_x = pos_x
        self.pos_y = pos_y

        self.height = self.pos_y

        self.speed = 0
        self.pos_tick = 0
        self.game_vel = game_velocity
        self.ROT_VEL = 600/game_velocity

        self.tick_count = 0
        self.tilt = 0
        self.img_count = 0
        self.img = self.IMGS[0]

    def jump(self):
        # change speed so bird goes up
        self.speed = -305/self.game_vel
        self.pos_tick = 0
        self.height = self.pos_y

    def move(self):
        # move bird
        # speed depends on last time the bird has jumped - pos_tick -
        # and it's terminal velocity
        self.pos_tick += 1

        velocity_final = self.speed * (self.pos_tick*30/self.game_vel) + (45/self.game_vel)*((self.pos_tick*30/self.game_vel))**2

        # terminal velocity
        if velocity_final >= (450/self.game_vel):
            velocity_final = (450/self.game_vel)

        if velocity_final < 0:
            velocity_final -= (60/self.game_vel)

        self.pos_y = self.pos_y + velocity_final

        if self.pos_y < 0:
            self.pos_y=0
        elif self.pos_y > 730:
            self.pos_y = 730

        if velocity_final < 0 or self.pos_y < self.height + 50:
            if self.tilt < self.MAX_ROT:
                if self.tilt + self.ROT_VEL > self.MAX_ROT:
                    self.tilt = self.MAX_ROT
                else:
                    self.tilt += self.ROT_VEL
        else:
            if self.tilt > -90:
                if self.tilt - self.ROT_VEL > self.MIN_ROT:
                    self.tilt -= self.ROT_VEL
                else:
                    self.tilt = self.MIN_ROT

    def draw(self, win):
        # draw animation of flapping wings and rotate image of bird

        self.img_count += 1
        if self.img_count <= self.ANIMATION_INTERVAL:
            self.img = self.IMGS[0]
        elif self.img_count <= self.ANIMATION_INTERVAL * 2:
            self.img = self.IMGS[1]
        elif self.img_count <= self.ANIMATION_INTERVAL * 3:
            self.img = self.IMGS[2]
        elif self.img_count <= self.ANIMATION_INTERVAL * 4:
            self.img = self.IMGS[1]
        elif self.img_count == self.ANIMATION_INTERVAL * 4 + 1:
            self.img = self.IMGS[0]
            self.img_count = 0

        if self.tilt <= -10 or self.pos_y == 730 or self.pos_y == 0:
            self.img = self.IMGS[1]
            self.img_count = self.ANIMATION_INTERVAL * 2

        # tilt the bird
        rotated_bird = pygame.transform.rotate(self.img, self.tilt)
        win.blit(rotated_bird, rotated_bird.get_rect(center=self.img.get_rect(topleft=(self.pos_x, self.pos_y)).center).topleft)

    def get_mask(self):
        # used to check either it has collide or not with pipe
        return pygame.mask.from_surface(self.img)

    def die(self):
        self.speed = 16
        self.tilt = -90
