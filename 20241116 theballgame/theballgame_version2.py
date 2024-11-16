'''
Author: Xiyuan Yang   xiyuan_yang@outlook.com
Date: 2024-11-16 09:48:49
LastEditors: Xiyuan Yang   xiyuan_yang@outlook.com
LastEditTime: 2024-11-16 10:26:44
FilePath: \CODE_for_Vscode\Python\theballgame_version2.py
Description: 
Do you code and make progress today?
Copyright (c) 2024 by Xiyuan Yang, All Rights Reserved. 
'''


import pygame
import sys
import random


pygame.init()

width, height = 800, 80
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Bouncing Balls Animation")


BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)

COLORS = [(255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 0), (255, 0, 255), (0, 255, 255), (128, 0, 128), (128, 128, 0), (0, 128, 128), (128, 0, 0), (0, 128, 0), (0, 0, 128)]


balls = []

N=int(input("Enter the numbers of the ball: "))
L=int (input("Enter the length of the table(approximately 800): "))
while L>=width:
    L=int(input("Error,please input again!"))

for i in range(N):
    pos = int(input(f"Enter the {i+1}th ball position: "))
    color=random.choice(COLORS)
    balls.append({"position": pos, "velocity": 1 if i%2 == 0 else -1,"color":color})


ball_radius = 5
time = 0

running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    screen.fill(WHITE)
    time+=1

    for ball in balls:
        ball['position'] += ball['velocity']
        pygame.draw.circle(screen, ball['color'], (ball['position'], height // 2), ball_radius)
        
    for i in range(len(balls)):
        if(i<len(balls)-1):
            if balls[i]['position'] >= balls[i+1]['position'] and balls[i]['velocity']*balls[i+1]['velocity']<0:
                balls[i]['position'] = balls[i+1]['position']
                temp1=balls[i]['velocity']
                temp2=balls[i+1]['velocity']
                balls[i]['velocity']=1.1*temp2
                balls[i+1]['velocity']=1.1*temp1
    
        if balls[i]['position']<=0:
            balls[i]['position']=1
            balls[i]['velocity']*=(-1.5)
        if balls[i]['position']>=L:
            balls[i]['position']=L-1
            balls[i]['velocity']*=(-1.5)
        if balls[i]['velocity']>10 or balls[i]['velocity']<-10:
            balls[i]['velocity']=1

    
    
    if time==10000:
        pygame.time.wait(2000)  
        break
    
    pygame.display.flip()
    clock.tick(60)  


pygame.quit()
sys.exit()
