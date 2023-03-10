import os
import readline
import time
from colorama import init, Fore, Back, Style

from object import CREATE_TOWNHALL, scenery

from object import scenery
from object import obs
from board import board
from input import *
from king import *
from object import disappear
from spell import spell
from canon import canon
from barberian import barberian

c=Get()
count=[0]
# king coordinates
kx=70
ky=7
kp=20
cp=10
c1=[100]
c2=[100]
c3=[100]
h1=[100]
h2=[100]
h3=[100]
h4=[100]
h5=[100]
th=[100]

mo=1
BarbList = []
r=4
# ================= set-up board =====================

obj_board = board(34, 140)
obj_obs =board(34, 140)
obj_board.initialize_board()
obj_obs.initialize_board()

# ================= set-up scenery =====================
obj_scenery = scenery()
obj_scenery.create_townhall(obj_board.get_grid(),'townhall')
# obj_town = CREATE_TOWNHALL(obj_board.get_grid(), obj_scenery)
obj_scenery.create_canon(obj_board.get_grid(),'canon 1',5,7)
obj_scenery.create_canon(obj_board.get_grid(),'canon 2',45,26)
obj_scenery.create_canon(obj_board.get_grid(),'canon 3',92,12)
obj_scenery.create_hut(obj_board.get_grid(),'Hut 1',15,10)
obj_scenery.create_hut(obj_board.get_grid(),'Hut 2',101,17)
obj_scenery.create_hut(obj_board.get_grid(),'Hut 3',11,19)
obj_scenery.create_hut(obj_board.get_grid(),'Hut 4',98,24)
obj_scenery.create_hut(obj_board.get_grid(),'Hut 5',117,29)
obj_scenery.create_king(obj_board.get_grid(),'King',kx,ky)

king_movement=king(kx,ky)
# ================= set-up observer =====================

obj_observer = obs()
obj_observer.create_townhall(obj_obs.get_grid(),'townhall')
obj_observer.create_canon(obj_obs.get_grid(),'canon 1',5,7)
obj_observer.create_canon(obj_obs.get_grid(),'canon 2',45,26)
obj_observer.create_canon(obj_obs.get_grid(),'canon 3',92,12)
obj_observer.create_hut(obj_obs.get_grid(),'Hut 1',15,10)
obj_observer.create_hut(obj_obs.get_grid(),'Hut 2',101,17)
obj_observer.create_hut(obj_obs.get_grid(),'Hut 3',11,19)
obj_observer.create_hut(obj_obs.get_grid(),'Hut 4',98,24)
obj_observer.create_hut(obj_obs.get_grid(),'Hut 5',117,29)

# obj_board.print_board(king_movement,c1,c2,c3,h1,h2,h3,h4,h5,th,obj_obs.get_grid(),king_movement.health, BarbList)q
# obj_obs.print_board()
# ================= set-up king moment =====================
# file = open(f'replays/replay{int(len(os.listdir("replays"))) + 1}.txt', "w")
# print(len(os.listdir('./replays')))
# lines = readline
file = open(f"replays/replay{sys.argv[1]}.txt", "r")
lines = file.readlines()
play = True
while play:
    # 
    for line in lines:
        # x = Get()
        # d=input_to(x)
        os.system("clear") 
        if line[0] == "-":
            d = None
        else:
            d = line[0]
            # file.write(d+"\n")
        koo=[king_movement.health]
        king_movement.health=canon.attack(kx,ky,r,koo,cp,obj_obs.get_grid(),obj_board.get_grid(),BarbList)
        king_movement.health=koo[0]
        for barb in BarbList:
            if barb.health > 0:
                br = obj_obs.get_grid()
                attacking = False
                neighbbors = [(barb.x + i, barb.y + j) for i,j in [(0, 1), (0, -1), (1, 0), (-1, 0)]]
                for nx, ny in neighbbors:
                    if br[ny][nx][0] in ['c', 'H', 't', 'w']:
                        attacking = True
                        barb.attack(obj_board.get_grid(), obj_obs.get_grid(),c1,c2,c3,h1,h2,h3,h4,h5,th,count)
                        break
                if not attacking:
                    barb.move(obj_board.get_grid(), obj_obs.get_grid())
                
        if(count==9):
            print("YOU WON")
            os.system('aplay -q ./sounds/won.wav& 2>/dev/null')
            break
        if(king_movement.health==0) and len(BarbList)==0:
            print("YOU LOST")
            os.system('aplay -q ./sounds/lose.wav& 2>/dev/null')
            break
        if d == None:
            pass
        elif(d=='1'):
            BarbList.append(barberian(2,2,'barberian 1',60,obj_board.get_grid(),obj_obs.get_grid()))
        elif(d=='2'):
            BarbList.append(barberian(2,3,'barberian 2',60,obj_board.get_grid(),obj_obs.get_grid()))
        elif(d=='3'):
            BarbList.append(barberian(2,4,'barberian 3',60,obj_board.get_grid(),obj_obs.get_grid()))
        elif(d=='q'):
            play = False
            break
        elif(d=='w'):
            ky=king_movement.move_up(obj_board.get_grid(),kx,ky,mo) 
        elif(d=='s'):
            ky=king_movement.move_down(obj_board.get_grid(),kx,ky,mo)
        elif(d=='a'):
            kx=king_movement.move_left(obj_board.get_grid(),kx,ky,mo)
        elif(d=='d'):
            kx=king_movement.move_right(obj_board.get_grid(),kx,ky,mo)
        elif(d=='e'):
            king_movement.health=king_movement.health*2
            if(king_movement.health>100):
                king_movement.health=100
            print(king_movement.health)
        elif(d=='r'):
            kp=spell.rage(kp)
            mo=2
        elif(d=='x'):
            king.damage(c1,c2,c3,h1,h2,h3,h4,h5,th,obj_board.get_grid(),obj_obs.get_grid(),kp,kx,ky,count) 
        elif(d==' '):
            ch=king_movement.check(obj_board.get_grid(),kx,ky,obj_obs.get_grid())
            if ch == None:
                pass
            elif(ch[0]=='c'):
                if(ch[6]=='1'):
                    c1[0]=c1[0]-kp
                    os.system('aplay -q ./sounds/sword.wav& 2>/dev/null')
                    if(c1[0]<=0):
                        disappear.delete_ele(obj_board.get_grid(),obj_obs.get_grid(),ch) 
                        count[0]+=1
                if(ch[6]=='2'):
                    c2[0]=c2[0]-kp
                    os.system('aplay -q ./sounds/sword.wav& 2>/dev/null')
                    if(c2[0]<=0):
                        disappear.delete_ele(obj_board.get_grid(),obj_obs.get_grid(),ch) 
                        count[0]+=1
                if(ch[6]=='3'):
                    c3[0]=c3[0]-kp
                    os.system('aplay -q ./sounds/sword.wav& 2>/dev/null')
                    if(c3[0]<=0):
                        disappear.delete_ele(obj_board.get_grid(),obj_obs.get_grid(),ch) 
                        count[0]+=1
            elif(ch[0]=='H'):
                if(ch[4]=='1'):
                    h1[0]=h1[0]-kp
                    os.system('aplay -q ./sounds/sword.wav& 2>/dev/null')
                    if(h1[0]<=0):
                        disappear.delete_ele(obj_board.get_grid(),obj_obs.get_grid(),ch) 
                        count[0]+=1
                if(ch[4]<='2'):
                    h2[0]=h2[0]-kp
                    os.system('aplay -q ./sounds/sword.wav& 2>/dev/null')
                    if(h2[0]<=0):
                        disappear.delete_ele(obj_board.get_grid(),obj_obs.get_grid(),ch) 
                        count[0]+=1
                if(ch[4]=='3'):
                    h3[0]=h3[0]-kp
                    os.system('aplay -q ./sounds/sword.wav& 2>/dev/null')
                    if(h3[0]<=0):
                        disappear.delete_ele(obj_board.get_grid(),obj_obs.get_grid(),ch) 
                        count[0]+=1
                if(ch[4]=='4'):
                    h4[0]=h4[0]-kp
                    os.system('aplay -q ./sounds/sword.wav& 2>/dev/null')
                    if(h4[0]<=0):
                        disappear.delete_ele(obj_board.get_grid(),obj_obs.get_grid(),ch) 
                        count[0]+=1
                if(ch[4]=='5'):
                    h5[0]=h5[0]-kp
                    os.system('aplay -q ./sounds/sword.wav& 2>/dev/null')
                    if(h5[0]<=0):
                        disappear.delete_ele(obj_board.get_grid(),obj_obs.get_grid(),ch) 
                        count[0]+=1
            elif(ch[0]=='t'):
                th[0]=th[0]-kp
                os.system('aplay -q ./sounds/sword.wav& 2>/dev/null')
                if(th[0]<=0):
                    disappear.delete_ele(obj_board.get_grid(),obj_obs.get_grid(),ch) 
                    count[0]+=1
        obj_board.print_board(king_movement,c1,c2,c3,h1,h2,h3,h4,h5,th,obj_obs.get_grid(),king_movement.health, BarbList)
        time.sleep(0.2)
# file.close()
        
            
        

    

    


