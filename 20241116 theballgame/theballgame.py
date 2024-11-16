
#Author: Xiyuan Yang   xiyuan_yang@outlook.com
#Date: 2024-11-16 09:31:44
#LastEditors: Xiyuan Yang   xiyuan_yang@outlook.com
#LastEditTime: 2024-11-16 09:45:00
#FilePath: \CODE_for_Vscode\Python\theballgame.py
#Description: 
#Do you code and make progress today?
#Copyright (c) 2024 by Xiyuan Yang, All Rights Reserved. 

import pygame
import sys


pygame.init()

width, height = 800, 80
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Bouncing Balls Animation")


BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)



balls = []

N=int(input("Enter the numbers of the ball: "))
L=int (input("Enter the length of the table(approximately 800): "))
while L>=width:
    L=int(input("Error,please input again!"))

for i in range(N):
    pos = int(input(f"Enter the {i+1}th ball position: "))
    balls.append({"position": pos, "velocity": 1 if i%2 == 0 else -1})


ball_radius = 5
first_drop = 0
last_drop = 0
success_count = 0
time = 0

running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    screen.fill(WHITE)

    for ball in balls:
        ball['position'] += ball['velocity']
        
        if ball['position'] == 0 or ball['position'] == L:
            success_count += 1
            if success_count == 1:
                first_drop = time
            if success_count == N:
                last_drop = time
        
        pygame.draw.circle(screen, RED, (ball['position'], height // 2), ball_radius)

    for i in range(len(balls) - 1):
        if balls[i]['position'] == balls[i+1]['position']:
            balls[i]['velocity'], balls[i+1]['velocity'] = balls[i+1]['velocity'], balls[i]['velocity']

    time += 1

    # 检查是否所有小球都落地
    if success_count == N:
        pygame.time.wait(2000)  # 等待2秒
        break

    # 更新显示
    pygame.display.flip()
    clock.tick(60)  # 限制帧率为60 FPS

# 结束程序
print(f"First drop: {first_drop} seconds, Last drop: {last_drop} seconds")
pygame.quit()
sys.exit()
