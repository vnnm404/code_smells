import os
from re import X
import time
from colorama import init, Fore, Back, Style

from object import scenery

from object import scenery
from object import obs
from board import *
from object import disappear

class king:
    def __init__(self,x,y):
        self.x = x 
        self.y = y 
        self.health=100
    def move_up(self,a,x,y,m):
        if y == 1 :
            return y
        y=y-1
        if(a[y][x]==' '):
            a[y][x]='K'
            a[y+1][x]=' '
            if(m==1):
                self.y = y
                return y
            else:
                y=y-1
                if(y>33):
                   y=33
                if(y<1):
                    y=1
                if(a[y][x]==' '):
                    a[y][x]='K'
                    a[y+1][x]=' '
                    self.y = y
                    return y
                self.y = y + 1
                return y+1
        self.y = y + 1
        return y+1


    def move_down(self,a,x,y,m):
        
        if(y==32):
            return y
        y=y+1
        if(a[y][x]==' '):
            a[y][x]='K'
            a[y-1][x]=' '
            if(m==1):
                self.y=y
                return y
            else:
                y=y+1
                if(y>33):
                   y=33
                if(y<1):
                    y=1
                if(a[y][x]==' '):
                    a[y][x]='K'
                    a[y-1][x]=' '
                    self.y=y
                    return y
                self.y=y-1
                return y-1
        self.y=y-1
        return y-1



    def move_left(self,a,x,y,m):
        
        if(x==1):return 1
        x=x-1
        
        if(a[y][x]==' '):
            a[y][x]='K'
            a[y][x+1]=' '
            if(m==1):
                self.x=x
                return x
            else:
                x=x-1
                if(x<1):
                    x=1
                if(a[y][x]==' '):
                    a[y][x]='K'
                    a[y][x+1]=' '
                    self.x=x
                    return x
                self.x=x+1
                return x+1
        self.x=x+1
        return x+1


    def move_right(self,a,x,y,m):
        
        if(x==138):return x
        x=x+1
        if(a[y][x]==' ' or a[y][x]=='x'):
            a[y][x]='K'
            a[y][x-1]=' '
            if(m==1):
                self.x=x
                return x
            else:
                x=x+1
                if(x>138):
                    x=138
                if(a[y][x]==' ' or a[y][x]=='x'):
                    a[y][x]='K'
                    a[y][x-1]=' '
                    self.x=x
                    return x
                self.x=x-1
                return x-1
        self.x=x-1
        return x-1

    def check(self,a,x,y,b):
        if(a[y+1][x]==' ' or a[y+1][x]=='x'):
            pass
        else:
            if(b[y+1][x]=='wall'):
                a[y+1][x]=' '
                os.system('aplay -q ./sounds/sword.wav& 2>/dev/null')
            return b[y+1][x]
        if(a[y-1][x]==' ' or a[y-1][x]=='x'):
            pass
        else:
            if(b[y-1][x]=='wall'):
                a[y-1][x]=' '
                os.system('aplay -q ./sounds/sword.wav& 2>/dev/null')
            return b[y-1][x]
        if(a[y][x+1]==' ' or a[y][x+1]=='x'):
            pass
        else:
            if(b[y][x+1]=='wall'):
                a[y][x+1]=' '
                os.system('aplay -q ./sounds/sword.wav& 2>/dev/null')
            return b[y][x+1]
        if(a[y][x-1]==' ' or a[y][x-1]=='x'):
            pass
        else:
            if(b[y][x-1]=='wall'):
                a[y][x-1]=' '
                os.system('aplay -q ./sounds/sword.wav& 2>/dev/null')
            return b[y][x-1]

    def damage(c1,c2,c3,h1,h2,h3,h4,h5,th,a,b,kp,x,y,count):
        if(a[y+1][x]==' ' or a[y+1][x]=='x'):
            pass
        
        if(b[y+1][x]=='wall'):
            a[y+1][x]=' '
            os.system('aplay -q ./sounds/sword.wav& 2>/dev/null')
        
        if(b[y+1][x][0]=='c' and b[y+1][x][6]=='1'):
            c1[0]=c1[0]-kp
            os.system('aplay -q ./sounds/sword.wav& 2>/dev/null')
            if(c1[0]<=0):
                disappear.delete_ele(a,b,b[y+1][x])
                count[0]+=1
        if(b[y+1][x][0]=='c' and b[y+1][x][6]=='2'):
            c2[0]=c2[0]-kp
            os.system('aplay -q ./sounds/sword.wav& 2>/dev/null')
            if(c2[0]<=0):
                disappear.delete_ele(a,b,b[y+1][x])
                count[0]+=1
        if(b[y+1][x][0]=='c' and b[y+1][x][6]=='3'):
            c3[0]=c3[0]-kp
            os.system('aplay -q ./sounds/sword.wav& 2>/dev/null')
            if(c3[0]<=0):
                disappear.delete_ele(a,b,b[y+1][x])
                count[0]+=1
        if(b[y+1][x][0]=='H' and b[y+1][x][4]=='1'):
            h1[0]=h1[0]-kp
            os.system('aplay -q ./sounds/sword.wav& 2>/dev/null')
            if(h1[0]<=0):
                disappear.delete_ele(a,b,b[y+1][x])
                count[0]+=1
        if(b[y+1][x][0]=='H' and b[y+1][x][4]=='2'):
            h2[0]=h2[0]-kp
            os.system('aplay -q ./sounds/sword.wav& 2>/dev/null')
            if(h2[0]<=0):
                disappear.delete_ele(a,b,b[y+1][x])
                count[0]+=1
        if(b[y+1][x][0]=='H' and b[y+1][x][4]=='3'):
            h3[0]=h3[0]-kp
            os.system('aplay -q ./sounds/sword.wav& 2>/dev/null')
            if(h3[0]<=0):
                disappear.delete_ele(a,b,b[y+1][x])
                count[0]+=1
        if(b[y+1][x][0]=='H' and b[y+1][x][4]=='4'):
            h4[0]=h4[0]-kp
            os.system('aplay -q ./sounds/sword.wav& 2>/dev/null')
            if(h4[0]<=0):
                disappear.delete_ele(a,b,b[y+1][x])
                count[0]+=1
        if(b[y+1][x][0]=='H' and b[y+1][x][4]=='5'):
            h5[0]=h5[0]-kp
            os.system('aplay -q ./sounds/sword.wav& 2>/dev/null')
            if(h5[0]<=0):
                disappear.delete_ele(a,b,b[y+1][x])
                count[0]+=1
        if(b[y+1][x][0]=='t'):
            th[0]=th[0]-kp
            os.system('aplay -q ./sounds/sword.wav& 2>/dev/null')
            if(th[0]<=0):
                disappear.delete_ele(a,b,b[y+1][x])
                count[0]+=1

        if(a[y-1][x]==' ' or a[y-1][x]=='x'):
            pass
        
        if(b[y-1][x]=='wall'):
            a[y-1][x]=' '
            os.system('aplay -q ./sounds/sword.wav& 2>/dev/null')
    
        if(b[y-1][x][0]=='c' and b[y-1][x][6]=='1'):
            c1[0]=c1[0]-kp
            os.system('aplay -q ./sounds/sword.wav& 2>/dev/null')
            if(c1[0]<=0):
                disappear.delete_ele(a,b,b[y-1][x])
                count[0]+=1
        if(b[y-1][x][0]=='c' and b[y-1][x][6]=='2'):
            c2[0]=c2[0]-kp
            os.system('aplay -q ./sounds/sword.wav& 2>/dev/null')
            if(c2[0]<=0):
                disappear.delete_ele(a,b,b[y-1][x])
                count[0]+=1
        if(b[y-1][x][0]=='c' and b[y-1][x][6]=='3'):
            c3[0]=c3[0]-kp
            os.system('aplay -q ./sounds/sword.wav& 2>/dev/null')
            if(c3[0]<=0):
                disappear.delete_ele(a,b,b[y-1][x])
                count[0]+=1
        if(b[y-1][x][0]=='H' and b[y-1][x][4]=='1'):
            h1[0]=h1[0]-kp
            os.system('aplay -q ./sounds/sword.wav& 2>/dev/null')
            if(h1[0]<=0):
                disappear.delete_ele(a,b,b[y-1][x])
                count[0]+=1
        if(b[y-1][x][0]=='H' and b[y-1][x][4]=='2'):
            h2[0]=h2[0]-kp
            os.system('aplay -q ./sounds/sword.wav& 2>/dev/null')
            if(h2[0]<=0):
                disappear.delete_ele(a,b,b[y-1][x])
                count[0]+=1
        if(b[y-1][x][0]=='H' and b[y-1][x][4]=='3'):
            h3[0]=h3[0]-kp
            os.system('aplay -q ./sounds/sword.wav& 2>/dev/null')
            if(h3[0]<=0):
                disappear.delete_ele(a,b,b[y-1][x])
                count[0]+=1
        if(b[y-1][x][0]=='H' and b[y-1][x][4]=='4'):
            h4[0]=h4[0]-kp
            os.system('aplay -q ./sounds/sword.wav& 2>/dev/null')
            if(h4[0]<=0):
                disappear.delete_ele(a,b,b[y-1][x])
                count[0]+=1
        if(b[y-1][x][0]=='H' and b[y-1][x][4]=='5'):
            h5[0]=h5[0]-kp
            os.system('aplay -q ./sounds/sword.wav& 2>/dev/null')
            if(h5[0]<=0):
                disappear.delete_ele(a,b,b[y-1][x])
                count[0]+=1
        if(b[y-1][x][0]=='t'):
            th[0]=th[0]-kp
            os.system('aplay -q ./sounds/sword.wav& 2>/dev/null')
            if(th[0]<=0):
                disappear.delete_ele(a,b,b[y-1][x])
                count[0]+=1
                
        if(a[y][x+1]==' ' or a[y][x+1]=='x'):
            pass
        
        if(b[y][x+1]=='wall'):
            a[y][x+1]=' '
            os.system('aplay -q ./sounds/sword.wav& 2>/dev/null')
        
        if(b[y][x+1][0]=='c' and b[y][x+1][6]=='1'):
            c1[0]=c1[0]-kp
            os.system('aplay -q ./sounds/sword.wav& 2>/dev/null')
            if(c1[0]<=0):
                disappear.delete_ele(a,b,b[y][x+1])
                count[0]+=1
        if(b[y][x+1][0]=='c' and b[y][x+1][6]=='2'):
            c2[0]=c2[0]-kp
            os.system('aplay -q ./sounds/sword.wav& 2>/dev/null')
            if(c2[0]<=0):
                disappear.delete_ele(a,b,b[y][x+1])
                count[0]+=1
        if(b[y][x+1][0]=='c' and b[y][x+1][6]=='3'):
            c3[0]=c3[0]-kp
            os.system('aplay -q ./sounds/sword.wav& 2>/dev/null')
            if(c3[0]<=0):
                disappear.delete_ele(a,b,b[y][x+1])
                count[0]+=1
        if(b[y][x+1][0]=='H' and b[y][x+1][4]=='1'):
            h1[0]=h1[0]-kp
            os.system('aplay -q ./sounds/sword.wav& 2>/dev/null')
            if(h1[0]<=0):
                disappear.delete_ele(a,b,b[y][x+1])
                count[0]+=1
        if(b[y][x+1][0]=='H' and b[y][x+1][4]=='2'):
            h2[0]=h2[0]-kp
            os.system('aplay -q ./sounds/sword.wav& 2>/dev/null')
            if(h2[0]<=0):
                disappear.delete_ele(a,b,b[y][x+1])
                count[0]+=1
        if(b[y][x+1][0]=='H' and b[y][x+1][4]=='3'):
            h3[0]=h3[0]-kp
            os.system('aplay -q ./sounds/sword.wav& 2>/dev/null')
            if(h3[0]<=0):
                disappear.delete_ele(a,b,b[y][x+1])
                count[0]+=1
        if(b[y][x+1][0]=='H' and b[y][x+1][4]=='4'):
            h4[0]=h4[0]-kp
            os.system('aplay -q ./sounds/sword.wav& 2>/dev/null')
            if(h4[0]<=0):
                disappear.delete_ele(a,b,b[y][x+1])
                count[0]+=1
        if(b[y][x+1][0]=='H' and b[y][x+1][4]=='5'):
            h5[0]=h5[0]
            os.system('aplay -q ./sounds/sword.wav& 2>/dev/null')
            if(h5[0]<=0):
                disappear.delete_ele(a,b,b[y][x+1])
                count[0]+=1
        if(b[y][x+1][0]=='t'):
            th[0]=th[0]-kp
            os.system('aplay -q ./sounds/sword.wav& 2>/dev/null')
            if(th[0]<=0):
                disappear.delete_ele(a,b,b[y][x+1])
                count[0]+=1

        if(a[y][x-1]==' ' or a[y][x-1]=='x'):
            pass
        if(b[y][x-1]=='wall'):
            a[y][x-1]=' '
            os.system('aplay -q ./sounds/sword.wav& 2>/dev/null')
        if(b[y][x-1][0]=='c' and b[y][x-1][6]=='1'):
            c1[0]=c1[0]-kp
            os.system('aplay -q ./sounds/sword.wav& 2>/dev/null')
            if(c1[0]<=0):
                disappear.delete_ele(a,b,b[y][x-1])
                count[0]+=1
        if(b[y][x-1][0]=='c' and b[y][x-1][6]=='2'):
            c2[0]=c2[0]-kp
            os.system('aplay -q ./sounds/sword.wav& 2>/dev/null')
            if(c2[0]<=0):
                disappear.delete_ele(a,b,b[y][x-1])
                count[0]+=1
        if(b[y][x-1][0]=='c' and b[y][x-1][6]=='3'):
            c3[0]=c3[0]-kp
            os.system('aplay -q ./sounds/sword.wav& 2>/dev/null')
            if(c3[0]<=0):
                disappear.delete_ele(a,b,b[y][x-1])
                count[0]+=1
        if(b[y][x-1][0]=='H' and b[y][x-1][4]=='1'):
            h1[0]=h1[0]-kp
            os.system('aplay -q ./sounds/sword.wav& 2>/dev/null')
            if(h1[0]<=0):
                disappear.delete_ele(a,b,b[y][x-1])
                count[0]+=1
        if(b[y][x-1][0]=='H' and b[y][x-1][4]=='2'):
            h2[0]=h2[0]-kp
            os.system('aplay -q ./sounds/sword.wav& 2>/dev/null')
            if(h2[0]<=0):
                disappear.delete_ele(a,b,b[y][x-1])
                count[0]+=1
        if(b[y][x-1][0]=='H' and b[y][x-1][4]=='3'):
            h3[0]=h3[0]-kp
            os.system('aplay -q ./sounds/sword.wav& 2>/dev/null')
            if(h3[0]<=0):
                disappear.delete_ele(a,b,b[y][x-1])
                count[0]+=1
        if(b[y][x-1][0]=='H' and b[y][x-1][4]=='4'):
            h4[0]=h4[0]-kp
            os.system('aplay -q ./sounds/sword.wav& 2>/dev/null')
            if(h4[0]<=0):
                disappear.delete_ele(a,b,b[y][x-1])
                count[0]+=1
        if(b[y][x-1][0]=='H' and b[y][x-1][4]=='5'):
            h5[0]=h5[0]-kp
            os.system('aplay -q ./sounds/sword.wav& 2>/dev/null')
            if(h5[0]<=0):
                disappear.delete_ele(a,b,b[y][x-1])
                count[0]+=1
        if(b[y][x-1][0]=='t'):
            th[0]=th[0]-kp
            os.system('aplay -q ./sounds/sword.wav& 2>/dev/null')
            if(th[0]<=0):
                disappear.delete_ele(a,b,b[y][x-1])
                count[0]+=1


       

        
        


        

        



