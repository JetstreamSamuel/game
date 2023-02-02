import requests
import pygame
import os


def show_map(ll, span="0.05,0.05", l="map", point=None):
    map_params = {
        "ll": ll,
        "spn": span,
        "l": l
    }

    if point:
        map_params["pt"] = ll + ",pm2dom" + "~" + ",".join(map(str, point)) + ",pm2rdm"
        map_params.pop("spn")

    map_ip_server = "http://static-maps.yandex.ru/1.x/"
    response = requests.get(map_ip_server, params=map_params)
    with open("map.png", "wb") as file:
        file.write(response.content)

    pygame.init()

    size = (600, 450)
    screen = pygame.display.set_mode(size)
    search_map = pygame.image.load("map.png")
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        screen.blit(search_map, (0, 0))
        pygame.display.flip()

    pygame.quit()

    os.remove("map.png")