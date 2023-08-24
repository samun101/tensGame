import random
class Board():
    def __init__(self, r):
        print(r)
        if r[2] < 1:
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

