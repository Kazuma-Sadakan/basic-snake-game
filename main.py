from utils import WIDTH, HEIGHT
from app import Snake, Food, SnakeGame

def main():
    snake = Snake(int(WIDTH/2), int(HEIGHT/2))
    food = Food()
    game = SnakeGame(snake, food)
    while not game.is_done:
        game.run()
    game.done()

if __name__ == "__main__":
    main()