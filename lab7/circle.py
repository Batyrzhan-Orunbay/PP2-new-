import pygame as pg
pg.init()

#окно ұзындықтары,аты,түсі,артқы фон түсі
window = (600, 600) 
screen = pg.display.set_mode(window) 
pg.display.set_caption("Circle")
ball_color = pg.Color('red')
bg_color = pg.Color('white')

pos = [300, 300] #шардың пайда болу аймағы

radius = 25 #шар радиусы

speed = 25 #шар жылдамдығы

while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
    keys = pg.key.get_pressed() #клавиштың барлық жерін алады
    if keys[pg.K_UP]: 
        pos[1] = max(pos[1] - speed, radius) # max(минимум, мән)
    if keys[pg.K_DOWN]:
        pos[1] = min(pos[1] + speed, window[1] - radius) # min(мән, максимум)
    if keys[pg.K_LEFT]:
        pos[0] = max(pos[0] - speed, radius) # max(минимум, мән)
    if keys[pg.K_RIGHT]:
        pos[0] = min(pos[0] + speed, window[0] - radius) # min(мән, максимум)
        
    screen.fill((255, 255, 255)) # фонды ақ түспен бояп отырады
    pg.draw.circle(screen, ball_color, pos, radius) # шарды салады
    pg.display.flip() # экранды жаңартады
    pg.time.Clock().tick(24) # фпс=24
    
pg.exit()
