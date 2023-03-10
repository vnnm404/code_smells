import config
import os

canon_pos = config.canon_pos

class canon:
    def attack(x,y,r,kh,cp,b,board,BarbList):
            for ele in canon_pos:
                xc=ele[0]
                yc=ele[1]
                for i in range(-r,r+1):
                    for j in range(-r,r+1):
                        if yc + i >= 0 and yc + i < len(board) and xc + j >= 0 and xc + j < len(board[0]):
                            if board[yc+i][xc+j]== 'K':
                                kh[0] = kh[0] - cp
                                os.system('aplay -q ./sounds/bullet.wav& 2>/dev/null')
                            elif board[yc+i][xc+j]== '@':
                                for k in range(len(BarbList)):
                                    if xc+j == BarbList[k].x and yc+i == BarbList[k].y:
                                        BarbList[k].health = BarbList[k].health - cp
                                        if BarbList[k].health <= 0:
                                            board[yc+i][xc+j] = ' '
                                            BarbList.remove(BarbList[k])
                                            os.system('aplay -q ./sounds/bullet.wav& 2>/dev/null')
                                            break
                                        else:
                                            break
            #     if(d<=r and b[yc][xc]!=' '):
            #         kh=kh-cp
            # return kh
