import pygame, random, time
from pygame.locals import *

# 變量
SCREEN_WIDTH = 400  #螢幕寬 
SCREEN_HEIGHT = 600  #螢幕高
SPEED = 20   #下降速度
GRAVITY = 2.5  #加速度
GAME_SPEED = 15  #水管、地板往左移速度

GROUND_WIDTH = 2 * SCREEN_WIDTH   #地板寬
GROUND_HEIGHT = 100  #地板高

PIPE_WIDTH = 80 #水管寬
PIPE_HEIGHT = 500  #水管高

PIPE_GAP = 150  #水管縫隙

wing = '教學簡報\\簡易遊戲code\\flappy\\assets\\audio\\wing.wav'  #揮動翅膀聲音路徑
hit = '教學簡報\\簡易遊戲code\\flappy\\assets\\audio\\hit.wav'  #撞到聲音路徑
gameover_image_path = '教學簡報\\簡易遊戲code\\flappy\\assets\\sprites\\gameover.png'  #game over 圖片路徑


pygame.mixer.init()

class Bird(pygame.sprite.Sprite):
    def __init__(self):
        self.speed = SPEED  
        #讓小鳥有動畫的效果
        pygame.sprite.Sprite.__init__(self)
        self.images =  [pygame.image.load('教學簡報\\簡易遊戲code\\flappy\\assets\\sprites\\bluebird-upflap.png').convert_alpha(),
                        pygame.image.load('教學簡報\\簡易遊戲code\\flappy\\assets\\sprites\\bluebird-midflap.png').convert_alpha(),
                        pygame.image.load('教學簡報\\簡易遊戲code\\flappy\\assets\\sprites\\bluebird-downflap.png').convert_alpha()]
        self.speed = SPEED  
        self.current_image = 0  #一開始的圖片
        self.image = pygame.image.load('教學簡報\\簡易遊戲code\\flappy\\assets\\sprites\\bluebird-upflap.png').convert_alpha()
        self.mask = pygame.mask.from_surface(self.image)  #偵測是否碰撞
        self.rect = self.image.get_rect()
        self.rect[0] = SCREEN_WIDTH / 6  #初始x座標
        self.rect[1] = SCREEN_HEIGHT / 2  #初始y座標

    def update(self):  #更新位置及圖片
        self.current_image = (self.current_image + 1) % 3 #小鳥動畫取餘數
        self.image = self.images[self.current_image]  #更新圖片
        self.speed += GRAVITY  #下降速度變快
        self.rect[1] += self.speed  #y座標增加，小鳥下降        

    def bump(self):  #往上跳
        self.speed = -SPEED  #y座標減少，小鳥上升

    def begin(self):  #初始介面
        self.current_image = (self.current_image + 1) % 3  #小鳥動畫取餘數
        self.image = self.images[self.current_image]  #更新圖片

    def is_off_screen(self):  #飛出螢幕外
        return self.rect[1] < 0 or self.rect[1] > SCREEN_HEIGHT  #偵測位置回傳ture or false

class Pipe(pygame.sprite.Sprite):
    def __init__(self, inverted, xpos, ysize):
        pygame.sprite.Sprite.__init__(self)
        #水管圖片路徑
        self.image = pygame.image.load('教學簡報\\簡易遊戲code\\flappy\\assets\\sprites\\pipe-green.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (PIPE_WIDTH, PIPE_HEIGHT))  #水管大小
        self.rect = self.image.get_rect()
        self.rect[0] = xpos  #正立、倒立水管x座標
        if inverted:  #倒立的水管
            self.image = pygame.transform.flip(self.image, False, True)  #左右不翻轉，上下顛倒
            self.rect[1] = - (self.rect[3] - ysize)  #倒立水管y座標
        else:  #正立水管
            self.rect[1] = SCREEN_HEIGHT - ysize   #正立水管y座標
        self.mask = pygame.mask.from_surface(self.image)  #偵測是否碰撞

    def update(self):  #更新位置
        self.rect[0] -= GAME_SPEED  #x軸座標減少，往左移動

class Ground(pygame.sprite.Sprite):
    def __init__(self, xpos):
        pygame.sprite.Sprite.__init__(self)
        #地板圖片路徑
        self.image = pygame.image.load('教學簡報\\簡易遊戲code\\flappy\\assets\\sprites\\base.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (GROUND_WIDTH, GROUND_HEIGHT))  #地板大小
        self.mask = pygame.mask.from_surface(self.image)  #偵測碰撞
        self.rect = self.image.get_rect()  
        self.rect[0] = xpos  #地板x座標
        self.rect[1] = SCREEN_HEIGHT - GROUND_HEIGHT #地板y座標

    def update(self):  #更新位置
        self.rect[0] -= GAME_SPEED  #x軸座標減少，往左移動

def is_off_screen(sprite):
    return sprite.rect[0] < -(sprite.rect[2])   
 #偵測各個圖片是否已經整個跑出螢幕外了回傳ture or false
    
def get_random_pipes(xpos):  
    size = random.randint(100, 300)  #算正立、倒立水管y座標
    pipe = Pipe(False, xpos, size)
    pipe_inverted = Pipe(True, xpos, SCREEN_HEIGHT - size - PIPE_GAP)
    return pipe, pipe_inverted

def load_digit_images():
    digits = []  #設一個儲存圖片陣列
    for i in range(10):  #分數圖片陣列儲存到digits裡
        digits.append(pygame.image.load(f'教學簡報\\簡易遊戲code\\flappy\\assets\\sprites\\{i}.png').convert_alpha())
    return digits

def display_score(screen, score, digit_images): 
    score_str = str(score) #分數轉換成字串
    total_width = sum(digit_images[int(digit)].get_width() for digit in score_str)  #計算分數總共需要的寬度
    x_offset = (SCREEN_WIDTH - total_width) / 2  #分數擺放位置
    #由左而右擺數字增加x座標向右擺放
    for digit in score_str: 
        screen.blit(digit_images[int(digit)], (x_offset, 50))   
        x_offset += digit_images[int(digit)].get_width()

def reset_game():
    global bird_group, ground_group, pipe_group, bird, score, begin, off_screen_time
    bird_group = pygame.sprite.Group()  
    bird = Bird()
    bird_group.add(bird)  #新增一隻小鳥

    ground_group = pygame.sprite.Group()
    for i in range(2):
        ground = Ground(GROUND_WIDTH * i)  #兩個地板位置不同
        ground_group.add(ground)  #新增兩個地板

    pipe_group = pygame.sprite.Group()
    for i in range(2):
        pipes = get_random_pipes(SCREEN_WIDTH * i + 800)  #兩個水管位置不同
        pipe_group.add(pipes[0])  #上下兩水管 兩組
        pipe_group.add(pipes[1])

    score = 0  #分數重置
    begin = True  #回到遊戲初介面
    off_screen_time = None  #小鳥飛到螢幕外的時間重置

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Flappy Bird')

BACKGROUND = pygame.image.load('教學簡報\\簡易遊戲code\\flappy\\assets\\sprites\\background-day.png')  #遊戲背景路徑
BACKGROUND = pygame.transform.scale(BACKGROUND, (SCREEN_WIDTH, SCREEN_HEIGHT))  #遊戲背景大小
BEGIN_IMAGE = pygame.image.load('教學簡報\\簡易遊戲code\\flappy\\assets\\sprites\\message.png').convert_alpha()  #遊戲初始介面圖片路徑
GAME_OVER_IMAGE = pygame.image.load(gameover_image_path).convert_alpha()  #gameover 圖片路徑

digit_images = load_digit_images()

reset_game()

clock = pygame.time.Clock()  #用於控制遊戲的幀率，讓遊戲在固定的速度下運行

while True:
    while begin:  #遊戲在初始畫面
        clock.tick(15)  #設定每秒鐘運行15幀，控制遊戲速度
        # 如果關閉視窗，會停止程式的所有運行並關閉。
        for event in pygame.event.get():   
            if event.type == QUIT:
                pygame.quit()
                exit()
            if event.type == KEYDOWN:  #如果有按鍵被按下
                if  event.key == K_UP:   #檢查是否是上鍵
                    bird.bump()  #小鳥往上
                    pygame.mixer.music.load(wing)   #加載翅膀聲音
                    pygame.mixer.music.play()  #播放翅膀聲音
                    begin = False  #設定遊戲開始改為false，結束此循環，進入遊戲主循環

        screen.blit(BACKGROUND, (0, 0)) #顯示背景圖片座標
        screen.blit(BEGIN_IMAGE, (120, 150))  #顯示初始遊戲圖片座標

        if is_off_screen(ground_group.sprites()[0]):  #如果地面移出視窗，重新生成一個地面
            ground_group.remove(ground_group.sprites()[0])  #移除跑出去的
            new_ground = Ground(GROUND_WIDTH - 20)  #創立一個新的
            ground_group.add(new_ground)  #新增一個新的

        ground_group.update()  #地板往左移動
        ground_group.draw(screen)  #繪製地板
        pygame.display.update()  #不斷更新顯示

        bird.begin()  #小鳥的動畫
        bird_group.draw(screen)  #繪製小鳥
        pygame.display.update()  #不斷更新顯示


        

    while not begin: #遊戲開始  
        clock.tick(15)  #設定每秒鐘運行15幀，控制遊戲速度
        # 如果關閉視窗，會停止程式的所有運行並關閉。
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit()
            if event.type == KEYDOWN:  #如果有按鍵被按下
                if  event.key == K_UP:  #檢查是否是空格鍵或上箭頭鍵
                    bird.bump()  #小鳥往上
                    pygame.mixer.music.load(wing)  #加載翅膀聲音
                    pygame.mixer.music.play()  #播放翅膀聲音

        screen.blit(BACKGROUND, (0, 0))  #顯示背景圖片座標

        if is_off_screen(ground_group.sprites()[0]):  #如果地面移出視窗，重新生成一個地面 
            ground_group.remove(ground_group.sprites()[0])  #移除跑出去的
            new_ground = Ground(GROUND_WIDTH - 20)   #創立一個新的
            ground_group.add(new_ground)  #新增一個新的

        if is_off_screen(pipe_group.sprites()[0]):  # 如果水管超出視窗範圍
            pipe_group.remove(pipe_group.sprites()[0])  #移除水管(其中一個
            pipe_group.remove(pipe_group.sprites()[0])  #移除水管(其中一個(要寫兩次)s
            pipes = get_random_pipes(SCREEN_WIDTH * 2)  #生成新的水管
            pipe_group.add(pipes[0])  #新增水管(上或下)
            pipe_group.add(pipes[1])  #新增水管(上或下)(要寫兩次)
            score += 1  #水管被移除後分數加1

        bird_group.update()  #更新小鳥的狀態
        ground_group.update()  #地板往左移動
        pipe_group.update()  #水管往左移動

        bird_group.draw(screen)  #繪製小鳥  
        pipe_group.draw(screen)  #繪製水管
        ground_group.draw(screen)  #繪製地板
        display_score(screen, score, digit_images)  #顯示分數

        pygame.display.update()  #不斷更新顯示

        if bird.is_off_screen():   #如果小鳥超出視窗範圍
            if off_screen_time is None:  #又剛好時間還沒被記錄
                off_screen_time = time.time()  #記錄當前時間(off_screen_time=剛飛出去的時間)
            elif time.time() - off_screen_time > 1.5:  #當現在的時間-剛飛出去德時間>1.5秒   
                pygame.mixer.music.load(hit)  #加載撞擊音效
                pygame.mixer.music.play()  #播放撞擊音效
                screen.blit(GAME_OVER_IMAGE, ((SCREEN_WIDTH - GAME_OVER_IMAGE.get_width()) / 2
                         ,(SCREEN_HEIGHT - GAME_OVER_IMAGE.get_height()) / 2))  #顯示gameover的位置
                pygame.display.update()  #顯示更新gameover
                time.sleep(2)  #顯示兩秒
                reset_game()  #重置遊戲
                break
        else:
            off_screen_time = None  #重置超出視窗時間

        # 如果小鳥撞到地面或水管
        if (pygame.sprite.groupcollide(bird_group, ground_group, False, False, pygame.sprite.collide_mask) or
                pygame.sprite.groupcollide(bird_group, pipe_group, False, False, pygame.sprite.collide_mask)):
            pygame.mixer.music.load(hit)  #加載撞擊音效
            pygame.mixer.music.play()  #播放撞擊音效
            screen.blit(GAME_OVER_IMAGE, ((SCREEN_WIDTH - GAME_OVER_IMAGE.get_width()) / 2
                          , (SCREEN_HEIGHT - GAME_OVER_IMAGE.get_height()) / 2))  #顯示gameover的位置
            time.sleep(2)  #顯示兩秒
            reset_game()  #重置遊戲  
            break
