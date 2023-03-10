from colorama import Fore, Back
from king import *
class board:
    def __init__(self, rows, columns):
        self.__rows = rows 
        self.__columns = columns 
        self.__grid = []

    # Get terminal size
    # columns = shutil.get_terminal_size().columns
    # rows = shutil.get_terminal_size().lines

    def get_grid(self):
        return self.__grid
    def set_grid(self,grid):
        self.__grid=grid

    def get_rows(self):
        return self.__rows
    
    def get_cols(self):
        return self.__columns
    

    def initialize_board(self):
        for i in range(self.__rows):
            row_array = []
            for j in range(self.__columns):
                row_array.append(" ")
            self.__grid.append(row_array)

        # Border of the board
        for i in range(self.__columns):
            self.__grid[0][i]="x"
            self.__grid[self.__rows-1][i]="x"

        for i in range(self.__rows-1):
            self.__grid[i][0]="x"
            self.__grid[i][self.__columns-1]="x"            
        # for i in range(self.__columns):
        #     self.__grid[0][i] = Fore.BLACK + " " + Fore.RESET
        #     self.__grid[self.__rows-1][i] = Fore.BLACK + " " + Fore.RESET

    def print_board(self,king_movement,c1,c2,c3,h1,h2,h3,h4,h5,th,b,health, BarbList):
        for i in range(self.__rows):
            for j in range(self.__columns):
                if (b[i][j]=='townhall') and th[0]>50:
                    print(Fore.GREEN + self.__grid[i][j] + Fore.RESET, end="")
                elif self.__grid[i][j] == 'o':
                    print(Fore.GREEN + self.__grid[i][j] + Fore.RESET, end="")
                elif self.__grid[i][j] == 'K':
                    print(Fore.GREEN + self.__grid[i][j] + Fore.RESET, end="")
                elif b[i][j]=='canon 1' and c1[0]>50:
                    print(Fore.GREEN + self.__grid[i][j] + Fore.RESET, end="")
                elif b[i][j]=='canon 2' and c2[0]>50:
                    print(Fore.GREEN + self.__grid[i][j] + Fore.RESET, end="")
                elif b[i][j]=='canon 3' and c3[0]>50:
                    print(Fore.GREEN + self.__grid[i][j] + Fore.RESET, end="")
                elif b[i][j]=='Hut 1' and h1[0]>50:
                    print(Fore.GREEN + self.__grid[i][j] + Fore.RESET, end="")
                elif b[i][j]=='Hut 2' and h2[0]>50:
                    print(Fore.GREEN + self.__grid[i][j] + Fore.RESET, end="")
                elif b[i][j]=='Hut 3' and h3[0]>50:
                    print(Fore.GREEN + self.__grid[i][j] + Fore.RESET, end="")
                elif b[i][j]=='Hut 4' and h4[0]>50:
                    print(Fore.GREEN + self.__grid[i][j] + Fore.RESET, end="")
                elif b[i][j]=='Hut 5' and h5[0]>50:
                    print(Fore.GREEN + self.__grid[i][j] + Fore.RESET, end="")
                elif (b[i][j]=='townhall') and th[0] >20:
                    print(Fore.YELLOW + self.__grid[i][j] + Fore.RESET, end="")
                elif self.__grid[i][j] == 'o':
                    print(Fore.YELLOW + self.__grid[i][j] + Fore.RESET, end="")
                elif self.__grid[i][j] == 'K':
                    print(Fore.YELLOW + self.__grid[i][j] + Fore.RESET, end="")
                elif b[i][j]=='canon 1' and c1[0]>20:
                    print(Fore.YELLOW + self.__grid[i][j] + Fore.RESET, end="")
                elif b[i][j]=='canon 2' and c2[0]>20:
                    print(Fore.YELLOW + self.__grid[i][j] + Fore.RESET, end="")
                elif b[i][j]=='canon 3' and c3[0]>20:
                    print(Fore.YELLOW + self.__grid[i][j] + Fore.RESET, end="")
                elif b[i][j]=='Hut 1' and h1[0]>20:
                    print(Fore.YELLOW + self.__grid[i][j] + Fore.RESET, end="")
                elif b[i][j]=='Hut 2' and h2[0]>20:
                    print(Fore.YELLOW + self.__grid[i][j] + Fore.RESET, end="")
                elif b[i][j]=='Hut 3' and h3[0]>20:
                    print(Fore.YELLOW + self.__grid[i][j] + Fore.RESET, end="")
                elif b[i][j]=='Hut 4' and h4[0]>20:
                    print(Fore.YELLOW + self.__grid[i][j] + Fore.RESET, end="")
                elif b[i][j]=='Hut 5' and h5[0]>20:
                    print(Fore.YELLOW + self.__grid[i][j] + Fore.RESET, end="")
                elif (b[i][j]=='townhall') and th[0]<=20:
                    print(Fore.RED + self.__grid[i][j] + Fore.RESET, end="")
                elif self.__grid[i][j] == 'o':
                    print(Fore.RED + self.__grid[i][j] + Fore.RESET, end="")
                elif self.__grid[i][j] == 'K':
                    print(Fore.RED + self.__grid[i][j] + Fore.RESET, end="")
                elif b[i][j]=='canon 1' and c1[0]<=20:
                    print(Fore.RED + self.__grid[i][j] + Fore.RESET, end="")
                elif b[i][j]=='canon 2' and c2[0]<=20:
                    print(Fore.RED + self.__grid[i][j] + Fore.RESET, end="")
                elif b[i][j]=='canon 3' and c3[0]<=20:
                    print(Fore.RED + self.__grid[i][j] + Fore.RESET, end="")
                elif b[i][j]=='Hut 1' and h1[0]<=20:
                    print(Fore.RED + self.__grid[i][j] + Fore.RESET, end="")
                elif b[i][j]=='Hut 2' and h2[0]<=20:
                    print(Fore.RED + self.__grid[i][j] + Fore.RESET, end="")
                elif b[i][j]=='Hut 3' and h3[0]<=20:
                    print(Fore.RED + self.__grid[i][j] + Fore.RESET, end="")
                elif b[i][j]=='Hut 4' and h4[0]<=20:
                    print(Fore.RED + self.__grid[i][j] + Fore.RESET, end="")
                elif b[i][j]=='Hut 5' and h5[0]<=20:
                    print(Fore.RED + self.__grid[i][j] + Fore.RESET, end="")
                else:
                    print(self.__grid[i][j] ,end="")
            print()
        # maxHealth=100
        # healthDashes=10
        # dashConvert = int(maxHealth/healthDashes)            # Get the number to divide by to convert health to dashes (being 10)
        # currentDashes = int(int(health)/dashConvert)              # Convert health to dash count: 80/10 => 8 dashes
        # remainingHealth = healthDashes - currentDashes       # Get the health remaining to fill as space => 12 spaces

        # healthDisplay = '-' * currentDashes                  # Convert 8 to 8 dashes as a string:   "--------"
        # remainingDisplay = ' ' * remainingHealth             # Convert 12 to 12 spaces as a string: "            "
        # percent = str(int((health/maxHealth)*100)) + "%"     # Get the percent as a whole number:   40%

        # print("|" + healthDisplay + remainingDisplay + "|")  # Print out textbased healthbar
        # print("         " + percent)        
        