import pygame as pg  
import random  
import time  
import psycopg2 as psg  

conn = psg.connect(host="localhost", dbname="postgres", user="postgres", password="21022012a", port=5432)# Дерекқорға қосылу
cur = conn.cursor()  # Курсор объектісін жасау

# Пайдаланушылар кестесін жасау
cur.execute(""" 
CREATE TABLE IF NOT EXISTS users (
    id SERIAL PRIMARY KEY,
    username VARCHAR(50) UNIQUE NOT NULL
);
""")

# Ұпайлар кестесін жасау
cur.execute("""
CREATE TABLE IF NOT EXISTS user_scores (
    id SERIAL PRIMARY KEY,
    user_id INTEGER REFERENCES users(id),
    score INTEGER,
    level INTEGER
);
""")

pg.init()

width, height = 600, 400 # Ойын терезесінің өлшемдері
cellsize = 20  # Ұяшық өлшемі

white, green, red, blue, black = (255, 255, 255), (0, 255, 0), (255, 0, 0), (0, 0, 255), (0, 0, 0) # Түстер
fps = 10  # Бастапқы FPS (жылдамдық)

screen = pg.display.set_mode((width, height)) # Ойын терезесін жасау
pg.display.set_caption("Snake Game")  # Терезе тақырыбын орнату

font = pg.font.Font(None, 30)  # Қаріп өлшемі 30
large_font = pg.font.Font(None, 50)  # Үлкен қаріп өлшемі 50

# Пайдаланушы атын енгізу функциясы
def get_username(): 
    input_box = pg.Rect(150, 150, 300, 50)  # Енгізу өрісі
    username = ""
    active = True
    while active:
        screen.fill(black)  # Экранды қара түспен бояу
        prompt = large_font.render("Enter your username:", True, white)
        screen.blit(prompt, (150, 100))  # Сұрау мәтінін шығару

        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                exit()  # Ойынды жабу
            elif event.type == pg.KEYDOWN:
                if event.key == pg.K_RETURN:
                    return username  # Enter басылса, атты қайтару
                elif event.key == pg.K_BACKSPACE:
                    username = username[:-1]  # Соңғы символды жою
                else:
                    username += event.unicode  # Жаңа символ қосу

        pg.draw.rect(screen, white, input_box, 2)  # Енгізу өрісін салу
        text_surface = font.render(username, True, white)
        screen.blit(text_surface, (input_box.x + 10, input_box.y + 10))
        pg.display.flip()  # Экранды жаңарту

# Пайдаланушыны тексеру және прогресті жүктеу
username = get_username()
cur.execute("SELECT id FROM users WHERE username = %s", (username,))
user = cur.fetchone()  # Пайдаланушы бар ма, тексеру

if not user:
    cur.execute("INSERT INTO users (username) VALUES (%s) RETURNING id", (username,))  # Жаңа пайдаланушыны қосу
    user_id = cur.fetchone()[0]
    conn.commit()
    score = 0  # Ұпай 0
    level = 1  # Деңгей 1
else:
    user_id = user[0]  # Пайдаланушы ID
    cur.execute("SELECT score, level FROM user_scores WHERE user_id = %s ORDER BY id DESC LIMIT 1", (user_id,)) # Соңғы нәтижені алу
    result = cur.fetchone()
    if result:
        score, level = result
    else:
        score, level = 0, 1

snake = [(100, 100), (90, 100), (80, 100)] # Жыланның бастапқы күйі
snake_dir = (cellsize, 0)  # Жылан бағыты

speed = fps + (level - 1) * 2  # Деңгейге байланысты жылдамдық
food = None
food_value = 0
food_timer = 0
paused = False

# Тамақ генерациялау функциясы
def generate_food():
    global food_value, food_timer
    while True:
        x = random.randint(0, (width // cellsize) - 1) * cellsize
        y = random.randint(0, (height // cellsize) - 1) * cellsize
        if (x, y) not in snake:
            food_value = random.choice([10, 20, 30])
            food_timer = time.time()
            return (x, y)

food = generate_food()  # Алғашқы тамақ

# Пауза функциясы
def pause_game():
    paused = True
    pause_text = large_font.render("Paused. Press P to resume.", True, white)
    screen.blit(pause_text, (100, 150))
    pg.display.flip()
    while paused:
        for event in pg.event.get():
            if event.type == pg.KEYDOWN and event.key == pg.K_p:
                return

# Ойын циклі
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
            elif event.key == pg.K_p:
                # Ойынды тоқтату және нәтижені сақтау
                cur.execute("INSERT INTO user_scores (user_id, score, level) VALUES (%s, %s, %s)", (user_id, score, level))
                conn.commit()
                pause_game()

    new_head = (snake[0][0] + snake_dir[0], snake[0][1] + snake_dir[1])

    if new_head[0] < 0 or new_head[0] >= width or new_head[1] < 0 or new_head[1] >= height:
        running = False  # Шекарадан шықса, ойын аяқталады

    if new_head in snake:
        running = False  # Өзіне соғылса, ойын аяқталады

    snake.insert(0, new_head)  # Бас жағын жаңарту

    if new_head == food:
        score += food_value  # Ұпай қосу
        if score % 30 == 0:
            level += 1
            speed += 2
        food = generate_food()
    else:
        snake.pop()  # Егер жемеген болса, құйрықты қысқарту

    if time.time() - food_timer > 5:
        food = generate_food()  # 5 секундтан кейін жаңа тамақ

    for segment in snake:
        pg.draw.rect(screen, green, (segment[0], segment[1], cellsize, cellsize))  # Жыланды сызу

    pg.draw.rect(screen, red, (food[0], food[1], cellsize, cellsize))  # Тамақты сызу

    score_text = font.render(f"Score: {score}  Level: {level}", True, white)
    screen.blit(score_text, (10, 10))

    pg.display.flip()  # Экранды жаңарту
    clock.tick(speed)  # Жылдамдықпен жаңарту

# Ойын соңында ұпайды сақтау
cur.execute("INSERT INTO user_scores (user_id, score, level) VALUES (%s, %s, %s)", (user_id, score, level))
conn.commit()
cur.close()
conn.close()
pg.quit()  # Pygame-ді жабу
