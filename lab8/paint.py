import pygame

# Инициализация Pygame
pygame.init()

# Устанавливаем размеры окна
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Paint на Pygame")

# Цвета
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)

# Текущий цвет рисования
current_color = BLACK

# Переменные для режима рисования
drawing = False
mode = "pen"  # pen, rect, circle, eraser
start_pos = None  # Начальная точка для фигур

# Основной цикл программы
running = True
screen.fill(WHITE)  # Заполняем экран белым цветом
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Обработка нажатий клавиш для смены режима
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                mode = "rect"  # Прямоугольник
            elif event.key == pygame.K_c:
                mode = "circle"  # Круг
            elif event.key == pygame.K_e:
                mode = "eraser"  # Ластик
            elif event.key == pygame.K_p:
                mode = "pen"  # Карандаш
            elif event.key == pygame.K_1:
                current_color = BLACK  # Чёрный
            elif event.key == pygame.K_2:
                current_color = RED  # Красный
            elif event.key == pygame.K_3:
                current_color = BLUE  # Синий
            elif event.key == pygame.K_4:
                current_color = GREEN  # Зелёный

        # Начало рисования (нажатие ЛКМ)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  # Левая кнопка мыши
                drawing = True
                start_pos = event.pos  # Запоминаем начальную позицию

        # Рисование (движение мыши с зажатой кнопкой)
        elif event.type == pygame.MOUSEMOTION:
            if drawing:
                if mode == "pen":
                    pygame.draw.line(screen, current_color, event.pos, event.pos, 5)
                elif mode == "eraser":
                    pygame.draw.circle(screen, WHITE, event.pos, 10)

        # Завершение рисования (отпускание ЛКМ)
        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                drawing = False
                end_pos = event.pos  # Конечная точка
                
                # Рисуем прямоугольник
                if mode == "rect" and start_pos:
                    rect = pygame.Rect(start_pos, (end_pos[0] - start_pos[0], end_pos[1] - start_pos[1]))
                    pygame.draw.rect(screen, current_color, rect, 2)

                # Рисуем круг
                elif mode == "circle" and start_pos:
                    radius = int(((end_pos[0] - start_pos[0]) ** 2 + (end_pos[1] - start_pos[1]) ** 2) ** 0.5)
                    pygame.draw.circle(screen, current_color, start_pos, radius, 2)

    # Обновление экрана
    pygame.display.flip()

pygame.quit()
