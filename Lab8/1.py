# Imports
import pygame, sys #pygame — основная библиотека для игр.
from pygame.locals import *  #Импорт всех констант из pygame.locals
import random, time  #Импорт модулей: random — для случайных чисел, time — для работы со временем 

# Initializing Pygame
pygame.init() #запускает все внутренние модули Pygame

# Setting up FPS
FPS = 60 #Ограничивает количество кадров в секунду
FramePerSec = pygame.time.Clock()

# Creating colors  #цвета, размеры экрана, скорость и счётчики
BLUE  = (0, 0, 255) 
RED   = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)  # Color for coins

# Other variables #переменные для логики игры, не связанные с цветом
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
SPEED = 5
SCORE = 0
COINS = 0  # Count of collected coins

# Setting up fonts #Шрифты и надписи
font = pygame.font.SysFont("Verdana", 60) #Создаёт объект шрифта под названием font
font_small = pygame.font.SysFont("Verdana", 20) #используется для счётчиков, очков, текста в углу 
game_over_text = font.render("Game Over", True, BLACK) #render() создаёт изображение текста, True — включает сглаживание букв

# Load background
background = pygame.image.load(
    "c:\\Users\\orazt\\OneDrive\\Изображения\\Снимки экрана\\Снимок экрана 2025-11-05 215847 — копия.png"
) #загружает изображение с указанного пути.

# Create display
DISPLAYSURF = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT)) #Создаёт окно игры заданного размера, DISPLAYSURF — это главная поверхность (экран)
DISPLAYSURF.fill(WHITE)
pygame.display.set_caption("Car Game") #Устанавливает название окна

# Audio setup 
pygame.mixer.init()
pygame.mixer.music.load('c:\\Users\\orazt\\Downloads\\background.wav')  # Background music #Загружает фоновую музыку из файла .wav
pygame.mixer.music.play(-1)  # Loop infinitely     #-1 означает зациклить музыку бесконечно
crash_sound = pygame.mixer.Sound('c:\\Users\\orazt\\Downloads\\crash.wav')  # звук столкования

# Player class 
class Player(pygame.sprite.Sprite): #Создаёт класс игрока
    def __init__(self):  
        super().__init__()  #конструктор родительского класса Sprite
        self.image = pygame.image.load(   #Загружает изображение машины игрока.
            "c:\\Users\\orazt\\OneDrive\\Изображения\\Снимки экрана\\Снимок экрана 2025-11-05 222615 — копия.png"
        )
        self.rect = self.image.get_rect()  #Создаёт прямоугольник (rect) вокруг изображения
        self.rect.center = (160, 520)  #Устанавливает начальную позицию игрока
       
    def move(self):
        pressed_keys = pygame.key.get_pressed()  #текущее состояние всех клавиш клавиатуры
        if self.rect.left > 0 and pressed_keys[K_LEFT]:  #чтобы не выйти за экран
            self.rect.move_ip(-5, 0) #двигает машину влево на 5 пикселей
        if self.rect.right < SCREEN_WIDTH and pressed_keys[K_RIGHT]:
            self.rect.move_ip(5, 0) #проверяет чтобы не ушло на право

#Enemy class #Создаёт класс врага
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load(
            "c:\\Users\\orazt\\OneDrive\\Изображения\\Снимки экрана\\Снимок экрана 2025-11-05 222610.png"
        )
        self.rect = self.image.get_rect() #Создаёт прямоугольник для позиции и коллизий
        self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)

    def move(self):
        global SCORE #чтобы увеличивать счёт при прохождении врага через экран.
        self.rect.move_ip(0, SPEED) #Двигает врага вниз по экрану
        if self.rect.bottom > SCREEN_HEIGHT:
            SCORE += 1 #Если дошёл, увеличивает счёт на 1
            self.rect.top = 0
            self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)

#Coin class 
class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((30, 30)) #Создаёт жёлтый квадрат 30x30 пикселей, который будет представлять монету
        self.image.fill(YELLOW)
        self.rect = self.image.get_rect() #rect нужен для позиции и коллизий.
        self.rect.center = (random.randint(40, SCREEN_WIDTH-40), random.randint(-1500, -100)) #вертикально и горизонтально 

    def move(self):
        self.rect.move_ip(0, SPEED)
        if self.rect.top > SCREEN_HEIGHT:
            # Сбросить монету на новую случайную позицию выше экрана
            self.rect.top = random.randint(-1500, -100) #чтобы монета "падала" вниз с разной высоты
            self.rect.center = (random.randint(40, SCREEN_WIDTH-40), self.rect.top) #Устанавливаем центр монеты по горизонтали и вертикали

# Creating sprites 
P1 = Player()
E1 = Enemy()
C1 = Coin()

# Sprite groups
enemies = pygame.sprite.Group()
enemies.add(E1) #Добавляет в неё одного врага E1

coins = pygame.sprite.Group()
coins.add(C1)

all_sprites = pygame.sprite.Group()
all_sprites.add(P1) #рисовать и обновлять объекты одновременно
all_sprites.add(E1)
all_sprites.add(C1)

#Событие для увеличения скорости
INC_SPEED = pygame.USEREVENT + 1
pygame.time.set_timer(INC_SPEED, 1000)

# Game Loop 
while True:
    #Обработка событий
    for event in pygame.event.get():
        if event.type == INC_SPEED:
            SPEED += 0.5
        if event.type == QUIT: #QUIT — закрываем игру, если пользователь нажал крестик окн
            pygame.quit()
            sys.exit()

    # Draw background
    DISPLAYSURF.blit(background, (0, 0))

    #Отображение счёта и монет,
    #Создаёт текст с текущим счётом и количеством монет и рисует его на экран
    score_text = font_small.render(f"Score: {SCORE}", True, BLACK)
    coins_text = font_small.render(f"Coins: {COINS}", True, BLACK)
    DISPLAYSURF.blit(score_text, (10, 10))
    DISPLAYSURF.blit(coins_text, (SCREEN_WIDTH - 100, 10))  # Top-right corner

    #Двигать и рисовать все спрайты
    for entity in all_sprites:
        entity.move()
        DISPLAYSURF.blit(entity.image, entity.rect)

    #Столкновение с врагами
    if pygame.sprite.spritecollideany(P1, enemies):
        crash_sound.play()
        pygame.mixer.music.stop()  # Stop background music
        time.sleep(1)
        DISPLAYSURF.fill(RED)
        DISPLAYSURF.blit(game_over_text, (30, 250))
        final_score_text = font_small.render(f"Final Score: {SCORE}, Coins: {COINS}", True, BLACK)
        DISPLAYSURF.blit(final_score_text, (50, 320))
        pygame.display.update()
        for entity in all_sprites:
            entity.kill() #Все объекты (игрок, враги, монеты) удаляются из игры.
        time.sleep(3) #Игра ждёт 3 секунды, чтобы игрок успел увидеть финальный результат.
        pygame.quit()
        sys.exit()

    #Столкновение с монетами
    collected_coins = pygame.sprite.spritecollide(P1, coins, False) #False означает, что монеты не удаляются автоматически после столкновения.
    for coin in collected_coins:
        COINS += 1
        coin.rect.top = random.randint(-1500, -100)
        coin.rect.center = (random.randint(40, SCREEN_WIDTH-40), coin.rect.top)

    pygame.display.update()
    FramePerSec.tick(FPS) #Ограничиваем частоту кадров до FPS
