import pygame

def main():
    pygame.init()
    screen = pygame.display.set_mode((640, 480)) #окно игры/рисовалки размером 640×480 пикселей.
    clock = pygame.time.Clock() #объект для контроля 
    
    # Настройки
    brush_radius = 5 #радиус кисти
    shape_thickness = 3 #толщина линий при рисовании прямоугольников или кругов
    mode = 'blue' 
    tool = 'brush'  #активный инструмент brush, rectangle, circle, eraser
    points = [] #список точек, через которые проводится кисть
    drawing = False
    start_pos = (0, 0) #начальная позиция мыши при рисовании.
    
    colors = {
        'red': (255, 0, 0),
        'green': (0, 255, 0),
        'blue': (0, 0, 255),
        'black': (0, 0, 0),
        'white': (255, 255, 255)
    }
    #Создаём белый фон, на котором будем рисовать
    background = pygame.Surface(screen.get_size())
    background.fill((255, 255, 255))  # белый фон
    #Цикл бесконечно проверяет события мыши и клавиатуры.
    while True:
        pressed = pygame.key.get_pressed()
        alt_held = pressed[pygame.K_LALT] or pressed[pygame.K_RALT]
        ctrl_held = pressed[pygame.K_LCTRL] or pressed[pygame.K_RCTRL] #Считываются нажатые клавиши Ctrl и Alt для выхода (Alt+F4 или Ctrl+W).
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE or (event.key == pygame.K_w and ctrl_held) or (event.key == pygame.K_F4 and alt_held):
                    return
                
                # Цвета
                if event.key == pygame.K_r:
                    mode = 'red'
                elif event.key == pygame.K_g:
                    mode = 'green'
                elif event.key == pygame.K_b:
                    mode = 'blue'
                elif event.key == pygame.K_l:
                    mode = 'black'
                elif event.key == pygame.K_w:
                    mode = 'white'
                
                # Инструменты, Меняем цвет и инструмент с клавиатуры.
                if event.key == pygame.K_1:
                    tool = 'brush'
                elif event.key == pygame.K_2:
                    tool = 'rectangle'
                elif event.key == pygame.K_3:
                    tool = 'circle'
                elif event.key == pygame.K_4:
                    tool = 'eraser'
            
            #Работа с мышью
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # левая кнопка #начало рисования
                    drawing = True
                    start_pos = event.pos #Сохраняется позиция начала
                    if tool in ['brush', 'eraser']:  #инструмент brush или eraser, точка добавляется в список points
                        points.append(start_pos)
                elif event.button == 3:  # правая кнопка уменьшает кисть
                    brush_radius = max(1, brush_radius - 1) #уменьшение радиуса кисти на 1, минимум 1.
            
            if event.type == pygame.MOUSEBUTTONUP:  #Этот блок срабатывает когда отпускают кнопку мыши
                if event.button == 1 and drawing: #Проверяем Левую кнопку мыши
                    end_pos = event.pos #Это будет конечная точка фигуры (для прямоугольника или круга).
                    color = colors[mode]
                    if tool == 'rectangle': #Если выбран инструмент прямоугольник
                        rect = pygame.Rect(start_pos, (end_pos[0]-start_pos[0], end_pos[1]-start_pos[1])) #вычисленными по разнице между end_pos и start_pos.
                        pygame.draw.rect(background, color, rect, shape_thickness)
                    elif tool == 'circle': #круг
                        radius_c = int(((end_pos[0]-start_pos[0])**2 + (end_pos[1]-start_pos[1])**2)**0.5)  #Вычисляем радиус как расстояние между точкой старта
                        pygame.draw.circle(background, color, start_pos, radius_c, shape_thickness)
                    drawing = False #Завершаем процесс рисования
                    points = []

            if event.type == pygame.MOUSEMOTION: #Это событие срабатывает когда мышь двигается.
                if drawing and tool in ['brush', 'eraser']: #drawing — пользователь держит левую кнопку мыши, то есть идёт процесс рисования. #tool — выбран инструмент "кисть" или "ластик".
                    pos = event.pos
                    points.append(pos)
                    points = points[-256:]
        
        # Отрисовка 
        screen.blit(background, (0, 0))
        color_value = colors[mode]
        
        # Рисуем кисть или ластик в реальном времени
        if tool in ['brush', 'eraser']:
            draw_lines(screen, points, brush_radius, color_value if tool == 'brush' else (255, 255, 255))
        
        # Превью прямоугольника и круга
        if drawing and tool in ['rectangle', 'circle']: #Пока мы держим кнопку мыши (drawing=True) и выбран инструмент "прямоугольник" или "круг"
            current_pos = pygame.mouse.get_pos()
            preview_color = colors[mode] #цвет фигуры.
            if tool == 'rectangle': #Создаём прямоугольник с верхним левым углом start_pos и размерами (width, height).
                rect = pygame.Rect(start_pos, (current_pos[0]-start_pos[0], current_pos[1]-start_pos[1]))
                pygame.draw.rect(screen, preview_color, rect, shape_thickness)
            elif tool == 'circle': #Вычисляем радиус круга как расстояние от start_pos до текущей позиции мыши.
                radius_c = int(((current_pos[0]-start_pos[0])**2 + (current_pos[1]-start_pos[1])**2)**0.5) #Рисуем круг с этим радиусом, центром в start_pos и цветом preview_color.
                pygame.draw.circle(screen, preview_color, start_pos, radius_c, shape_thickness)
        
        pygame.display.flip() #обновляет экран, чтобы увидеть все изменения.
        clock.tick(60) #ограничивает частоту кадров до 60 FPS, чтобы анимация была плавной.

def draw_lines(screen, points, width, color):
    for i in range(len(points)-1): #Проходит по всем точкам списка points, кроме последней
        pygame.draw.line(screen, color, points[i], points[i+1], width) #Соединяет каждую точку с следующей точкой линией

def new_func(main):
    main()

new_func(main)