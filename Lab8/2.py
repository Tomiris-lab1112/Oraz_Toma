import pygame
import random
import sys

# Инициализация Pygame 
pygame.init()

# Цвета 
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (213, 50, 80)
GREEN = (0, 255, 0)
BLUE = (50, 153, 213)

# Размеры экрана 
dis_width = 800
dis_height = 600

# Настройки змейки 
snake_block = 10 #размер одного блока змейки
initial_speed = 15

# Создание окна
dis = pygame.display.set_mode((dis_width, dis_height))
pygame.display.set_caption('Snake Game') #задаёт заголовок окна
clock = pygame.time.Clock()

# Шрифт для текста 
font_style = pygame.font.SysFont("bahnschrift", 25) #И размер текста для счёта

# Функция отображения счёта и уровня 
def show_score_level(score, level):
    score_text = font_style.render("Score: " + str(score), True, WHITE)
    level_text = font_style.render("Level: " + str(level), True, WHITE)
    dis.blit(score_text, [0, 0]) #выводится в координатах
    dis.blit(level_text, [0, 30]) #выводится чуть ниже

# Функция отрисовки змейки, Рисует все сегменты змейки (тело)
def draw_snake(snake_list):
    for x in snake_list: #Каждый сегмент — это список [x, y], содержащий координаты блока змейки.
        pygame.draw.rect(dis, GREEN, [x[0], x[1], snake_block, snake_block])

# Функция генерации еды, чтобы она не появлялась на змее 
def generate_food(snake_list):
    while True:
        x = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0 #это чтобы координаты совпадали с сеткой змейки,змейка двигается блоками по 10 пикселей
        y = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
        if [x, y] not in snake_list:  # проверяем, что еда не на змее
            return x, y

#  Основной игровой цикл 
def gameLoop():
    # Начальные настройки
    game_over = False #переменная, которая станет True, когда игра полностью закончится.
    game_close = False #когда игрок проиграл, но окно игры ещё открыто для перезапуска.

    x1 = dis_width / 2 #Начальная позиция головы змейки — по центру экрана.
    y1 = dis_height / 2

    x1_change = 0
    y1_change = 0

    snake_List = [] #список сегментов змейки. Сначала он пустой.
    Length_of_snake = 1 #длина змейки в блоках, сначала 1.

    # Начальная еда
    foodx, foody = generate_food(snake_List) #Генерация первой еды с помощью функции generate_food

    # Счёт и уровень
    score = 0
    level = 1
    foods_eaten = 0 #количество съеденной еды
    snake_speed = initial_speed #скорость змейки

    while not game_over:

        # Окно "Game Over" 
        while game_close:
            dis.fill(BLACK)
            message = font_style.render("Game Over! Press Q-Quit or C-Play Again", True, RED) #Если змейка столкнулась с границей или с самой собой — game_close = True.
            dis.blit(message, [dis_width / 6, dis_height / 3])
            show_score_level(score, level)
            pygame.display.update()

            for event in pygame.event.get(): #Обработка нажатий в окне Game Over
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q: #Q-выйти из игры
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c: #C-перезапустить игру
                        gameLoop()  # перезапуск игры

        # Обработка событий 
        for event in pygame.event.get():
            if event.type == pygame.QUIT: # Обработка закрытия окна
                game_over = True #Стрелки клавиатуры задают направление движения змейки.
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -snake_block
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = snake_block
                    x1_change = 0

        # Проверка выхода за границы 
        if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
            game_close = True #Если голова змейки выходит за границы окна, игра переходит в состояние Game Over

        # Перемещение змейки, Голова змейки перемещается на текущую скорость
        x1 += x1_change
        y1 += y1_change

        dis.fill(BLACK)

        # Отрисовка еды 
        pygame.draw.rect(dis, BLUE, [foodx, foody, snake_block, snake_block])

        # Обновление тела змейки 
        snake_Head = [x1, y1] #координаты головы.
        snake_List.append(snake_Head)
        if len(snake_List) > Length_of_snake: #Если список длиннее, чем текущая длина змейки — удаляем самый старый сегмент(хвост)
            del snake_List[0]

        # Проверка столкновения с самим собой 
        for segment in snake_List[:-1]:
            if segment == snake_Head:
                game_close = True

        draw_snake(snake_List) #Рисуем все сегменты змейки.
        show_score_level(score, level) #Показываем счёт и уровень.
        pygame.display.update()

        # Проверка поедания еды
        #увеличиваем длину змейки, счёт, количество съеденной еды;
        #генерируем новую еду;
        #каждые 3 съеденные еды — повышаем уровень и скорость.
        if x1 == foodx and y1 == foody:
            Length_of_snake += 1
            score += 1
            foods_eaten += 1
            foodx, foody = generate_food(snake_List)

            # Повышение уровня каждые 3 еды 
            if foods_eaten % 3 == 0: #проверяет, делится ли количество съеденной еды на 3.
                level += 1 #увеличение длинну
                snake_speed += 2  # увеличение скорости

        clock.tick(snake_speed)

    pygame.quit()
    sys.exit() #авершает выполнение

# Запуск игры 
gameLoop() 
