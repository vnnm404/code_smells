import os
import sys
import termios, tty, time

from colorama import init, Fore, Back, Style

canon_pos = [
    (6,8),(46,27),(93,13)
]

building_pos = [
    (5,7),(45,26),(92,12),(15,10),(101,17),(11,19),(98,24),(117,29)
]

C1DEAD = False