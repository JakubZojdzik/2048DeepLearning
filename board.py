from tile import Tile
import pygame
import random
class Board:
    def __init__(self, pos_x, pos_y):
        self.grid = [[None for _ in range(4)] for _ in range(4)]
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.texture = pygame.image.load('assets/board.png').convert()
        self.grid[0][2] = Tile(2)
        self.grid[1][1] = Tile(4)
        self.grid[3][3] = Tile(2)

    def add_tile(self):
        empty_positions = [(i, j) for i in range(4) for j in range(4) if self.grid[i][j] is None]
        if empty_positions:
            i, j = random.choice(empty_positions)
            value = random.choices([2, 4], weights=[0.9, 0.1], k=1)[0]
            self.grid[i][j] = Tile(value)

    def move_tiles(self, direction):
        for i in range(4):
            for j in range(4):
                if(self.grid[i][j] is not None):
                    self.grid[i][j].joinable = True
        action = False
        if(direction == 'u'):
            for itr in range(3):
                for x in range(4):
                    for y in range(1, 4):
                        if(self.grid[x][y] is None):
                            continue
                        if(self.grid[x][y-1] is None):
                            self.grid[x][y-1] = self.grid[x][y]
                            self.grid[x][y] = None
                            action = True
                        elif(self.grid[x][y-1].value == self.grid[x][y].value and self.grid[x][y-1].joinable and self.grid[x][y].joinable):
                            self.grid[x][y-1].update(self.grid[x][y-1].value * 2)
                            self.grid[x][y-1].joinable = False
                            self.grid[x][y] = None
                            action = True
        elif(direction == 'd'):
            for itr in range(3):
                for x in range(4):
                    for y in range(2, -1, -1):
                        if(self.grid[x][y] is None):
                            continue
                        if(self.grid[x][y+1] is None):
                            self.grid[x][y+1] = self.grid[x][y]
                            self.grid[x][y] = None
                            action = True
                        elif(self.grid[x][y+1].value == self.grid[x][y].value and self.grid[x][y+1].joinable and self.grid[x][y].joinable):
                            self.grid[x][y+1].update(self.grid[x][y+1].value * 2)
                            self.grid[x][y] = None
                            self.grid[x][y+1].joinable = False
                            action = True
        elif(direction == 'l'):
            for itr in range(3):
                for x in range(1, 4):
                    for y in range(4):
                        if(self.grid[x][y] is None):
                            continue
                        if(self.grid[x-1][y] is None):
                            self.grid[x-1][y] = self.grid[x][y]
                            self.grid[x][y] = None
                            action = True
                        elif(self.grid[x-1][y].value == self.grid[x][y].value and self.grid[x-1][y].joinable and self.grid[x][y].joinable):
                            self.grid[x-1][y].update(self.grid[x-1][y].value * 2)
                            self.grid[x][y] = None
                            self.grid[x-1][y].joinable = False
                            action = True
        elif(direction == 'r'):
            for itr in range(3):
                for x in range(2, -1, -1):
                    for y in range(4):
                        if(self.grid[x][y] is None):
                            continue
                        if(self.grid[x+1][y] is None):
                            self.grid[x+1][y] = self.grid[x][y]
                            self.grid[x][y] = None
                            action = True
                        elif(self.grid[x+1][y].value == self.grid[x][y].value and self.grid[x+1][y].joinable and self.grid[x][y].joinable):
                            self.grid[x+1][y].update(self.grid[x+1][y].value * 2)
                            self.grid[x][y] = None
                            self.grid[x+1][y].joinable = False
                            action = True
        if action:
            self.add_tile()

        # for y in range(4):
        #     for x in range(4):
        #         if(self.grid[x][y] is None):
        #             print("0", end=" ")
        #         else:
        #             print(self.grid[x][y].value, end=" ")
        #     print()
        # print()
        # print()

    def is_game_over(self):
        # Check if the game is over (e.g., no more valid moves)
        pass

    def reset_board(self):
        self.grid = [[None for _ in range(4)] for _ in range(4)]

    def draw(self, screen):
        screen.blit(self.texture, (self.pos_x, self.pos_y))
        for x in range(4):
            for y in range(4):
                if self.grid[x][y] is not None:
                    self.grid[x][y].draw(screen, x, y, self.pos_x, self.pos_y)
