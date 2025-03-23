import pygame as pg 
import time         
import random        

pg.init()            # жүйені іске қосамыз
pg.mixer.init()      # музыка мен дыбыстарды қолдану үшін

# Фондық музыканы жүктеу және ойнату
pg.mixer.music.load('sounds/background.wav')  # Фондық әуенді жүктеу
pg.mixer.music.set_volume(0.1)                # Музыка дыбысын 10%-ға төмендету
pg.mixer.music.play(-1)                       # Музыканы циклдік режимде (шексіз) ойнату

W = 400  # Терезе ені
H = 600  # Терезе биіктігі

screen = pg.display.set_mode((W, H))  # Ойын терезесін жасау

clock = pg.time.Clock() 
FPS = 60  # Ойынның жаңару жиілігі (секундына 60 кадр)

pg.display.set_caption("Racer!")  # терезесіне ат беру

# Ойын графикасын жүктеу
bg_img = pg.image.load("graphs/AnimatedStreet.png")  # Жол фонының суретін жүктеу
player_img = pg.image.load("graphs/Player.png")      # Ойыншы көлігінің суретін жүктеу
enemy_img = pg.image.load("graphs/Enemy.png")        # Қарсылас көлігінің суретін жүктеу
coin_img = pg.transform.scale(pg.image.load("graphs/coin.png"), (30, 30))  # Монетаны 30x30 пиксельге өзгерту

bgy = 0  # Фонның жылжу координатасы

sound_crash = pg.mixer.Sound('sounds/crash.wav')  # Апат болған кездегі дыбысты жүктеу

# Шрифт орнату және "Game Over" мәтінін дайындау
font = pg.font.SysFont("Verdana", 60)  # Verdana шрифтін 60 пиксель өлшемінде орнату
game_over = font.render("Game Over", True, "black")  # "Game Over" мәтінін жасау
game_over_rect = game_over.get_rect(center=(W // 2, H // 2))  # "Game Over" мәтінін экранның ортасына орналастыру

# Ойын ұпайын көрсету функциясы
def drawtext(score):
    score_text = font.render(f"Score: {score}", True, "WHITE")  # ақ түсті мәтін жасау
    screen.blit(score_text, (10, 10))  # экранның жоғарғы сол жағына орналастыру

class Player(pg.sprite.Sprite): # Ойыншы көлігі player класы
    def __init__(self):
        super().__init__()  
        self.image = player_img  # Ойыншының суретін орнату
        self.rect = self.image.get_rect()  # Суреттің өлшемін анықтау
        self.rect.centerx = W // 2  # Ойыншыны экранның ортасына қою
        self.rect.bottom = H  # Ойыншыны төменгі бөлікке орналастыру
        self.speed = 5  # Ойыншының қозғалу жылдамдығы

    def move(self):
        key = pg.key.get_pressed()  # Басылған пернелерді алу

        if key[pg.K_d]: # Оңға қозғалу (D батырмасы)
            self.rect.move_ip(self.speed, 0)
        if key[pg.K_a]: # Солға қозғалу (A батырмасы)
            self.rect.move_ip(-self.speed, 0)
        if self.rect.left < 0: # Сол жақ шектен шықпауды қамтамасыз ету
            self.rect.left = 0
        if self.rect.right > W: # Оң жақ шектен шықпауды қамтамасыз ету
            self.rect.right = W

class Enemy(pg.sprite.Sprite): # Қарсылас көлік еnemy класы
    def __init__(self):
        super().__init__()
        self.image = enemy_img  # Қарсылас көліктің суретін орнату
        self.rect = self.image.get_rect()  # Суреттің өлшемін анықтау
        self.speed = 10  # Қарсылас көлігінің жылдамдығы

    def gen_rect(self):
        self.rect.left = random.randint(0, W - self.rect.w)  # Қарсыласты кездейсоқ орынға қою
        self.rect.bottom = 0  # Қарсыласты экранның жоғарғы шетіне қою

    def move(self):
        self.rect.move_ip(0, self.speed)  # Төмен қарай жылжыту
        if self.rect.top > H:  # Егер экраннан шықса
            self.gen_rect()  # Жаңа қарсылас генерациялау

class Coin(pg.sprite.Sprite): # Монета (Coin) класы
    def __init__(self):
        super().__init__()
        self.img = coin_img  # Монетаның суретін орнату
        self.rect = self.img.get_rect()  # Монетаның өлшемін анықтау
        self.speed = 7  # Монетаның құлау жылдамдығы
        self.score = 0  # Бастапқы ұпай

    def gen_coin(self):
        self.rect.left = random.randint(0, W - self.rect.w)  # Монетаны кездейсоқ орынға қою
        self.rect.bottom = 0  # Монетаны экранның жоғарғы жағына орналастыру

    def move(self):
        self.rect.move_ip(0, self.speed)  # Төменге жылжыту
        if self.rect.top > H:  # Егер экраннан шықса
            self.gen_coin()  # Жаңа монета генерациялау
        elif self.rect.colliderect(player.rect):  # Егер ойыншы жинаса
            self.score += 1  # Ұпайды арттыру
            self.gen_coin()  # Жаңа монета генерациялау
        else:
            screen.blit(self.img, self.rect)  # Монетаны экранға салу

# Ойыншы, қарсылас және монетаны жасау
player = Player()
enemy = Enemy()
coin = Coin()

# Спрайт топтарын жасау
all_sprites = pg.sprite.Group()
enemy_sprites = pg.sprite.Group()

all_sprites.add(player, enemy)
enemy_sprites.add(enemy)

run = True
while run: # Негізгі ойын циклі
    for event in pg.event.get():
        if event.type == pg.QUIT:  # Егер ойыннан шығу батырмасы басылса
            run = False
            pg.quit()
            exit()
    
    # Фонды жылжыту
    screen.blit(bg_img, (0, bgy))
    screen.blit(bg_img, (0, bgy - H))
    bgy += 5
    if bgy == H:
        bgy = 0

    player.move()  # Ойыншыны жылжыту

    for entity in all_sprites:
        entity.move()
        screen.blit(entity.image, entity.rect)
    
    coin.move()  # Монетаны жылжыту

    drawtext(coin.score)  # Ұпайды экранға шығару

    if pg.sprite.spritecollideany(player, enemy_sprites):  # Егер ойыншы қарсыласпен соқтығысса
        sound_crash.play()
        time.sleep(1)
        run = False
        screen.fill("red")
        screen.blit(game_over, game_over_rect)
        pg.display.flip()
        time.sleep(3)

    pg.display.update()
    clock.tick(FPS)  # Кадр жылдамдығын ұстап тұру (60 FPS)
