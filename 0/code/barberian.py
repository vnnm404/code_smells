from cmath import inf
from time import sleep
import numpy as np
import config
from object import disappear
canon_pos = config.canon_pos
building_pos = config.building_pos
import os

class barberian:
    def __init__(self,x,y,name,damage,a,b) :
        self.x=x
        self.y=y
        self.name=name
        self.health=10
        # dddd
        a[y][x]='@'
        self.damage = damage

    def move(self, a, b):
        dis=inf
        buildingPosition = [-1, -1]
        for ele1 in building_pos:
            xc=ele1[0]
            yc=ele1[1]
            d = ((xc-self.x)**2+(yc-self.y)**2)**0.5
            if d < dis and b[yc][xc]!=' ' and b[yc][xc]!='wall':
                dis = d
                buildingPosition = [xc, yc]
        if buildingPosition[0] == -1 and buildingPosition[1] == -1:
            return
        x_direction = 1 if buildingPosition[0] > self.x else (-1 if buildingPosition[0] < self.x else 0)
        y_direction = 1 if buildingPosition[1] > self.y else (-1 if buildingPosition[1] < self.x else 0)
        if x_direction * y_direction != 0:
            if abs(buildingPosition[0] - self.x) < abs(buildingPosition[1] - self.y):
                y_direction = 0
            else:
                x_direction = 0
        if self.y + y_direction > 0 and self.y + y_direction < 39 and self.x + x_direction > 0 and self.x + x_direction < 39:
            if config.C1DEAD:
                os.system(f"echo '{b[self.y + y_direction][self.x + x_direction][0]}, ' >> temp.txt")
            if b[self.y + y_direction][self.x + x_direction][0] in ['c', 'H', 't', 'w']: 
                pass
            else:
                a[self.y][self.x] = ' '
                self.x += x_direction
                self.y += y_direction
                a[self.y][self.x] = '@'

    def attack(self, a, b, c1,c2,c3,h1,h2,h3,h4,h5,th,count):
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        for i, j in directions:
            adjacentX, adjacentY = self.x + i, self.y + j
            if b[adjacentY][adjacentX] == 'canon 1':
                c1[0] -= self.damage
                if c1[0] <= 0:
                    config.C1DEAD = True
                    disappear.delete_ele(a, b, 'canon 1')
                    count[0]+=1
            elif b[adjacentY][adjacentX] == 'canon 2':
                c2[0] -= self.damage
                if c2[0] <= 0:
                    disappear.delete_ele(a, b, 'canon 2')
                    count[0]+=1
            elif b[adjacentY][adjacentX] == 'canon 3':
                c3[0] -= self.damage
                if c3[0] <= 0:
                    disappear.delete_ele(a, b,'canon 3')
                    count[0]+=1
            elif b[adjacentY][adjacentX] == 'Hut 1':
                h1[0] -= self.damage
                if h1[0] <= 0:
                    disappear.delete_ele(a, b,'Hut 1')
                    count[0]+=1
            elif b[adjacentY][adjacentX] == 'Hut 2':
                h2[0] -= self.damage
                if h2[0] <= 0:
                    disappear.delete_ele(a, b, 'Hut 2')
                    count[0]+=1
            elif b[adjacentY][adjacentX] == 'Hut 3':
                h3[0] -= self.damage
                if h3[0] <= 0:
                    disappear.delete_ele(a, b, 'Hut 3')
                    count[0]+=1
            elif b[adjacentY][adjacentX] == 'Hut 4':
                h4[0] -= self.damage
                if h4[0] <= 0:
                    disappear.delete_ele(a, b, 'Hut 4')
                    count[0]+=1
            elif b[adjacentY][adjacentX] == 'Hut 5':
                h5[0] -= self.damage
                if h5[0] <= 0:
                    disappear.delete_ele(a, b, 'Hut 5')
                    count[0]+=1
            elif b[adjacentY][adjacentX] == 'townhall':
                th[0] -= self.damage
                if th[0] <= 0:
                    disappear.delete_ele(a, b, 'townhall')
                    count[0]+=1
                


        