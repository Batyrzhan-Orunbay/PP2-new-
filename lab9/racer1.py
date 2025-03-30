import pygame as pg
import time
import random

pg.init()
pg.mixer.init()

pg.mixer.music.load('sounds/background.wav')  # Ойынға арналған фондық әуенді жүктейміз
pg.mixer.music.set_volume(0.1)  # Дыбыс деңгейін 0.1 қоямыз
pg.mixer.music.play(-1)  # Әуенді циклмен ойнату (-1 — шексіз қайталау)

W = 400  # Терезе ені
H = 600  # Терезе биіктігі

screen = pg.display.set_mode((W, H))  # Ойын терезесін жасау
clock = pg.time.Clock()
FPS = 60  # Кадр жылдамдығы
pg.display.set_caption("Racer!")  # Терезе атауын орнату

bg_img = pg.image.load("graphs/AnimatedStreet.png")  # Жолдың фондық суретін жүктеу
player_img = pg.image.load("graphs/Player.png")  # Ойыншының суретін жүктеу
enemy_img = pg.image.load("graphs/Enemy.png")  # Қарсылас көлігінің суретін жүктеу
coin_img = pg.transform.scale(pg.image.load("graphs/coin.png"), (30, 30))  # Монетаның суретін жүктеу және өлшемін өзгерту

bgy = 0  # Фонның жылжу координатасы
sound_crash = pg.mixer.Sound('sounds/crash.wav')  # Апат кезіндегі дыбысты жүктеу

font = pg.font.Font(None, 60)  # Шрифт орнату
game_over = font.render("Game Over", True, "black")  # Ойын аяқталған кезде шығатын мәтін
game_over_rect = game_over.get_rect(center=(W // 2, H // 2))  # "Game Over" мәтінінің орны

def drawtext(score):
    score_text = font.render(f"Score: {score}", True, "WHITE")  # Ұпайды экранға шығару
    screen.blit(score_text, (10, 10))  # Ұпай санын экранның жоғарғы сол жағына орналастыру

class Player(pg.sprite.Sprite):  # Ойыншының класын анықтау
    def __init__(self):
        super().__init__()
        self.image = player_img  # Ойыншының суреті
        self.rect = self.image.get_rect()  # Ойыншының шекарасын анықтау
        self.rect.centerx = W // 2  # Ойыншының бастапқы орны
        self.rect.bottom = H  # Төменгі шетке орналастыру
        self.speed = 5  # Ойыншының қозғалыс жылдамдығы

    def move(self):
        key = pg.key.get_pressed()  # Пернелерді тексеру
        if key[pg.K_RIGHT]:  # Егер "right" басылса, оңға жылжу
            self.rect.move_ip(self.speed, 0)
        if key[pg.K_LEFT]:  # Егер "left" басылса, солға жылжу
            self.rect.move_ip(-self.speed, 0)
        if self.rect.left < 0:
            self.rect.left = 0  # Сол жақ шекарадан өтпеу үшін
        if self.rect.right > W:
            self.rect.right = W  # Оң жақ шекарадан өтпеу үшін

class Enemy(pg.sprite.Sprite):  # Қарсылас класын анықтау
    def __init__(self):
        super().__init__()
        self.image = enemy_img  # Қарсылас көлігінің суреті
        self.rect = self.image.get_rect()
        self.speed = 10  # Қозғалыс жылдамдығы
        self.gen_rect()  # Кездейсоқ координаталарды орнату

    def gen_rect(self):
        self.rect.left = random.randint(0, W - self.rect.w)  # Кездейсоқ ені бойынша орналастыру
        self.rect.bottom = 0  # Үстіңгі шеттен пайда болу

    def move(self):
        self.rect.move_ip(0, self.speed)  # Төмен қарай жылжу
        if self.rect.top > H:
            self.gen_rect()  # Егер экраннан шықса, қайтадан пайда болу

class Coin(pg.sprite.Sprite):  # тиын класын анықтау
    def __init__(self):
        super().__init__()
        self.image = coin_img  # тиынның суреті
        self.rect = self.image.get_rect()
        self.speed = 7  # тиынның құлау жылдамдығы
        self.value = random.choice([1, 2, 3])  # тиынның кездейсоқ салмағы (1, 2, 3)
        self.score = 0  # Ойыншының жинаған ұпайы
        self.gen_coin()

    def gen_coin(self):
        self.rect.left = random.randint(0, W - self.rect.w)  # тиынның кездейсоқ орналасуы
        self.rect.bottom = 0  # Жоғарыдан түсу
        self.value = random.choice([1, 2, 3])  # Жаңа салмақ беру

    def move(self):
        self.rect.move_ip(0, self.speed)  # Төмен қарай түсу
        if self.rect.top > H:
            self.gen_coin()  # Егер экраннан шықса, қайта пайда болу
        elif self.rect.colliderect(player.rect):  # Егер ойыншы жинаса
            self.score += self.value  # Ұпай қосу
            self.gen_coin()  # Жаңа тиын жасау
        else:
            screen.blit(self.image, self.rect)  # тиынды экранға шығару

# Ойын нысандарын инициализациялау
player = Player()
enemy = Enemy()
coin = Coin()

all_sprites = pg.sprite.Group()  # Барлық объектілер тобы
enemy_sprites = pg.sprite.Group()  # Қарсыластар тобы
all_sprites.add(player, enemy)
enemy_sprites.add(enemy)

run = True
while run:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False
            pg.quit()
            exit()
    
    screen.blit(bg_img, (0, bgy))  # Фонды салу
    screen.blit(bg_img, (0, bgy - H))
    bgy += 5  # Фонды төмен жылжыту
    if bgy == H:
        bgy = 0  # Қайтадан бастау

    player.move()
    
    for entity in all_sprites:
        entity.move()
        screen.blit(entity.image, entity.rect)
    
    coin.move()
    drawtext(coin.score)
    
    if coin.score % 5 == 0 and coin.score > 0:
        enemy.speed = 10 + coin.score // 5  # Жылдамдықты арттыру
    
    if pg.sprite.spritecollideany(player, enemy_sprites):
        sound_crash.play()
        time.sleep(1)
        run = False
        screen.fill("red")
        screen.blit(game_over, game_over_rect)
        pg.display.flip()
        time.sleep(3)

    pg.display.update()
    clock.tick(FPS)  # Кадр жылдамдығын сақтау


