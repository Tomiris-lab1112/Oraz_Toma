import pygame
import math
import datetime #чтобы брать текущее время для стрелок
import sys #для правильного завершения программы

pygame.init()

# Настройки окна 
WIDTH, HEIGHT = 800, 800
screen = pygame.display.set_mode((WIDTH, HEIGHT)) #это объект Surface
pygame.display.set_caption("Mickey Mouse Clock")  #заголовок окна — то, что написано сверху на панели окна.

# Загрузка изображений 
base = pygame.image.load(r"c:\\Users\\orazt\\Downloads\\base_micky.jpg").convert_alpha()  #загружает изображение с компьютера в программу.
minute_hand = pygame.image.load(r"c:\\Users\\orazt\\Downloads\\minute.png").convert_alpha() #сохраняет прозрачность
second_hand = pygame.image.load(r"c:\\Users\\orazt\\Downloads\\second.png").convert_alpha()

# Масштабирование фона 
base = pygame.transform.smoothscale(base, (WIDTH, HEIGHT))  #функция, которая изменяет размер картинки.

#  руки чуть короче
minute_hand = pygame.transform.smoothscale(
    minute_hand,
    (minute_hand.get_width(), int(minute_hand.get_height() * 0.85))  # чуть короче, ширину стрелки
)
second_hand = pygame.transform.smoothscale(
    second_hand,
    (second_hand.get_width(), int(second_hand.get_height() * 0.7))   # заметно короче, чтобы не выходила за циферблат, высоту стрелки
)

# Центр вращения
CENTER = (WIDTH // 2, HEIGHT // 2) #координаты центра часов

clock = pygame.time.Clock() #скорость обновления экрана
running = True #должна работать, пока окно не будет закрыто.

def rotate_center(image, angle):
    """Вращает изображение вокруг центра"""
    rotated_image = pygame.transform.rotozoom(image, -angle, 1) #поворачивает изображение на заданный угол.
    rotated_rect = rotated_image.get_rect(center=CENTER) #чтобы центр стрелки совпадал с центром часов
    return rotated_image, rotated_rect

while running:
    for event in pygame.event.get(): #отслеживает события — например, если пользователь закрыл окно.
        if event.type == pygame.QUIT:
            running = False #должна работать, пока окно не будет закрыто.

    now = datetime.datetime.now()
    second = now.second + now.microsecond / 1_000_000 #количество секунд
    minute = now.minute + second / 60 #минутная стрелка тоже двигалась плавно

    # Расчёт углов вращения
    second_angle = second * 6   #угол поворота секундной стрелки на часах.     # 360° / 60 сек
    minute_angle = minute * 6            # 360° / 60 мин

    # Отрисовка
    screen.fill((255, 255, 255)) #очищаю экран, заливая его белым цветом
    screen.blit(base, (0, 0))

    rotated_minute, rect_minute = rotate_center(minute_hand, minute_angle)  #поворачивает изображение стрелки на заданный угол.
    rotated_second, rect_second = rotate_center(second_hand, second_angle)

    # Рисуем обе руки
    screen.blit(rotated_minute, rect_minute) #blit() — это команда Pygame, которая рисует одно изображение на другом.
    screen.blit(rotated_second, rect_second)

    pygame.display.flip()
    clock.tick(60)

pygame.quit() #Завершает работу библиотеки Pygame
sys.exit() 