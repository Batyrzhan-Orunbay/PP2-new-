import pygame as pg  
import random 
import time  

pg.init() 

width, height = 600, 400  # Ойын терезесінің өлшемдері
cellsize = 20  # Жылан мен тамақтың 1 өлшемі

white, green, red, blue, black = (255, 255, 255), (0, 255, 0), (255, 0, 0), (0, 0, 255), (0, 0, 0)
fps = 10  # Жыланның бастапқы жылдамдығы

screen = pg.display.set_mode((width, height)) # Ойын терезесін құру
pg.display.set_caption("Snake Game")  # Ойын атауын орнату

font = pg.font.Font(None, 30)  # Ойын мәтіндері үшін қаріп орнату

# Жыланның бастапқы орналасуы
snake = [(100, 100), (90, 100), (80, 100)]  # Үш бөліктен тұратын жыланның бастапқы орналасуы
snake_dir = (cellsize, 0)  # Алғашқы бағыты - оңға

speed = fps  # Жылдамдық
score = 0  # Ұпай саны
level = 1  # Деңгей

food = None
food_value = 0  # Тамақтың ұпай мәні
food_timer = 0  # Тамақтың пайда болған уақыты

def generate_food(): # Тамақты кездейсоқ орналастыратын функция
    global food_value, food_timer # Егер global food_value, food_timer болмаса, айнымалылар жаңартылмайды
    while True:
        x = random.randint(0, (width // cellsize) - 1) * cellsize
        y = random.randint(0, (height // cellsize) - 1) * cellsize
        if (x, y) not in snake:  # Тамақ жыланның үстіне түспеуін тексереміз
            food_value = random.choice([10, 20, 30])  # Әртүрлі ұпай мәндері
            food_timer = time.time()  # Тамақтың пайда болған уақытын сақтаймыз
            return (x, y)

food = generate_food()  # Алғашқы тамақты жасау

running = True 
clock = pg.time.Clock()

while running: # Ойын циклі
    screen.fill(black)  # Терезені қара түспен тазарту
    for event in pg.event.get():
        if event.type == pg.QUIT:  # Егер ойын терезесі жабылса
            running = False
        elif event.type == pg.KEYDOWN:  # Пернетақтадан батырма басылса
            if event.key == pg.K_UP and snake_dir != (0, cellsize):
                snake_dir = (0, -cellsize)  # Жоғарыға қозғалу
            elif event.key == pg.K_DOWN and snake_dir != (0, -cellsize):
                snake_dir = (0, cellsize)  # Төменге қозғалу
            elif event.key == pg.K_LEFT and snake_dir != (cellsize, 0):
                snake_dir = (-cellsize, 0)  # Солға қозғалу
            elif event.key == pg.K_RIGHT and snake_dir != (-cellsize, 0):
                snake_dir = (cellsize, 0)  # Оңға қозғалу
    
    new_head = (snake[0][0] + snake_dir[0], snake[0][1] + snake_dir[1]) # Жыланның жаңа бас координатасын есептеу
    
    if new_head[0] < 0 or new_head[0] >= width or new_head[1] < 0 or new_head[1] >= height: # Егер жылан шекарадан шықса - ойын аяқталады
        running = False 
    
    if new_head in snake: # Егер жылан өз денесіне тиіп кетсе - ойын аяқталады
        running = False
    
    snake.insert(0, new_head)  # Жыланның жаңа басын қосамыз
    
    if new_head == food: # Егер жылан тамақты жесе
        score += food_value  # Ұпай қосылады
        if score % 30 == 0:  # Әр 30 ұпай сайын деңгей өседі
            level += 1
            speed += 2  # Жылдамдық +2ге  артады
        food = generate_food()  # Жаңа тамақ жасалады
    else:
        snake.pop()  # Егер тамақ жесе, құйрығы қысқармайды, жемесе - қысқарады
    
    if time.time() - food_timer > 5: # Егер тамақ 5 секунд ішінде желінбесе - жаңа тамақ жасалады
        food = generate_food()
    
    for segment in snake: # Жыланның әр сегментін экранға сызу
        pg.draw.rect(screen, green, (segment[0], segment[1], cellsize, cellsize))
    
    pg.draw.rect(screen, red, (food[0], food[1], cellsize, cellsize)) # Тамақты экранға сызу
    
    score_text = font.render(f"Score: {score}  Level: {level}", True, white) # Ұпай мен деңгейді көрсету
    screen.blit(score_text, (10, 10))
    
    pg.display.flip()  # Экранды жаңарту
    clock.tick(speed)  # Ойынның жылдамдығын басқару
pg.quit()  # Pygame-ді жабу