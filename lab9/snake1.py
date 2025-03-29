import pygame as pg
import random
import time

pg.init()

width, height = 600, 400  # Размер окна
cellsize = 20  # Размер ячейки змеи и еды
white, green, red, blue, black = (255, 255, 255), (0, 255, 0), (255, 0, 0), (0, 0, 255), (0, 0, 0)
fps = 10  # Начальная скорость змеи

screen = pg.display.set_mode((width, height))
pg.display.set_caption("Snake Game")

font = pg.font.Font(None, 30)  # Шрифт для счёта и уровня

snake = [(100, 100), (90, 100), (80, 100)]  # Начальная позиция змеи
snake_dir = (cellsize, 0)  # Движение вправо
speed = fps
score = 0
level = 1

# Генерация еды с весом и таймером
food = None
food_value = 0
food_timer = 0

def generate_food():
    global food_value, food_timer
    while True:
        x = random.randint(0, (width // cellsize) - 1) * cellsize
        y = random.randint(0, (height // cellsize) - 1) * cellsize
        if (x, y) not in snake:
            food_value = random.choice([10, 20, 30])  # Разные веса еды
            food_timer = time.time()  # Запоминаем время появления еды
            return (x, y)

food = generate_food()

running = True
clock = pg.time.Clock()

while running:
    screen.fill(black)

    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        elif event.type == pg.KEYDOWN:
            if event.key == pg.K_UP and snake_dir != (0, cellsize):
                snake_dir = (0, -cellsize)
            elif event.key == pg.K_DOWN and snake_dir != (0, -cellsize):
                snake_dir = (0, cellsize)
            elif event.key == pg.K_LEFT and snake_dir != (cellsize, 0):
                snake_dir = (-cellsize, 0)
            elif event.key == pg.K_RIGHT and snake_dir != (-cellsize, 0):
                snake_dir = (cellsize, 0)
    
    new_head = (snake[0][0] + snake_dir[0], snake[0][1] + snake_dir[1])
    
    if new_head[0] < 0 or new_head[0] >= width or new_head[1] < 0 or new_head[1] >= height:
        running = False
    
    if new_head in snake:
        running = False
    
    snake.insert(0, new_head)
    
    # Проверяем, съела ли змея еду
    if new_head == food:
        score += food_value
        if score % 30 == 0:
            level += 1
            speed += 2
        food = generate_food()
    else:
        snake.pop()
    
    # Проверяем, не истёк ли таймер еды (5 секунд)
    if time.time() - food_timer > 5:
        food = generate_food()
    
    for segment in snake:
        pg.draw.rect(screen, green, (segment[0], segment[1], cellsize, cellsize))
    
    pg.draw.rect(screen, red, (food[0], food[1], cellsize, cellsize))
    
    score_text = font.render(f"Score: {score}  Level: {level}", True, white)
    screen.blit(score_text, (10, 10))
    
    pg.display.flip()
    clock.tick(speed)

pg.quit()

