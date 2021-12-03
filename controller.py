import numpy as np
import pygame
import keyboard

class Controller():
    def __init__(self, f = 0, vphi = 0):
        self.g = 9.8

        self.f_ind = 0
        self.vphi_ind = 1

        self.f_table = [0.2, 1.0, 2.0]
        self.vphi_table = [-30, 0, 30]

    def key_pressed(self, keys):
        if keys[pygame.K_s] and 0 < self.f_ind < 2:
            self.f_ind += 1
        if keys[pygame.K_a] and 0 < self.vphi_ind < 2:
            self.vphi_ind -= 1
        if keys[pygame.K_d] and 0 < self.vphi_ind < 2:
            self.vphi_ind += 1
        if keys[pygame.K_w] and 0 < self.f_ind < 2:
            self.f_ind -= 1


    # def acclerate(self):
    #     if self.f_ind < 2:
    #         self.f_ind += 1
    #
    # def declerate(self):
    #     if self.f_ind > 0:
    #         self.f_ind = 1
    #
    # def neg_angular(self):
    #     if self.vphi_ind > 0:
    #         self.vphi_ind -= 1
    #
    # def pos_angular(self):
    #     if self.vphi_ind < 2:
    #         self.vphi_ind += 1

    def get_action(self):
        f = self.f_table[self.f_ind]
        vphi = self.vphi_table[self.vphi_ind]
        return f * self.g, vphi / 180 * np.pi
