from pygamegui import *
import pygame
pygame.init()

config.default_style["text_side"] = "center"

mw = pygame.display.set_mode((500, 400))
clock = pygame.time.Clock()
run = True

main_group = Group()
with main_group as g0:
    with Group(g0, vertical=True) as g1:
        with Group(g1, margin=(5, 5), vertical=True) as g2:
            Label(g2, text="left", style=LabelStyle(color=(255, 0, 0), font_size=30, text_side="left"))
            Label(g2, text="center", style=LabelStyle(color=(0, 255, 0), font_size=20, text_side="center"))
            Label(g2, text="right", style=LabelStyle(color=(0, 0, 255), font_size=40, text_side="right"))
        with Group(g1, margin=(5, 5)) as g2_1:
            Label(g2_1, text="Приветик!) Если ты это читаешь, то у меня всё получилось.")
    with Size_box(g0, width=2, margin=(2, 2), max_size_px=(200, 300), side="right+bottom") as g1_1:
        with Group(g1_1, margin=(0, 5)) as g2:
            pass
        with Group(g1_1, margin=(4, 5), height=0.5, width=2) as g2_1:
            with Button(g2_1, on_click=lambda:print("Clicked!")) as b1:
                Label(b1, text="Кнопка")

# main_group.render(mw, debug_outlines=1)
# exit(0)

while run:
    events = pygame.event.get()
    main_group.check_events(events)
    for e in events:
        if e.type == pygame.QUIT:
            run = False
    mw.fill((0, 0, 0))

    main_group.render(mw, debug_outlines=False)

    pygame.display.update()
    clock.tick(60)