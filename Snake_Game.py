import pygame
import random

# 初始化游戏
pygame.init()

# 游戏窗口尺寸
width = 640
height = 480

# 定义颜色
black = pygame.Color(0, 0, 0)
white = pygame.Color(255, 255, 255)
red = pygame.Color(255, 0, 0)
green = pygame.Color(0, 255, 0)
blue = pygame.Color(0, 0, 255)

# 创建游戏窗口
window = pygame.display.set_mode((width, height))
pygame.display.set_caption('贪吃蛇游戏')

# 定义蛇的初始位置和速度
snake_position = [100, 50]
snake_body = [[100, 50], [90, 50], [80, 50]]
snake_speed = pygame.time.Clock()

# 定义食物的初始位置
food_position = [random.randrange(1, width // 10) * 10, random.randrange(1, height // 10) * 10]
food_spawn = True

# 定义初始分数
score = 0

# 定义方向
direction = 'RIGHT'
change_to = direction

# 定义游戏结束函数
def game_over():
    pygame.quit()
    quit()

# 游戏主循环
while True:
    # 处理键盘事件
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP or event.key == ord('w'):
                change_to = 'UP'
            if event.key == pygame.K_DOWN or event.key == ord('s'):
                change_to = 'DOWN'
            if event.key == pygame.K_LEFT or event.key == ord('a'):
                change_to = 'LEFT'
            if event.key == pygame.K_RIGHT or event.key == ord('d'):
                change_to = 'RIGHT'
    
    # 判断方向是否相反
    if change_to == 'UP' and direction != 'DOWN':
        direction = 'UP'
    if change_to == 'DOWN' and direction != 'UP':
        direction = 'DOWN'
    if change_to == 'LEFT' and direction != 'RIGHT':
        direction = 'LEFT'
    if change_to == 'RIGHT' and direction != 'LEFT':
        direction = 'RIGHT'
    
    # 根据方向更新蛇的位置
    if direction == 'UP':
        snake_position[1] -= 10
    if direction == 'DOWN':
        snake_position[1] += 10
    if direction == 'LEFT':
        snake_position[0] -= 10
    if direction == 'RIGHT':
        snake_position[0] += 10
    
    # 增加蛇的身体
    snake_body.insert(0, list(snake_position))
    
    # 判断蛇是否吃到食物
    if snake_position[0] == food_position[0] and snake_position[1] == food_position[1]:
        score += 1
        food_spawn = False
    else:
        snake_body.pop()
    
    # 生成新的食物
    if not food_spawn:
        food_position = [random.randrange(1, width // 10) * 10, random.randrange(1, height // 10) * 10]
        food_spawn = True
    
    # 绘制游戏窗口
    window.fill(black)
    for position in snake_body:
        pygame.draw.rect(window, green, pygame.Rect(position[0], position[1], 10, 10))
    pygame.draw.rect(window, blue, pygame.Rect(food_position[0], food_position[1], 10, 10))
    
    # 判断游戏是否结束
    if snake_position[0] < 0 or snake_position[0] > width - 10 or snake_position[1] < 0 or snake_position[1] > height - 10:
        game_over()
    for block in snake_body[1:]:
        if snake_position[0] == block[0] and snake_position[1] == block[1]:
            game_over()
    
    # 更新分数
    pygame.display.set_caption(f'贪吃蛇游戏 | 分数: {score}')
    
    # 更新游戏窗口
    pygame.display.flip()
    
    # 控制游戏速度
    snake_speed.tick(15)
