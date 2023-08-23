import pygame
from pygame.locals import *
import random
import os

# 播放音乐
def play_music(music_file, wait = True):
    pygame.mixer.init()
    pygame.mixer.music.load(os.path.join(current_directory, music_file))
    pygame.mixer.music.play()
    if not wait: return
    # 等待音频播放完毕
    while pygame.mixer.music.get_busy():
        pygame.time.wait(50)
    return

#播放声音
def play_sound(sound_file):
    pygame.init()
    sound = pygame.mixer.Sound(os.path.join(current_directory, sound_file))
    sound.play()
    pygame.time.wait(50)
    return

# 游戏结束
def game_over():
    play_sound(sound_HitWall)   # 撞墙声
            #停顿，游戏结束
    play_music(sound_GameOver)
    
# 提示是否继续游戏
def promptGameOver():
    pygame.init()
    screen = pygame.display.set_mode((width, height))
    # 加载中文字体文件
    font_path = os.path.join(current_directory, "fonts/毛笔体.ttf")
    font = pygame.font.Font(font_path, 28)
    
    # 创建文本对象
    text = font.render("游戏结束，是否继续游戏？", True, (255, 255, 255))
    
    # 创建按钮对象
    button_yes = pygame.Rect(100, 100, 80, 50)
    button_no = pygame.Rect(220, 100, 80, 50)
    
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                return False
            elif event.type == MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if button_yes.collidepoint(mouse_pos):
                    # 在这里添加继续游戏的逻辑
                    pygame.quit()
                    return True
                elif button_no.collidepoint(mouse_pos):
                    pygame.quit()
                    return False
        
        screen.fill((0, 0, 0))
        
        # 绘制文本和按钮
        screen.blit(text, (50, 50))
        pygame.draw.rect(screen, (0, 255, 0), button_yes)
        pygame.draw.rect(screen, (255, 0, 0), button_no)
        
        pygame.display.update()
    return False

# 定义游戏主体
def game_main():
    # 初始化游戏
    pygame.init()

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

    # 播放开始音乐
    musicFile = random.choice(music_GameBackgroundMusics)
    play_music(musicFile, False)

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
            play_sound(sound_GetScore) #得分
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
            break
        else:
            for block in snake_body[1:]:
                if snake_position[0] == block[0] and snake_position[1] == block[1]:
                    game_over()
                    break
            
        # 更新分数
        pygame.display.set_caption(f'贪吃蛇游戏 | 分数: {score}')
        
        # 更新游戏窗口
        pygame.display.flip()
        
        # 控制游戏速度
        snake_speed.tick(15)    # todo: 游戏速度越来越快

    # 游戏结束
    pygame.quit()
    return

##########################################################################
# 获取当前文件的绝对路径
current_file_path = os.path.abspath(__file__)
# 获取当前文件所在目录
current_directory = os.path.dirname(current_file_path)

# 游戏窗口尺寸
width = 640
height = 480

# 定义声音和对应的文件
sound_GetScore = "sounds/超级玛丽_捡金币.mp3"
sound_GameOver = "sounds/超级玛丽_过关失败.mp3"
sound_HitWall = "sounds/超级玛丽_打晕.mp3"
music_GameBackgroundMusics = ["sounds/魂斗罗_基地.mp3","sounds/超级马里奥兄弟_地面主题.mp3"]

# 定义颜色
black = pygame.Color(0, 0, 0)
white = pygame.Color(255, 255, 255)
red = pygame.Color(255, 0, 0)
green = pygame.Color(0, 255, 0)
blue = pygame.Color(0, 0, 255)

while True:
    game_main()
    if not promptGameOver():
        quit()
