import pygame as pg
import random

pg.init()

width, height = 600, 400 # терезенің өлшемдері
cellsize = 20 # жыланмен тамақтың 1 сегмент өлшемі
white, green, red, blue, black = (255, 255, 255), (0, 255, 0), (255, 0, 0), (0, 0, 255), (0, 0, 0) # қолданылған түстер ргб форматта
fps = 10 # жыланның бастапқы жылдамдығы

screen = pg.display.set_mode((width, height)) # терезені құрамыз
pg.display.set_caption("Snake Game") # терезеге ат береміз

font = pg.font.Font(None, 30) #счетпен уровен шрифт

snake = [(100, 100), (90, 100), (80, 100)] # жыланның бастапқы орны
snake_dir = (cellsize, 0) # оң жақа қарай қозғалып бастайды
food = (200, 200) # тамақтың бастапқы позициясы
speed = fps # ағымдағы жылдамдығы
score = 0 # өзіне счет сақтайды
level = 1 # өзіне уровен сақтайды

def generate_food(): # тамақты генерация жасайтын функция
    while True:
        x = random.randint(0, (width // cellsize) - 1) * cellsize # х үшін кездейсоқ координаттарды жасайды
        y = random.randint(0, (height // cellsize) - 1) * cellsize # у үшін кездейсоқ координаттарды жасайды
        if (x, y) not in snake: # тамақтың жыланның үстіне түспеуін тексереді
            return (x, y)

food = generate_food()

running = True # ойынның флагы
clock = pg.time.Clock() # фпс реттейді

while running: # басты ойын циклы
    screen.fill(black) # әр кадр алдында экранды қараға тазалап отырады

    for event in pg.event.get(): # жыланның қозғалысының 
        if event.type == pg.QUIT: # х басқанда ойынды жауып тастайды
            running = False
        elif event.type == pg.KEYDOWN: # обрабатывает нажатия клавиш
            if event.key == pg.K_UP and snake_dir != (0, cellsize):
                snake_dir = (0, -cellsize)
            elif event.key == pg.K_DOWN and snake_dir != (0, -cellsize):
                snake_dir = (0, cellsize)
            elif event.key == pg.K_LEFT and snake_dir != (cellsize, 0):
                snake_dir = (-cellsize, 0)
            elif event.key == pg.K_RIGHT and snake_dir != (-cellsize, 0):
                snake_dir = (cellsize, 0)
    
    new_head = (snake[0][0] + snake_dir[0], snake[0][1] + snake_dir[1]) # жыланның басына жаңа позиция береді
    
    if new_head[0] < 0 or new_head[0] >= width or new_head[1] < 0 or new_head[1] >= height: # егер жылан терезенің границасынан шығып кетсе
        running = False # ойын аяқталады
    
    if new_head in snake: # жыланның өзіне өзі тиіп кетпеуін тексереді
        running = False 
    
    snake.insert(0, new_head) # сегменттарға 
    
    if new_head == food: # жыланның тамақты жегенін тексереді
        score += 10 # әр тамақ сайын счет 10 косады
        if score % 30 == 0: # әр 3 тамақ сайын уровен көтереді
            level += 1 # уровенге 1 уровен қосады
            speed += 2 # жылдамдыққа +2 қосады
        food = generate_food()
    else:
        snake.pop() # егер тамақты жемесе хвост алып тастайды
    
    for segment in snake: # жыланды жасыл квадраттармен бояды
        pg.draw.rect(screen, green, (segment[0], segment[1], cellsize, cellsize))
    
    pg.draw.rect(screen, red, (food[0], food[1], cellsize, cellsize)) # тамақты қызыл квадратпен бояды
    
    score_text = font.render(f"Score: {score}  Level: {level}", True, white) # счетпен уровен сол жақ бұрышқа шығарады
    screen.blit(score_text, (10, 10)) # счетпен уровен шығатын позициясы
    
    pg.display.flip() # экранды жаңартып отырамыз
    clock.tick(speed)  # ойын жылдамдығын регулировка жасайды

pg.quit()

