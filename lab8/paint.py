import pygame as pg 

pg.init()

width, heigth = 800, 600 # терезесінің өлшемдері
screen = pg.display.set_mode((width, heigth))  # Терезені орнату
pg.display.set_caption("Pygame Paint")  # Терезенің атауын орнату

white, green, red, blue, black = (255, 255, 255), (0, 255, 0), (255, 0, 0), (0, 0, 255), (0, 0, 0) # қолданылған түстер ргб форматта

current_color = black # бастапқы сызу түсі – қара

# Айнымалылар – сызу режимін сақтау үшін
drawing = False  # Сурет салып жатырмыз ба?
mode = "pen"  # бастапқы режим pen, басқа режимдер: rect, circle, eraser
start_pos = None  # Фигуралар үшін бастапқы координата
last_pos = None  # Қаламмен үздіксіз сызу үшін соңғы координата

running = True
screen.fill(white)  # Экранды ақ түспен бояу (таза күйде бастау)
while running: # негізгі циклі
    for event in pg.event.get():  # Оқиғаларды өңдеу
        if event.type == pg.QUIT:  # Егер қолданушы жабу батырмасын басса
            running = False

        elif event.type == pg.KEYDOWN: # Пернетақтадағы батырмаларға жауап беру
            if event.key == pg.K_r:
                mode = "rect"  # Тікбұрыш сызу режимі
            elif event.key == pg.K_c:
                mode = "circle"  # Шеңбер сызу режимі
            elif event.key == pg.K_e:
                mode = "eraser"  # Өшіргіш режимі
            elif event.key == pg.K_p:
                mode = "pen"  # Қалам режимі
            elif event.key == pg.K_1:
                current_color = black  # Қара түсті таңдау
            elif event.key == pg.K_2:
                current_color = red  # Қызыл түсті таңдау
            elif event.key == pg.K_3:
                current_color = blue  # Көк түсті таңдау
            elif event.key == pg.K_4:
                current_color = green  # Жасыл түсті таңдау

        elif event.type == pg.MOUSEBUTTONDOWN: # Егер тінтуірдің сол жақ батырмасы басылса – сурет сала бастаймыз
            if event.button == 1:  # Сол жақ батырма
                drawing = True  # Сурет сала бастадық
                start_pos = event.pos  # Бастапқы координатаны есте сақтау
                last_pos = event.pos  # Соңғы координатаны есте сақтау қалам үшін

        elif event.type == pg.MOUSEMOTION: # Егер тінтуір қозғалып жатса
            if drawing:  # Егер сызу режимі қосулы болса
                if mode == "pen" and last_pos:  # Егер қалам режимі болса
                    pg.draw.line(screen, current_color, last_pos, event.pos, 5)  # Соңғы және жаңа нүкте арасында сызық сызу
                    last_pos = event.pos  # Соңғы координатаны жаңарту
                elif mode == "eraser":  # Егер өшіргіш режимі болса
                    pg.draw.circle(screen, white, event.pos, 10)  # Ақ түспен дөңгелек жасау 

        elif event.type == pg.MOUSEBUTTONUP: # Егер тінтуір батырмасы жіберілсе – сызуды аяқтаймыз
            if event.button == 1:  # Сол жақ батырма
                drawing = False  # Сызуды тоқтату
                end_pos = event.pos  # Соңғы координатаны сақтау
                
                if mode == "rect" and start_pos: # Егер тікбұрыш режимінде болсақ – тікбұрыш салу
                    rect = pg.Rect(start_pos, (end_pos[0] - start_pos[0], end_pos[1] - start_pos[1]))
                    pg.draw.rect(screen, current_color, rect, 2)

                elif mode == "circle" and start_pos:  # Егер шеңбер режимінде болсақ – шеңбер салу
                    radius = int(((end_pos[0] - start_pos[0]) ** 2 + (end_pos[1] - start_pos[1]) ** 2) ** 0.5)  # Радиус есептеу
                    pg.draw.circle(screen, current_color, start_pos, radius, 2)

    pg.display.flip() # Экранды жаңарту барлық өзгерістерді көрсету

pg.quit()
