import pygame as pg
import time

pg.mixer.init()
pg.init()

window = (500, 500)

screen = pg.display.set_mode(window) #  создаем окно

pg.display.set_caption("Music")  # заголовок окно

imgs = [
    pg.transform.scale(pg.image.load("musics/5000.jpg"), window),
    pg.transform.scale(pg.image.load("musics/tun.jpg"), window),
    pg.transform.scale(pg.image.load("musics/айдахар.jpg"), window),
    pg.transform.scale(pg.image.load("musics/чина.jpg"), window)
]

musics = [
    "musics/5000.mp3",
    "musics/Tun.mp3",
    "musics/Айдахар.mp3",
    "musics/Чина.mp3"
]

playdm = 0  # индекс трека
isplaying = False # играет ли сейчас музыка
lenz = len(musics) # длина списка

def play_music():
    global isplaying
    pg.mixer.music.load(musics[playdm]) # загружает текущий трек
    pg.mixer.music.play() # воспроизводим
    pg.mixer.music.set_volume(0.5) # громкость 50
    isplaying = True # указывает что музыка играет

def playnext():
    global playdm
    playdm = (playdm + 1) % lenz # увеличиваем индекс трека
    play_music() # запускаем новый трек

def playprev():
    global playdm
    if playdm - 1 < 0: 
        playdm = lenz - 1 # если индекс меньше 0, переключает на следующий трек
    else:
        playdm = (playdm - 1) % lenz # переключаем циклично
    play_music() # запускаем трек

run = True
while run:
    for event in pg.event.get():
        if event.type == pg.QUIT: # если окно закрывается завершает цикл
            run = False 
    
    screen.blit(imgs[playdm], (0,0)) # отожражает изображение на 0,0 позиции

    key = pg.key.get_pressed() # текущее состояние клавиша 

    if(key[pg.K_LEFT]):
        playprev() # если нажат влево, вызывает предедующий трек
        time.sleep(0.5) # небольшая пауза, которую когда меняется трек
    elif key[pg.K_RIGHT]:
       playnext() # если надат вправо, вызывает следующий трек
       time.sleep(0.5)
    elif key[pg.K_SPACE]:
        if isplaying:
            pg.mixer.music.pause() # если играет ставим паузу
            isplaying = False
        else:
            pg.mixer.music.unpause() # если неиграет, нужно играть
            isplaying = True
        time.sleep(0.5)
    pg.display.update() # окновляет окно
   
pg.quit() # завершает работу