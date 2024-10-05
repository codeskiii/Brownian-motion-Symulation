import pygame
from calculations import *

keepSymulation = True

if __name__ == '__main__':
    pygame.init()
    window = pygame.display.set_mode((400,400))

    clock = pygame.time.Clock()

    Temp = 273 # K

    Time = 0.0
    Time_form_last_calcs = 0.0
    Time_step_per_frame = 1.0
    time_step_per_calcs = 30.0

    y = 1e-9
    m = 1e-21

    particle_position_vector: list[list[float], list[float]] = [[[200.0, 200.0], 1.0]]

    while keepSymulation:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                keepSymulation = False

        window.fill("white")

        Time += Time_step_per_frame
        Time_form_last_calcs += Time_step_per_frame

        if Time == time_step_per_calcs:
            for particle in particle_position_vector:
                #dx = movement_equation(Time_step_per_frame, 1, get_n())
                #dy = movement_equation(Time_step_per_frame, 1, get_n())
                
                #velocity_langevin_equation(v: float, d_t: float, y: float, T: float, n: float, m: float)
                xv = velocity_langevin_equation(particle[0][0], 
                                                time_step_per_calcs, 
                                                y, Temp, random.random(), m)
                
                particle[1] = xv
                
                particle[0][0] += dx
                particle[0][1] += dy

            Time_form_last_calcs = 0.0

        for particle in particle_position_vector:
            pygame.draw.circle(window, "black", (particle[0][0], particle[0][1]), 5)

        clock.tick(60)
        pygame.display.flip()