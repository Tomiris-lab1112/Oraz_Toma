import pygame
import math
import datetime
import sys

pygame.init()

# Настройки окна 
WIDTH, HEIGHT = 800, 800
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Mickey Mouse Clock")

# Загрузка изображений 
# ✅ Используем сырые строки, чтобы избежать ошибок путей на Windows
base = pygame.image.load(r"c:\Users\orazt\Downloads\base_micky.jpg").convert_alpha()
minute_hand = pygame.image.load(r"c:\Users\orazt\Downloads\minute.png").convert_alpha()
second_hand = pygame.image.load(r"c:\Users\orazt\Downloads\second.png").convert_alpha()

# Масштабирование (при необходимости) 
base = pygame.transform.smoothscale(base, (WIDTH, HEIGHT))

# Центр вращения (где руки закреплены) 
CENTER = (WIDTH // 2, HEIGHT // 2)

# Основной цикл 
clock = pygame.time.Clock()
running = True

def rotate_center(image, angle):
    """Вращает изображение вокруг центра"""
    rotated_image = pygame.transform.rotozoom(image, -angle, 1)
    rotated_rect = rotated_image.get_rect(center=CENTER)
    return rotated_image, rotated_rect

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Получаем текущее время 
    now = datetime.datetime.now()
    second = now.second + now.microsecond / 1_000_000  # для плавного движения
    minute = now.minute + second / 60

    # Расчёт углов вращения 
    second_angle = second * 6            # 360° / 60 сек
    minute_angle = minute * 6            # 360° / 60 мин

    # Отрисовка 
    screen.fill((255, 255, 255))
    screen.blit(base, (0, 0))

    # Вращаем и рисуем руки
    rotated_minute, rect_minute = rotate_center(minute_hand, minute_angle)
    rotated_second, rect_second = rotate_center(second_hand, second_angle)

    screen.blit(rotated_minute, rect_minute)
    screen.blit(rotated_second, rect_second)

    pygame.display.flip()
    clock.tick(60)  # плавное обновление 60 FPS

pygame.quit()
sys.exit()