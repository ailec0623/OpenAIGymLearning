import gym
import pygame
from gym.utils.play import play
mapping = {(pygame.K_UP,): 0, (pygame.K_RIGHT,): 1, (pygame.K_DOWN,): 2, (pygame.K_LEFT,): 3}
play(gym.make('LunarLander-v2', render_mode="rgb_array"), keys_to_action=mapping)