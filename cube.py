import numpy as np
import copy
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import random

from PIL import Image
class Cube():
    def __init__(self):
        self.reset()
    def reset(self):
        self.state = {'up':np.array([['w', 'w', 'w'], ['w', 'w', 'w'], ['w', 'w', 'w']]),
                'front':np.array([['o', 'o', 'o'], ['o', 'o', 'o'], ['o', 'o', 'o']]),
                'left':np.array([['b', 'b', 'b'], ['b', 'b', 'b'], ['b', 'b', 'b']]),
                'right':np.array([['g', 'g', 'g'], ['g', 'g', 'g'], ['g', 'g', 'g']]),
                'back':np.array([['r', 'r', 'r'], ['r', 'r', 'r'], ['r', 'r', 'r']]),
                'down':np.array([['y', 'y', 'y'], ['y', 'y', 'y'], ['y', 'y', 'y']])}
    def disp(self, face):
        def show(color):
            if color == 'r':
                img = Image.new('RGB', (30, 30), color='red')
            elif color == 'b':
                img = Image.new('RGB', (30, 30), color='blue')
            elif color == 'g':
                img = Image.new('RGB', (30, 30), color='green')
            elif color == 'o':
                img = Image.new('RGB', (30, 30), color='orange')
            elif color == 'w':
                img = Image.new('RGB', (30, 30), color='white')
            elif color == 'y':
                img = Image.new('RGB', (30, 30), color='yellow')
            return img

        fig, ax = plt.subplots(3, 3)
        for i in range(3):
            for j in range(3):
                ax[i][j].set_xticklabels([])
                ax[i][j].set_yticklabels([])
                img = show(self.state[face][i][j])
                ax[i][j].imshow(img, interpolation='none')
        fig.show()

    def right(self):
        temp = copy.deepcopy(self.state)
        self.state['up'][:, 2] = temp['front'][:, 2]
        self.state['front'][:, 2] = temp['down'][:, 2]
        self.state['back'][:, 0] = (temp['up'][:, 2])[::-1]
        self.state['down'][:, 2] = (temp['back'][:, 0])[::-1]
        self.state['right'][0, :] = temp['right'][:, 0][::-1]
        self.state['right'][:, 0] = temp['right'][2, :]
        self.state['right'][:, 2] = temp['right'][0, :]
        self.state['right'][2, :] = temp['right'][:, 2][::-1]


    def front(self):
        temp = copy.deepcopy(self.state)
        self.state['up'][2, :] = temp['left'][:, 2][::-1]
        self.state['left'][:, 2] = temp['down'][0, :]
        self.state['right'][:, 0] = (temp['up'][2, :])
        self.state['down'][0, :] = (temp['right'][:, 0])[::-1]
        self.state['front'][0, :] = temp['front'][:, 0][::-1]
        self.state['front'][:, 0] = temp['front'][2, :]
        self.state['front'][:, 2] = temp['front'][0, :]
        self.state['front'][2, :] = temp['front'][:, 2][::-1]

    def down(self):
        temp = copy.deepcopy(self.state)
        self.state['back'][2, :] = temp['right'][2, :]
        self.state['left'][2, :] = temp['back'][2, :]
        self.state['right'][2, :] = temp['front'][2, :]
        self.state['front'][2, :] = temp['left'][2, :]
        self.state['down'][0, :] = temp['down'][:, 0][::-1]
        self.state['down'][:, 0] = temp['down'][2, :]
        self.state['down'][:, 2] = temp['down'][0, :]
        self.state['down'][2, :] = temp['down'][:, 2][::-1]

    def up(self):
        temp = copy.deepcopy(self.state)
        self.state['back'][0, :] = temp['left'][0, :]
        self.state['left'][0, :] = temp['front'][0, :]
        self.state['right'][0, :] = temp['back'][0, :]
        self.state['front'][0, :] = temp['right'][0, :]
        self.state['up'][0, :] = temp['up'][:, 0][::-1]
        self.state['up'][:, 0] = temp['up'][2, :]
        self.state['up'][:, 2] = temp['up'][0, :]
        self.state['up'][2, :] = temp['up'][:, 2][::-1]

    def left(self):
        temp = copy.deepcopy(self.state)
        self.state['back'][:, 2] = temp['down'][:, 0][::-1]
        self.state['up'][:, 0] = temp['back'][:, 2][::-1]
        self.state['down'][:, 0] = temp['front'][:, 0]
        self.state['front'][:, 0] = temp['up'][:, 0]
        self.state['left'][0, :] = temp['left'][:, 0][::-1]
        self.state['left'][:, 0] = temp['left'][2, :]
        self.state['left'][:, 2] = temp['left'][0, :]
        self.state['left'][2, :] = temp['left'][:, 2][::-1]

    def front(self):
        temp = copy.deepcopy(self.state)
        self.state['up'][2, :] = temp['left'][:, 2][::-1]
        self.state['left'][:, 2] = temp['down'][0, :]
        self.state['right'][:, 0] = (temp['up'][2, :])
        self.state['down'][0, :] = (temp['right'][:, 0])[::-1]
        self.state['front'][0, :] = temp['front'][:, 0][::-1]
        self.state['front'][:, 0] = temp['front'][2, :]
        self.state['front'][:, 2] = temp['front'][0, :]
        self.state['front'][2, :] = temp['front'][:, 2][::-1]

    def back(self):
        temp = copy.deepcopy(self.state)
        self.state['up'][0, :] = temp['right'][:, 2]
        self.state['left'][:, 0] = temp['up'][0, :][::-1]
        self.state['right'][:, 2] = (temp['down'][2, :])[::-1]
        self.state['down'][2, :] = (temp['left'][:, 0])
        self.state['back'][0, :] = temp['back'][:, 0][::-1]
        self.state['back'][:, 0] = temp['back'][2, :]
        self.state['back'][:, 2] = temp['back'][0, :]
        self.state['back'][2, :] = temp['back'][:, 2][::-1]

    def locate_edge(self, cols):
        if self.state['front'][1][2] == cols[0] and self.state['right'][1][0] == cols[1]:
            return ("front", "right")
        if self.state['front'][1][2] == cols[1] and self.state['right'][1][0] == cols[0]:
            return ("right", "front")

        if self.state['front'][1][0] == cols[0] and self.state['left'][1][2] == cols[1]:
            return ("front", "left")
        if self.state['front'][1][0] == cols[1] and self.state['left'][1][2] == cols[0]:
            return ("left", "front")

        if self.state['front'][0][1] == cols[0] and self.state['up'][2][1] == cols[1]:
            return ("front", "up")
        if self.state['front'][0][1] == cols[1] and self.state['up'][2][1] == cols[0]:
            return ("up", "front")

        if self.state['front'][2][1] == cols[0] and self.state['down'][0][1] == cols[1]:
            return ("front", "down")
        if self.state['front'][2][1] == cols[1] and self.state['down'][0][1] == cols[0]:
            return ("down", "front")

        if self.state['up'][1][2] == cols[0] and self.state['right'][0][1] == cols[1]:
            return ("up", "right")
        if self.state['up'][1][2] == cols[1] and self.state['right'][0][1] == cols[0]:
            return ("right", "up")

        if self.state['up'][1][0] == cols[0] and self.state['left'][0][1] == cols[1]:
            return ("up", "left")
        if self.state['up'][1][0] == cols[1] and self.state['left'][0][1] == cols[0]:
            return ("left", "up")

        if self.state['down'][1][2] == cols[0] and self.state['right'][2][1] == cols[1]:
            return ("down", "right")
        if self.state['down'][1][2] == cols[1] and self.state['right'][2][1] == cols[0]:
            return ("right", "down")

        if self.state['down'][1][0] == cols[0] and self.state['left'][2][1] == cols[1]:
            return ("down", "left")
        if self.state['down'][1][0] == cols[1] and self.state['left'][2][1] == cols[0]:
            return ("left", "down")

        if self.state['back'][1][2] == cols[0] and self.state['left'][1][0] == cols[1]:
            return ("back", "left")
        if self.state['back'][1][2] == cols[1] and self.state['left'][1][0] == cols[0]:
            return ("left", "back")

        if self.state['back'][1][0] == cols[0] and self.state['right'][1][2] == cols[1]:
            return ("back", "right")
        if self.state['back'][1][0] == cols[1] and self.state['right'][1][2] == cols[0]:
            return ("right", "back")

        if self.state['back'][0][1] == cols[0] and self.state['up'][0][1] == cols[1]:
            return ("back", "up")
        if self.state['back'][0][1] == cols[1] and self.state['up'][0][1] == cols[0]:
            return ("up", "back")

        if self.state['back'][2][1] == cols[0] and self.state['down'][2][1] == cols[1]:
            return ("back", "down")
        if self.state['front'][2][1] == cols[1] and self.state['down'][2][1] == cols[0]:
            return ("down", "back")

    def randomize(self):
        scramble = []
        moves = ['R', 'L', 'U', 'D', 'F', 'B', 'R2', "R'", 'L2', "L'", 'U2', "U'", 'D2', "D'", 'F2', "F'", 'B2', "B'"]
        for i in range(20):
            x = random.randint(0, 17)
            if not scramble:
                scramble.append(moves[x])
            else:
                while scramble[i-1][0] == moves[x][0]:
                    x = random.randint(0, 17)
                scramble.append(moves[x])
        for move in scramble:
            if move=="R":
                self.right()
            if move=="R2":
                self.right()
                self.right()
            if move=="R'":
                self.right()
                self.right()
                self.right()
            if move=="L":
                self.left()
            if move=="L2":
                self.left()
                self.left()
            if move=="L'":
                self.left()
                self.left()
                self.left()
            if move=="F":
                self.front()
            if move=="F2":
                self.front()
                self.front()
            if move=="F'":
                self.front()
                self.front()
                self.front()
            if move=="U":
                self.up()
            if move=="U2":
                self.up()
                self.up()
            if move=="U'":
                self.up()
                self.up()
                self.up()
            if move=="D":
                self.down()
            if move=="D2":
                self.down()
                self.down()
            if move=="D'":
                self.down()
                self.down()
                self.down()
            if move=="B":
                self.back()
            if move=="B2":
                self.back()
                self.back()
            if move=="B'":
                self.back()
                self.back()
                self.back()
        return scramble
