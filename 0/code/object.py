import os
from colorama import Fore, Back



class scenery:
    def create_townhall(self, a,ino):
        self.name=ino
        for i in range(62,80):
            a[8][i]="o"
            a[21][i]="o"

        for i in range(14  ,20):
            for j in range(67,74):
              a[i][j]="T"

        for i in range(17,20):
            for j in range(64,67):
               a[i][j]="T"
               a[i][j+10]="T"


        for i in range(9,21):
            a[i][62]="o"
            a[i][79]="o"
        a[13][67]="^"
        a[12][68]="^"
        a[12][72]="^"
        a[11][69]="^"
        a[11][71]="^"
        a[10][70]="^"
    
    def create_canon(self,a,ino,x,y):
        self.name=ino
        for i in range(y,y+3):
            for j in range(x,x+4):
                a[i][j]="C"

    def create_hut(self, a,ino,x,y):
        self.name=ino
        for i in range(y,y+2):
            for j in range(x,x+2):
                a[i][j]="H"
        a[y][x]='/'
        a[y][x+1]='\\'
        a[y+1][x]='L'
        a[y+1][x+1]='⅃'


    def create_king(self,a,ino,x,y):
        self.name=ino
        a[y][x]='K'

class CREATE_TOWNHALL(scenery):
    def create_townhall(self, a,ino):
        self.name=ino
        for i in range(62,80):
            a[8][i]="o"
            a[21][i]="o"

        for i in range(14  ,20):
            for j in range(67,74):
              a[i][j]="T"

        for i in range(17,20):
            for j in range(64,67):
               a[i][j]="T"
               a[i][j+10]="T"


        for i in range(9,21):
            a[i][62]="o"
            a[i][79]="o"
        a[13][67]="^"
        a[12][68]="^"
        a[12][72]="^"
        a[11][69]="^"
        a[11][71]="^"
        a[10][70]="^"


class obs:
    def create_townhall(self, a,ino):
        self.name=ino
        for i in range(62,80):
            a[8][i]="wall"
            a[21][i]="wall"

        for i in range(14  ,20):
            for j in range(67,74):
              a[i][j]="townhall"

        for i in range(17,20):
            for j in range(64,67):
               a[i][j]="townhall"
               a[i][j+10]="townhall"


        for i in range(9,21):
            a[i][62]="wall"
            a[i][79]="wall"
        for i in range(67,76):
            a[13][67]="townhall"
        
        for i in range(68,75):
           a[12][i]="townhall"

        a[11][69]="townhall"
        a[11][71]="townhall"
        a[11][70]="townhall"
        a[10][70]="townhall"

    def create_canon(self,a,ino,x,y):
        self.name=ino
        for i in range(y,y+3):
            for j in range(x,x+4):
                a[i][j]=ino

    def create_hut(self, a,ino,x,y):
        self.name=ino
        for i in range(y,y+2):
            for j in range(x,x+2):
                a[i][j]=ino

class disappear:
    def delete_ele(a,b,ino):
        for i in range(34):
            for j in range(140):
                if(b[i][j]==ino):
                    a[i][j]=" "
                    b[i][j]=" "

        
                    



        

            

    