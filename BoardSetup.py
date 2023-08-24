from random import random
class Board():
    def __init__(self, size, time, loop, seed):
        if seed:
            self.seed = random.randint(1, 2100000)
        self.rand = random.seed(self.seed)
        self.max = 9
        self.board = []
        self.min = 1
        self.size = size
        self.time = time
        self.loop = loop
        self.setBoard()

    def setBoard(self):
        for row in range(self.size[0]):
            row = []
            for col in range(self.size[1]):
                bit = self.makeBit()
            row.append(bit)
        self.board.append(row)

    def makeBit(self):
        bit = self.rand.randint(1, 9)
        return bit


