import random
import math
class Board():
    def __init__(self, r):
        print(r)
        if r[2] == 10:
            self.seed = random.randint(1, 2100000)
            print(self.seed)
        else:
            self.seed = r[2]
        self.rand = random.seed(self.seed)
        self.max = r[0]-1
        self.board = []
        self.min = 1
        self.x = r[3]
        self.y = r[4]
        self.time = r[1]
        self.setBoard()
        self.score = 0

    def setBoard(self):
        for row in range(self.x):
            row = []
            for col in range(self.y):
                bit = self.makeBit()
                row.append(bit)
            self.board.append(row)

    def getBoard(self):
        return self.board
    def getSeed(self):
        return self.seed

    def makeBit(self):
        bit = random.randint(self.min, self.max)
        return bit

    def clearBits(self,xs,ys,xe,ye,xlen,ylen):
        if xs <0:
            return
        sx = math.floor(xs / (665/xlen))
        sy = math.floor(ys / (665/ylen))
        ex = math.floor(xe / (665 / xlen))
        ey = math.floor(ye / (665 / ylen))
        sum =0
        if(ex > xlen):
            ex = xlen
        if(ey > ylen):
            ey = ylen
        if ex < sx:
            ex, sx = sx, ex
        if ey < sy:
            ey, sy = sy, ey
        for x in range(sx,ex):
            for y in range(sy,ey):
                sum += self.board[x][y]

        if sum % (self.max+1) == 0:
            for x in range(sx, ex):
                for y in range(sy, ey):
                    self.board[x][y] =0
        print(self.max+1)
        print(sum)
