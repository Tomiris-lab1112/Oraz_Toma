import pygame
import sys

# Инициализация Pygame 
pygame.init()

# Настройки окна 
WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Red Ball Movement")

# Цвета и параметры шара 
WHITE = (255, 255, 255)
RED = (255, 0, 0)
RADIUS = 25
STEP = 20

# Начальная позиция шара (центр окна) 
x, y = WIDTH // 2, HEIGHT // 2

# Основной цикл
clock = pygame.time.Clock()
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Получаем нажатые клавиши 
    keys = pygame.key.get_pressed()

    # Движение шара с проверкой границ 
    if keys[pygame.K_UP] and y - RADIUS - STEP >= 0:
        y -= STEP
    if keys[pygame.K_DOWN] and y + RADIUS + STEP <= HEIGHT:
        y += STEP
    if keys[pygame.K_LEFT] and x - RADIUS - STEP >= 0:
        x -= STEP
    if keys[pygame.K_RIGHT] and x + RADIUS + STEP <= WIDTH:
        x += STEP

    # Отрисовка 
    screen.fill(WHITE)
    pygame.draw.circle(screen, RED, (x, y), RADIUS)
    pygame.display.flip()

    clock.tick(30)  # 30 FPS

pygame.quit()
sys.exit()
