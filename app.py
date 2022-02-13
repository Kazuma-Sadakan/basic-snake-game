import time
import random

import pygame

from utils import(
BLOCK_SIZE, 
WIDTH, HEIGHT,
BLACK,
WHITE,
RED,
ORANGE,
font,
Point,
Direction)



class Snake:
    def __init__(self, x, y):
        print("snake init")
        self.head = Point(x, y)
        self.size = 3
        self.body = [
            self.head, 
            Point(self.head.x - (self.size - 2) *  BLOCK_SIZE, self.head.y),
            Point(self.head.x - (self.size - 1) * BLOCK_SIZE, self.head.y)
        ]

    def move(self, direction):
        print("snake moves")
        to_x, to_y = 0, 0

        if direction == Direction.RIGHT:
            to_x += BLOCK_SIZE

        elif direction == Direction.LEFT:
            to_x -= BLOCK_SIZE

        elif direction == Direction.UP:
            to_y -= BLOCK_SIZE

        elif direction == Direction.DOWN:
            to_y += BLOCK_SIZE
            
        return to_x, to_y
        

    def update(self, direction, is_feed):
        print("snake updates")
        to_x, to_y = self.move(direction)
        self.head = Point(self.head.x + to_x, self.head.y + to_y)
        self.body.insert(0, self.head)
        print(self.head)
        if not is_feed:
            self.body.pop()
        else:
            self.size += 1


class Food:
    def __init__(self):
        print("food init")
        self.position = self.place()

    def place(self):
        print("food place")
        x = random.randint(0, (WIDTH - BLOCK_SIZE)//BLOCK_SIZE) * BLOCK_SIZE
        y = random.randint(0, (HEIGHT - BLOCK_SIZE)//BLOCK_SIZE) * BLOCK_SIZE
        return Point(x, y)


class SnakeGame:
    def __init__(self, snake, food):
        print("game init")
        self.snake = snake 
        self.food = food
        self.score = 0
        self.is_done = False

        self.window = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Snake Game")
        self.clock = pygame.time.Clock()

        self.direction = Direction.RIGHT

    def control(self):
        print("game control")
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.is_done = True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    if self.direction != Direction.LEFT:
                        self.direction = Direction.RIGHT

                elif event.key == pygame.K_LEFT:
                    if self.direction != Direction.RIGHT:
                        self.direction = Direction.LEFT

                elif event.key == pygame.K_UP:
                    if self.direction != Direction.DOWN:
                        self.direction = Direction.UP

                elif event.key == pygame.K_DOWN:
                    if self.direction != Direction.UP:
                        self.direction = Direction.DOWN

    def run(self):
        print("game run")
        self.control()
        print(self.snake.head, self.food.position)
        if self.snake.head == self.food.position:
            self.snake.update(self.direction, is_feed=True)
            self.place_food()
            self.score += 1
        else:
            self.snake.update(self.direction, is_feed=False)
            
        self.collision()

        self.window.fill(BLACK)
        for pos in self.snake.body: 
            pygame.draw.rect(self.window, WHITE, pygame.Rect(pos.x, pos.y, BLOCK_SIZE, BLOCK_SIZE))

        pygame.draw.rect(self.window, RED, pygame.Rect(self.food.position.x, self.food.position.y , BLOCK_SIZE, BLOCK_SIZE))
        pygame.display.flip()
        self.clock.tick(10)


    def place_food(self):
        print("food now placed")
        self.food.position = self.food.place()
        if self.food.position in self.snake.body:
            self.food.position = self.food.place()

    def done(self):
        print("game is donw")
        if self.is_done: 
            self.window.fill(BLACK)
            game_over = font.render(f"Game Over: {self.score}", True, RED)
            self.window.blit(game_over, [0,0])
            pygame.display.flip()
            time.sleep(3)

    def collision(self):
        
        if self.snake.head.x <0 or self.snake.head.x > (WIDTH - BLOCK_SIZE) \
            or self.snake.head.y < 0 or self.snake.head.y > HEIGHT - BLOCK_SIZE:
            self.is_done = True
            print("game collision---1")

        if self.snake.head in self.snake.body[1: ]:
            self.is_done = True
            print("game collision--2")


