import pygame
import random
import time

#constant colors
BLACK = (0,0,0)
WHITE = (255,255,255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

WIDTH = 1000
HEIGHT = 1000
#initiate pygame and create screen
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Snake game')

class Snake:
    def __init__(self, x, y, dir):
        self.head = [x, y]
        self.points = [self.head]
        self.dir = dir

    def move(self):
        if self.dir == 'up':
            self.head = [self.head[0], self.head[1] - 50]
            self.points.append(self.head)
        elif self.dir == 'down':
            self.head = [self.head[0], self.head[1] + 50]
            self.points.append(self.head)
        elif self.dir == 'left':
            self.head = [self.head[0] - 50, self.head[1]]
            self.points.append(self.head)
        elif self.dir == 'right':
            self.head = [self.head[0] + 50, self.head[1]]
            self.points.append(self.head)

    def isDead(self):
        #out of screen
        if self.head[0] <= 0 or self.head[0] >= WIDTH or self.head[1] <= 0 or self.head[1] >= HEIGHT:
            return True
        #runs into itself
        for i in range(0, len(self.points) - 2):
            if self.head[0] == self.points[i][0] and self.head[1] == self.points[i][1]:
                return True
        return False

class Food:
    def __init__(self, x, y):
        self.x = x
        self.y = y

def newFood(snake):
    food = Food(random.randint(3, 17) * 50, random.randint(3, 17) * 50)
    while [food.x, food.y] in snake.points:
        food = Food(random.randint(3, 17) * 50, random.randint(3, 17) * 50)
    return food

font = pygame.font.Font('freesansbold.ttf', 100)
def game_over():
    text = font.render('You died', True, RED)
    screen.blit(text, text.get_rect(center = (WIDTH/2, HEIGHT/2)))
    pygame.display.update()
    time.sleep(2)

def draw(snake, food):
    screen.fill(BLACK)
    for i in range(50, WIDTH, 50):
        pygame.draw.line(screen, WHITE, (i, 0), (i, WIDTH))
        pygame.draw.line(screen, WHITE, (0, i), (HEIGHT, i))
    for point in snake.points:
        pygame.draw.rect(screen, GREEN, pygame.Rect(point[0] + 3, point[1] + 3, 44, 44))
    pygame.draw.rect(screen, RED, pygame.Rect(food.x, food.y, 50, 50))

clock = pygame.time.Clock()

def main():
    #create a snake and food
    snake = Snake(500, 500, 'none')
    food = newFood(snake)
    
    #game loop
    running = True
    while running:
        clock.tick(8)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                quit()
            if event.type == pygame.KEYDOWN:
                if (event.key == pygame.K_UP and snake.dir != 'down'):
                    snake.dir = 'up'
                if (event.key == pygame.K_DOWN and snake.dir != 'up'):
                    snake.dir = 'down'
                if (event.key == pygame.K_LEFT and snake.dir != 'right'):
                    snake.dir = 'left'
                if (event.key == pygame.K_RIGHT and snake.dir != 'left'):
                    snake.dir = 'right'
        snake.move()

        #check if snake died
        if (snake.isDead()):
            game_over()
            running = False

        #check if snake eats food
        if (snake.head[0] == food.x and snake.head[1] == food.y):
            food = newFood(snake)
        elif (len(snake.points) > 1):
            snake.points.pop(0)

        draw(snake, food)
        pygame.display.update()
        
main()
