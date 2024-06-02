import pygame, random, time
from pygame.locals import *

# 變量
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
SPEED = 20
GRAVITY = 2.5
GAME_SPEED = 15

GROUND_WIDTH = 2 * SCREEN_WIDTH
GROUND_HEIGHT = 100

PIPE_WIDTH = 80
PIPE_HEIGHT = 500

PIPE_GAP = 150

wing = '教學簡報\\簡易遊戲code\\flappy\\assets\\audio\\wing.wav'
hit = '教學簡報\\簡易遊戲code\\flappy\\assets\\audio\\hit.wav'
gameover_image_path = '教學簡報\\簡易遊戲code\\flappy\\assets\\sprites\\gameover.png'

pygame.mixer.init()

class Bird(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.images =  [pygame.image.load('教學簡報\\簡易遊戲code\\flappy\\assets\\sprites\\bluebird-upflap.png').convert_alpha(),
                        pygame.image.load('教學簡報\\簡易遊戲code\\flappy\\assets\\sprites\\bluebird-midflap.png').convert_alpha(),
                        pygame.image.load('教學簡報\\簡易遊戲code\\flappy\\assets\\sprites\\bluebird-downflap.png').convert_alpha()]
        self.speed = SPEED
        self.current_image = 0
        self.image = pygame.image.load('教學簡報\\簡易遊戲code\\flappy\\assets\\sprites\\bluebird-upflap.png').convert_alpha()
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect[0] = SCREEN_WIDTH / 6
        self.rect[1] = SCREEN_HEIGHT / 2

    def update(self):
        self.current_image = (self.current_image + 1) % 3
        self.image = self.images[self.current_image]
        self.speed += GRAVITY
        self.rect[1] += self.speed

    def bump(self):
        self.speed = -SPEED

    def begin(self):
        self.current_image = (self.current_image + 1) % 3
        self.image = self.images[self.current_image]

    def is_off_screen(self):
        return self.rect[1] < 0 or self.rect[1] > SCREEN_HEIGHT

class Pipe(pygame.sprite.Sprite):
    def __init__(self, inverted, xpos, ysize):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('教學簡報\\簡易遊戲code\\flappy\\assets\\sprites\\pipe-green.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (PIPE_WIDTH, PIPE_HEIGHT))
        self.rect = self.image.get_rect()
        self.rect[0] = xpos
        if inverted:
            self.image = pygame.transform.flip(self.image, False, True)
            self.rect[1] = - (self.rect[3] - ysize)
        else:
            self.rect[1] = SCREEN_HEIGHT - ysize
        self.mask = pygame.mask.from_surface(self.image)

    def update(self):
        self.rect[0] -= GAME_SPEED

class Ground(pygame.sprite.Sprite):
    def __init__(self, xpos):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('教學簡報\\簡易遊戲code\\flappy\\assets\\sprites\\base.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (GROUND_WIDTH, GROUND_HEIGHT))
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect[0] = xpos
        self.rect[1] = SCREEN_HEIGHT - GROUND_HEIGHT

    def update(self):
        self.rect[0] -= GAME_SPEED

def is_off_screen(sprite):
    return sprite.rect[0] < -(sprite.rect[2])

def get_random_pipes(xpos):
    size = random.randint(100, 300)
    pipe = Pipe(False, xpos, size)
    pipe_inverted = Pipe(True, xpos, SCREEN_HEIGHT - size - PIPE_GAP)
    return pipe, pipe_inverted

def load_digit_images():
    digits = []
    for i in range(10):
        digits.append(pygame.image.load(f'教學簡報\\簡易遊戲code\\flappy\\assets\\sprites\\{i}.png').convert_alpha())
    return digits

def display_score(screen, score, digit_images):
    score_str = str(score)
    total_width = sum(digit_images[int(digit)].get_width() for digit in score_str)
    x_offset = (SCREEN_WIDTH - total_width) / 2
    for digit in score_str:
        screen.blit(digit_images[int(digit)], (x_offset, 50))
        x_offset += digit_images[int(digit)].get_width()

def reset_game():
    global bird_group, ground_group, pipe_group, bird, score, begin, off_screen_time
    bird_group = pygame.sprite.Group()
    bird = Bird()
    bird_group.add(bird)

    ground_group = pygame.sprite.Group()
    for i in range(2):
        ground = Ground(GROUND_WIDTH * i)
        ground_group.add(ground)

    pipe_group = pygame.sprite.Group()
    for i in range(2):
        pipes = get_random_pipes(SCREEN_WIDTH * i + 800)
        pipe_group.add(pipes[0])
        pipe_group.add(pipes[1])

    score = 0
    begin = True
    off_screen_time = None

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Flappy Bird')

BACKGROUND = pygame.image.load('教學簡報\\簡易遊戲code\\flappy\\assets\\sprites\\background-day.png')
BACKGROUND = pygame.transform.scale(BACKGROUND, (SCREEN_WIDTH, SCREEN_HEIGHT))
BEGIN_IMAGE = pygame.image.load('教學簡報\\簡易遊戲code\\flappy\\assets\\sprites\\message.png').convert_alpha()
GAME_OVER_IMAGE = pygame.image.load(gameover_image_path).convert_alpha()

digit_images = load_digit_images()

reset_game()

clock = pygame.time.Clock()

while True:
    while begin:
        clock.tick(15)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit()
            if event.type == KEYDOWN:
                if event.key == K_SPACE or event.key == K_UP:
                    bird.bump()
                    pygame.mixer.music.load(wing)
                    pygame.mixer.music.play()
                    begin = False

        screen.blit(BACKGROUND, (0, 0))
        screen.blit(BEGIN_IMAGE, (120, 150))

        if is_off_screen(ground_group.sprites()[0]):
            ground_group.remove(ground_group.sprites()[0])
            new_ground = Ground(GROUND_WIDTH - 20)
            ground_group.add(new_ground)

        bird.begin()
        ground_group.update()

        bird_group.draw(screen)
        ground_group.draw(screen)

        pygame.display.update()

    while not begin:
        clock.tick(15)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit()
            if event.type == KEYDOWN:
                if event.key == K_SPACE or event.key == K_UP:
                    bird.bump()
                    pygame.mixer.music.load(wing)
                    pygame.mixer.music.play()

        screen.blit(BACKGROUND, (0, 0))

        if is_off_screen(ground_group.sprites()[0]):
            ground_group.remove(ground_group.sprites()[0])
            new_ground = Ground(GROUND_WIDTH - 20)
            ground_group.add(new_ground)

        if is_off_screen(pipe_group.sprites()[0]):
            pipe_group.remove(pipe_group.sprites()[0])
            pipe_group.remove(pipe_group.sprites()[0])
            pipes = get_random_pipes(SCREEN_WIDTH * 2)
            pipe_group.add(pipes[0])
            pipe_group.add(pipes[1])
            score += 1

        bird_group.update()
        ground_group.update()
        pipe_group.update()

        bird_group.draw(screen)
        pipe_group.draw(screen)
        ground_group.draw(screen)
        display_score(screen, score, digit_images)

        pygame.display.update()

        if bird.is_off_screen():
            if off_screen_time is None:
                off_screen_time = time.time()
            elif time.time() - off_screen_time > 1.5:
                pygame.mixer.music.load(hit)
                pygame.mixer.music.play()
                screen.blit(GAME_OVER_IMAGE, ((SCREEN_WIDTH - GAME_OVER_IMAGE.get_width()) / 2, (SCREEN_HEIGHT - GAME_OVER_IMAGE.get_height()) / 2))
                pygame.display.update()
                time.sleep(2)
                reset_game()
                break
        else:
            off_screen_time = None

        if (pygame.sprite.groupcollide(bird_group, ground_group, False, False, pygame.sprite.collide_mask) or
                pygame.sprite.groupcollide(bird_group, pipe_group, False, False, pygame.sprite.collide_mask)):
            pygame.mixer.music.load(hit)
            pygame.mixer.music.play()
            screen.blit(GAME_OVER_IMAGE, ((SCREEN_WIDTH - GAME_OVER_IMAGE.get_width()) / 2, (SCREEN_HEIGHT - GAME_OVER_IMAGE.get_height()) / 2))
            pygame.display.update()
            time.sleep(2)
            reset_game()
            break
