import pygame
import random

pygame.init()
screen = pygame.display.set_mode((400,400))
clock = pygame.time.Clock()
snake = [(200,200)]
snake_direction = (0,0)
food = pygame.Rect(random.randrange(0, 380, 20),
                   random.randrange(0, 380, 20), 20, 20)

score = 0
font = pygame.font.Font(None, 36)

def reset_game():
    global snake, snake_direction, food, score
    snake = [(200,200)]
    snake_direction = (0,0)
    food.topleft = (random.randrange(0, 380, 20),
                    random.randrange(0, 380, 20))
    score = 0

game_running = True
while game_running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_running = False
            
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP] or keys[pygame.K_w] and snake_direction != (0,20):
        snake_direction = (0,-20)
    if keys[pygame.K_DOWN] or keys[pygame.K_s] and snake_direction != (0,-20):
        snake_direction = (0,20)
    if keys[pygame.K_LEFT] or keys[pygame.K_a] and snake_direction != (20,0):
        snake_direction = (-20,0)
    if keys[pygame.K_RIGHT] or keys[pygame.K_d] and snake_direction != (-20,0):
        snake_direction = (20,0)
    
    if snake_direction != (0,0):
        head = (snake[0] [0] + snake_direction[0],
                snake[0] [1] + snake_direction[1])
        snake.insert(0, head)
        if pygame.Rect(head, (20, 20)).colliderect(food):
            score+=1
            food.topleft = (random.randrange(0, 380, 20),
                            random.randrange(0, 380, 20))
        else:
            snake.pop()
        if (head in snake[1:] or
            head[0] < 0 or head[0] >= 400 or
            head[1] < 0 or head[1] >= 400 ):
            reset_game()
            
    screen.fill((0,0,0))
    for pos in snake:
        pygame.draw.rect(screen, (0, 255, 0),
                         (pos[0], pos[1], 20, 20))
    pygame.draw.rect(screen, (255, 0, 0), food)
    score_text = font.render(f"Score : {score}",
                             True, (255,255,255))
    screen.blit(score_text, (10,10))
    pygame.display.flip()
    clock.tick(15)

pygame.quit