from random import choice, seed
import pygame
import sys
import time
st = time.time()
seed(48909)
pygame.init()
cellrows=eval(input('enter the size of the grid: '))
cellsize = round(1200/cellrows)  
screen=pygame.display.set_mode((cellsize*cellrows,cellsize*cellrows))
lof = []
for x in (1, 0, -1):
    for y in (1, 0, -1):
        lof.append((x, y))
lof.remove((0, 0))
loggc = [[5, 1], [5, 2], [6, 1], [6, 2], [3, 13], [3, 14], [4, 12], [4, 16], [5, 11], [5, 17], [6, 11], [6, 15], [6, 17], [6, 18], [7, 11], [7, 17], [8, 12], [8, 16], [9, 13],
         [9, 14], [1, 25], [2, 23], [2, 25], [3, 21], [3, 22], [4, 21], [4, 22], [5, 21], [5, 22], [6, 23], [6, 25], [7, 25], [3, 35], [3, 36], [4, 35],  [4, 36]]  # list of living cell cordinates
los = [False, False, False, False, False, False, True, True]


class cell:
    def __init__(self, x, y, size):
        self.ul = x, y
        self.size = size
        self.sizeofx = [n for n in range(x, x+self.size+1)]
        self.sizeofy = [n for n in range(y, y+self.size+1)]
        self.living = choice(los)
        self.celldrawing = pygame.Rect(
            self.ul[0], self.ul[1], self.size, self.size)
        co = (0, 0, 0) if self.living else (255, 255, 255)
        pygame.draw.rect(screen, co, self.celldrawing)
        self.last_living = 'placeholder'

    def draw_cell(self):
        if self.last_living == self.living:
            return
        co = (0, 0, 0) if self.living else (255, 255, 255)
        pygame.draw.rect(screen, co, self.celldrawing)
        self.last_living = self.living

    def determine(self, acn):
        if acn == 3:
            self.living = True
        elif acn > 3:
            self.living = False
        elif acn < 2:
            self.living = False


class grid:
    def __init__(self, cellrows):
        self.total_cells = cellrows**2
        self.celllist = []
        self.cellrows = cellrows
        self.cellsize = round(1200/cellrows)

        self.neighbors = {}

        for y in range(cellrows):
            y = y*self.cellsize
            for x in range(cellrows):
                x = x*self.cellsize
                self.celllist.append(cell(x, y, self.cellsize))

        self.findneigbors()
        self.ggg = [self.cellrows*x[0]+x[1] for x in loggc]

    def findneigbors(self):

        self.nbrlbry = {}

        for ci in range(self.total_cells):

            nbrcs = []
            xoc = ci % self.cellrows
            yoc = ci//self.cellrows

            for y in lof:
                nx, ny = xoc+y[0], yoc+y[1]

                if self.cellrows > nx >= 0 and self.cellrows > ny >= 0:
                    idx = self.cellrows*ny + nx
                    nbrcs.append(idx)

            self.nbrlbry[ci] = nbrcs

    def draw(self):

        c = [x.living for x in self.celllist]

        for ci in range(self.total_cells):

            nbrcs = 0

            for x in self.nbrlbry[ci]:
                nbrcs += c[x]

            if nbrcs != 2:
                self.celllist[ci].determine(nbrcs)

            self.celllist[ci].draw_cell()
#        time.sleep(0.05)


c = grid(cellrows)
computing = True
clicked = False
screen.fill((255, 255, 255))
erase = False
while True:
    for x in pygame.event.get():
        if x.type == pygame.QUIT:
            sys.exit()
        if x.type == pygame.KEYUP:
            if x.key == pygame.K_p:
                if computing:
                    computing = False
                else:
                    computing = True
            elif x.key == pygame.K_c:
                for y in c.celllist:
                    y.living = False
                    y.draw_cell()
            elif x.key == pygame.K_f:
                for y in c.celllist:
                    y.living = True
                    y.draw_cell()
            elif x.key == pygame.K_g:
                for y in c.ggg:
                    c.celllist[y].living = True
                    c.celllist[y].draw_cell()
        if x.type == pygame.MOUSEBUTTONDOWN:
            clicked = True
            mx = pygame.mouse.get_pos()[0]
            my = pygame.mouse.get_pos()[1]
            for y in c.celllist:
                if mx in y.sizeofx and my in y.sizeofy:
                    erase = True if y.living else False
        if x.type == pygame.MOUSEBUTTONUP:
            clicked = False
        if clicked:
            mx = pygame.mouse.get_pos()[0]
            my = pygame.mouse.get_pos()[1]
            for y in c.celllist:
                if mx in y.sizeofx and my in y.sizeofy:
                    y.living = False if erase else True
                y.draw_cell()

    if computing:
        c.draw()
    pygame.display.flip()
print(time.time()-st)


run()
