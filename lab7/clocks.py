import pygame as pg
import datetime as dt

pg.init()

window = (800,600)
clock = pg.time.Clock() # фпс
screen = pg.display.set_mode(window) # терезе создавать етеді

bg = pg.image.load("clockimg/clock.png") # циферблат суреті
min_hand = pg.image.load("clockimg/min_hand.png") # минут тілі суреті
sec_hand = pg.image.load("clockimg/sec_hand.png") # сек тілі суреті

def rotate(surf, img, times, angle): # функция для поворота
    rot_img = pg.transform.rotate(img, -(times % 60) * 6 + angle) # вычисляет угол поворота
    new_img = rot_img.get_rect(center = img.get_rect(center = (400, 300)).center) # центрирует изображение
    print(new_img)
    surf.blit(rot_img, new_img) # рисует повернутое изображение 


pg.display.set_caption("Clock!") # терезенің атын қояды

while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            exit()
    
    curtime = dt.datetime.now() # Получает текущее время
    minuts = curtime.minute
    seconds = curtime.second

    screen.fill("BLACK") # Очищает экран

    screen.blit(bg, (0,0)) # циферблат суретін қояды
    
    rotate(screen, sec_hand, seconds, 60) # Рисует секундную стрелку
    rotate(screen, min_hand, minuts, -45) # Рисует минутную стрелку

    pg.display.update()
    clock.tick(60) # фпс до 60
    
pg.quit()