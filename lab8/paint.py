import pygame as pg  # Pygame кітапханасын импорттаймыз

# Pygame-ді инициализациялау (іске қосу)
pg.init()

# Ойын терезесінің өлшемдері
WIDTH, HEIGHT = 800, 600
screen = pg.display.set_mode((WIDTH, HEIGHT))  # Терезені орнату
pg.display.set_caption("Pygame Paint")  # Терезенің атауын орнату

# Түстерді анықтау (RGB форматында)
WHITE = (255, 255, 255)  # Ақ
BLACK = (0, 0, 0)  # Қара
RED = (255, 0, 0)  # Қызыл
BLUE = (0, 0, 255)  # Көк
GREEN = (0, 255, 0)  # Жасыл

# Әдепкі (бастапқы) сызу түсі – қара
current_color = BLACK

# Айнымалылар – сызу режимін сақтау үшін
drawing = False  # Сурет салып жатырмыз ба?
mode = "pen"  # Әдепкі режим – "қалам" (pen), басқа режимдер: rect, circle, eraser
start_pos = None  # Фигуралар үшін бастапқы координата
last_pos = None  # Қаламмен үздіксіз сызу үшін соңғы координата

# Бағдарламаның негізгі циклі
running = True
screen.fill(WHITE)  # Экранды ақ түспен бояу (таза күйде бастау)
while running:
    for event in pg.event.get():  # Оқиғаларды өңдеу (мысалы, тінтуір басу)
        if event.type == pg.QUIT:  # Егер қолданушы "жабу" батырмасын басса
            running = False

        # Пернетақтадағы батырмаларға жауап беру
        elif event.type == pg.KEYDOWN:
            if event.key == pg.K_r:
                mode = "rect"  # Тікбұрыш сызу режимі
            elif event.key == pg.K_c:
                mode = "circle"  # Шеңбер сызу режимі
            elif event.key == pg.K_e:
                mode = "eraser"  # Өшіргіш режимі
            elif event.key == pg.K_p:
                mode = "pen"  # Қалам (сызық) режимі
            elif event.key == pg.K_1:
                current_color = BLACK  # Қара түсті таңдау
            elif event.key == pg.K_2:
                current_color = RED  # Қызыл түсті таңдау
            elif event.key == pg.K_3:
                current_color = BLUE  # Көк түсті таңдау
            elif event.key == pg.K_4:
                current_color = GREEN  # Жасыл түсті таңдау

        # Егер тінтуірдің сол жақ батырмасы басылса – сурет сала бастаймыз
        elif event.type == pg.MOUSEBUTTONDOWN:
            if event.button == 1:  # Сол жақ батырма
                drawing = True  # Сурет сала бастадық
                start_pos = event.pos  # Бастапқы координатаны есте сақтау
                last_pos = event.pos  # Соңғы координатаны есте сақтау (қалам үшін)

        # Егер тінтуір қозғалып жатса
        elif event.type == pg.MOUSEMOTION:
            if drawing:  # Егер сызу режимі қосулы болса
                if mode == "pen" and last_pos:  # Егер қалам режимі болса
                    pg.draw.line(screen, current_color, last_pos, event.pos, 5)  # Соңғы және жаңа нүкте арасында сызық сызу
                    last_pos = event.pos  # Соңғы координатаны жаңарту
                elif mode == "eraser":  # Егер өшіргіш режимі болса
                    pg.draw.circle(screen, WHITE, event.pos, 10)  # Ақ түспен дөңгелек жасау (өшіргіш)

        # Егер тінтуір батырмасы жіберілсе – сызуды аяқтаймыз
        elif event.type == pg.MOUSEBUTTONUP:
            if event.button == 1:  # Сол жақ батырма
                drawing = False  # Сызуды тоқтату
                end_pos = event.pos  # Соңғы координатаны сақтау
                
                # Егер тікбұрыш режимінде болсақ – тікбұрыш салу
                if mode == "rect" and start_pos:
                    rect = pg.Rect(start_pos, (end_pos[0] - start_pos[0], end_pos[1] - start_pos[1]))
                    pg.draw.rect(screen, current_color, rect, 2)

                # Егер шеңбер режимінде болсақ – шеңбер салу
                elif mode == "circle" and start_pos:
                    radius = int(((end_pos[0] - start_pos[0]) ** 2 + (end_pos[1] - start_pos[1]) ** 2) ** 0.5)  # Радиус есептеу
                    pg.draw.circle(screen, current_color, start_pos, radius, 2)

    # Экранды жаңарту (барлық өзгерістерді көрсету)
    pg.display.flip()

# Pygame-ді жабу
pg.quit()
