import pygame 
import time
from enum import Enum
from collections import namedtuple
import random

pygame.init()

BLOCK_SIZE = 20
WIDTH, HEIGHT = 640, 480

BLACK = pygame.Color("Black")
WHITE = pygame.Color("White")
RED = pygame.Color("Red")
ORANGE = pygame.Color("Orange")

font = pygame.font.SysFont("ubuntu", 25)

Point = namedtuple("Point", ["x", "y"])

class Direction(Enum):
    RIGHT = 1
    LEFT = 2
    UP = 3
    DOWN = 4