import pygame
import random
import json
from calculations import *

keepSymulation = True

def generator_of_mols(n: int) -> list:
    mols = []
    for _ in range(n):
        mol = [[random.randint(0,800), random.randint(0,800)], [random.uniform(-1, 1), random.uniform(-1, 1)]]
        mols.append(mol)
    return mols

if __name__ == '__main__':
    f = open("config.json", "r")
    settings = json.load(f)
    pygame.init()
    window = pygame.display.set_mode((800, 800))

    clock = pygame.time.Clock()

    scale = 10 ** settings["scale"]

    Temp = settings['temp_in_k']  # K
    Time = 0.0
    Time_step_per_frame = 1.0
    time_step_per_calcs = 1.0

    y = float(settings['ressistance_coeficient'])  # Współczynnik oporu
    m = float(settings['particle_mass'])  # Masa cząsteczki

    # Lista z pozycją i prędkością cząsteczek
    particle_position_vector: list[list[float], list[float]] = generator_of_mols(settings['num_of_particles'])

    while keepSymulation:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                keepSymulation = False

        window.fill("white")

        # Symulacja czasu
        Time += Time_step_per_frame

        # Obliczenia wykonywane w każdym kroku czasowym
        for particle in particle_position_vector:
            # Aktualizacja prędkości w kierunku x
            v_x = velocity_langevin_equation(particle[1][0], 
                                             time_step_per_calcs, 
                                             y, Temp, m)
            # Aktualizacja prędkości w kierunku y
            v_y = velocity_langevin_equation(particle[1][1], 
                                             time_step_per_calcs, 
                                             y, Temp, m)

            # Przemieszczenie na podstawie prędkości
            dx = v_x * time_step_per_calcs
            dy = v_y * time_step_per_calcs

            # Zaktualizuj pozycję cząsteczki
            particle[0][0] += dx
            particle[0][1] += dy

            # Aktualizacja prędkości w liście
            particle[1][0] = v_x / scale
            particle[1][1] = v_y / scale

        # Rysowanie cząsteczki
        for particle in particle_position_vector:
            y_pos = particle[0][0]
            x_pos = particle[0][1]

            print(f"x = {x_pos}, y = {y_pos}")

            if 0 <= x_pos < 800 and 0 <= y_pos < 800:
                pygame.draw.circle(window, "black", (particle[0][0], particle[0][1]), 5)

        clock.tick(60)
        pygame.display.flip()