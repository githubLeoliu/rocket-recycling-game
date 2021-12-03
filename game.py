import numpy as np
import pygame
from controller import Controller
from rocket import Rocket
import keyboard

# constant
g = 9.8


if __name__ == '__main__':
    f_ind = 0
    vphi_ind = 1

    f_table = [0.2, 1.0, 2.0]
    vphi_table = [-30, 0, 30]

    task = 'landing'  # 'hover' or 'landing'

    max_steps = 800
    step_id = 0
    env = Rocket(task=task, max_steps=max_steps)

    last_episode_id = 0

    FPS = 10
    pygame.init()
    clock = pygame.time.Clock()

    while True:
        clock.tick(FPS)
        keys = pygame.key.get_pressed()
        if keys[pygame.K_s] and 0 < f_ind <= 2:
            f_ind -= 1
        if keys[pygame.K_a] and 0 < vphi_ind <= 2:
            vphi_ind -= 1
        if keys[pygame.K_d] and 0 <= vphi_ind < 2:
            vphi_ind += 1
        if keys[pygame.K_w] and 0 <= f_ind < 2:
            f_ind += 1
        pygame.event.pump()

        f = f_table[f_ind] * g
        vphi = vphi_table[vphi_ind] / 180 * np.pi
        state, _, done, _ = env.step_from_input(f, vphi)

        # draw game
        env.render()

        if done or step_id == max_steps-1:
            success = env.check_landing_success(env.state)
            if success:
                print("landing success")
            else:
                print("ship crashed")
            break

        step_id +=1

