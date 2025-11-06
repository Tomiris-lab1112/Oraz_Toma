import pygame
import sys

# Инициализация Pygame 
pygame.init()
pygame.mixer.init()  # Для работы с музыкой

# Настройки окна
WIDTH, HEIGHT = 400, 200
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Simple Music Player")

# Цвета
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Список песен 
# музыкальные файлы (mp3)
songs = [
    r"c:\Users\orazt\Downloads\Drake ft. Kyla ft. Wizkid - One Dance.mp3",
    r"c:\Users\orazt\Downloads\Rihanna feat Jay-Z - Umbrella.mp3",
    r"c:\Users\orazt\Downloads\Kendrick Lamar - Money Trees (Feat. Jay Rock).mp3"
]
current_index = 0 #индекс текущей песни.
is_playing = False #логическая переменная, показывает играет ли музыка.

# Шрифты для отображения текста 
font = pygame.font.SysFont(None, 30)

def draw_text(text, pos):
    img = font.render(text, True, BLACK)
    screen.blit(img, pos)

def play_song(index): #загружает и воспроизводит выбранную песню.
    global is_playing
    pygame.mixer.music.load(songs[index]) 
    pygame.mixer.music.play()
    is_playing = True

def stop_song():
    global is_playing
    pygame.mixer.music.stop()
    is_playing = False

# Основной цикл 
clock = pygame.time.Clock()
running = True

while running:
    screen.fill(WHITE) #заливает фон белым цветом.

    # Отображение информации 
    draw_text(f"Current song: {songs[current_index].split('/')[-1]}", (20, 50))
    draw_text(f"Status: {'Playing' if is_playing else 'Stopped'}", (20, 100))
    draw_text("Controls: P=Play, S=Stop, ←=Prev, →=Next", (20, 150))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_p:  # Play
                play_song(current_index)
            elif event.key == pygame.K_s:  # Stop
                stop_song()
            elif event.key == pygame.K_n:  # Next
                stop_song()
                current_index = (current_index + 1) % len(songs)
                play_song(current_index)
            elif event.key == pygame.K_r:  # Previous
                stop_song()
                current_index = (current_index - 1) % len(songs)
                play_song(current_index)

    pygame.display.flip()
    clock.tick(30)

pygame.quit()
sys.exit()
