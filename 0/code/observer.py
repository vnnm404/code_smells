import os
from colorama import Fore, Back


class obs:
    def create_townhall(self, a):
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
        a[13][73]="^"
        a[12][68]="^"
        a[12][72]="^"
        a[11][69]="^"
        a[11][71]="^"
        a[10][70]="^"

    def create_canon(self, a):
        for i in range(7,10):
            for j in range(5,9):
                a[i][j]="C"

        for i in range(26,29):
            for j in range(45,49):
                a[i][j]="C"

        for i in range (12,15):
            for j in range(92,96):
                a[i][j]="C"
        

    def create_hut(self, a):
        for i in range(10,12):
            for j in range(15,17):
                a[i][j]="H"

        for i in range(17,19):
            for j in range(101,103):
                a[i][j]="H"

        for i in range(19,21):
            for j in range(11,13):
                a[i][j]="H"

        for i in range(24,26):
            for j in range(98,100):
                a[i][j]="H"

        for i in range(29,31):
            for j in range(117,119):
                a[i][j]="H"

